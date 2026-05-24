# 🌆 NEON CONVERTER v1.0

A futuristic unit converter desktop application built with Python and CustomTkinter, featuring a dark neon aesthetic inspired by cyberpunk interfaces.

---

## 📸 Overview

NEON CONVERTER is a lightweight GUI application that allows users to convert between common units of length and weight. The interface uses a dark background with vibrant neon colors (electric blue, hot pink, neon green) to create a distinctive sci-fi look and feel.

---

## ✨ Features

- **Length Conversion**
  - Meters ↔ Feet

- **Weight Conversion**
  - Kilograms ↔ Pounds

- Tabbed interface for easy navigation between conversion categories
- Real-time input validation with error feedback
- Results displayed with 4 decimal precision
- Futuristic dark UI with neon color scheme

---

## 🖥️ Requirements

- Python 3.8+
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter)

---

## 📦 Installation

1. **Clone or download** this repository.

2. **Install dependencies:**

```bash
pip install customtkinter
```

3. **Run the application:**

```bash
python neon_converter.py
```

---

## 🚀 Usage

1. Enter a numeric value in the **"ENTER VALUE TO CONVERT"** field.
2. Select a category tab: **LENGTH** or **WEIGHT**.
3. Choose the desired conversion direction using the radio buttons.
4. Click **"EXECUTE CONVERSION"** to see the result.

Results appear in the bottom panel in neon green. If the input is invalid, an error message is shown in pink.

---

## 🎨 Color Scheme

| Role              | Color     | Hex       |
|-------------------|-----------|-----------|
| Background        | Dark Navy | `#0D0E15` |
| Panel / Input BG  | Dark Blue | `#1A1C28` |
| Title / Accent    | Hot Pink  | `#FF007F` |
| Labels / Borders  | Electric Blue | `#00E5FF` |
| Button            | Electric Blue | `#00E5FF` |
| Button Hover      | Neon Green | `#00FF66` |
| Result / Success  | Neon Green | `#00FF66` |
| Waiting State     | Neon Yellow | `#ECEB4B` |
| Error State       | Hot Pink  | `#FF007F` |

---

## 🗂️ Project Structure

```
neon_converter.py   # Main application file (single-file project)
README.md           # Project documentation
```

---

## 🔢 Conversion Formulas

| Conversion          | Formula                  |
|---------------------|--------------------------|
| Meters → Feet       | `feet = meters × 3.28084` |
| Feet → Meters       | `meters = feet ÷ 3.28084` |
| Kilograms → Pounds  | `pounds = kg × 2.20462`  |
| Pounds → Kilograms  | `kg = pounds ÷ 2.20462`  |

---

## 🛠️ Built With

- [Python](https://www.python.org/)
- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) — Modern UI framework for Tkinter

---

## 📄 License

This project is open source. Feel free to modify and distribute it as you see fit.
