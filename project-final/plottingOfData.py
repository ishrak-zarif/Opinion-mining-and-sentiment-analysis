import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
from project.WithGmailAsInput import Gmail

class dataPlot:
    def __init__(self, textName = "gmail_out.txt"):
        self.tName = textName
    def plot(self):
        style.use("ggplot")

        fig1 = plt.figure()
        ax1 = fig1.add_subplot(1, 1, 1)

        def animate(i):
            pullData = open(self.tName, "r").read()
            lines = pullData.split('\n')

            xar = []
            yar = []

            x = 0
            y = 0

            for l in lines[-200:]:
                x += 1
                if "pos" in l:
                    y += 1
                elif "neg" in l:
                    y -= 1
                xar.append(x)
                yar.append(y)

            ax1.clear()
            ax1.plot(xar, yar)

        ani = animation.FuncAnimation(fig1, animate, interval=1000)
        plt.show()

