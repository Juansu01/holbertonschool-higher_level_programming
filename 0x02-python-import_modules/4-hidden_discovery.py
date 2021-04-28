#!/usr/bin/python3


if __name__ == "__main__":
    import hidden_4

    directories = dir(hidden_4)

    for i in range(0, len(directories)):
        if directories[i][0:1] != "_":
            print(directories[i])
