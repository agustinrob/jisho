import hikari
import lightbulb
import csv
import config
from translation import Translation

#START GLOBAL VARIABLES
dead_rows = [0,1]
vocab_arr = []
#END GLOBAL VARIABLES

#START PROCESS CSVs
#START PROCESS MINNA NO NIHONGO 1 VOCAB
with open('csvFiles/minna_vocabulary.csv', 'r', encoding='UTF-8') as vocab:
    reader = csv.reader(vocab)
    for row_id in dead_rows:
        next(reader)

    for row in reader:
        ROMAJI = 1
        KANA = 2
        KANJI = 3
        TRANS_SP = 4
        TRANS_EN = 5
        LESSON = 11
        new_translation = Translation(row[ROMAJI], row[KANA], row[KANJI], row[TRANS_SP], row[TRANS_EN], 'Minna 1 ' + row[LESSON])
        vocab_arr.append(new_translation)

    print(len(vocab_arr))
#END PROCESS MINNA NO NIHONGO 1 VOCAB

#START PROCESS MINNA NO NIHONGO 2 VOCAB
with open('csvFiles/minna2_vocabulary.csv', 'r', encoding='UTF-8') as vocab2:
    reader = csv.reader(vocab2)
    for row_id in dead_rows:
        next(reader)

    for row in reader:
        ROMAJI = 1
        KANA = 2
        KANJI = 3
        TRANS_SP = 4
        TRANS_EN = 5
        LESSON = 11
        new_translation = Translation(row[ROMAJI], row[KANA], row[KANJI], row[TRANS_SP], row[TRANS_EN], 'Minna 2 ' + row[LESSON])
        vocab_arr.append(new_translation)

    print(len(vocab_arr))
#END PROCESS MINNA NO NIHONGO 2 VOCAB

#END PROCESS CSVs

#START AUX FUNCTIONS
def findTranslation(arr, attr, keyword):
    found_trans = ''
    for trans in arr:
        if trans.getValue(attr).lower().strip() == keyword.lower():
            found_trans = trans
            break
    
    return found_trans

def generateResponse(found_trans):
    response = ''
    if found_trans != '':
        response = str(found_trans)
    else:
        response = "Lo siento :-( Traduccion no encontrada."
    
    return response

#END AUX FUNCTIONS

#START BOT STARTUP
bot = lightbulb.BotApp(
    token=config.access_token, 
    default_enabled_guilds=(862367125481324585)
)

@bot.listen(hikari.StartedEvent)
async def bot_started(event):
    print('Bot has started!')
    print(len(vocab_arr))
#END BOT STARTUP

#START BOT COMMANDS
@bot.command
@lightbulb.command('jisho', 'Encontrar traducciones de vocabulario, expresiones y kanjis.')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def jisho(context):
    pass

@jisho.child
@lightbulb.option('romaji_input', 'Romaji a buscar.')
@lightbulb.command('buscar_romaji', 'Obtener informacion a partir del Romaji.')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def busca_romaji(context):
    found_trans = findTranslation(vocab_arr, "romaji", context.options.romaji_input)
    response = generateResponse(found_trans)
    await context.respond(response)

@jisho.child
@lightbulb.option('kana_input', 'Hiragana/Katakana a buscar.')
@lightbulb.command('buscar_kana', 'Obtener informacion a partir del Hiragana/Katakana.')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def busca_kana(context):
    found_trans = findTranslation(vocab_arr, "kana", context.options.kana_input)
    response = generateResponse(found_trans)
    await context.respond(response)

@jisho.child
@lightbulb.option('kanji_input', 'Kanji a buscar.')
@lightbulb.command('buscar_kanji', 'Obtener informacion a partir del Kanji.')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def busca_kanji(context):
    found_trans = findTranslation(vocab_arr, "kanji", context.options.kanji_input)
    response = generateResponse(found_trans)
    await context.respond(response)

#END BOT COMMANDS

bot.run()