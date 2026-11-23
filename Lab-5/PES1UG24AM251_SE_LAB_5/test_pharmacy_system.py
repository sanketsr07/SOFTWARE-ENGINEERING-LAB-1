"""Behavior checks for pharmacy stock and prescription handling."""

import unittest

import pharmacy_system


class PharmacySystemTests(unittest.TestCase):
    """Check core pharmacy stock and allergy rules."""

    def setUp(self):
        pharmacy_system.conn.execute("DROP TABLE IF EXISTS patients")
        pharmacy_system.setup_database()
        pharmacy_system.stock.clear()
        pharmacy_system.prescriptions.clear()

    def test_dispense_uses_case_insensitive_stock_name(self):
        pharmacy_system.add_stock("Ibuprofen", 8, "2027-12-31")

        self.assertTrue(pharmacy_system.dispense("Arjun", "ibuprofen", 2))
        self.assertEqual(pharmacy_system.stock["Ibuprofen"]["units"], 6)

    def test_allergy_check_is_case_insensitive(self):
        pharmacy_system.add_stock("Penicillin", 8, "2027-12-31")

        self.assertFalse(
            pharmacy_system.dispense("Kavya", "PENICILLIN", 1)
        )
        self.assertEqual(pharmacy_system.stock["Penicillin"]["units"], 8)

    def test_non_positive_stock_and_dispense_quantities_are_rejected(self):
        with self.assertRaises(ValueError):
            pharmacy_system.add_stock("Aspirin", -4, "2027-12-31")

        pharmacy_system.add_stock("Aspirin", 4, "2027-12-31")
        self.assertFalse(pharmacy_system.dispense("Arjun", "Aspirin", -1))
        self.assertEqual(pharmacy_system.stock["Aspirin"]["units"], 4)


if __name__ == "__main__":
    unittest.main()
