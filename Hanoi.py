from matplotlib import pyplot as plt
import time,random

from HanoiTower import ColorBar,HanoiStack

speed = 10


def draw_(poll1x, poll2x, poll3x, first_n,poll_1,poll_2,poll_3):
    plt.clf()
    # printing the graph
    # x = [0 for a in range(first_n)]
    # y = [a for a in range(first_n)]
    plt.plot([0, poll1x*4], [0, 0],color="black")
    plt.plot([0, 0], [0, first_n+5],color="black")
    # first poll
    x = [poll1x ,poll1x]
    y = [0,first_n+2]
    plt.plot(x, y, color="yellow")

    # second poll
    x = [poll2x,poll2x]
    y = [0,first_n+2]
    plt.plot(x, y, color='yellow')

    # third poll
    x = [poll3x,poll3x]
    y = [0,first_n+2]
    plt.plot(x, y, color='yellow')

    # printing color bars
    length_one = len(poll_1)
    length_two = len(poll_2)
    length_three = len(poll_3)
    for i,bar in enumerate(poll_1):
        plt.plot([poll1x-bar.size,poll1x+bar.size],[length_one-i,length_one-i],color=bar.color)

    for i,bar in enumerate(poll_2):
        plt.plot([poll2x-bar.size,poll2x+bar.size],[length_two-i,length_two-i],color=bar.color)

    for i,bar in enumerate(poll_3):
        plt.plot([poll3x-bar.size,poll3x+bar.size],[length_three-i,length_three-i],color=bar.color)

    plt.pause(1/speed)


def hanoi(n, start, end, first_time=False):
    if first_time:
        # init block of some configuration
        global poll1x, poll2x, poll3x, first_n, poll_1, poll_2, poll_3
        poll1x, poll2x, poll3x = ((n+2)*2) * 1, ((n+2)*2) * 2, ((n+2)*2) * 3
        first_n = n
        colors = ["indigo",'cyan','green','red','blue']
        bar_li = [ColorBar(i,random.choice(colors)) for i in range(1, n + 1)]
        bar_li.sort(reverse=True)

        # init block of three bar
        poll_1 = HanoiStack()
        poll_2 = HanoiStack()
        poll_3 = HanoiStack()

        for bar in bar_li:
            poll = eval(f"poll_{start}")
            poll.push(bar)



        # endblock of init three bar

        #end block config

    if n == 1:
        start_poll = eval(f"poll_{start}")
        end_poll = eval(f"poll_{end}")
        end_poll.push(start_poll.pop())
        draw_(poll1x, poll2x, poll3x, first_n, poll_1,poll_2,poll_3)
        print(f"{start}-->{end}")
    else:
        hanoi(n - 1, start, 6 - start - end)
        start_poll = eval(f"poll_{start}")
        end_poll = eval(f"poll_{end}")
        end_poll.push(start_poll.pop())
        draw_(poll1x, poll2x, poll3x, first_n, poll_1,poll_2,poll_3)
        print(f"{start}-->{end}")

        hanoi(n - 1, 6 - start - end, end)

def play(n,start,end):
        global poll1x, poll2x, poll3x, first_n, poll_1, poll_2, poll_3
        poll1x, poll2x, poll3x = ((n+2)*2) * 1, ((n+2)*2) * 2, ((n+2)*2) * 3
        colors = ["indigo",'cyan','green','red','blue']
        bar_li = [ColorBar(i,random.choice(colors)) for i in range(1, n + 1)]
        bar_li.sort(reverse=True)

        # init block of three bar
        poll_1 = HanoiStack()
        poll_2 = HanoiStack()
        poll_3 = HanoiStack()

        for bar in bar_li:
            poll = eval(f"poll_{start}")
            poll.push(bar)

        # endblock of init three bar

        #end block config

        draw_(poll1x,poll2x,poll3x,n,poll_1,poll_2,poll_3)

        while True:
            try:
                a,b = [int(i) for i in (input().split(sep=' '))]
                try:
                    start_poll = eval(f"poll_{a}")
                    end_poll = eval(f"poll_{b}")
                    end_poll.push(start_poll.pop())
                    draw_(poll1x,poll2x,poll3x,n,poll_1,poll_2,poll_3)
                except ValueError as e:
                    print('wrong move.')
            except ValueError:
                print("two charecter must be in range(1-3)")
plt.show()

