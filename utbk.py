def hitungTPS():
  pu = float(input("Masukkan nilai Penalaran Umum: "))
  km = float(input("Masukkan nilai Kemampuan Memahami Bacaan: "))
  ppu = float(input("Masukkan nilai Pengetahuan dan Pemahaman Umum: "))
  pk = float(input("Masukkan nilai Pengetahuan Kuantitatif: "))
  averageTPS = (pu + km + ppu + pk) / 4
  return(averageTPS)
def hitungTKASAINTEK():
  mtk = float(input("Masukkan nilai Matematika: "))
  fsk = float(input("Masukkan nilai Fisika: "))
  kma = float(input("Masukkan nilai Kimia: "))
  bio = float(input("Masukkan nilai Biologi: "))
  averageTKASAINTEK = (mtk + fsk + kma + bio) / 4
  return(averageTKASAINTEK)
def hitungBING():
  bing = float(input("Masukkan nilai Bahasa Inggris: "))
  return(bing)
while True:
  skorUTBK = (float(hitungTPS()+hitungTKASAINTEK()+hitungBING()) / 3)
  print("Total Skor UTBK Anda:", skorUTBK)