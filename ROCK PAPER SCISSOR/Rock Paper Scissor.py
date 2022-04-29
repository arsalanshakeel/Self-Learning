from os import system
from random import randint

score = {'player':0, 'cpu':0}
choices = 'Rock', 'Paper', 'Scissor'
verbs = 'smashes', 'covers', 'cut'
match = 'Tie', 'Win', 'Lose'
msg = '\nMake your choice:\n\t1.Rock\n\t2.Paper\n\t3.Scissor\n'
final_msg = '\nFinal Scores:\n\tCPU = {cpu} \n\tPlayer = {player}'

while (player := input(msg)) != 'end':
    player = int(player) - 1
    cpu = randint(0, 2)

    print(f'\nCPU plays {choices[cpu]}')
    input()
    point = match[(player - cpu) % 3]

    if point == 'Tie':
        print("TIE!")
    elif point == 'Win':
        print(f'You Win! {choices[player]} {verbs[player]} {choices[cpu]}')
        score['player'] += 1
    else:
        print(f'You Lose! {choices[cpu]} {verbs[cpu]} {choices[player]}')
        score['cpu'] += 1


print(final_msg.format(cpu=score['cpu'], player=score['player']))

