Internationalize your bot
Step 1: extract texts
    pybabel extract --input-dirs=. -o ./counties_bot/interface/locales/counties_bot.pot

Step 2: create *.po files. E.g. create en, ru, uk locales.
    pybabel init -i ./counties_bot/interface/locales/counties_bot.pot -d locales -D counties_bot -l en
    pybabel init -i ./counties_bot/interface/locales/counties_bot.pot -d locales -D counties_bot -l ru 
   
Step 3: translate texts located in locales/{language}/LC_MESSAGES/mybot.po
    To open .po file you can use basic text editor or any PO editor, e.g. https://poedit.net/
Step 4: compile translations
    # pybabel compile -d locales -D mybot
Step 5: When you change the code of your bot you need to update po & mo files.
    Step 5.1: regenerate pot file:
        command from step 1
    Step 5.2: update po files
        pybabel update -d ./counties_bot/interface/locales -D counties_bot -i ./counties_bot/interface/locales/counties_bot.pot 
    Step 5.3: update your translations 
        location and tools you know from step 3
    Step 5.4: compile mo files
        command from step 4