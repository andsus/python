PHRASES = [
        "twelve Drummers Drumming, ",
        "eleven Pipers Piping, ",
        "ten Lords-a-Leaping, ",
        "nine Ladies Dancing, ",
        "eight Maids-a-Milking, ",
        "seven Swans-a-Swimming, ",
        "six Geese-a-Laying, ",
        "five Gold Rings, ",
        "four Calling Birds, ",
        "three French Hens, ",
        "two Turtle Doves, ",
        "{}a Partridge in a Pear Tree."
    ]
DAYS = { 1:'first', 2:'second', 3:'third', 4:'fourth', 5:'fifth', 6:'sixth',
         7:'seventh', 8:'eighth', 9:'ninth', 10:'tenth', 11:'eleventh', 12:'twelfth' }    

def build_recite(day):
    recite = "On the {0} day of Christmas my true love gave to me: ".format(DAYS[day]) 
    zero_day = PHRASES[-1].format("" if day == 1 else "and " )
    recite += "".join(PHRASES[12-day:-1]) + zero_day
    return recite

def recite(start_verse, end_verse):
    return [build_recite(i) for i in range(start_verse, end_verse+1)]
    