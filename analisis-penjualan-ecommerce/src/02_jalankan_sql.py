"""Muat data bersih ke SQLite, jalankan semua query di sql/analisis.sql (Materi 5)."""
import sqlite3
import pandas as pd

con = sqlite3.connect(":memory:")
pd.read_csv("data/clean/transaksi_clean.csv").to_sql("transaksi", con, index=False)
pd.read_csv("data/raw/produk.csv").to_sql("produk", con, index=False)

isi = open("sql/analisis.sql", encoding="utf-8").read()
for blok in isi.split("-- Q: ")[1:]:
    nama, query = blok.split("\n", 1)
    hasil = pd.read_sql(query, con)
    nama = nama.split(" ")[0]
    hasil.to_csv(f"output/hasil_sql/{nama}.csv", index=False)
    print(f"\n== {nama} ==\n{hasil.head(8).to_string(index=False)}")
