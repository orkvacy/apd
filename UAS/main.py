from uas1 import *
import os
from colorama import Fore, Style, init
import time
import sys
import pandas as pd
import matplotlib.pyplot as plt

def midPrint(text, width=50):
    spaces = (width - len(text)) // 2 #menghitung jumlah spasi yang dibutuhkan di setiap sisi
    extra_space = (width - len(text)) % 2  #Menghitung spasi jika panjangnya ganjil
    return " " * spaces + text + " " * (spaces + extra_space) #mengembalikkan dan menambahkan


def clear(): #buat clear terminal
    os.system('cls || clear')

def mainMenu():
    width = 50  #lebar
    while True:
        clear()
        # Header
        print(Fore.CYAN + Style.BRIGHT + "=" * width)
        print(midPrint("=== GYM MEMBERSHIP ===", width))
        print("=" * width + Style.RESET_ALL)
        print("|" + " " * (width - 2) + "|")
        print("|" + midPrint("1. Deskripsi Data", width - 2) + "|")
        print("|" + midPrint("2. 10 data Pertama", width - 2) + "|")
        print("|" + midPrint("3. Top 10 Member Terlama Berada di Gym", width - 2) + "|")
        print("|" + midPrint("4. Jumlah data kosong", width - 2) + "|")
        print("|" + midPrint("5. Visualisasi data", width - 2) + "|")
        print("|" + midPrint("0. Keluar", width - 2) + "|")
        print("|" + " " * (width - 2) + "|")
        print("=" * width)

        choice = input(Fore.YELLOW + Style.BRIGHT + "Pilih menu: " + Style.RESET_ALL)
        
        if choice == "1":
            descData()
        elif choice == "2":
            head()
        elif choice == "3":
            longest()
        elif choice == "4":
            na()
        elif choice == "5":
            visualisas()
        elif choice == "0":
            kalimat = """Terimakasih telah menggunakan program!\n⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣴⣦⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣴⠾⠛⠉⠉⠀⠀⠀⠀⠈⠉⠛⠿⣦⣄⠀⠀⠀⠀⠀
⠀⠀⣠⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢷⣄⠀⠀⠀
⠀⣰⡟⠁⠀⠀⠀⣀⡤⡀⠀⠀⠀⠀⠀⣠⢄⠀⠀⠀⠀⠻⣧⠀⠀
⣰⡟⠀⠀⠀⠀⢰⣿⣿⣷⠀⠀⠀⠀⣼⣿⣿⡇⠀⠀⠀⠀⢻⣧⠀
⣿⠃⠀⠀⠀⠀⠘⣿⣿⡿⠀⠀⠀⠀⢹⣿⣿⠇⠀⠀⠀⠀⠈⣿⡄
⣿⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠉⠉⠀⠀⠀⠀⠀⠀⣿⡇
⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠃
⠹⣧⠀⠀⠀⢳⣤⣄⣀⡀⠀⠀⠀⠀⠀⣀⣀⣤⡾⠀⠀⠀⣸⡟⠀
⠀⠻⣧⡀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⣴⡟⠀⠀
⠀⠀⠙⢷⣄⡀⠀⠈⠛⠿⣿⣿⣿⣿⠿⠟⠋⠀⠀⣠⣾⠏⠀⠀⠀
⠀⠀⠀⠀⠙⠻⣶⣤⣀⡀⠀⠀⠀⠀⠀⣀⣠⣴⠿⠋⠁⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠿⠿⠛⠛⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠒⠀⠀⠂⠀⠀⠀⠀\nHave a nice day!"""
            for _ in kalimat:
                sys.stdout.write(_) #menulis perhuruf
                time.sleep(0.005) #jeda penulisan perhuruf
            break
        else:
            input("Menu tidak valid! Tekan Enter untuk melanjutkan...")

if __name__ == "__main__":
    mainMenu()