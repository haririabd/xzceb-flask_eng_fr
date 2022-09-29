import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

"""To declare function for translation between english and French"""

load_dotenv()

#apikey = os.environ['apikey']
apikey = "O12gtyqYW5-AmTxfIpRThuY_gzYZ4PQC10XaGRrA8-F_"
#url = os.environ['url']
url = "https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/f6c924c2-d722-4c87-80aa-1afa1aa4cf66"

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=IAMAuthenticator(apikey)
)

language_translator.set_service_url(url)

def englishToFrench(english_text):
    """write the code here"""
    translation = language_translator.translate(
    text = english_text,
    model_id='en-fr').get_result()

    french_text = translation['translations'][0]['translation']
    return french_text

def frenchToEnglish(french_text):
    """write the code here"""
    translation = language_translator.translate(
    text = french_text,
    model_id='fr-en').get_result()

    english_text = translation['translations'][0]['translation']
    return english_text
