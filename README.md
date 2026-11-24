# AUJLA SZN TOUR — Official Concert & Merch Portal

> **PVR-style pass booking, 38-track live setlist explorer, and official tour merch store—running straight from your terminal in pure Python.**

Built with zero external dependencies (`json`, `math`, and `pathlib` from the Python standard library), this terminal portal brings the **AUJLA SZN TOUR** experience to life with modular JSON data, pass limits, complimentary wristband drops, and persistent local booking storage.

---

## Highlights & Features

* **Tour Dates & Ticket Zones:** Browse upcoming stops (`New Delhi`, `Chandigarh`, `Mumbai`) with pricing across **General**, **Fan Pit**, and **VIP** zones.
* **5-Pass Cap Per Person:** Enforces a strict limit of up to **5 passes per attendee** with clear input validation.
* **Official Merch Store + Free Drops:** Add tour hoodies, caps, tees, oversized jackets, totes, poster packs, or complimentary **LED Concert Wristbands (`FREE`)**.
* **5% Booking Fee Calculation:** Computes ticket subtotals, merch totals, a 5% ceiling-rounded fee (`math.ceil`), and grand totals cleanly.
* **38-Song Live Setlist:** Explore every track from *AUJLA SZN 1 EP*, *P-POP CULTURE*, *Making Memories*, *BTFU*, *Four Me EP*, *Four You EP*, and classic singles.
* **Auto-Persisting `bookings.json`:** Automatically creates and updates `bookings.json` locally on booking without requiring manual setup on first run.

---

## Repository Structure

```text
aujla-szn-tour-portal/
├── capstone.py       # Main CLI portal, pricing logic, and JSON persistence
├── concerts.json     # Tour stops, dates, venues, and zone ticket prices
├── playlist.json     # 38-track live concert setlist with album/EP/single tags
├── merch.json        # Official merchandise catalog and pricing
└── README.md         # Project documentation
```

*(Note: `bookings.json` is generated automatically in the project folder when you run the app and book passes, keeping the repository clean on fresh clones.)*

---

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone <YOUR_GITHUB_REPO_URL>
   cd aujla-szn-tour-portal
   ```

2. **Run the portal (Python 3):**
   ```bash
   python3 capstone.py
   ```

3. **Navigate the menu (`1`–`6`):**
   * `1` — View tour dates & ticket zones
   * `2` — View official merch store
   * `3` — View live concert playlist (38 tracks)
   * `4` — Book concert passes & merch
   * `5` — View booked passes
   * `6` — Exit

---

## Tech Stack

* **Language:** Python 3
* **Standard Library Modules:** `json`, `math`, `pathlib`
* **Data Format:** Structured JSON files (`concerts.json`, `playlist.json`, `merch.json`, `bookings.json`)

---

## Author

Built by **Yuvraj Maan** (`@yuvraj-maan`) — B.Tech CSE (AI & ML) student crafting hands-on Python & software projects.
