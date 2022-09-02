'''This class contains methods for translating between texts from french to english and from
english to french'''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
version = os.environ['version']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version=version,
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english_to_french(english_text):
    '''Traduces english_text to a french text.'''
    french_text = ""
    try:
        translation = language_translator.translate(
            text = english_text, model_id = "en-fr"
            ).get_result()
        french_text = translation['translations'][0]['translation']
    except:
        french_text = "there was an error"
    return french_text

def french_to_english(french_text):
    '''Traduces french_text to a english text.'''
    english_text = ""
    try:
        translation = language_translator.translate(
            text = french_text, model_id = "fr-en"
            ).get_result()
        english_text = translation['translations'][0]['translation']
    except:
        english_text = "there was an error"
    return english_text
