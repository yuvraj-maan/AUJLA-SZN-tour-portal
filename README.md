# 🎤 AUJLA SZN TOUR // Concert & Merch CLI Portal

> **PVR-style pass booking, 38-track live setlist explorer, and official tour merch store—built in pure Python with zero external dependencies.**

![Python 3](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Zero Dependencies](https://img.shields.io/badge/Dependencies-Standard%20Library%20Only-2ea44f?style=for-the-badge)
![Storage](https://img.shields.io/badge/Persistence-JSON-f59e0b?style=for-the-badge)
![Setlist](https://img.shields.io/badge/Live%20Setlist-38%20Tracks-ec4899?style=for-the-badge)

---

## ✨ What It Does

* 🎟️ **Tour Dates & Zones:** Browse tour stops (`New Delhi`, `Chandigarh`, `Mumbai`) with pricing tiers across **General**, **Fan Pit**, and **VIP**.
* 🛑 **5-Pass Limit Per Person:** Validates pass quantities cleanly and caps bookings at **5 passes per attendee**.
* 👕 **Merch Store & Free Drops:** Pick from hoodies, caps, tees, oversized jackets, totes, poster packs, or complimentary **LED Concert Wristbands (`FREE`)**.
* 🧮 **Smart Total Calculation:** Calculates ticket subtotals, merch totals, a 5% booking fee (`math.ceil`), and final totals.
* 🎶 **38-Track Live Setlist:** Browse tracks across *AUJLA SZN 1 EP*, *P-POP CULTURE*, *Making Memories*, *BTFU*, *Four Me EP*, *Four You EP*, and singles.
* 💾 **Auto-Created `bookings.json`:** Creates and updates `bookings.json` locally on booking without needing a pre-populated file in the repo.

---

## 📁 Folder Layout

```text
aujla-szn-tour-portal/
├── capstone.py     # Main terminal application, booking flow & JSON persistence
├── concerts.json   # Tour cities, dates, venues & zone pricing
├── playlist.json   # 38-song concert setlist with project tags
├── merch.json      # Official tour merch items & prices
└── README.md       # Project overview & setup guide
```

> 💡 `bookings.json` is automatically generated locally when passes are booked, keeping the repository clean on fresh clones.

---

## 🚀 Run in 3 Steps

### 1. Clone & Enter the Folder
```bash
git clone <YOUR_GITHUB_REPO_URL>
cd aujla-szn-tour-portal
```

### 2. Start the App
```bash
python3 capstone.py
```

### 3. Pick an Option (`1`–`6`)
| Option | Action |
| :--- | :--- |
| `1` | 🏟️ View tour dates & ticket zones |
| `2` | 🛍️ View official tour merch |
| `3` | 🎧 View 38-song live setlist playlist |
| `4` | 🎫 Book concert passes & merch |
| `5` | 📋 View saved bookings |
| `6` | 🚪 Exit portal |

---

## 🛠️ Built With

* 🐍 **Python 3** (`json`, `math`, `pathlib`)
* 📄 **JSON Data Stores** (`concerts.json`, `playlist.json`, `merch.json`, `bookings.json`)

---

## 👨‍💻 Author

**Yuvraj Maan** (`@yuvraj-maan`) — B.Tech CSE (AI & ML)
