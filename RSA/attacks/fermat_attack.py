from RSA.rsalibnum import isqrt


# Source - http://stackoverflow.com/a/20465181
class FermatAttack(object):
    def __init__(self, n):

        def fermat(n):
            a = isqrt(n)
            b2 = a * a - n
            b = isqrt(n)
            count = 0
            while b * b != b2:
                a = a + 1
                b2 = a * a - n
                b = isqrt(b2)
                count += 1
            p = a + b
            q = a - b
            assert n == p * q
            return p, q

        self.p, self.q = fermat(n)
