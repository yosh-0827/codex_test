import argparse
import sys


def calculate_bmi(height: float, weight: float) -> float:
    if height <= 0:
        raise ValueError("身長は0より大きい値を指定してください。")
    if weight <= 0:
        raise ValueError("体重は0より大きい値を指定してください。")
    return weight / (height ** 2)


def classify_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return "低体重"
    if bmi < 25:
        return "普通体重"
    if bmi < 30:
        return "肥満(1度)"
    if bmi < 35:
        return "肥満(2度)"
    if bmi < 40:
        return "肥満(3度)"
    return "肥満(4度)"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="BMIを計算するCLIツール")
    parser.add_argument("--height", type=float, required=True, help="身長(m)を指定します。例: 1.70")
    parser.add_argument("--weight", type=float, required=True, help="体重(kg)を指定します。例: 65")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        bmi = calculate_bmi(args.height, args.weight)
    except ValueError as error:
        print(f"エラー: {error}", file=sys.stderr)
        return 1

    category = classify_bmi(bmi)

    print(f"BMI: {bmi:.2f}")
    print(f"判定: {category}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
