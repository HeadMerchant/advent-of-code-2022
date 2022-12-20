from collections import Counter
from unicodedata import name

with open("input.txt", "r") as f:
    message = f.readline().strip()

# 4-window slide algorithm. find first window with
def window_slide(window_size):
    window = Counter(message[:window_size])

    for i in range(window_size, len(message)):
        if len(window) == window_size:
            print(i)
            break

        remove = message[i-window_size]
        
        if window[remove] == 1:
            del window[remove]
        else:
            window[remove] -= 1
        
        window[message[i]] += 1

if __name__ == "__main__":
    window_slide(4)