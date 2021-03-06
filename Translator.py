def main():
    import googletrans
    from googletrans import Translator
    import os.path

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
        "tr",
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

    def print_lang():
        print_languages = input(
            "There are currently 106 languages supported, would you like to see them? [Y/N] "
        ).lower()
        if print_languages == "y":
            print(
                """
                Abbreviations & Languages"""
            )
            for x, y in zip(a, b):
                print(x, y, sep=" - ")
        elif print_languages == "n":
            pass
        else:
            print("Invalid input. Try again.")
            print_lang()

    print_lang()

    def File():
        FILE = input("\nWould you like to translate from a file? [Y/N] ").lower()

        if FILE == "y":
            options = input("Would you like to translate in multiple languages? [Y/N] ")

            if options == "y":
                multiple_langs = int(input("How many languages do you want? "))

                while multiple_langs > 0:
                    Langs = input("Please input one of the languages: ").lower()
                    while Langs not in googletrans.LANGUAGES and Langs not in b:
                        print(
                            "Invalid language. Please look at the supported languages."
                        )
                        Langs = input("Please input one of the languages: ").lower()
                    translation_langs.append(Langs)
                    multiple_langs -= 1

                path = input("Input the directory to the file: ")
                isExist = os.path.exists(path)
                while isExist == False:
                    print("Invalid file or directory try again.")
                    path = input("Input the directory to the file: ")
                    isExist = os.path.exists(path)

                i = 0
                while i < len(translation_langs):
                    f = open(path, "r")
                    read_file = f.read()
                    translator = Translator()
                    translated = translator.translate(
                        read_file, dest=translation_langs[i]
                    )
                    print(translated.text)
                    i += 1
                mainloop()

            elif options == "n":
                Lang = input(
                    "What language would you like to translate the file to? "
                ).lower()
                while Lang not in googletrans.LANGUAGES and Lang not in b:
                    print("Invalid language. Please look at the supported languages.")
                    Lang = input("Please input the language: ").lower()

                path = input("Input the directory to the file: ")
                isExist = os.path.exists(path)
                while isExist == False:
                    print("Invalid file or directory try again.")
                    path = input("Input the directory to the file: ")
                    isExist = os.path.exists(path)

                f = open(path, "r")
                read_file = f.read()
                translator = Translator()
                translated = translator.translate(read_file, dest=Lang)
                print(translated.text)
                mainloop()
            else:
                print("Invalid input. Please try again.")
                File()

        elif FILE == "n":
            options = input(
                "Would you like to translate in multiple languages? [Y/N] "
            ).lower()

            if options == "y":
                phrase = input("What would you like to translate? ")
                multi_lang = None
                while multi_lang is None or multi_lang < 0:
                    multiple_langs = input("How many languages do you want? ")
                    try:
                        multi_lang = int(multiple_langs)
                    except ValueError:
                        print("Invalid input. Please try again.")
                        continue
                    if multi_lang < 0:
                        print("Invalid input. Please try again.")
                    while multi_lang > 0:
                        Langs = input("Please input one of the languages: ").lower()
                        while Langs not in googletrans.LANGUAGES and Langs not in b:
                            print(
                                "Invalid language. Please look at the supported languages."
                            )
                            Langs = input("Please input one of the languages: ").lower()
                        translation_langs.append(Langs)
                        multi_lang -= 1
                    i = 0
                    while i < len(translation_langs):
                        translator = Translator()
                        translated = translator.translate(phrase, dest=translation_langs[i])
                        print(translated.text)
                        i += 1
                mainloop()

            elif options == "n":
                phrase = input("What would you like to translate? ")
                Lang = input("What language would you like to translate to? ")

                while Lang not in googletrans.LANGUAGES and Lang not in b:
                    print("Invalid language. Please look at the supported languages.")
                    Lang = input("Please input the language: ")

                translator = Translator()
                translated = translator.translate(phrase, dest=Lang)
                print(translated.text)
                mainloop()
            else:
                print("Invalid input. Please try again")
                File()
        else:
            print("Invalid input. Please try again.")
            File()

    File()


def mainloop():
    answer = str(input("\nWould you like to translate anything else? [Y/N] ").lower())
    if answer == "y":
        main()
    elif answer == "n":
        print("Goodbye.")
        quit()
    else:
        print("Im sorry what was that?")
        mainloop()


main()
