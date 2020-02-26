def brainfuck_to_c(source_code):
    valid_chars = '+-<>,.[]'
    output = ''
    output2 = ''
    for c in source_code:
        if c in valid_chars:
            if output:
                if c == '+' and output[-1] == '-':
                    output = output[:len(output) - 1]
                    continue
                if c == '-' and output[-1] == '+':
                    output = output[:len(output) - 1]
                    continue
                if c == '<' and output[-1] == '>':
                    output = output[:len(output) - 1]
                    continue
                if c == '>' and output[-1] == '<':
                    output = output[:len(output) - 1]
                    continue
                if c == ']' and output[-1] == '[':
                    output = output[:len(output) - 1]
                    continue
            output += c
    if '[' in output and ']' not in output or ']' in output and '[' not in output:
        return 'Error!'

    print(output)
    count = 1
    for i in range(1, len(output)):
        if output[i - 1] == output[i]:
            count += 1
        else:
            



test1 = "++--+."
test2 = "[][+++]"
test3 = "<>><"
test4 = "[[[]]"

s_c1 = "++++"
s_c2 = "----"

brainfuck_to_c(test1)
brainfuck_to_c(test3)
brainfuck_to_c(test2)
brainfuck_to_c(test4)

