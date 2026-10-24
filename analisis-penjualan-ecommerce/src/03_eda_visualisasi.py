import pandas as pd
import matplotlib.pyplot as plt

BIRU, ORANYE, TEAL, UNGU, ABU = "#2a6fbb", "#d9631e", "#2a9d8f", "#8e6bbf", "#b5b5b5"
INK = "#222222"
plt.rcParams.update({"font.size": 11, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.edgecolor": "#999999", "text.color": INK, "axes.labelcolor": INK,
                     "xtick.color": INK, "ytick.color": INK, "figure.dpi": 130})

df = pd.read_csv("data/clean/transaksi_clean.csv")
produk = pd.read_csv("data/raw/produk.csv")
df = df.merge(produk[["ID_Produk", "Nama_Produk", "Kategori"]], on="ID_Produk")
jt = lambda x: x / 1e6   # ke juta rupiah

normal = df[~df["Grosir"]]
tot = normal["Total"]
q1, q3 = tot.quantile(0.25), tot.quantile(0.75)
stat = f"""Statistik Total transaksi (tanpa pesanan grosir)
Mean   : Rp {tot.mean():,.0f}
Median : Rp {tot.median():,.0f}
Std    : Rp {tot.std():,.0f}
Q1/Q3  : Rp {q1:,.0f} / Rp {q3:,.0f}  (IQR = {q3 - q1:,.0f})
Mean > Median -> distribusi miring kanan (ada transaksi besar seperti laptop)
Korelasi Harga vs Qty : {df['Harga'].corr(df['Qty']):.2f}
Total omzet: Rp {df['Total'].sum():,.0f} | Omzet grosir: Rp {df[df['Grosir']]['Total'].sum():,.0f}
"""
print(stat)
open("output/statistik.txt", "w", encoding="utf-8").write(stat)

def simpan(nama):
    plt.tight_layout()
    plt.savefig(f"output/charts/{nama}.png")
    plt.close()

bln = df.groupby("Bulan")["Total"].sum().apply(jt)
plt.figure(figsize=(8, 4))
plt.plot(bln.index, bln.values, color=BIRU, lw=2, marker="o", ms=6)
plt.plot(bln.index[-2:], bln.values[-2:], color=ORANYE, lw=2, marker="o", ms=6)
plt.title("Omzet naik tajam di Nov–Des 2025", loc="left", fontweight="bold")
plt.ylabel("Omzet (juta Rp)")
plt.xticks(range(12), [b[5:] for b in bln.index])
plt.xlabel("Bulan (2025)")
plt.ylim(0, None)
plt.grid(axis="y", color="#e5e5e5")
simpan("01_tren_omzet_bulanan")

kat = df.groupby("Kategori")["Total"].sum().apply(jt).sort_values()
plt.figure(figsize=(8, 4))
plt.barh(kat.index, kat.values, color=BIRU)
for y, v in enumerate(kat.values):
    plt.text(v + 15, y, f"{v:,.0f}", va="center", fontsize=10)
plt.title("Laptop & Smartphone menyumbang >55% omzet", loc="left", fontweight="bold")
plt.xlabel("Omzet (juta Rp)")
simpan("02_omzet_per_kategori")

kota = df[df["Kota"] != "Tidak diketahui"].groupby("Kota")["Total"].sum().apply(jt).sort_values()
plt.figure(figsize=(8, 4))
warna = [ORANYE if k == "Jakarta" else BIRU for k in kota.index]
plt.barh(kota.index, kota.values, color=warna)
for y, v in enumerate(kota.values):
    plt.text(v + 15, y, f"{v:,.0f}", va="center", fontsize=10)
plt.title("Jakarta adalah pasar terbesar", loc="left", fontweight="bold")
plt.xlabel("Omzet (juta Rp)")
simpan("03_omzet_per_kota")

mb = df["Metode_Bayar"].value_counts()
warna_mb = {"E-Wallet": BIRU, "Transfer": ORANYE, "COD": TEAL, "Kartu Kredit": UNGU, "Tidak diketahui": ABU}
plt.figure(figsize=(6, 4.5))
plt.pie(mb.values, labels=mb.index, colors=[warna_mb[m] for m in mb.index], autopct=lambda p: f"{p:.0f}%" if p >= 5 else "",
        startangle=90, counterclock=False, wedgeprops={"edgecolor": "white", "linewidth": 2},
        textprops={"color": INK})
plt.title("E-Wallet jadi metode bayar favorit", loc="left", fontweight="bold")
simpan("04_metode_bayar")

plt.figure(figsize=(8, 4))
plt.hist(jt(tot[tot <= tot.quantile(0.99)]), bins=30, color=BIRU, edgecolor="white")
plt.axvline(jt(tot.mean()), color=ORANYE, lw=2, label=f"Mean {jt(tot.mean()):.1f} jt")
plt.axvline(jt(tot.median()), color=INK, lw=2, ls="--", label=f"Median {jt(tot.median()):.1f} jt")
plt.title("Mean > median: sedikit transaksi besar menarik rata-rata", loc="left", fontweight="bold")
plt.xlabel("Total transaksi (juta Rp, 99% data)")
plt.ylabel("Jumlah transaksi")
plt.legend(frameon=False)
simpan("05_distribusi_transaksi")

p = df.groupby("Nama_Produk").agg(unit=("Qty", "sum"), harga=("Harga", "median"))
plt.figure(figsize=(8, 4.5))
plt.scatter(jt(p["harga"]), p["unit"], color=BIRU, s=60)
for nama, r in p.iterrows():
    geser = (5, -10) if nama == "Smartphone B" else (5, 4)
    plt.annotate(nama, (jt(r["harga"]), r["unit"]), xytext=geser, textcoords="offset points", fontsize=8)
plt.xscale("log")
plt.title("Produk murah terjual lebih banyak (unit)", loc="left", fontweight="bold")
plt.xlabel("Harga median (juta Rp, skala log)")
plt.ylabel("Unit terjual")
simpan("06_harga_vs_unit")
print("Grafik tersimpan di output/charts/")
