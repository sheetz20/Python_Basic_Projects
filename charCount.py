def charCount(sequence):
    count = {}
    for i in sequence:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count
if __name__ == "__main__":
    count = charCount("Thisissoexciting")
    print(count)
