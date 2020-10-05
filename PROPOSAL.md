# Proposal

## Language Translator

### Description and Motivation
The purpose of this program is to translate any language into another language of your choice.
This is possible with the help of importing translate onto the program.you can redirect a file if you want to read it in a different language,there are 71 languages you can choose from.

### Prior Art
Many translasting applications exist, you input what you want and select the langauge output. We aren't remaking how translating works but we will have things different than others. We will be making a translating project with *googletrans 3.0.0*. We chose *googletrans 3.0.0* beacuse its updated and is known.

The user will input what they want and select the language. This is the basics of every translating application, the user will also be able to translate items from a file. Smart translating from *googletrans 3.0.0* will detect the language you are speaking in and translate to the desired language.


## Core User Workflows
- User input
  - The user will first be asked if they would like to translate from a file and depending what they respond with will prompt the other options. If yes they will be asked what langauge and what is the file called. If no will move on the the next prompt.
   - The user will be asked if they want multiple translation if yes it will ask for 3 langauges to be translated to and if no the script continues.
  - The user will be prompted to select a language, they will select the language desired if the language doesn't exist or isnt compatiable they will be prompted with *invalid language* and will be asked to select a language.
  - After the desired input is translated they will be asked if anything else is translated depending on the input it will restart with asking if they want to read from a file and select a language. If yes then it loops, if no the program will exit
  
