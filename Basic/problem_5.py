import pyautogui
import time

try:
    rows = int(input("Enter the number of rows for the pyramid: "))
except ValueError:
    print("Invalid input. Please enter an integer.")
    exit()

if rows <= 0:
    print("Please enter a positive number of rows.")
    exit()

# Give some time to switch to a text editor or wi     #
#    ###
#   #####
#  #######
# #########
# #
#    ###
#   #####
#  #######
# #########
# ndow where you want to draw
print("Switch to the window where you want to draw the pyramid in 5 seconds...")
time.sleep(5)

for i in range(1, rows + 1):
    spaces = " " * (rows - i)
    hashes = "#" * (2 * i - 1)
    line = spaces + hashes
    pyautogui.typewrite(line, interval=0.1)  # Adding a small interval between typing
    pyautogui.press('enter')

print(f"Pyramid with {rows} rows drawn.")
