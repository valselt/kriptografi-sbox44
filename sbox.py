import numpy as np

class SBox:
    def __init__(self, K, C, irreducible_poly=0x11b):
        self.K = K
        self.C = C
        self.irreducible_poly = irreducible_poly
        self.sbox = []

    def gf_inverse(self, x):
        """Find the multiplicative inverse in GF(2^8)."""
        if x == 0:
            return 0
        for i in range(256):
            if (x * i) % 256 == 1:
                return i
        return 0

    def affine_transformation(self, x_inv):
        """Apply affine transformation."""
        x_inv_bits = np.array([int(b) for b in format(x_inv, '08b')])
        result = (np.dot(self.K, x_inv_bits) + self.C) % 2
        return int("".join(map(str, result)), 2)

    def construct_sbox(self):
        """Construct the S-Box."""
        self.sbox = [self.affine_transformation(self.gf_inverse(i)) for i in range(256)]
        return self.sbox
