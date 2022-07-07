import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def englishToFrench(englishText):
    #write the code here
    if englishText is None:
        return "" 
    result = language_translator.translate(
        text=englishText, model_id='en-fr').get_result()
    frenchText = result['translations'][0]['translation']
    return frenchText

def frenchToEnglish(frenchText):
    #write the code here
    if frenchText is None:
        return "" 
    result = language_translator.translate(
        text=frenchText, model_id='fr-en').get_result()
    englishText = result['translations'][0]['translation']
    return englishText

print(englishToFrench("Hello"))
print(frenchToEnglish("Oui"))