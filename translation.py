class Translation:
    def __init__(self, romaji, kana, kanji, trans_sp, trans_en, lesson):
        self.romaji = romaji
        self.kana = kana
        self.kanji = kanji
        self.trans_sp = trans_sp
        self.trans_en = trans_en
        self.lesson = lesson

    def __str__(self):
        message = "| Romaji: " + self.romaji + " |\n" 
        message += "| Hiragana/Katakana: " + self.kana + " |\n" 
        message += "| Kanji: " + self.kanji + " |\n" 
        message += "| Traducción Español: " + self.trans_sp + " |\n" 
        message += "| Traducción Inglés: " + self.trans_en + " |\n" 
        message += "| Lección: " + self.lesson + " |" 
        return message

    def romaji(self):
        return self.__romaji

    def kana(self):
        return self.__kana

    def kanji(self):
        return self.__kanji

    def getValue(self, param): 
        if(param == "romaji"):
            return self.romaji
        if(param == "kana"):
            return self.kana
        if(param == "kanji"):
            return self.kanji