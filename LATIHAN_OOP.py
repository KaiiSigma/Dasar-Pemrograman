class siswa:
    def __init__(self, nama, kelas, nilai):
        self.nama = nama
        self.kelas = kelas
        self.nilai = nilai

    def info(self):
        print("nama :", self.nama)
        print("kelas :", self.kelas)

    def status(self):
        if self.nilai >= 75:
            print(self.nama, "lulus")
        else:
            print(self.nama, "tidak lulus")


siswa1 = siswa("budi", "X PPLG 1", 10)
siswa2 = siswa("ani", "X PPLG 1", 75)

siswa1.info()
print("-------------")
siswa2.info()
print("-------------")

siswa1.status()
siswa2.status()
