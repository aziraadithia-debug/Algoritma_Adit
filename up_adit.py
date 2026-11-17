HARGA = {"reguler": 35000, "vip": 50000, "premium": 75000}

total_pendapatan = 0
jumlah_pelanggan = 0

print("=== APLIKASI PEMESANAN TIKET BIOSKOP ===")

lanjut = "y"
while lanjut == "y":
    # 1. Nama (tidak boleh kosong)
    nama = input("\nMasukkan nama pelanggan: ").strip()
    while nama == "":
        print("Nama tidak boleh kosong!")
        nama = input("Masukkan nama pelanggan: ").strip()

    # 2. Jenis tiket (harus valid)
    print("Jenis tiket: Reguler / VIP / Premium")
    jenis = input("Pilih jenis tiket: ").strip().lower()
    while jenis not in HARGA:
        print("Jenis tiket tidak valid!")
        jenis = input("Pilih jenis tiket: ").strip().lower()

    # Jumlah tiket (harus angka positif)
    while True:
        teks = input("Masukkan jumlah tiket: ").strip()
        if teks.isdigit() and int(teks) > 0:
            jumlah = int(teks)
            break
        print("Jumlah harus berupa angka lebih dari 0!")

    # 3. Tentukan harga
    if jenis == "reguler":
        harga = 35000
    elif jenis == "vip":
        harga = 50000
    else:
        harga = 75000

    total = harga * jumlah

    # 4. Cek diskon
    if jumlah > 3:
        diskon = total * 0.10
    else:
        diskon = 0

    total_bayar = total - diskon

    # Struk
    print("\n--- STRUK PEMESANAN ---")
    print(f"Nama Pelanggan : {nama}")
    print(f"Jenis Tiket    : {jenis.capitalize()}")
    print(f"Jumlah Tiket   : {jumlah}")
    print(f"Harga Satuan   : Rp{harga:,}")
    print(f"Total Harga    : Rp{total:,.0f}")
    print(f"Diskon         : Rp{diskon:,.0f}")
    print(f"Total Bayar    : Rp{total_bayar:,.0f}")

    total_pendapatan += total_bayar
    jumlah_pelanggan += 1

    # 5. Ulang?
    lanjut = input("\nLayani pelanggan lain? (y/n): ").strip().lower()

# Ringkasan
print("\n=== RINGKASAN HARI INI ===")
print(f"Jumlah pelanggan : {jumlah_pelanggan}")
print(f"Total pendapatan : Rp{total_pendapatan:,.0f}")
print("Terima kasih! Program selesai.")
