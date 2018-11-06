from string import printable


def solver(variants):
    result = []
    for name, decoded in variants.items():
        print(str(name) + " " + str(decoded))
        line = decoded.decode("utf-8")
        if line == "".join(filter(lambda x: x in printable, line)):
            result.append((decoded, name))

    return result[0]


class Solver:
    pass

