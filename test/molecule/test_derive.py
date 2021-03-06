# -*- coding: utf-8 -*-
import unittest
import numpy

from sagar.molecule.structure import Molecule
from sagar.molecule.derive import ConfigurationGenerator

# c60的用于测试
positions_c60 = numpy.array([8.0139797e+00, 1.2307888e+01, 1.1831318e+01,
                             6.5740211e+00, 1.0726525e+01, 1.0595208e+01,
                             7.1922590e+00, 1.1175578e+01, 1.1831371e+01,
                             7.6557315e+00, 1.2600981e+01, 9.4047951e+00,
                             8.2504787e+00, 1.3033716e+01, 1.0595008e+01,
                             6.8011791e+00, 1.1425831e+01, 9.4047725e+00,
                             9.6320871e+00, 1.3483070e+01, 1.0595084e+01,
                             8.4196456e+00, 1.2601104e+01, 8.1686968e+00,
                             9.2495934e+00, 1.2307001e+01, 1.2595101e+01,
                             7.5742544e+00, 1.0000000e+01, 1.2594760e+01,
                             7.0371670e+00, 1.0699472e+01, 8.1684841e+00,
                             6.5740211e+00, 9.2734749e+00, 1.0595208e+01,
                             1.0249361e+01, 1.3033496e+01, 1.1831375e+01,
                             8.0378142e+00, 1.1425589e+01, 7.4050514e+00,
                             7.1922590e+00, 8.8244218e+00, 1.1831371e+01,
                             8.7641880e+00, 1.0000000e+01, 1.3330553e+01,
                             7.0371670e+00, 9.3005277e+00, 8.1684841e+00,
                             9.6176527e+00, 1.1175560e+01, 1.3331021e+01,
                             9.7506389e+00, 1.3033496e+01, 8.1686245e+00,
                             1.0367913e+01, 1.3483070e+01, 9.4049164e+00,
                             6.8011791e+00, 8.5741692e+00, 9.4047725e+00,
                             9.0002389e+00, 1.0726515e+01, 6.6686478e+00,
                             1.1580354e+01, 1.2601104e+01, 1.1831303e+01,
                             8.0139797e+00, 7.6921121e+00, 1.1831318e+01,
                             1.0999761e+01, 1.0726515e+01, 1.3331352e+01,
                             1.1749521e+01, 1.3033716e+01, 9.4049924e+00,
                             1.0750407e+01, 1.2307001e+01, 7.4048990e+00,
                             9.6176527e+00, 8.8244403e+00, 1.3331021e+01,
                             8.0378142e+00, 8.5744108e+00, 7.4050514e+00,
                             7.6557315e+00, 7.3990193e+00, 9.4047951e+00,
                             1.0382347e+01, 1.1175560e+01, 6.6689793e+00,
                             1.1962186e+01, 1.1425589e+01, 1.2594949e+01,
                             9.0002389e+00, 9.2734848e+00, 6.6686478e+00,
                             1.2344269e+01, 1.2600981e+01, 1.0595205e+01,
                             9.2495934e+00, 7.6929995e+00, 1.2595101e+01,
                             8.2504787e+00, 6.9662840e+00, 1.0595008e+01,
                             1.0999761e+01, 9.2734848e+00, 1.3331352e+01,
                             1.1986020e+01, 1.2307888e+01, 8.1686818e+00,
                             8.4196456e+00, 7.3988961e+00, 8.1686968e+00,
                             1.0382347e+01, 8.8244403e+00, 6.6689793e+00,
                             1.3198821e+01, 1.1425831e+01, 1.0595228e+01,
                             1.1235812e+01, 1.0000000e+01, 6.6694473e+00,
                             9.6320871e+00, 6.5169305e+00, 1.0595084e+01,
                             1.2962833e+01, 1.0699472e+01, 1.1831516e+01,
                             1.0249361e+01, 6.9665037e+00, 1.1831375e+01,
                             1.1962186e+01, 8.5744108e+00, 1.2594949e+01,
                             1.2807741e+01, 1.1175578e+01, 8.1686288e+00,
                             9.7506389e+00, 6.9665037e+00, 8.1686245e+00,
                             1.0750407e+01, 7.6929995e+00, 7.4048990e+00,
                             1.3425979e+01, 1.0726525e+01, 9.4047924e+00,
                             1.2962833e+01, 9.3005277e+00, 1.1831516e+01,
                             1.1580354e+01, 7.3988961e+00, 1.1831303e+01,
                             1.2425746e+01, 1.0000000e+01, 7.4052402e+00,
                             1.0367913e+01, 6.5169305e+00, 9.4049164e+00,
                             1.2807741e+01, 8.8244218e+00, 8.1686288e+00,
                             1.3198821e+01, 8.5741692e+00, 1.0595228e+01,
                             1.1749521e+01, 6.9662840e+00, 9.4049924e+00,
                             1.2344269e+01, 7.3990193e+00, 1.0595205e+01,
                             1.1986020e+01, 7.6921121e+00, 8.1686818e+00,
                             1.3425979e+01, 9.2734749e+00, 9.4047924e+00])
atoms_c60 = ['C'] * 60


class TestDerive(unittest.TestCase):

    def setUp(self):
        molecule = Molecule(positions_c60, atoms_c60)
        self.cg = ConfigurationGenerator(molecule, symprec=0.05)

    def test_get_configurations_binary_alloy(self):
        e_num = (59, 1)
        sites = [(6, 5)] * 60
        all_type = self.cg.get_configurations(sites, e_num)
        num_confs = len([i for i in all_type])
        self.assertEqual(num_confs, 1)

        e_num = (58, 2)
        sites = [(6, 5)] * 60
        all_type = self.cg.get_configurations(sites, e_num)
        num_confs = len([i for i in all_type])
        self.assertEqual(num_confs, 23)

    def test_get_configurations_square_alloy(self):
        positions = numpy.array([0.0, 0.0, 0.0,
                                 0.0, 0.0, 2.0,
                                 0.0, 2.0, 0.0,
                                 0.0, 2.0, 2.0,
                                 2.0, 0.0, 0.0,
                                 2.0, 0.0, 2.0,
                                 2.0, 2.0, 0.0,
                                 2.0, 2.0, 2.0]).reshape((-1, 3))
        atoms = ['C'] * 8
        molecule = Molecule(positions, atoms)
        cg = ConfigurationGenerator(molecule, symprec=0.05)
        e_num = (6, 2)
        sites = [(5, 6)] * 8
        all_type = cg.get_configurations(sites, e_num)
        num_confs = len([i for i in all_type])
        self.assertEqual(num_confs, 3)

    # def test_get_configurations_trinary_alloy(self):
    #     e_num = (57, 2, 1)
    #     sites = [(5, 6, 7)] * 60
    #     all_type = self.cg.get_configurations(sites, e_num)
    #     num_confs = len([i for i in all_type])
    #     self.assertEqual(num_confs, 871)
