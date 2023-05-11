def read_from_input(self):
    for i in range(self.n):
        row = list(map(int, input().split()))
        for j in range(self.m):
            self.data[i][j] = row[j]


def __mul__(self, other):
    assert self.m == other.n, "Invalid matrix dimensions"
    res = Matrix(self.n, other.m)
    for i in range(self.n):
        for j in range(other.m):
            for k in range(self.m):
                res.data[i][j] += self.data[i][k] * other.data[j][k]
    return res


def transpose(self):
    res = Matrix(self.m, self.n)
    for i in range(self.n):
        for j in range(self.m):
            res.data[j][i] = self.data[i][j]
    return res


def write_to_output(self):
    for i in range(self.n):
        for j in range(self.m):
            print(self.data[i][j], end=" ")
        print()

