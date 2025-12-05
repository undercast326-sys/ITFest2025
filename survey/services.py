import anthropic
from anthropic.types import MessageParam
from django.conf import settings
import json


class AIAnalyzer:
    def __init__(self):
        self.client = anthropic.Anthropic(
            api_key=settings.ANTHROPIC_API_KEY
        )

    def analyze_survey_responses(self, responses_data, universities):
        universities_info = self._format_universities(universities)


        prompt = f"""
Ты - эксперт по профориентации и подбору университетов в Казахстане.

Вот ответы студента на опрос:
{json.dumps(responses_data, ensure_ascii=False, indent=2)}

Вот список доступных университетов из базы данных:
{universities_info}

Твоя задача:
1. Проанализировать интересы, предпочтения и цели студента
2. Определить наиболее подходящие направления обучения
3. ИЗ ПРЕДОСТАВЛЕННОГО СПИСКА выбрать 3-5 наиболее подходящих университетов
4. Для каждого университета объяснить, ПОЧЕМУ он подходит на основе ответов студента
5. Дать краткие персональные советы
6. Сравнить все университеты и выдать самый подходящий

ВАЖНО: Рекомендуй ТОЛЬКО университеты из предоставленного списка! Используй их точные названия.

Ответ дай СТРОГО в формате JSON (без markdown, без ```json):
{{
    "analysis": "Детальный анализ интересов и целей студента (2-3 предложения)",
    "recommended_fields": ["направление1", "направление2", "направление3"],
    "recommended_universities": [
        {{
            "name": "точное название из списка",
            "match_score": 95,
            "reasons": [
                "причина 1 на основе ответов",
                "причина 2 на основе ответов"
            ]
        }}
    ],
    "advice": "Персональные советы студенту (2-3 предложения)"
}}
"""

        try:
            message = self.client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=2000,
                messages=[
                    MessageParam(role='user', content=prompt)
                ]
            )


            response_text = message.content[0].text

            result = self._parse_ai_response(response_text)

            return result

        except Exception as e:
            return {
                "error": str(e),
                "analysis": "Не удалось проанализировать ответы",
                "recommended_fields": [],
                "recommended_universities": [],
                "advice": "Пожалуйста, попробуйте снова позже"
            }

    def _format_universities(self, universities):
        uni_list = []
        for uni in universities:
            uni_info = f"- {uni.name}"

            if hasattr(uni, 'description') and uni.description:
                uni_info += f"\n  Описание: {uni.description[:200]}"

            if hasattr(uni, 'specializations') and uni.specializations:
                uni_info += f"\n  Специализации: {uni.specializations}"

            if hasattr(uni, 'location') and uni.location:
                uni_info += f"\n  Расположение: {uni.location}"

            uni_list.append(uni_info)

        return "\n".join(uni_list)

    def _parse_ai_response(self, response_text):
        try:
            response_text = response_text.strip()
            if response_text.startswith('```json'):
                response_text = response_text[7:]
            if response_text.startswith('```'):
                response_text = response_text[3:]
            if response_text.endswith('```'):response_text = response_text[:-3]

            response_text = response_text.strip()

            result = json.loads(response_text)
            return result

        except json.JSONDecodeError:
            return {
                "analysis": response_text,
                "recommended_fields": [],
                "recommended_universities": [],
                "advice": ""
            }