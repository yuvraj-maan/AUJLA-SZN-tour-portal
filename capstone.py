import json
import math
from pathlib import Path


def get_file_path(filename):
    base_dir = Path(__file__).resolve().parent
    return base_dir / filename


def load_json_data(filename):
    file_path = get_file_path(filename)
    if not file_path.exists():
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump([], f, indent=2)
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read().strip()
        if content == "":
            return []
        return json.loads(content)


def save_json_data(filename, data):
    file_path = get_file_path(filename)
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def main():
    tour_headline = "AUJLA SZN TOUR"
    max_passes_per_person = 5

    concerts = load_json_data("concerts.json")
    playlist = load_json_data("playlist.json")
    merch_items = load_json_data("merch.json")
    bookings = load_json_data("bookings.json")

    while True:
        print("\n==========================================")
        print("           " + tour_headline)
        print("     Official Concert & Merch Portal")
        print("==========================================")
        print("1. View tour dates & ticket zones")
        print("2. View official merch store")
        print("3. View live concert playlist")
        print("4. Book concert passes & merch")
        print("5. View booked passes")
        print("6. Exit")

        choice = input("Enter choice (1-6): ").strip()

        if choice == "1":
            print("\n=== " + tour_headline + " - DATES & ZONES ===")
            print("(Max limit: " + str(max_passes_per_person) + " passes per person)")
            for c in concerts:
                print("\nShow ID:", c["id"], "|", tour_headline, "-", c["city"])
                print("Venue:", c["venue"], "| Date:", c["date"])
                for zone_name in c["zones"]:
                    info = c["zones"][zone_name]
                    print("  -", zone_name, ": Rs." + str(info["price"]))

        elif choice == "2":
            print("\n=== OFFICIAL MERCH STORE ===")
            for item in merch_items:
                if item["price"] == 0:
                    print(str(item["id"]) + ". " + item["name"] + " - FREE")
                else:
                    print(str(item["id"]) + ". " + item["name"] + " - Rs." + str(item["price"]))

        elif choice == "3":
            print("\n=== " + tour_headline + " - LIVE SETLIST PLAYLIST ===")
            for p in playlist:
                print("Track " + str(p["track"]) + ": " + p["song"] + " [" + p["project"] + "]")
            print("\nTotal Songs in Setlist:", len(playlist))

        elif choice == "4":
            print("\n=== BOOK PASSES FOR " + tour_headline + " ===")
            for c in concerts:
                print(str(c["id"]) + ". " + tour_headline + " - " + c["city"] + " (" + c["date"] + ")")

            raw_id = input("Enter Show ID: ").strip()
            if not raw_id.isdigit():
                print("Please enter a valid Show ID.")
                continue

            show_id = int(raw_id)
            selected_show = None
            for c in concerts:
                if c["id"] == show_id:
                    selected_show = c
                    break

            if selected_show is None:
                print("Show not found.")
                continue

            print("\nAvailable Zones (Max " + str(max_passes_per_person) + " passes per person):")
            for zone_name in selected_show["zones"]:
                info = selected_show["zones"][zone_name]
                print("  -", zone_name, ": Rs." + str(info["price"]))

            raw_zone = input("Enter zone name (General / Fan Pit / VIP): ").strip().lower()
            selected_zone = None
            for zone_name in selected_show["zones"]:
                if zone_name.lower() == raw_zone:
                    selected_zone = zone_name
                    break

            if selected_zone is None:
                print("Invalid zone name.")
                continue

            raw_tickets = input("How many passes do you want (1-" + str(max_passes_per_person) + ")? ").strip()
            if not raw_tickets.isdigit():
                print("Enter a valid number of passes.")
                continue

            ticket_qty = int(raw_tickets)
            if ticket_qty <= 0 or ticket_qty > max_passes_per_person:
                print("Limit exceeded! One person can book a maximum of", max_passes_per_person, "passes.")
                continue

            zone_info = selected_show["zones"][selected_zone]

            fan_name = input("Enter lead attendee name: ").strip()
            if fan_name == "":
                fan_name = "Guest"

            bought_merch = []
            want_merch = input("Add official merch? (yes/no): ").strip().lower()

            while want_merch == "yes":
                print("\n--- OFFICIAL MERCH STORE ---")
                for item in merch_items:
                    if item["price"] == 0:
                        print(str(item["id"]) + ". " + item["name"] + " - FREE")
                    else:
                        print(str(item["id"]) + ". " + item["name"] + " - Rs." + str(item["price"]))

                raw_mid = input("Enter Merch ID: ").strip()
                if not raw_mid.isdigit():
                    print("Invalid Merch ID.")
                else:
                    mid = int(raw_mid)
                    selected_merch = None
                    for item in merch_items:
                        if item["id"] == mid:
                            selected_merch = item
                            break

                    if selected_merch is None:
                        print("Merch item not found.")
                    else:
                        raw_mqty = input("Enter quantity: ").strip()
                        if not raw_mqty.isdigit():
                            print("Invalid quantity.")
                        else:
                            mqty = int(raw_mqty)
                            if mqty <= 0:
                                print("Quantity must be at least 1.")
                            else:
                                sub = selected_merch["price"] * mqty
                                bought_merch.append({
                                    "name": selected_merch["name"],
                                    "qty": mqty,
                                    "total": sub,
                                })
                                print("Added:", selected_merch["name"], "x" + str(mqty))

                want_merch = input("Add another merch item? (yes/no): ").strip().lower()

            ticket_total = ticket_qty * zone_info["price"]
            merch_total = 0
            for m in bought_merch:
                merch_total = merch_total + m["total"]

            fee = math.ceil((ticket_total + merch_total) * 0.05)
            grand_total = ticket_total + merch_total + fee

            booking = {
                "fan": fan_name,
                "tour": tour_headline + " - " + selected_show["city"],
                "venue": selected_show["venue"],
                "date": selected_show["date"],
                "zone": selected_zone,
                "passes": ticket_qty,
                "merch": bought_merch,
                "total": grand_total,
            }
            bookings.append(booking)
            save_json_data("bookings.json", bookings)

            print("\n=== DIGITAL CONCERT PASS ===")
            print("Event:", booking["tour"])
            print("Attendee:", booking["fan"])
            print("Venue:", booking["venue"], "| Date:", booking["date"])
            print("Zone:", booking["zone"], "| Passes:", booking["passes"])
            for m in bought_merch:
                if m["total"] == 0:
                    print("Merch:", m["name"], "x" + str(m["qty"]), "= FREE")
                else:
                    print("Merch:", m["name"], "x" + str(m["qty"]), "= Rs." + str(m["total"]))
            print("Tickets: Rs." + str(ticket_total) + " | Merch: Rs." + str(merch_total) + " | Fee (5%): Rs." + str(fee))
            print("Total Paid: Rs." + str(grand_total))
            print("Saved to bookings.json!")

        elif choice == "5":
            if len(bookings) == 0:
                print("No concert passes booked yet.")
            else:
                num = 1
                for b in bookings:
                    print("\nPass #" + str(num), "-", b["fan"])
                    print("Event:", b["tour"], "(" + b["date"] + ")")
                    print("Zone:", b["zone"], "| Quantity:", b["passes"])
                    if len(b["merch"]) == 0:
                        print("Merch: None")
                    else:
                        for m in b["merch"]:
                            if m["total"] == 0:
                                print("  -", m["name"], "x" + str(m["qty"]), "(FREE)")
                            else:
                                print("  -", m["name"], "x" + str(m["qty"]), "(Rs." + str(m["total"]) + ")")
                    print("Total Paid: Rs." + str(b["total"]))
                    num = num + 1

        elif choice == "6":
            print("Exiting " + tour_headline + " Portal. Enjoy the show!")
            break

        else:
            print("Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()