#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for hid in dir(hidden_4):
        if hid[0:2] != "__":
            print("{}".format(hid))
