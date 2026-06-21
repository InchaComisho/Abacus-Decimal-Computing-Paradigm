#!/usr/bin/env python3
"""Basic unit tests for abacus_decimal.py.

Run from the repository root:

    python -m unittest simulations/test_abacus_decimal.py
"""

import unittest

from abacus_decimal import (
    AbacusCell,
    AbacusDecimalError,
    add_digits,
    add_numbers,
    decode_cell,
    encode_digit,
    error_detection_simulation,
    subtract_digits,
    subtract_numbers,
)


class TestAbacusDecimalCell(unittest.TestCase):
    def test_encode_decode_digits(self) -> None:
        expected = {
            0: "00000",
            1: "01000",
            2: "01100",
            3: "01110",
            4: "01111",
            5: "10000",
            6: "11000",
            7: "11100",
            8: "11110",
            9: "11111",
        }
        for digit, bit_string in expected.items():
            with self.subTest(digit=digit):
                cell = encode_digit(digit)
                self.assertEqual(cell.as_bit_string(), bit_string)
                self.assertTrue(cell.is_canonical)
                self.assertEqual(cell.decode(), digit)

    def test_invalid_digit_rejected(self) -> None:
        with self.assertRaises(AbacusDecimalError):
            encode_digit(10)
        with self.assertRaises(AbacusDecimalError):
            encode_digit(-1)

    def test_non_canonical_rejected(self) -> None:
        cell = AbacusCell((0, 0, 1, 0, 0))
        self.assertFalse(cell.is_canonical)
        with self.assertRaises(AbacusDecimalError):
            cell.decode(strict=True)
        self.assertEqual(cell.decode(strict=False), 1)

    def test_decode_cell(self) -> None:
        self.assertEqual(decode_cell([1, 1, 1, 0, 0]), 7)


class TestArithmetic(unittest.TestCase):
    def test_add_digits(self) -> None:
        self.assertEqual(add_digits(4, 5, 0), (9, 0))
        self.assertEqual(add_digits(9, 9, 0), (8, 1))
        self.assertEqual(add_digits(9, 0, 1), (0, 1))

    def test_subtract_digits(self) -> None:
        self.assertEqual(subtract_digits(9, 4, 0), (5, 0))
        self.assertEqual(subtract_digits(0, 1, 0), (9, 1))
        self.assertEqual(subtract_digits(0, 0, 1), (9, 1))

    def test_add_numbers(self) -> None:
        result, cells = add_numbers("1234", "5678")
        self.assertEqual(result, "6912")
        self.assertEqual(" ".join(cell.as_bit_string() for cell in cells), "11000 11111 01000 01100")

    def test_subtract_numbers(self) -> None:
        result, cells = subtract_numbers("9000", "1234")
        self.assertEqual(result, "7766")
        self.assertEqual(" ".join(cell.as_bit_string() for cell in cells), "11100 11100 11000 11000")

    def test_negative_subtraction_rejected(self) -> None:
        with self.assertRaises(AbacusDecimalError):
            subtract_numbers("10", "20")


class TestErrorSimulation(unittest.TestCase):
    def test_error_simulation_counts(self) -> None:
        result = error_detection_simulation(trials=100, flips=1, seed=1)
        total = (
            result["detected_invalid"]
            + result["silent_valid_same"]
            + result["silent_valid_changed"]
        )
        self.assertEqual(total, 100)


if __name__ == "__main__":
    unittest.main()
