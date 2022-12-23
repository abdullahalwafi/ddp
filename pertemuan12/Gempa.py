class Gempa:
  def __init__(self, lokasi, skala):
    self.lokasi = lokasi
    self.skala = skala

  def dampak(self):
    if self.skala < 2:
      print("Gempat terjadi di", self.lokasi)
      print("dengan skala", self.skala)
      print("Dampak gempa tidak berasa.")
      print()
    elif self.skala >= 2 and self.skala < 4:
      print("Gempat terjadi di", self.lokasi)
      print("dengan skala", self.skala)
      print("Dampak gempa tidak berasa.")
      print()
    elif self.skala >= 4 and self.skala < 6:
      print("Gempat terjadi di", self.lokasi)
      print("dengan skala", self.skala)
      print("Dampak gempa tidak berasa.")
      print()
    else:
      print("Gempat terjadi di", self.lokasi)
      print("dengan skala", self.skala)
      print("Dampak gempa tidak berasa.")
      print()
