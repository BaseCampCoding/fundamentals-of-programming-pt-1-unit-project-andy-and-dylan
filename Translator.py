import googletrans
from googletrans import Translator


a = [
    "af",
    "sq",
    "am",
    "ar",
    "hy",
    "az",
    "eu",
    "be",
    "bn",
    "bs",
    "bg",
    "ca",
    "ceb",
    "ny",
    "zh-cn",
    "zh-tw",
    "co",
    "hr",
    "cs",
    "da",
    "nl",
    "en",
    "eo",
    "et",
    "tl",
    "fi",
    "fr",
    "fy",
    "gl",
    "ka",
    "de",
    "el",
    "gu",
    "ht",
    "ha",
    "haw",
    "iw",
    "he",
    "hi",
    "hmn",
    "hu",
    "is",
    "ig",
    "id",
    "ga",
    "it",
    "ja",
    "jw",
    "kn",
    "kk",
    "km",
    "ko",
    "ku",
    "ky",
    "lo",
    "la",
    "lv",
    "lt",
    "lb",
    "mk",
    "mg",
    "ms",
    "ml",
    "mt",
    "mi",
    "mr",
    "mn",
    "my",
    "ne",
    "no",
    "or",
    "ps",
    "fa",
    "pl",
    "pt",
    "pa",
    "ro",
    "ru",
    "sm",
    "gd",
    "sr",
    "st",
    "sn",
    "sd",
    "si",
    "sk",
    "sl",
    "so",
    "es",
    "su",
    "sw",
    "sv",
    "tg",
    "ta",
    "te",
    "th",
    "ty",
    "uk",
    "ur",
    "ug",
    "uz",
    "vi",
    "cy",
    "xh",
    "yi",
    "yo",
    "zu",
]

b = [
    "afrikaans",
    "albanian",
    "amharic",
    "arabic",
    "armenian",
    "azerbaijani",
    "basque",
    "belarusian",
    "bengali",
    "bosnian",
    "bulgarian",
    "catalan",
    "cebuano",
    "chichewa",
    "chinese (simplified)",
    "chinese (traditional)",
    "corsican",
    "croatian",
    "czech",
    "danish",
    "dutch",
    "english",
    "esperanto",
    "estonian",
    "filipino",
    "finnish",
    "french",
    "frisian",
    "galician",
    "georgian",
    "german",
    "greek",
    "gujarati",
    "haitian creole",
    "hausa",
    "hawaiian",
    "hebrew",
    "hebrew",
    "hindi",
    "hmong",
    "hungarian",
    "icelandic",
    "igbo",
    "indonesian",
    "irish",
    "italian",
    "japanese",
    "javanese",
    "kannada",
    "kazakh",
    "khmer",
    "korean",
    "kurdish (kurmanji)",
    "kyrgyz",
    "lao",
    "latin",
    "latvian",
    "lithuanian",
    "luxembourgish",
    "macedonian",
    "malagasy",
    "malay",
    "malayalam",
    "maltese",
    "maori",
    "marathi",
    "mongolian",
    "myanmar (burmese)",
    "nepali",
    "norwegian",
    "odia",
    "pashto",
    "persian",
    "polish",
    "portuguese",
    "punjabi",
    "romanian",
    "russian",
    "samoan",
    "scots gaelic",
    "serbian",
    "sesotho",
    "shona",
    "sindhi",
    "sinhala",
    "slovak",
    "slovenian",
    "somali",
    "spanish",
    "sundanese",
    "swahili",
    "swedish",
    "tajik",
    "tamil",
    "telugu",
    "thai",
    "turkish",
    "ukrainian",
    "urdu",
    "uyghur",
    "uzbek",
    "vietnamese",
    "welsh",
    "xhosa",
    "yiddish",
    "yoruba",
    "zulu",
]

translation_langs = []

print_languages = input(
    "Welcome to the translator there are currently 106 languages supported, would you like to see them? [Y/N] "
).lower()

if print_languages == "y":
    print(
        """
abbreviations\tLanguages"""
    )

    for x, y in zip(a, b):
        print(x, y, sep="=")

if print_languages == "n":
    pass

FILE = input("Would you like to translate from a file [Y/N] ").lower()
if FILE == "y":
    options = input("Would you like to translate in multiple languages? [Y/N] ").lower()
    if options == "y":
        multiple_langs = int(input("How many languages do you want? "))
        FILE_NAME = input("What is the file name: ")
        while multiple_langs > 0:
            Langs = input("Please input one of the languages: ")
            translation_langs.append(Langs)
            multiple_langs -= 1
        i = 0
        while i < len(translation_langs):
            f = open(FILE_NAME, "r")
            read_file = f.read()
            translator = Translator()
            translated = translator.translate(read_file, dest=translation_langs[i])
            print(translated.text)
            i += 1

    if options == "n":
        Lang = input("What language would you like to translate the file to: ")
        FILE_NAME = input("What is the file name: ")
        f = open(FILE_NAME, "r")
        read_file = f.read()
        translator = Translator()
        translated = translator.translate(read_file, dest=Lang)
        print(translated.text)
        print(translated)

elif FILE == 'n':
    options = input('Would you like to translate in multiple languages [Y/N] ').lower()
    if options == 'y':
        phrase = input('What would you like to translate: ')
        multiple_langs = int(input("How many languages do you want? "))
       
        while multiple_langs > 0:
            Langs = input("Please input one of the languages: ")
            translation_langs.append(Langs)
            multiple_langs -= 1
        i = 0
        while i < len(translation_langs):
            translator = Translator()
            translated = translator.translate(phrase, dest=translation_langs[i])
            print(translated.text)
            i += 1
    elif options == 'n':
        phrase = input('What would you like to translate: ')
        Lang = input("What language would you like to translate to: ")
        translator = Translator()
        translated = translator.translate(phrase, dest=Lang)
        print(translated.text)

