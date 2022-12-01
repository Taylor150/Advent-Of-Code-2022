with open('input.in') as file:
        data = [i for i in file.read().strip().split("\n")]

elf_list = []
elf = 0

for item in data:
        if item == '':
                elf = 0
        else:
                num = int(item)
                elf += num
                elf_list.append(elf)

#part 1
print("Part 1 Answer " + str(max(elf_list)))

#part 2

top3elves = sorted(elf_list, reverse=True)
print("Part 2 Answer " + str((top3elves[0]) + (top3elves[1]) + (top3elves[2])))
