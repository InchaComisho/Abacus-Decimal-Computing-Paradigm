#!/usr/bin/env python3
"""
Reference simulation for the Abacus Decimal Computing Paradigm.

This script defines a five-bit abacus decimal cell:

    [H, L1, L2, L3, L4]

Where:
    H  = upper bead position, value 5
    L1 = lower bead position, value 1
    L2 = lower bead position, value 1
    L3 = lower bead position, value 1
    L4 = lower bead position, value 1

The canonical lower-bit patterns are sequential:

    0 -> 0000
    1 -> 1000
    2 -> 1100
    3 -> 1110
    4 -> 1111

The orientation can be reversed in a physical LED layout. This reference
implementation defines one logical convention so that experiments are repeatable.

Usage examples:

    python simulations/abacus_decimal.py table
    python simulations/abacus_decimal.py encode 7
    python simulations/abacus_decimal.py decode 1 1 1 0 0
    python simulations/abacus_decimal.py add 1234 5678
    python simulations/abacus_decimal.py sub 9000 1234
    python simulations/abacus_decimal.py error --trials 10000 --flips 1
"""

from __future__ import annotations

import argparse
import random
from dataclasses import dataclass
from typing import Iterable, List, Sequence, Tuple

Bit = int
CellTuple = Tuple[Bit, Bit, Bit, Bit, Bit]


class AbacusDecimalError(ValueError):
    """Raised when an invalid abacus decimal state is encountered."""


@dataclass(frozen=True)
class AbacusCell:
    """One canonical or non-canonical five-bit abacus decimal cell."""

    bits: CellTuple

    def __post_init__(self) -> None:
        if len(self.bits) != 5:
            raise AbacusDecimalError("A cell must contain exactly five bits.")
        if any(bit not in (0, 1) for bit in self.bits):
            raise AbacusDecimalError("Cell bits must be 0 or 1.")

    @property
    def H(self) -> Bit:
        return self.bits[0]

    @property
    def lower(self) -> Tuple[Bit, Bit, Bit, Bit]:
        return self.bits[1:]

    @property
    def lower_count(self) -> int:
        return sum(self.lower)

    @property
    def raw_value(self) -> int:
        return 5 * self.H + self.lower_count

    @property
    def is_canonical(self) -> bool:
        return self.lower in CANONICAL_LOWER_PATTERNS and 0 <= self.raw_value <= 9

    def decode(self, *, strict: bool = True) -> int:
        """Decode the cell into a decimal digit.

        If strict is True, non-canonical patterns are rejected.
        If strict is False, the raw weighted value is returned.
        """
        if strict and not self.is_canonical:
            raise AbacusDecimalError(f"Non-canonical cell: {self.as_bit_string()}")
        return self.raw_value

    def as_bit_string(self) -> str:
        return "".join(str(bit) for bit in self.bits)

    def as_led_lines(self) -> str:
        """Return a simple vertical LED-style display."""
        labels = ["H(5)", "L1 ", "L2 ", "L3 ", "L4 "]
        return "\n".join(
            f"{label}: {'●' if bit else '○'}" for label, bit in zip(labels, self.bits)
        )

    def flip_bits(self, positions: Iterable[int]) -> "AbacusCell":
        """Return a new cell with selected bit positions flipped.

        Positions are zero-based: 0=H, 1=L1, 2=L2, 3=L3, 4=L4.
        """
        bits = list(self.bits)
        for pos in positions:
            if pos < 0 or pos >= 5:
                raise AbacusDecimalError(f"Invalid bit position: {pos}")
            bits[pos] = 1 - bits[pos]
        return AbacusCell(tuple(bits))


CANONICAL_LOWER_PATTERNS: Tuple[Tuple[Bit, Bit, Bit, Bit], ...] = (
    (0, 0, 0, 0),
    (1, 0, 0, 0),
    (1, 1, 0, 0),
    (1, 1, 1, 0),
    (1, 1, 1, 1),
)


def encode_digit(digit: int) -> AbacusCell:
    """Encode one decimal digit into a canonical abacus cell."""
    if digit < 0 or digit > 9:
        raise AbacusDecimalError("Digit must be in the range 0..9.")

    if digit < 5:
        h = 0
        lower_count = digit
    else:
        h = 1
        lower_count = digit - 5

    lower = tuple(1 if i < lower_count else 0 for i in range(4))
    return AbacusCell((h, *lower))


def decode_cell(bits: Sequence[int], *, strict: bool = True) -> int:
    """Decode a bit sequence as an abacus decimal cell."""
    return AbacusCell(tuple(bits)).decode(strict=strict)  # type: ignore[arg-type]


