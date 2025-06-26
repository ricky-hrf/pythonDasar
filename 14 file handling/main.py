# menangani file
import os
def main():
  # membuat file
  with open("file.txt", "w") as f:
    f.write("Hello World")
  # membaca file
  with open("file.txt", "r") as f:
    print(f.read())
  # menghapus file
  os.remove("file.txt")

