<div align="center">

# 🎤 AUJLA-SZN-tour-portal 🔥

### *Official Terminal Concert Booking, 38-Track Setlist Explorer & Merch Store*

> **PVR-style pass booking, live setlist browsing, and tour merch drops—running straight from your terminal.**

**[GitHub Repository](https://github.com/yuvraj-maan/AUJLA-SZN-tour-portal)** • **[Run Guide](#-run-in-3-steps)** • **[Features](#-what-it-does)**

</div>

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
AUJLA-SZN-tour-portal/
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
git clone https://github.com/yuvraj-maan/AUJLA-SZN-tour-portal.git
cd AUJLA-SZN-tour-portal
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