def encode_number(number: int | str) -> List[AbacusCell]:
    """Encode a non-negative integer into a list of abacus decimal cells."""
    text = str(number)
    if not text.isdigit():
        raise AbacusDecimalError("Only non-negative integer strings are supported.")
    return [encode_digit(int(ch)) for ch in text]


def decode_number(cells: Sequence[AbacusCell], *, strict: bool = True) -> int:
    """Decode a list of abacus decimal cells into an integer."""
    digits = [str(cell.decode(strict=strict)) for cell in cells]
    return int("".join(digits)) if digits else 0


def add_digits(a: int, b: int, carry_in: int = 0) -> Tuple[int, int]:
    """Add two decimal digits and return result digit plus carry."""
    if not (0 <= a <= 9 and 0 <= b <= 9 and carry_in in (0, 1)):
        raise AbacusDecimalError("add_digits expects digits 0..9 and carry 0/1.")
    s = a + b + carry_in
    if s >= 10:
        return s - 10, 1
    return s, 0


def subtract_digits(a: int, b: int, borrow_in: int = 0) -> Tuple[int, int]:
    """Subtract two decimal digits and return result digit plus borrow."""
    if not (0 <= a <= 9 and 0 <= b <= 9 and borrow_in in (0, 1)):
        raise AbacusDecimalError("subtract_digits expects digits 0..9 and borrow 0/1.")
    s = a - b - borrow_in
    if s < 0:
        return s + 10, 1
    return s, 0


def add_numbers(a: int | str, b: int | str) -> Tuple[str, List[AbacusCell]]:
    """Add two non-negative integer numbers using digit-wise decimal arithmetic."""
    a_digits = [int(ch) for ch in str(a)]
    b_digits = [int(ch) for ch in str(b)]
    if not all(0 <= d <= 9 for d in a_digits + b_digits):
        raise AbacusDecimalError("Only non-negative integer strings are supported.")

    result_reversed: List[int] = []
    carry = 0
    for da, db in zip(reversed(a_digits), reversed(b_digits)):
        digit, carry = add_digits(da, db, carry)
        result_reversed.append(digit)

    longer = a_digits if len(a_digits) > len(b_digits) else b_digits
    remaining = list(reversed(longer[: abs(len(a_digits) - len(b_digits))]))
    for d in remaining:
        digit, carry = add_digits(d, 0, carry)
        result_reversed.append(digit)

    if carry:
        result_reversed.append(carry)

    result_digits = list(reversed(result_reversed))
    result_text = "".join(str(d) for d in result_digits)
    return result_text, [encode_digit(d) for d in result_digits]


def subtract_numbers(a: int | str, b: int | str) -> Tuple[str, List[AbacusCell]]:
    """Subtract b from a using digit-wise decimal arithmetic.

    This reference implementation supports a >= b.
    """
    ai = int(str(a))
    bi = int(str(b))
    if ai < bi:
        raise AbacusDecimalError("subtract_numbers currently requires a >= b.")

    a_digits = [int(ch) for ch in str(a)]
    b_digits = [int(ch) for ch in str(b)]

    result_reversed: List[int] = []
    borrow = 0
    max_len = max(len(a_digits), len(b_digits))
    a_rev = list(reversed(a_digits)) + [0] * (max_len - len(a_digits))
    b_rev = list(reversed(b_digits)) + [0] * (max_len - len(b_digits))

    for da, db in zip(a_rev, b_rev):
        digit, borrow = subtract_digits(da, db, borrow)
        result_reversed.append(digit)

    while len(result_reversed) > 1 and result_reversed[-1] == 0:
        result_reversed.pop()

    result_digits = list(reversed(result_reversed))
    result_text = "".join(str(d) for d in result_digits)
    return result_text, [encode_digit(d) for d in result_digits]


def all_binary_states() -> List[AbacusCell]:
    """Return all 32 possible five-bit states."""
    cells: List[AbacusCell] = []
    for value in range(32):
        bits = tuple((value >> shift) & 1 for shift in range(4, -1, -1))
        cells.append(AbacusCell(bits))  # type: ignore[arg-type]
    return cells


