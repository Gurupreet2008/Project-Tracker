# This is project Timer.
import time

# Timer Function
def timer(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        print(f"{mins:02d}:{secs:02d}", end="\r")
        time.sleep(1)
        seconds -= 1

# Take Focus Targets
print("What's your today's target: ")
print("NOTE: Type your target in sequence. Type 'submit' to finish.")

targets = []
while True:
    target = input(f"{len(targets)+1}. ")
    if target.lower() == "submit":
        break
    targets.append(target)

print("\nYour targets:")
for Index, target in enumerate(targets, 1):
    iterated_target = print(f"{Index}. {target}")

while True:
    indexing = 0
    print("Let's do:\nTarget: ")

    # Focus Timer Input
    print("\nEnter total focus time in minutes:")

    focus_time = int(input("Focus time: "))
    # Pomodoro Loop
    while focus_time >= 25:
        print("\nFocus session started (25 min)")
        timer(25)
        focus_time -= 25
        print("Focus session ended. Time for a 5 min break!\n")
        
        if focus_time >= 5:
            timer(5)
            focus_time -= 5
            print("Break over! Get ready for next focus session.\n")
        else:
            print("Not enough time left for a full break. Ending session.")
            break

    # Final remaining time
    if 0 < focus_time < 25:
        print(f"\nThis is short focus session for {focus_time} minutes.")
        timer(focus_time)
    

