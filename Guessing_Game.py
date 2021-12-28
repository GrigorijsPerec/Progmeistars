from colorama import init
from colorama import Fore, Back, Style
init()

print(Fore.LIGHTRED_EX + """
      _______  __    __   _______      _______.     _______. __  .__   __.   _______ 
     /  _____||  |  |  | |   ____|    /       |    /       ||  | |  \ |  |  /  _____|
    |  |  __  |  |  |  | |  |__      |   (----`   |   (----`|  | |   \|  | |  |  __  
    |  | |_ | |  |  |  | |   __|      \   \        \   \    |  | |  . `  | |  | |_ | 
    |  |__| | |  `--'  | |  |____ .----)   |   .----)   |   |  | |  |\   | |  |__| | 
     \______|  \______/  |_______||_______/    |_______/    |__| |__| \__|  \______| 
                                                                                     
                         _______      ___      .___  ___.  _______ 
                        /  _____|    /   \     |   \/   | |   ____|
                       |  |  __     /  ^  \    |  \  /  | |  |__   
                       |  | |_ |   /  /_\  \   |  |\/|  | |   __|  
                       |  |__| |  /  _____  \  |  |  |  | |  |____ 
                        \______| /__/     \__\ |__|  |__| |_______|
                                                                   

""" + Style.RESET_ALL)



vel = [10, 20, 30, 40, 50, 60, 60, 60, 80]
print("Список: \n" + str((vel)))
searched = int(input("Какое число надо найти?: "))
left = 0
right = len(vel)-1
index = -1
while (left <= right) and (index == -1):
    mid = (left + right)//2
    if vel[mid] == searched:
        index = mid
    else:
        if searched <= vel[mid]:
            right = mid -1
        else:
            left = mid +1
print("Компьютер нашел ваше число с помощью баначного поиска, и индекс этого числа:\n\n"+ Fore.LIGHTYELLOW_EX + str(index))


