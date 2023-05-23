import ibm_watson

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator



def englishtofrench(english_text):
    """This class does english to french translation"""

    url_lt ='https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/9cb67f12-c9da-4d02-9b39-39802b132223'
    apikey_lt = 'i2uLBHjnNxXlQGG7FiqUR7kMD4uoVOSl4yYMltyTjpHb'
    version_lt='2018-05-01'
    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    lt = language_translator
    translation = lt.translate(text=english_text, model_id="en-fr").get_result()
    if english_text == " ":
        print("Please enter a word")
    else:
        pass
    return translation['translations'][0]['translation']

def frenchToEnglish(french_text):
    """This class does english to german translation"""

    url_lt = ' https://api.au-syd.language-translator.watson.cloud.ibm.com/instances/9cb67f12-c9da-4d02-9b39-39802b132223'
    apikey_lt = 'i2uLBHjnNxXlQGG7FiqUR7kMD4uoVOSl4yYMltyTjpHb'
    version_lt='2018-05-01'
    authenticator = IAMAuthenticator(apikey_lt)
    language_translator = LanguageTranslatorV3(version=version_lt,authenticator=authenticator)
    language_translator.set_service_url(url_lt)
    lt = language_translator
    translation = lt.translate(text=french_text, model_id="fr-en").get_result()
    return translation['translations'][0]['translation']
