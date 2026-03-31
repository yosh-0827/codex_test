import tkinter as tk
from tkinter import ttk

from bmi import calculate_bmi, classify_bmi


class BmiApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("BMI Calculator")
        self.root.resizable(False, False)

        self.height_var = tk.StringVar()
        self.weight_var = tk.StringVar()
        self.result_var = tk.StringVar(value="身長と体重を入力してください。")

        frame = ttk.Frame(root, padding=16)
        frame.grid(row=0, column=0, sticky="nsew")

        ttk.Label(frame, text="身長(m)").grid(row=0, column=0, sticky="w", pady=(0, 8))
        ttk.Entry(frame, textvariable=self.height_var, width=20).grid(row=0, column=1, pady=(0, 8))

        ttk.Label(frame, text="体重(kg)").grid(row=1, column=0, sticky="w", pady=(0, 8))
        ttk.Entry(frame, textvariable=self.weight_var, width=20).grid(row=1, column=1, pady=(0, 8))

        ttk.Button(frame, text="計算", command=self.calculate).grid(row=2, column=0, columnspan=2, sticky="ew", pady=(0, 12))
        ttk.Label(frame, textvariable=self.result_var, justify="left").grid(row=3, column=0, columnspan=2, sticky="w")

    def calculate(self) -> None:
        try:
            height = float(self.height_var.get())
            weight = float(self.weight_var.get())
        except ValueError:
            self.result_var.set("エラー: 身長と体重は数値で入力してください。")
            return

        try:
            bmi = calculate_bmi(height, weight)
        except ValueError as error:
            message = str(error)
            self.result_var.set(f"エラー: {message}")
            return

        category = classify_bmi(bmi)
        self.result_var.set(f"BMI: {bmi:.2f}\n判定: {category}")


def main() -> None:
    root = tk.Tk()
    BmiApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
