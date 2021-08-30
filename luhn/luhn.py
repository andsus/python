class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ","")

    def valid(self):
        if len(self.card_num) < 2:
            return False
        parity = len(self.card_num)%2 == 0
        sum = 0
        for c in self.card_num:
            if not c.isdigit():
                return False
            digit = int(c)
            if parity:
                digit *= 2
                if digit > 9:
                    digit -= 9
            sum += digit
            parity = not parity
        return sum%10 == 0

