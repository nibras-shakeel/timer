import time  
import random  
print("Players stand!")

sleep_time = random.randint(10, 25)

sit_down_list = []

print(f"You have between 10 and 25 seconds to sit down.")
print("Enter the names of players who sit down one by one.")
print("When no more players will sit down, type 'finish'.")
start_time=time.time()

while time.time() - start_time < sleep_time:
    player = input("Enter player's name who sat down (or type 'finish' to stop): ")
    if player.lower() == 'finish':
        break
    sit_down_list.append(player)