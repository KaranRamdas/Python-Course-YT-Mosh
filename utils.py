class Numbers:

    def __init__(self, numbers):
        self.numbers = numbers

    def find_max(self):
        max_num = self.numbers[0]

        for number in self.numbers:
            if number > max_num:
                max_num = number

        return max_num