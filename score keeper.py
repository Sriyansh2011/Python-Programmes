# Score tracker
# Topics: Asymptotic Analysis / Big-O / Omega / Theta / Best / Worst / Average Case / O(1) O(n) O(n**2)

# - PART 1 : The leaderboard
# 5 player and their scores.we will run 3 operations
# and classify each one with formal asymtotic notation.

names = ["Aarav","Priya","Dev","Meera","Kabir"]
scores = [90,75,88,62,95]
n = len(scores)
print("=== Score tracker (n=",n,"players)===")
for i in range(n):
    print(i+1,".",names[i],":",scores[i],sep="")
print()

# PART 2: Theta(1)-direct index access
#get the score at position 0: always exactly 1 step.
#Best case=worst case=exactly 1that is theta(1) - a tight bound.
# tHEA COST never changes no matter how many players there are.

steps = 1
print("Score at index 0 :",scores[0]," steps =",steps," Theta(1) - tight bound")
print()

# PART 3: O(n) - linear search best and worst case
# Omega(1) is best case
#O(n) is worst case

target="Aarav"
steps=0
for name in names:
    steps+= 1
    if name == target:
        break
print("Search for",target," steps =",steps," Omega(1) - best case lower bound")
target ="Kabir"
steps=0
for name in names:
    steps += 1
    if name == target:
        break
print("search for",target," steps =", steps, "O(n) =",n, "-worst case upper bound")

# PART 4: O(n**2)

steps = 0
target_sum = 150
print(" Pairs with total score =", target_sum, ":")
for i in range(n):
    for j in range(i + 1,n):
        steps += 1
        if scores[i] + scores[j] == target_sum:
            print(" ",names[i],"+",names[j],"=",scores[i]+scores[j])
print("Total comparisions :",steps, " O(n**2) - drop constants, keep n**2")
print()

