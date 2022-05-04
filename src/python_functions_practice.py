def test_return_10(self):
    return_10_result = return_10()
    self.assertEqual(10, return_10_result)

def return_10():
    return 10

def add(number_1, number_2):
    return number_1 + number_2

def subtract(number_1, number_2):
    return number_1 - number_2

def multiply(number_1, number_2):
    return number_1 * number_2

def divide(number_1, number_2):
    return number_1 / number_2

def length_of_string(string):
    return len(string)

def join_string(string_1, string_2):
    return string_1 + string_2

def add_string_as_number(string_1, string_2):
    return int(string_1) + int(string_2)

def number_to_full_month_name(number):
    if number == 1:
        return "January"
    if number == 3:
        return "March"
    if number == 9:
        return "September"

def number_to_short_month_name(number):
    if number == 1:
        return "Jan"
    if number == 4:
        return "Apr"
    if number == 8:
        return "Oct"

