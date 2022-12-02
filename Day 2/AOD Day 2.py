"""
Written by Laurence Taylor for AOC Day 2 Challenge
"""

with open('input.in') as file:
        moves = [i for i in file.read().strip().split("\n")]

player_move = ''
elf_move = ''
score_part1 = 0
score_part2 = 0

#part 1
outcomes_part1 = {
       "A X":4, "A Y":8, "A Z":3,
        "B X":1, "B Y":5, "B Z":9,
        "C X":7, "C Y":2, "C Z":6
}
for move in moves:
        score_part1 += outcomes_part1[move]

print('Part 1 Answer =',score_part1)

#part 2
#A for Rock, B for Paper, and C for Scissors.
#1 for Rock, 2 for Paper, and 3 for Scissors

#X means you need to lose, Y means you need to end the round in a draw, and Z means you need to win
#0 if you lost, 3 if the round was a draw, and 6 if you won

outcomes_part2 = {
       "A X":3, "A Y":4, "A Z":8,
        "B X":1, "B Y":5, "B Z":9,
        "C X":2, "C Y":6, "C Z":7
}

for move in moves:
        score_part2 += outcomes_part2[move]

print('Part 1 Answer =',score_part2)


