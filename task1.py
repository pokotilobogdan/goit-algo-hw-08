import heapq
from colorama import Fore

def min_value_join(cables):
    total_value = 0
    while len(cables) > 1:
        heapq.heapify(cables)

        print("The pile now is ", cables)
        print()

        cable1 = heapq.heappop(cables)
        cable2 = heapq.heappop(cables)
        
        new_cable = cable1 + cable2   # Join two shortest cables
        total_value += new_cable
        
        print(f"Joining cables " + Fore.YELLOW + f"{cable1}" + Fore.RESET + " and " + Fore.YELLOW + f"{cable2}" + Fore.RESET + ". Total value is " + Fore.GREEN + f"{total_value}" + Fore.RESET)
        print()
        
        heapq.heappush(cables, new_cable)           # Add new cable to the heap to use it later
    # return total_value


if __name__ == "__main__":

    cables = [1, 2, 3, 4, 5, 6, 7]
    min_value_join(cables)
