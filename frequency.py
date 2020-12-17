import numpy as np


class Frequency(object):
    A4_FREQUENCY = 440

    def __init__(self, *args):
        if len(args) == 1:
            self.frequency = args[0]
            c0_ratio = self.frequency / (Frequency.A4_FREQUENCY * np.power(2, -4.75))
            self.octave = np.int(np.log2(c0_ratio))
            self.pitch_class = np.int(np.round((np.log2(c0_ratio) - self.octave) * 12))

        elif len(args) == 2:
            self.octave = args[0]
            self.pitch_class = args[1]
            self.frequency = Frequency.A4_FREQUENCY * np.power(2, -4.75 + self.octave + self.pitch_class / 12)
            
        if self.pitch_class >= 12:
            self.pitch_class -= 12
            self.octave += 1

    def nth_overtone(self, n):
        return Frequency(self.frequency * n)

    def to_tet_ratio(self):
        tet_frequency = Frequency.A4_FREQUENCY * np.power(2, -4.75 + self.octave + self.pitch_class / 12)
        return self.frequency / tet_frequency

    def cent_from_tet(self):
        return np.log(self.to_tet_ratio()) / np.log(np.power(2, 1 / 12)) * 100
