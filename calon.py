calon_list = []

def tambah_calon():
    id_calon = input("Masukan ID Calon")
    if any(c['id'] == id_calon for c in calon_list):
         print("ID sudah terdaftar.")
         return
    nama = input("Masukan Nama Calon: ")
    visi = input("Masukan Visi dan Misi: ")
    calon_list.append({
        "id": id_calon,
        "nama": nama,
        "visi": visi,
        "jumlah_suara": 0
    })
    print("Calon berhasil ditambahkan")