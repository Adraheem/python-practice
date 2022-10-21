def get_day(day):
    word = "\nOn the "
    match day:
        case 1:
            word += "first"
        case 2:
            word += "second"
        case 3:
            word += "third"
        case 4:
            word += "forth"
        case 5:
            word += "fifth"
        case 6:
            word += "sixth"
        case 7:
            word += "seventh"
        case 8:
            word += "eighth"
        case 9:
            word += "ninth"
        case 10:
            word += "tenth"
        case 11:
            word += "eleventh"
        case 12:
            word += "twelfth"
    word += " day of Christmas my true love sent to me"
    return word


def get_lyrics(day):
    lyrics = {12: "twelve drummers drumming\n",
              11: "eleven pipers piping\n",
              10: "ten lords a-leaping\n",
              9: "nine ladies dancing\n",
              8: "eight maids a-milking\n",
              7: "seven swans a-swimming\n",
              6: "six geese a-laying\n",
              5: "five gold rings\n",
              4: "four calling birds\n",
              3: "Three French hens\n",
              2: "Two turtle doves\n",
              1: "And a partridge in a pear tree."}

    gifts = ""
    for i in range(day, 0, -1):
        if day == 1:
            gifts += "A" + lyrics[i][5:]
        else:
            gifts += lyrics[i]

    return gifts


def christmas_song():
    for i in range(1, 13):
        print(get_day(i))
        print(get_lyrics(i))
