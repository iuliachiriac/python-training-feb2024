def grep(text, file):
    lines_matching = []
    with open(file) as f:
        for line in f:
            if text in line:
                lines_matching.append(line)
    return lines_matching


if __name__ == "__main__":
    with open("imports.py") as f:
        for line in f:
            print(line.rstrip())


    fruits = ['apples', 'oranges', 'pears', 'bananas', 'peaches', 'cherries']
    with open("out.txt", "w+") as f:
        for fruit in fruits:
            f.write(fruit)
            f.write("\n")

        print("After writing to file:", f.tell())
        f.seek(0)
        for line in f:
            print(line, end='')
