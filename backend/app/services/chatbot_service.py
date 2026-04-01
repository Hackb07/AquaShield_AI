from googletrans import Translator
import asyncio

translator = Translator()

class ChatbotService:
    @staticmethod
    async def process_chat(message: str, target_lang: str) -> str:
        """
        Multilingual Chatbot mock using googletrans.
        Pipeline: Detect -> Translate to English -> Process (Mock LLM) -> Translate back to target_lang
        """
        try:
            # 1. Detect & Translate to English if needed
            if target_lang != "en":
                # Assuming incoming message is in target_lang
                translated_in = await translator.translate(message, dest='en', src=target_lang)
                eng_message = translated_in.text
            else:
                eng_message = message

            # 2. Process query in English (Mock AI logic)
            lower_msg = eng_message.lower()
            if "flood" in lower_msg or "danger" in lower_msg or "risk" in lower_msg:
                eng_response = "There is currently a moderate risk of flooding in low-lying areas due to expected heavy rainfall. Please stay alert and follow local news."
            elif "hello" in lower_msg or "hi" in lower_msg:
                eng_response = "Hello! I am the AquaShield AI assistant. How can I help you today?"
            elif "tomorrow" in lower_msg:
                eng_response = "Tomorrow's forecast indicates continuous rain. Infrastructure in zone C might experience water accumulation."
            else:
                eng_response = "I can help with flood predictions, safety recommendations, and real-time alerts. What do you need to know?"

            # 3. Translate back to target language
            if target_lang != "en":
                translated_out = await translator.translate(eng_response, dest=target_lang, src='en')
                final_response = translated_out.text
            else:
                final_response = eng_response

            return final_response
            
        except Exception as e:
            # Fallback for translation errors
            return f"Error processing request: {str(e)}"
