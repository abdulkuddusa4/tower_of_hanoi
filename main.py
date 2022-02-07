import sys,math
from Hanoi import hanoi,speed,play

if __name__ == '__main__':
    mode = sys.argv[1]
    level = int(sys.argv[2])
    if mode == 'auto':
        try:
            speed = int(sys.argv[3])
        except IndexError as e:
            pass
        hanoi(int(math.sqrt(level*level)+3),1,3,first_time=True)
    elif mode == "play":
        play(int(math.sqrt(level*level)+3),1,3)



