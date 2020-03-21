import pandas as pd
import matplotlib.pyplot as plt
import platform
import os


def plot_yahoo_csv(user, file, x, y, ret=False, save=False, show=False):
    if platform.system() == "Windows":
        path = "C:\\Users\\\{}\\Downloads\\{}".format(user, file)
        loc = "C:\\Users\\\{}\\Desktop".format(user)
    elif platform.system() == "Darwin":
        path = "/Users/{}/Downloads/{}".format(user, file)
        loc = "/Users/{}/Desktop".format(user)
    data = pd.read_csv(path)
    data.plot(kind="line", x=x, y=y)
    plt.title(label="{} given {}".format(y, x))

    if ret is True:
        return data
    if save is True:
        n = file.index(".")
        arr_name = []
        for i in range(n):
            arr_name += file[i]
        plot_name = "".join(arr_name)
        os.chdir(loc)
        plt.savefig(plot_name + ".png")
    if show is True:
        plt.show()






print("Function dict:")
f_dict = {"plot_yahoo_csv": "user, file, x, y, ret=False, save=False, show=False"}
print(f_dict)
print("NOTE: All Saves located in Desktop")



