import io
import unittest
from contextlib import redirect_stderr, redirect_stdout
from types import SimpleNamespace
from unittest.mock import patch

from bmi import calculate_bmi, classify_bmi, main


class CalculateBmiTest(unittest.TestCase):
    def test_calculate_bmi_returns_expected_value(self) -> None:
        self.assertAlmostEqual(calculate_bmi(1.70, 65), 22.49134948, places=6)

    def test_calculate_bmi_raises_when_height_is_not_positive(self) -> None:
        with self.assertRaises(ValueError):
            calculate_bmi(0, 65)

    def test_calculate_bmi_raises_when_weight_is_not_positive(self) -> None:
        with self.assertRaises(ValueError):
            calculate_bmi(1.70, 0)


class ClassifyBmiTest(unittest.TestCase):
    def test_classify_bmi_boundary_values(self) -> None:
        cases = [
            (18.4, "低体重"),
            (18.5, "普通体重"),
            (24.9, "普通体重"),
            (25.0, "肥満(1度)"),
            (29.9, "肥満(1度)"),
            (30.0, "肥満(2度)"),
            (34.9, "肥満(2度)"),
            (35.0, "肥満(3度)"),
            (39.9, "肥満(3度)"),
            (40.0, "肥満(4度)"),
        ]

        for bmi, expected in cases:
            with self.subTest(bmi=bmi):
                self.assertEqual(classify_bmi(bmi), expected)


class MainTest(unittest.TestCase):
    def test_main_prints_result_and_returns_zero(self) -> None:
        stdout = io.StringIO()

        with patch("bmi.parse_args", return_value=SimpleNamespace(height=1.70, weight=65)):
            with redirect_stdout(stdout):
                exit_code = main()

        self.assertEqual(exit_code, 0)
        self.assertIn("BMI: 22.49", stdout.getvalue())
        self.assertIn("判定: 普通体重", stdout.getvalue())

    def test_main_prints_error_and_returns_one(self) -> None:
        stderr = io.StringIO()

        with patch("bmi.parse_args", return_value=SimpleNamespace(height=0, weight=65)):
            with redirect_stderr(stderr):
                exit_code = main()

        self.assertEqual(exit_code, 1)
        self.assertIn("エラー: 身長は0より大きい値を指定してください。", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
