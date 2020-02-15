# Analog digit counter
def presses(phrase):
    BUTTONS = ['1', 'abc2', 'def3',
               'ghi4', 'jkl5', 'mno6',
               'pqrs7', 'tuv8', 'wxyz9',
               '*', ' 0', '#']
    return (sum(1 + button.find(c) for c in phrase.lower() for button in BUTTONS if c in button))


presses('test')
presses("LOL")
presses("HOW R U")
