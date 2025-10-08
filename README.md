# stock-pattern-detection-reverse-and-inverse-pattern-
A pattern detection model for technical analysis, powered by an algorithm that automatically identifies key trend reversals and inverse patterns in stock and crypto data.

# 🧠 Stock Pattern Detection — Reverse & Inverse Patterns

[![Python](https://img.shields.io/badge/Python-3.10+-blue)]() [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)]() [![Status](https://img.shields.io/badge/Status-Active-success)]()

โครงการนี้ออกแบบมาเพื่อ **ตรวจจับรูปแบบราคา (Price Patterns)** ของหุ้นและคริปโต โดยเฉพาะ  
**Reverse Patterns** (รูปแบบกลับทิศแนวโน้ม) และ **Inverse Patterns** (รูปแบบกลับด้านหรือสมมาตรของแม่แบบ)  
รองรับการตรวจจับรูปแบบ **Harmonic XABCD**, **Directional Change (DC)** และการพล็อตกราฟอัตโนมัติด้วย `mplfinance`

---

## 📋 Features
- 🔍 ตรวจจับ **Harmonic Patterns** (Gartley, Bat, Butterfly, Crab)
- 🔄 วิเคราะห์ **Reverse / Inverse** patterns
- 📉 ใช้ **Directional Change (DC)** เพื่อตัด noise และหาจุด swing สำคัญ
- 📊 พล็อตกราฟด้วย `mplfinance` พร้อมจุด X-A-B-C-D
- ⚙️ ปรับแต่งผ่าน `config.yaml` ได้
- 🧪 ใช้เพื่อ backtest, วิเคราะห์แนวโน้ม, หรือสร้างระบบแจ้งเตือน

---

## 🧩 Supported Patterns
| Pattern | XA_AB | AB_BC | BC_CD | XA_AD |
|----------|--------|--------|--------|--------|
| Gartley | 0.618 | [0.382, 0.886] | [1.13, 1.618] | 0.786 |
| Bat | [0.382, 0.50] | [0.382, 0.886] | [1.618, 2.618] | 0.886 |
| Butterfly | - | - | - | - |
| Crab | - | - | - | - |

> สามารถแก้ไขสัดส่วน Fibonacci ได้ในไฟล์ `config.yaml`

---

## 📁 Project Structure
```bash
stock-pattern-detection-reverse-and-inverse-pattern-/
├─ data/                     # CSV หรือ Parquet ไฟล์ราคา
├─ notebooks/                # ตัวอย่างการใช้งาน Jupyter Notebook
├─ src/
│  ├─ patterns/              # โมดูลตรวจจับแพทเทิร์น
│  ├─ dc/                    # Directional Change
│  ├─ plot/                  # การวาดกราฟ
│  ├─ io/                    # โหลดข้อมูล
│  ├─ scan.py                # batch scan หลายสัญลักษณ์
│  └─ cli.py                 # คำสั่ง CLI
├─ config.yaml               # ไฟล์ตั้งค่า
├─ requirements.txt
└─ README.md
