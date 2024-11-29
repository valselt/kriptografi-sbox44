import numpy as np

class Evaluator:
    def __init__(self, sbox):
        self.sbox = sbox

    def calculate_nonlinearity(self):
        """Calculate nonlinearity (NL)."""
        max_nl = 0
        for i in range(256):
            hamming_dist = np.sum([bin(i ^ x).count('1') for x in self.sbox])
            max_nl = max(max_nl, hamming_dist)
        return max_nl

    def calculate_sac(self):
        """Calculate Strict Avalanche Criterion (SAC)."""
        sac_score = 0
        for i in range(256):
            flipped_bits = [self.sbox[i ^ (1 << j)] for j in range(8)]
            sac_score += np.mean([bin(x).count('1') / 8.0 for x in flipped_bits])
        return sac_score / 256

    def calculate_lap(self):
        """Calculate Linear Approximation Probability (LAP)."""
        lap = 0
        for i in range(256):
            for j in range(256):
                correlation = sum([(bin(x & i).count('1') ^ bin(self.sbox[x] & j).count('1')) == 0 for x in range(256)])
                lap = max(lap, abs(correlation - 128) / 256)
        return lap

    def calculate_dap(self):
        """Calculate Differential Approximation Probability (DAP)."""
        dap = 0
        for delta_in in range(256):
            for delta_out in range(256):
                diff = sum([self.sbox[x] ^ self.sbox[x ^ delta_in] == delta_out for x in range(256)])
                dap = max(dap, diff / 256)
        return dap
