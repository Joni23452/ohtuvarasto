import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)
        self.epavarasto = Varasto(-2)
        self.saldovarasto = Varasto(10,3)
        self.epasaldovarasto = Varasto(10,-1)
        self.liikasaldovarasto = Varasto(10,11)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_konstruktori_luo_varaston_oikealla_saldolla(self):
        self.assertAlmostEqual(self.saldovarasto.saldo, 3)

    def test_konstruktori_luo_varaston_virheellisella_saldolla(self):
        self.assertAlmostEqual(self.epasaldovarasto.saldo, 0)

    def test_konstruktori_luo_varaston_liiallisella_saldolla(self):
        self.assertAlmostEqual(self.liikasaldovarasto.saldo, 10)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)


    def test_varaston_tilavuus_nolla_virheellisella_syotteella(self):
        self.assertAlmostEqual(self.epavarasto.tilavuus, 0)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_liika_lisays_tayttaa_varaston(self):
        self.varasto.lisaa_varastoon(11)

        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_liika_lisays_poistaa_tilan(self):
        self.varasto.lisaa_varastoon(11)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_negatiivinen_lisays_ei_tee_mitaan(self):
        self.varasto.lisaa_varastoon(-1)

    def test_liika_ottaminen_tyhjentaa_saldon(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(9)

        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_liika_ottaminen_tayttaa_mahtuvuuden(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(9)

        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_negatiivinen_ottaminen_palauttaa_nolla(self):
        self.assertAlmostEqual(self.varasto.ota_varastosta(-1),0)

    def test_negatiivinen_ottaminen_ei_muuta_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(-1)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_ottaminen_vahentaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(self.varasto.saldo, 6)

    def test_string(self):
        str(self.varasto)