# -*- coding: utf-8 -*-
"""1_diskon_ecommerce.py

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ra_xKDq6Ib2CliioAZ-iAO2IAaHgsxBh
"""

# Program Diskon E-Commerce

# Meminta input total belanja dari user
total_belanja = float(input("Masukkan total belanja Anda (Rp): "))

# Mengecek apakah total belanja memenuhi syarat untuk diskon
if total_belanja > 500000:
    diskon = total_belanja * 0.10
    total_bayar = total_belanja - diskon
    print(f"Anda mendapat diskon 10%. Total bayar: Rp{total_bayar:,.2f}")
else:
    print(f"Tidak ada diskon. Total bayar: Rp{total_belanja:,.2f}")