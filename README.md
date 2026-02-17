<div align="center">

# 🌌 UDP Lab Tool – Nexus Galaxy Edition 🌠
### 🔵 Herramienta educativa UDP para pruebas de red local (MCPE Status + Flood Lab)

![Python](https://img.shields.io/badge/Python-3.x-1E90FF?style=for-the-badge&logo=python&logoColor=white)
![UDP](https://img.shields.io/badge/Protocol-UDP-4169E1?style=for-the-badge)
![MCPE](https://img.shields.io/badge/Target-Minecraft_PE-00008B?style=for-the-badge)
![Nexus](https://img.shields.io/badge/Nexus-2026-0000CD?style=for-the-badge)
![Vibe](https://img.shields.io/badge/Vibe-Galaxy_Blue-0000FF?style=for-the-badge)

</div>

<grok:render card_id="f36d63,3a54cf" card_type="image_card_group"></grok:render>

---

## ⚠️ ADVERTENCIA COSMICA 🔵🌌

**SOLO PARA LABORATORIO Y REDES PROPIAS**  
Usa esto en:

- Tu localhost  
- Servidor MCPE que **tú controlas**  
- Red privada con permiso  

Cualquier flood a servidores ajenos, amigos o públicos es **ilegal** y puede traerte problemas serios.  
**No soy responsable.** Tú eliges el camino de la galaxia oscura o la luz educativa. 🌑✨

---

## 📜 ¿Qué onda con esta herramienta? 🔵

Script en Python para:

- Aprender **UDP sockets** sin conexión  
- Enviar paquetes random masivos (256-512 bytes) en lab controlado  
- Checar estado de servidores **Minecraft PE** (MOTD, online, ping)  
- Practicar multithreading y networking low-level  

Perfecto para curiosos de ciberseguridad ética, redes y MCPE modding.

---

## 🚀 Instalación en Termux (Android) – Modo Galaxia 🔵📱

Abre **Termux** (descárgalo de F-Droid o GitHub oficial, NO Play Store viejo)

```bash
# 1. Actualiza el universo Termux
pkg update && pkg upgrade -y

# 2. Instala lo básico (git + python)
pkg install git python -y

# 3. Clona el repo (cambia la URL por la tuya cuando lo subas)
git clone https://github.com/tu-usuario/udp-lab-tool.git
# o si ya lo tienes descargado por zip, usa:
# termux-setup-storage   → luego mueve el zip y unzip

# 4. Entra al directorio galáctico
cd udp-lab-tool

# 5. Dale permisos de ejecución (por si acaso)
chmod +x main.py

# 6. Lánzalo al espacio
python main.py
# o
python3 main.py
