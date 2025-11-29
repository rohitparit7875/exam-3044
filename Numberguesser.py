low, high = 1, 100
feedback = ""

print("Think of a number between 1 and 100!")

while feedback != "correct":
    guess = (low + high) // 2
    print(f"My guess is: {guess}")
    feedback = input("Is it too high (h), too low (l), or correct (c)? ").lower()

    if feedback == "h":
        high = guess - 1
    elif feedback == "l":
        low = guess + 1

print("Yay! I guessed your number 😄")
