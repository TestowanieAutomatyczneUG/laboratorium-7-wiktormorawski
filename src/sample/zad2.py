class Song_lyrics:
    def __init__(self):
        self.lyrics = ['On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree.',
                       'On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree.',
                       'On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                       'On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                       'On the fifth day of Christmas my true love gave to me: five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                       'On the sixth day of Christmas my true love gave to me: six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                       'On the seventh day of Christmas my true love gave to me: seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                       'On the eighth day of Christmas my true love gave to me: eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                       'On the ninth day of Christmas my true love gave to me: nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                       'On the tenth day of Christmas my true love gave to me: ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                       'On the eleventh day of Christmas my true love gave to me: eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.',
                       'On the twelfth day of Christmas my true love gave to me: twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.']

    def byLine(self, line):
        if type(line) == int and len(self.lyrics) > line > 0:
            return self.lyrics[line - 1]
        else:
            return False

    def byLineInterval(self, start, end):
        if type(start) == int and type(end) == int:
            if 0 < start < len(self.lyrics) and start < end <= len(self.lyrics):
                result = ''
                for index in range((start - 1), end):
                    result = result + self.lyrics[index]
                return result
            else:
                raise ValueError('Złe długosci')
        else:
            raise ValueError('Zły typ wprowadzonych danych')
    def All(self):
        result = ''
        for i in range(len(self.lyrics)):
            result = result + self.lyrics[i]
        return result

tmp = Song_lyrics()
print(tmp.byLineInterval(10,12))