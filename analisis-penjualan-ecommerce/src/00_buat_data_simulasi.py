import numpy as np
import pandas as pd

np.random.seed(42)

produk = pd.DataFrame({
    "ID_Produk": [f"P{i:02d}" for i in range(1, 17)],
    "Nama_Produk": ["Laptop Gaming", "Laptop Kantor", "Smartphone A", "Smartphone B",
                    "Tablet", "Earbuds", "Headphone", "Smartwatch", "Powerbank",
                    "Charger", "Kabel USB", "Mouse", "Keyboard", "Monitor",
                    "Webcam", "Speaker"],
    "Kategori": ["Laptop", "Laptop", "Smartphone", "Smartphone", "Tablet",
                 "Audio", "Audio", "Wearable", "Aksesoris", "Aksesoris",
                 "Aksesoris", "Aksesoris", "Aksesoris", "Monitor", "Aksesoris", "Audio"],
    "Harga_Dasar": [15_000_000, 8_000_000, 5_000_000, 3_000_000, 4_000_000,
                    500_000, 900_000, 1_500_000, 250_000, 150_000, 50_000,
                    200_000, 400_000, 2_500_000, 450_000, 700_000],
})

n = 1500
kota = np.random.choice(["Jakarta", "Bandung", "Surabaya", "Medan", "Makassar", "Bandar Lampung"],
                        n, p=[0.30, 0.18, 0.18, 0.14, 0.10, 0.10])
tgl = pd.to_datetime("2025-01-01") + pd.to_timedelta(np.random.randint(0, 365, n), unit="D")
# pola musiman: Nov-Des (belanja akhir tahun) lebih ramai -> tambah transaksi
extra = pd.to_datetime("2025-11-01") + pd.to_timedelta(np.random.randint(0, 61, 400), unit="D")
tgl = tgl.append(extra) if hasattr(tgl, "append") else pd.DatetimeIndex(list(tgl) + list(extra))
n = len(tgl)
kota = np.concatenate([kota, np.random.choice(["Jakarta", "Bandung", "Surabaya", "Medan", "Makassar", "Bandar Lampung"],
                                              400, p=[0.38, 0.18, 0.18, 0.12, 0.07, 0.07])])
pid = np.random.choice(produk.ID_Produk, n, p=np.array([2, 3, 5, 6, 3, 9, 6, 4, 10, 10, 12, 8, 6, 3, 4, 9]) / 100)
harga = produk.set_index("ID_Produk").loc[pid, "Harga_Dasar"].values * np.random.uniform(0.9, 1.1, n)
qty = np.random.choice([1, 2, 3, 4], n, p=[0.6, 0.25, 0.1, 0.05])
df = pd.DataFrame({
    "ID_Transaksi": [f"T{i:05d}" for i in range(1, n + 1)],
    "Tanggal": tgl, "ID_Produk": pid, "Kota": kota, "Qty": qty,
    "Harga": harga.round(-3).astype(int),
    "Metode_Bayar": np.random.choice(["Transfer", "E-Wallet", "COD", "Kartu Kredit"], n, p=[0.35, 0.40, 0.15, 0.10]),
})
df = df.sample(frac=1, random_state=1).reset_index(drop=True)
df["ID_Transaksi"] = [f"T{i:05d}" for i in range(1, n + 1)]

idx = lambda k: np.random.choice(df.index, k, replace=False)
df["Tanggal"] = df["Tanggal"].dt.strftime("%Y-%m-%d")

i = idx(120)  # format tanggal campur
df.loc[i, "Tanggal"] = pd.to_datetime(df.loc[i, "Tanggal"]).dt.strftime("%d/%m/%Y")
i = idx(150)  # JAKARTA
df.loc[i, "Kota"] = df.loc[i, "Kota"].str.upper()
i = idx(100)  # spasi + huruf kecil
df.loc[i, "Kota"] = "  " + df.loc[i, "Kota"].str.lower() + " "
df.loc[idx(60), "Metode_Bayar"] = np.nan   # missing
df.loc[idx(40), "Kota"] = np.nan           # missing
df.loc[idx(25), "Harga"] = np.nan          # missing
i = idx(15)   # salah ketik: harga x10
df.loc[i, "Harga"] = df.loc[i, "Harga"] * 10
df.loc[idx(8), "Qty"] = np.random.choice([50, 80, 100], 8)  # pesanan grosir (valid)
df = pd.concat([df, df.sample(30, random_state=3)], ignore_index=True)    # 30 duplikat

df.to_csv("data/raw/transaksi_raw.csv", index=False)
produk.to_csv("data/raw/produk.csv", index=False)
print("transaksi_raw:", df.shape, "| produk:", produk.shape)
