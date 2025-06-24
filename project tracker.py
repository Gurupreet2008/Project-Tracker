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
    # Focus Timer Input
    print("NOTE: Type done or exit to exit the timer.")
    print("\nEnter total focus time in minutes:")

    focus_time = input("Focus time: ")
    try:
        str_focus_time = str(focus_time)
        if str_focus_time.lower() == "done" or str_focus_time.lower() == "exit" :
            break
        else:
            raise ValueError("Enter the valid value.")

    except:
        pass
    
    try:
        focus_time = int(focus_time)

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
    except ValueError:
        print("Please enter a valid number for focus time.")
    

