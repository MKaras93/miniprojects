''' aim is to generate a random file with blank lines in random places. If there are a few lines in a row, they will
have to be in the same file. '''
import random


def generate_file(path):
    line_sequence = ('Wlazł kotek na płotek i mruga; Wlazł kotek na płotek i mruga; Wlazł kotek na płotek i mruga',
                     'Ładna to piosenka niedługa; Ładna to piosenka niedługa; Ładna to piosenka niedługa',
                     'Niedługa niekrótka ale starczy; Niedługa niekrótka ale starczy; Niedługa niekrótka ale starczy')
    lines_count = 10 # random.randint(1000, 5000)
    new_line_num = 0
    line_var = 0
    with open(path, 'w') as file:
        for line_num in range(1, lines_count+1):
            if line_num % 4 == 0:
                line = ''
                line_var = 0
            else:
                new_line_num += 1
                line = str(new_line_num) + ' ' + line_sequence[line_var]
                line_var += 1
            file.write(line + '\n')


generate_file('test_textfile.txt')
