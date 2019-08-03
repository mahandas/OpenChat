from googletrans import Translator
import hyper.http20.exceptions as hpy

translator = None

LANGUAGES = {
    'af': 'afrikaans',
    'sq': 'albanian',
    'am': 'amharic',
    'ar': 'arabic',
    'hy': 'armenian',
    'az': 'azerbaijani',
    'eu': 'basque',
    'be': 'belarusian',
    'bn': 'bengali',
    'bs': 'bosnian',
    'bg': 'bulgarian',
    'ca': 'catalan',
    'ceb': 'cebuano',
    'ny': 'chichewa',
    'zh-cn': 'chinese (simplified)',
    'zh-tw': 'chinese (traditional)',
    'co': 'corsican',
    'hr': 'croatian',
    'cs': 'czech',
    'da': 'danish',
    'nl': 'dutch',
    'en': 'english',
    'eo': 'esperanto',
    'et': 'estonian',
    'tl': 'filipino',
    'fi': 'finnish',
    'fr': 'french',
    'fy': 'frisian',
    'gl': 'galician',
    'ka': 'georgian',
    'de': 'german',
    'el': 'greek',
    'gu': 'gujarati',
    'ht': 'haitian creole',
    'ha': 'hausa',
    'haw': 'hawaiian',
    'iw': 'hebrew',
    'hi': 'hindi',
    'hmn': 'hmong',
    'hu': 'hungarian',
    'is': 'icelandic',
    'ig': 'igbo',
    'id': 'indonesian',
    'ga': 'irish',
    'it': 'italian',
    'ja': 'japanese',
    'jw': 'javanese',
    'kn': 'kannada',
    'kk': 'kazakh',
    'km': 'khmer',
    'ko': 'korean',
    'ku': 'kurdish (kurmanji)',
    'ky': 'kyrgyz',
    'lo': 'lao',
    'la': 'latin',
    'lv': 'latvian',
    'lt': 'lithuanian',
    'lb': 'luxembourgish',
    'mk': 'macedonian',
    'mg': 'malagasy',
    'ms': 'malay',
    'ml': 'malayalam',
    'mt': 'maltese',
    'mi': 'maori',
    'mr': 'marathi',
    'mn': 'mongolian',
    'my': 'myanmar (burmese)',
    'ne': 'nepali',
    'no': 'norwegian',
    'ps': 'pashto',
    'fa': 'persian',
    'pl': 'polish',
    'pt': 'portuguese',
    'pa': 'punjabi',
    'ro': 'romanian',
    'ru': 'russian',
    'sm': 'samoan',
    'gd': 'scots gaelic',
    'sr': 'serbian',
    'st': 'sesotho',
    'sn': 'shona',
    'sd': 'sindhi',
    'si': 'sinhala',
    'sk': 'slovak',
    'sl': 'slovenian',
    'so': 'somali',
    'es': 'spanish',
    'su': 'sundanese',
    'sw': 'swahili',
    'sv': 'swedish',
    'tg': 'tajik',
    'ta': 'tamil',
    'te': 'telugu',
    'th': 'thai',
    'tr': 'turkish',
    'uk': 'ukrainian',
    'ur': 'urdu',
    'uz': 'uzbek',
    'vi': 'vietnamese',
    'cy': 'welsh',
    'xh': 'xhosa',
    'yi': 'yiddish',
    'yo': 'yoruba',
    'zu': 'zulu',
    'fil': 'Filipino',
    'he': 'Hebrew'
}

LANGCODES = dict(map(reversed, LANGUAGES.items()))

def getLanguage_fromcode(langcode):
    try:
      return LANGUAGES[langcode]
    except KeyError:
        return "INVALIDKEY"
    except:
        return "ERROR"


def getLanguagelist_fromcode(langcodes):
    Langs = []
    try:
        for langcode in langcodes:
            Langs.append(LANGUAGES[langcode])
        return Lang
    except KeyError:
        return Langs.append("INVALIDKEY")
    except:
        return Langs.append("ERROR")

def getLanguageCode(language):
    try:
      return LANGCODES[language]
    except KeyError:
        return "INVALIDKEY"
    except:
        return "ERROR"


def getLanguageCode_list(languages):
    LanguageCodes = []
    try:
        for language in languages:
            LanguageCodes.append(LANGCODES[language])
        return Languages
    except KeyError:
        return LanguageCodes.append("INVALIDKEY")
    except:
        return LanguageCodes.append("ERROR")

def getSupportedLanguages():
    return LANGUAGES

def tanslatedata(requestdata, responseLanguage):
    try:
        translator = Translator()
        return((translator.translate(requestdata,dest=responseLanguage , src='auto')).text)
    except ValueError:
        return "LANGUAGEINCORRECT"
    except hpy.StreamResetError:
        return "NETWORKERROR"


def tanslatedatafromList(requestdata, responseLanguage):
    TranslatedResponseList = []
    try:
        translator = Translator()
        translateresp = translator.translate(str(requestdata),dest=str(responseLanguage))
        for resp in translatedresp:
            TranslatedResponseList.append(resp)
        return TranslatedResponseList
    except ValueError:
        return "LANGUAGEINCORRECT"
    except hpy.StreamResetError:
        return "NETWORKERROR"
    except:
        return "ERROR"



