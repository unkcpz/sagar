import unittest

from pyabc.crystal.structure import Cell
from pyabc.crystal.hnf import hnf_cells

class testHnf(unittest.TestCase):

    def test(self):
        pass

    def setUp(self):
        # BCC
        bcc_latt = [0.5, 0.5, -0.5,
                    -0.5, 0.5, 0.5,
                    0.5, -0.5, 0.5]
        bcc_pos = [(0, 0, 0)]
        bcc_atoms = [0]
        self.bcc_pcell = Cell(bcc_latt, bcc_pos, bcc_atoms)

        # HCP
        hcp_b = [2.51900005,  0.,  0.,
                 -1.25950003,  2.18151804, 0.,
                 0., 0.,  4.09100008]
        hcp_positions = [(0.33333334,  0.66666669,  0.25),
                         (0.66666663,  0.33333331,  0.75)]
        hcp_numbers = [0, 0]
        self.hcp_pcell = Cell(hcp_b, hcp_positions, hcp_numbers)

    def test_hnf_cells(self):
        # Results from <PHYSICAL REVIEW B 80, 014120 (2009)>

        # BCC
        wanted = [1, 2, 3, 7, 5, 10, 7]
        got = [len(hnf_cells(self.bcc_pcell, i))
               for i in range(1, 8)]
        self.assertEqual(got, wanted)

        # HCP
        wanted = [1, 3, 5, 11, 7, 19, 11, 34, 23]
        got = [len(hnf_cells(self.hcp_pcell, i))
               for i in range(1, 10)]
        self.assertEqual(got, wanted)
