def get_day(day):
    word = "\nOn the "
    match day:
        case 1: word += "first"
        case 2: word += "second"
        case 3: word += "third"
        case 4: word += "forth"
        case 5: word += "fifth"
        case 6: word += "sixth"
        case 7: word += "seventh"
        case 8: word += "eighth"
        case 9: word += "ninth"
        case 10: word += "tenth"
        case 11: word += "eleventh"
        case 12: word += "twelfth"
    word += " day of Christmas my true love sent to me"
    return word


def get_lyrics(day):
    lyrics = ""

    if day >= 12:
        lyrics += "twelve drummers drumming\n"
    if day >= 11:
        lyrics += "eleven pipers piping\n"
    if day >= 10:
        lyrics += "ten lords a-leaping\n"
    if day >= 9:
        lyrics += "nine ladies dancing\n"
    if day >= 8:
        lyrics += "eight maids a-milking\n"
    if day >= 7:
        lyrics += "seven swans a-swimming\n"
    if day >= 6:
        lyrics += "six geese a-laying\n"
    if day >= 5:
        lyrics += "five gold rings\n"
    if day >= 4:
        lyrics += "four calling birds\n"
    if day >= 3:
        lyrics += "Three French hens\n"
    if day >= 2:
        lyrics += "Two turtle doves\n"
    if day >= 1:
        lyrics += "And a partridge in a pear tree."

    return lyrics


def christmas_song():
    for i in range(1, 13):
        print(get_day(i))
        print(get_lyrics(i))