def error_detection_simulation(trials: int, flips: int, seed: int | None = None) -> dict[str, int | float]:
    """Simulate random bit flips from canonical states.

    Returns counts for:
    - detected_invalid: mutated state is non-canonical
    - silent_valid_same: mutated state is canonical and same digit
    - silent_valid_changed: mutated state is canonical but different digit
    """
    if trials <= 0:
        raise AbacusDecimalError("trials must be positive.")
    if flips <= 0 or flips > 5:
        raise AbacusDecimalError("flips must be in the range 1..5.")

    rng = random.Random(seed)
    detected_invalid = 0
    silent_valid_same = 0
    silent_valid_changed = 0

    for _ in range(trials):
        original_digit = rng.randrange(10)
        original = encode_digit(original_digit)
        positions = rng.sample(range(5), flips)
        mutated = original.flip_bits(positions)

        if not mutated.is_canonical:
            detected_invalid += 1
            continue

        mutated_digit = mutated.decode(strict=True)
        if mutated_digit == original_digit:
            silent_valid_same += 1
        else:
            silent_valid_changed += 1

    return {
        "trials": trials,
        "flips_per_trial": flips,
        "detected_invalid": detected_invalid,
        "silent_valid_same": silent_valid_same,
        "silent_valid_changed": silent_valid_changed,
        "detected_invalid_rate": detected_invalid / trials,
        "silent_valid_changed_rate": silent_valid_changed / trials,
    }


def format_cells(cells: Sequence[AbacusCell]) -> str:
    return " ".join(cell.as_bit_string() for cell in cells)


def print_table() -> None:
    print("Digit | Bits  | Canonical | LED")
    print("------|-------|-----------|---------------------")
    for digit in range(10):
        cell = encode_digit(digit)
        led = cell.as_led_lines().replace("\n", " / ")
        print(f"{digit:>5} | {cell.as_bit_string()} | {cell.is_canonical!s:<9} | {led}")


def command_encode(args: argparse.Namespace) -> None:
    cell = encode_digit(args.digit)
    print(f"digit: {args.digit}")
    print(f"bits : {cell.as_bit_string()}")
    print("LED pattern:")
    print(cell.as_led_lines())


def command_decode(args: argparse.Namespace) -> None:
    cell = AbacusCell(tuple(args.bits))  # type: ignore[arg-type]
    print(f"bits       : {cell.as_bit_string()}")
    print(f"canonical  : {cell.is_canonical}")
    print(f"raw value  : {cell.raw_value}")
    if cell.is_canonical:
        print(f"strict digit: {cell.decode(strict=True)}")
    else:
        print("strict digit: invalid")


def command_add(args: argparse.Namespace) -> None:
    result, cells = add_numbers(args.a, args.b)
    print(f"{args.a} + {args.b} = {result}")
    print(f"abacus bits: {format_cells(cells)}")


def command_sub(args: argparse.Namespace) -> None:
    result, cells = subtract_numbers(args.a, args.b)
    print(f"{args.a} - {args.b} = {result}")
    print(f"abacus bits: {format_cells(cells)}")


def command_states(_: argparse.Namespace) -> None:
    canonical = 0
    non_canonical = 0
    for cell in all_binary_states():
        if cell.is_canonical:
            canonical += 1
            status = f"valid digit {cell.decode()}"
        else:
            non_canonical += 1
            status = "non-canonical"
        print(f"{cell.as_bit_string()} -> {status}")
    print()
    print(f"canonical states    : {canonical}")
    print(f"non-canonical states: {non_canonical}")


def command_error(args: argparse.Namespace) -> None:
    result = error_detection_simulation(args.trials, args.flips, args.seed)
    for key, value in result.items():
        print(f"{key}: {value}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Abacus decimal cell reference simulation")
    subparsers = parser.add_subparsers(dest="command", required=True)

    subparsers.add_parser("table", help="show canonical digit table").set_defaults(func=lambda args: print_table())

    encode = subparsers.add_parser("encode", help="encode one decimal digit")
    encode.add_argument("digit", type=int)
    encode.set_defaults(func=command_encode)

    decode = subparsers.add_parser("decode", help="decode a five-bit cell")
    decode.add_argument("bits", type=int, nargs=5, choices=[0, 1])
    decode.set_defaults(func=command_decode)

    add = subparsers.add_parser("add", help="add two non-negative integers")
    add.add_argument("a")
    add.add_argument("b")
    add.set_defaults(func=command_add)

    sub = subparsers.add_parser("sub", help="subtract b from a, with a >= b")
    sub.add_argument("a")
    sub.add_argument("b")
    sub.set_defaults(func=command_sub)

    subparsers.add_parser("states", help="list all 32 possible states").set_defaults(func=command_states)

    error = subparsers.add_parser("error", help="run a random bit-flip error detection simulation")
    error.add_argument("--trials", type=int, default=10000)
    error.add_argument("--flips", type=int, default=1)
    error.add_argument("--seed", type=int, default=42)
    error.set_defaults(func=command_error)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
