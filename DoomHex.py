import os
import base64
import time
from colorama import Fore, Style, init
from pyfiglet import Figlet

# تهيئة اللون
init(autoreset=True)

# =========================
# CONFIG
# =========================
APP_NAME = "DoomHex"
CREDIT_LINE = f"{Style.DIM}credit by DoomSlayer{Style.NORMAL}"
SPINNER_FRAMES = ['\\', '/', '-', '|']

# =========================
# FUNCTIONS
# =========================

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def spinner(text, duration=0.8):
    t_end = time.time() + duration
    i = 0
    while time.time() < t_end:
        print(f"{Fore.CYAN}{text} {SPINNER_FRAMES[i % len(SPINNER_FRAMES)]}", end='\r')
        time.sleep(0.1)
        i += 1
    print(" " * 30, end='\r')

def banner():
    clear()
    f = Figlet(font='slant')
    print(Fore.CYAN + f.renderText(APP_NAME))
    print(f"{Fore.CYAN}{'═'*40}")
    print(f"{Fore.CYAN}Interactive Binary/Hex/Base64 Tool")
    print(f"{Fore.CYAN}{'═'*40}")
    print(f"{Fore.LIGHTBLACK_EX}{CREDIT_LINE}\n")

def text_to_binary(text):
    return ' '.join(format(ord(i), '08b') for i in text)

def binary_to_text(binary):
    try:
        return ''.join(chr(int(b, 2)) for b in binary.split())
    except:
        return "Invalid binary input."

def text_to_hex(text):
    return text.encode().hex()

def hex_to_text(hex_str):
    try:
        return bytes.fromhex(hex_str).decode()
    except:
        return "Invalid hex input."

def text_to_base64(text):
    return base64.b64encode(text.encode()).decode()

def base64_to_text(b64_str):
    try:
        return base64.b64decode(b64_str).decode()
    except:
        return "Invalid Base64 input."

def credits():
    print(Fore.CYAN + "\n[+] Credits")
    print(Fore.LIGHTCYAN_EX + "Discord: 7o9l")
    print(Fore.LIGHTCYAN_EX + "GitHub : DoOmSlAyEr")
    print()

# =========================
# MAIN MENU
# =========================

def main_menu():
    while True:
        banner()
        print(Fore.LIGHTCYAN_EX + "Choose an option:\n")
        print(Fore.CYAN + "[1]" + Fore.WHITE + " Text → Binary")
        print(Fore.CYAN + "[2]" + Fore.WHITE + " Binary → Text")
        print(Fore.CYAN + "[3]" + Fore.WHITE + " Text → Hex")
        print(Fore.CYAN + "[4]" + Fore.WHITE + " Hex → Text")
        print(Fore.CYAN + "[5]" + Fore.WHITE + " Text → Base64")
        print(Fore.CYAN + "[6]" + Fore.WHITE + " Base64 → Text")
        print(Fore.CYAN + "[7]" + Fore.WHITE + " Credits")
        print(Fore.CYAN + "[0]" + Fore.WHITE + " Exit\n")

        choice = input(Fore.LIGHTCYAN_EX + "Enter choice: ").strip()

        if choice == '0':
            spinner("Exiting")
            clear()
            break
        elif choice == '1':
            text = input("Enter text: ")
            spinner("Converting")
            print(Fore.GREEN + text_to_binary(text))
            input(Fore.LIGHTBLACK_EX + "\nPress Enter to continue...")
        elif choice == '2':
            binary = input("Enter binary: ")
            spinner("Converting")
            print(Fore.GREEN + binary_to_text(binary))
            input(Fore.LIGHTBLACK_EX + "\nPress Enter to continue...")
        elif choice == '3':
            text = input("Enter text: ")
            spinner("Converting")
            print(Fore.GREEN + text_to_hex(text))
            input(Fore.LIGHTBLACK_EX + "\nPress Enter to continue...")
        elif choice == '4':
            hex_str = input("Enter hex: ")
            spinner("Converting")
            print(Fore.GREEN + hex_to_text(hex_str))
            input(Fore.LIGHTBLACK_EX + "\nPress Enter to continue...")
        elif choice == '5':
            text = input("Enter text: ")
            spinner("Converting")
            print(Fore.GREEN + text_to_base64(text))
            input(Fore.LIGHTBLACK_EX + "\nPress Enter to continue...")
        elif choice == '6':
            b64_str = input("Enter Base64: ")
            spinner("Converting")
            print(Fore.GREEN + base64_to_text(b64_str))
            input(Fore.LIGHTBLACK_EX + "\nPress Enter to continue...")
        elif choice == '7':
            spinner("Loading")
            credits()
            input(Fore.LIGHTBLACK_EX + "Press Enter to go back...")
        else:
            print(Fore.RED + "Invalid option!")
            time.sleep(1)

# =========================
# RUN
# =========================

if __name__ == "__main__":
    banner()
    main_menu()
