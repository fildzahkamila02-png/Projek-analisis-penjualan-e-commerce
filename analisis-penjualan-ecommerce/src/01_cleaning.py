import pandas as pd

df = pd.read_csv("data/raw/transaksi_raw.csv")
produk = pd.read_csv("data/raw/produk.csv")
log = []
def catat(teks):
    print(teks)
    log.append(teks)

catat(f"Baris awal: {len(df)}")

#Duplikat
n = df.duplicated().sum()
df = df.drop_duplicates()
catat(f"1. Duplikat dihapus: {n}")

#Format tanggal
iso = pd.to_datetime(df["Tanggal"], format="%Y-%m-%d", errors="coerce")
dmy = pd.to_datetime(df["Tanggal"], format="%d/%m/%Y", errors="coerce")
df["Tanggal"] = iso.fillna(dmy)
catat(f"2. Tanggal diseragamkan, gagal diparse: {df['Tanggal'].isnull().sum()}")

#Kota, rapikan spasi + huruf, lalu isi yang kosong
df["Kota"] = df["Kota"].str.strip().str.title()
catat(f"3. Kota kosong -> 'Tidak diketahui': {df['Kota'].isnull().sum()}")
df["Kota"] = df["Kota"].fillna("Tidak diketahui")

#Metode bayar kosong
catat(f"4. Metode_Bayar kosong -> 'Tidak diketahui': {df['Metode_Bayar'].isnull().sum()}")
df["Metode_Bayar"] = df["Metode_Bayar"].fillna("Tidak diketahui")

#Outlier harga 3x harga dasar produk, dianggap error
df = df.merge(produk[["ID_Produk", "Harga_Dasar"]], on="ID_Produk")
salah = df["Harga"] > 3 * df["Harga_Dasar"]
catat(f"5. Harga outlier (salah ketik) dijadikan kosong: {salah.sum()}")
df.loc[salah, "Harga"] = None

#Harga kosong diisi median harga per produk
kosong = df["Harga"].isnull().sum()
df["Harga"] = df["Harga"].fillna(df.groupby("ID_Produk")["Harga"].transform("median"))
catat(f"6. Harga kosong diisi median per produk: {kosong}")

#Qty hanya diberi penanda
df["Grosir"] = df["Qty"] >= 50
catat(f"7. Pesanan grosir (Qty>=50) ditandai, tidak dihapus: {df['Grosir'].sum()}")

#Kolom baru
df["Total"] = df["Qty"] * df["Harga"]
df["Bulan"] = df["Tanggal"].dt.strftime("%Y-%m")
df = df.drop(columns="Harga_Dasar").sort_values("Tanggal")
catat(f"Baris akhir: {len(df)}")

df.to_csv("data/clean/transaksi_clean.csv", index=False)
open("output/cleaning_log.txt", "w", encoding="utf-8").write("\n".join(log))
