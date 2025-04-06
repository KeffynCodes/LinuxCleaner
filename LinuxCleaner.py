#!/usr/bin/env python3
# =============================================================================
# Linux Cleanup Commander - System Maintenance Utility - Marie Kondo Style!
#
# Author: Damien (VK4DDK)
# Created: 2025-04-06
# License: MIT
#
# Description:
#   This script performs safe, prompt-based cleanup operations on a Linux system.
#   It handles apt cache cleanup, log rotation, Snap/Flatpak junk, temp files,
#   and user-level cache and trash — all with confirmations.
#
# Usage:
#   Run the script with root privileges or use `sudo` where prompted.
#   Example: python3 LinuxCleaner.py
#
# DISCLAIMER:
#   This script is provided as-is. While it avoids destructive actions,
#   use with care and always keep backups of critical data.
# =============================================================================


import os
import shutil
import subprocess

def run_cmd(cmd):
    print(f"\n>>> Running: {cmd}")
    os.system(cmd)

def ask(prompt):
    reply = input(f"\n{prompt} [y/N]: ").lower().strip()
    return reply == 'y'

def clean_apt():
    run_cmd("sudo apt autoremove --purge -y")
    run_cmd("sudo apt clean")

def clean_journal_logs():
    run_cmd("sudo journalctl --vacuum-time=7d")

def clean_logs():
    log_paths = [
        "/var/log/*.gz",
        "/var/log/*.[0-9]",
        "/var/log/*/*.gz",
        "/var/log/*/*.[0-9]"
    ]
    for path in log_paths:
        run_cmd(f"sudo rm -f {path}")

def clean_tmp():
    run_cmd("sudo rm -rf /tmp/*")
    run_cmd("sudo rm -rf /var/tmp/*")

def clean_user_cache():
    home = os.path.expanduser("~")
    thumbs = os.path.join(home, ".cache", "thumbnails")
    trash = os.path.join(home, ".local", "share", "Trash")

    if os.path.exists(thumbs):
        shutil.rmtree(thumbs, ignore_errors=True)
        print("🧹 Thumbnails cache cleared.")

    if os.path.exists(trash):
        shutil.rmtree(trash, ignore_errors=True)
        print("🧹 Trash cleared.")

def clean_snap_revisions():
    snap_list = subprocess.getoutput("snap list --all")
    for line in snap_list.splitlines():
        if "disabled" in line:
            parts = line.split()
            if len(parts) >= 3:
                name, revision = parts[0], parts[2]
                run_cmd(f"sudo snap remove {name} --revision={revision}")

def clean_flatpak():
    run_cmd("flatpak uninstall --unused -y")

def main():
    print("🚀 Welcome to the Linux Cleanup Commander\n")

    if ask("1. Clean apt cache and orphaned packages?"):
        clean_apt()

    if ask("2. Clean systemd journal logs (keep 7 days)?"):
        clean_journal_logs()

    if ask("3. Delete rotated and archived logs in /var/log?"):
        clean_logs()

    if ask("4. Clean /tmp and /var/tmp directories?"):
        clean_tmp()

    if ask("5. Clear user thumbnails and trash?"):
        clean_user_cache()

    if ask("6. Remove old Snap package revisions?"):
        clean_snap_revisions()

    if ask("7. Remove unused Flatpak packages?"):
        clean_flatpak()

    print("\n✅ All selected cleanup tasks completed. Your system just got a digital shower. 🛁")

if __name__ == "__main__":
    main()
