class PhanSo:
    def __init__(self, tu_so, mau_so):
        self.tu_so = tu_so
        self.mau_so = mau_so

    def gcd(self, a, b):
        if b == 0:
            return a
        else:
            return self.gcd(b, a % b)

    def rut_gon(self):
        ucln = self.gcd(self.tu_so, self.mau_so)
        self.tu_so //= ucln
        self.mau_so //= ucln

    def __str__(self):
        return "{}/{}".format(self.tu_so, self.mau_so)


if __name__ == '__main__':
    tu_so, mau_so = map(int, input().split())
    phan_so = PhanSo(tu_so, mau_so)
    phan_so.rut_gon()
    print(phan_so)
