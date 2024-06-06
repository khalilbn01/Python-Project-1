import random
import time

OPORATORS = ["+","-","*"]
MIN_OPERAND = 3
MAX_OPERAND = 10
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND,MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    oporator = random.choice(OPORATORS)

    expr = str(left) + " " + oporator + " " + str(right)
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press enter to start!")
print("---------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        guess = input("Probme #" + str(i + 1) + ": " +expr + " = ")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
total_time = end_time - start_time

print("---------------------")
print("Nice work! you finished in", total_time, "seconds!")

