# Python3 translator
This is a translator written in Python3 it sopports up to 106 languages 

## Getting Started 

### Prerequisites
- Python3
- Googletrans module `pip install googletrans`

### Running
After you have Python3 and googletranslate installed you can run the `translator.py`. You can read a file and translate them into multiple langauages or single langauages, you can see all supported languages and or translate any text into any language
```
>>> Would you like to see all supported langauged [Y/N]: N
>>> Would you like to translate a file [Y/N]: N
>>> Multiple languages [Y/N]: N
>>> What would you like to translate? Hello how are you?
>>> What language: ja
こんにちは、元気ですか?
```

### Google Trans Module
Currently the GoogleTrans module is broken and you will recieve an error when trying to translate information. The unoffical fix is to `pip install googletrans==4.0.0-rc1`
