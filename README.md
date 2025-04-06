# 🧹 LinuxCleaner

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Linux-blue.svg)]()
[![Python](https://img.shields.io/badge/python-3.6%2B-blue.svg)]()

> ⚙️ **LinuxCleaner** is a safe, interactive Python tool for decluttering your Linux system — no magic, no surprises, just clean code and clean machines.

---

## 🚀 Features

- 🔧 Clean apt cache and autoremove orphaned packages
- 🧾 Vacuum system journal logs (configurable retention)
- 🗑️ Clear rotated logs, temp files, trash, thumbnails
- 📦 Remove stale Snap and Flatpak packages
- 🧠 Prompt-based: choose exactly what gets cleaned
- 🧼 Minimal, fast, and safe for daily/weekly use

---

## 📸 Screenshot

```bash
🚀 Welcome to the Linux Cleanup Commander

1. Clean apt cache and orphaned packages? [y/N]:
2. Clean systemd journal logs (keep 7 days)? [y/N]:
3. Delete rotated and archived logs in /var/log? [y/N]:
4. Clean /tmp and /var/tmp directories? [y/N]:
5. Clear user thumbnails and trash? [y/N]:
6. Remove old Snap package revisions? [y/N]:
7. Remove unused Flatpak packages? [y/N]:
