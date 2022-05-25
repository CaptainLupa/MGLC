import re


def main():
    fname = input("File Name: ")
    
    f = open(fname, "r")
    lines = f.readlines()

    i = 0
    for line in lines:
        l = line
        l = re.sub(r"\s\d+[a-z]+\s", " ", l)
        l = l.replace("sayori", "raiden")
        l = l.replace("Sayori", "raiden")
        l = l.replace("monika", "armstrong")
        l = l.replace("Monika", "Armstrong")
        l = l.replace("natsuki", "bladewolf")
        l = l.replace("Natsuki", "Bladewolf")
        l = l.replace("yuri", "sam")
        l = l.replace("Yuri", "Sam")

        g = re.search(r"(?:armstrong|raiden|sam|bladewolf) \d", l)
        if g is not None:
            s = g.span()
            stri = l[:s[0]] + l[s[1]:]
            lines[i] = stri
        else:
            lines[i] = l

        print(l)
        i += 1

    f.close()

    f = open(fname, "w")
    f.writelines(lines)
    f.close()


if __name__ == "__main__":
    while 1:
        main()
