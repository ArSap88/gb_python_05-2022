class DivideByNull:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return divider / denominator
        except:
            return f'Unable to divide by zero'


div = DivideByNull(10, 100)
print(DivideByNull.divide_by_null(10, 0))
print(DivideByNull.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))
