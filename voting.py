from modul import pemilih, calon

def lakukan_voting():
    id_pemilih = input("Masukan ID Pemilih: ")
    pemilih_data = next((p for p in pemilih.pemilih_list if p['id'] == id_pemilih), None)

    if not pemilih_data:
        print("ID Pemilih tidak ditemukan.")
        return
    if not pemilih_data:
        print("ID Pemilih sudah menggunakan hak suaranya.")
        return
    
    print("\nDaftar Calon:")
    for c in calon.calon_list:
        print(f"{c['id'] - {c['nama']}}")

    
    id_calon = input("Masukan ID Calon yang dipilih: ")
    calon_data = next((c for c in calon.calon_list if c['id'] == id_calon), None)
    
    if not calon_data:
        print("ID calon tidak ditemukan.")
        return
    
    calon_data['jumlah_suara'] += 1
    pemilih_data['sudah_memilih'] = True
    print("Voting berhasil!")

def tampilkan_hasil():
    print("\n===== Hasil Sementara ======")
    for c in calon.calon_list:
        print(f"{c['nama']} ({c['id']}) - {c['jumlah suara']} suara")
