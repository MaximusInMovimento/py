def agg(*args):
    return sum(args) / len(args)


if __name__ == '__main__':
    print(agg(5, 5, 5, 5))
