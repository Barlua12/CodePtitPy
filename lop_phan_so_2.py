from math import gcd

class PhanSo:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def rutGon(self):
        ucln = gcd(self.tu, self.mau)
        self.tu //= ucln
        self.mau //= ucln

    def cong(self, other):
        mau_chung = self.mau * other.mau // gcd(self.mau, other.mau)
        tu_tong = self.tu * (mau_chung // self.mau) + other.tu * (mau_chung // other.mau)
        ket_qua = PhanSo(tu_tong, mau_chung)
        ket_qua.rutGon()
        return ket_qua

    def __str__(self):
        return str(self.tu) + '/' + str(self.mau)
if __name__ == '__main__':
    tu_p, mau_p, tu_q, mau_q = map(int, input().split())
    p = PhanSo(tu_p, mau_p)
    q = PhanSo(tu_q, mau_q)
    tong = p.cong(q)
    print(tong)