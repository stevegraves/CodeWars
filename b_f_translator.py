# Not correct

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
    if output == '':
        return ''

    # print(output)
    count = 1
    for i in range(1, len(output)):
        if output[i - 1] == output[i]:
            count += 1
            if output[i - 1] == '.':
                output2 += 'putchar(*p);\n'
            if output[i - 1] == ',':
                output2 += '*p = getchar();\n'
            if output[i - 1] == '[':
                output2 += 'if (*p) do {\n  '
            if output[i - 1] == ']':
                output2 += '} while (*p);\n'
        else:
            if output[i - 1] == '+':
                output2 += '*p += {};\n'.format(count)
            if output[i - 1] == '-':
                output2 += '*p -= {};\n'.format(count)
            if output[i - 1] == '<':
                output2 += 'p -= {};\n'.format(count)
            if output[i - 1] == '>':
                output2 += 'p += {};\n'.format(count)
            if output[i - 1] == '.':
                output2 += 'putchar(*p);\n'
            if output[i - 1] == ',':
                output2 += '*p = getchar();\n'
            if output[i - 1] == '[':
                output2 += 'if (*p) do {\n  '
            if output[i - 1] == ']':
                output2 += '} while (*p);\n'
            count = 1
    if output[-1] == '+':
        output2 += '*p += {};\n'.format(count)
    if output[-1] == '-':
        output2 += '*p -= {};\n'.format(count)
    if output[-1] == '<':
        output2 += 'p -= {};\n'.format(count)
    if output[-1] == '>':
        output2 += 'p += {};\n'.format(count)
    if output[-1] == '.':
        output2 += 'putchar(*p);\n'
    if output[-1] == ',':
        output2 += '*p = getchar();\n'
    if output[-1] == '[':
        output2 += 'if (*p) do {\n  '
    if output[-1] == ']':
        output2 += '} while (*p);\n'

    print(output2)
    return output2


test1 = "++--+."
test2 = "[][+++]"
test3 = "<>><"
test4 = "[[[]]"

s_c1 = "++++"
s_c2 = "----"

brainfuck_to_c(test1)
# brainfuck_to_c(test3)
brainfuck_to_c(test2)
brainfuck_to_c(s_c1)
