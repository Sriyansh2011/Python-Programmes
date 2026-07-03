# ---- algorithm analysis -- counting game points
# Topics: Algorithm , Pseudocode,Time complexity,Space complexity,One problem 3 solutions,Comparing Efficiency

#PART 1: The Problem - set n = 4 rounds
#in a game: Round 1 = 1 point,  Round 2 = 2 ponts,... round n=n points.
#we will solve "find the total" three ways and count the steps each one takes.

n = 4
print("=== Counting Game Points(n=",n,"rounds)===")
print()

#PART 2: Formula way - always 1 step
# Algorithm : Use the shortcut formula to get the answer instantly
# Pseudocode : total = n*(n+1)/2
#Time cost : 1 step - stays the same no matter how big n is
#space cost : 1 variable(total)

total = n * (n+1)//2
print("Formula way: total=",total,"steps = 1")

# PART 3 : Loop way - n steps
# Algorithm : Add each round's points one by one using a loop
# Pseudocode : For round from 1 to n: total = total + round
# Time cost : n steps - grows with the number of rounds
# Space cost : 2 variables (total,round_num)

total = 0
steps = 0
for round_num in range(1,n+1):
    total += round_num
    steps += 1
print("Loop way   : total =",total,"steps =",steps)

# PART 4: Nested Loop way - roughly n*n steps
# Algorithm : add 1 at a time for every single point in every round
# Pseudocode : For round from 1 to n: For point from 1 to round:total += 1
# Time cot : Roughly n*n steps - explodes as n grows!
# space cost : 3 variables (total,round_num,point)

total = 0
steps = 0
for round_num in range(1,n+1):
    for point in range(1,round_num + 1):
        total += 1
        steps += 1
print("Nested loop: total=",total," steps =",steps)

# PART 5 : try n = 10 and see what happens to the steps

n = 10
nested_steps=0
for round_num in range (1,n+1):
    for point in range(1,round_num+1):
        nested_steps += 1

print()
