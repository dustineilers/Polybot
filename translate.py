# Module used to translate messages into the target langguage(s)
import os
from dotenv import load_dotenv

import deepl

load_dotenv()
auth_key = os.getenv('AUTH_KEY')
translator = deepl.Translator(auth_key)

def translate_message(text, target_lang = "EN-US"):

    translation = translator.translate_text(text, target_lang=target_lang)

    translated_message = str(translation)
    source_language = translation.detected_source_lang

    return translated_message, source_language
