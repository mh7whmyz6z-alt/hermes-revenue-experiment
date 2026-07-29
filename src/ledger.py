#!/usr/bin/env python3
"""
Simple ledger helper for the Hermes Revenue Experiment.
Usage examples:
  python src/ledger.py add --revenue 25 --source "gumroad-prompt-pack" --experiment "0002" --proof "screenshots/receipt-2026-08-01.png" --notes "First sale"
  python src/ledger.py show
"""

import json
import sys
import datetime
from pathlib import Path
from typing import Any

LEDGER_PATH = Path(__file__).parent.parent / "earnings" / "ledger.json"

def load_ledger() -> dict[str, Any]:
    if not LEDGER_PATH.exists():
        return {
            "experiment_id": "hermes-revenue-experiment",
            "starting_capital_usd": 0.0,
            "total_verified_revenue_usd": 0.0,
            "total_costs_usd": 0.0,
            "net_usd": 0.0,
            "currency": "USD",
            "entries": [],
            "last_updated": None,
            "notes": ""
        }
    with open(LEDGER_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_ledger(data: dict[str, Any]) -> None:
    data["last_updated"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    LEDGER_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(LEDGER_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def add_entry(revenue: float = 0.0, cost: float = 0.0, source: str = "", experiment: str = "",
              proof: str = "", notes: str = "") -> dict[str, Any]:
    ledger = load_ledger()
    entry = {
        "id": f"entry-{len(ledger['entries']) + 1:04d}",
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "revenue_usd": round(revenue, 2),
        "cost_usd": round(cost, 2),
        "net_usd": round(revenue - cost, 2),
        "source": source,
        "experiment": experiment,
        "proof": proof,
        "notes": notes
    }
    ledger["entries"].append(entry)
    ledger["total_verified_revenue_usd"] = round(
        ledger["total_verified_revenue_usd"] + revenue, 2
    )
    ledger["total_costs_usd"] = round(ledger["total_costs_usd"] + cost, 2)
    ledger["net_usd"] = round(
        ledger["total_verified_revenue_usd"] - ledger["total_costs_usd"], 2
    )
    save_ledger(ledger)
    print(f"Added entry {entry['id']}. New net: ${ledger['net_usd']:.2f}")
    return entry

def show() -> None:
    ledger = load_ledger()
    print(json.dumps(ledger, indent=2))

def main():
    if len(sys.argv) < 2:
        print("Commands: add, show")
        return

    cmd = sys.argv[1]
    if cmd == "show":
        show()
    elif cmd == "add":
        # Very basic arg parsing for now
        revenue = 0.0
        cost = 0.0
        source = "manual"
        experiment = ""
        proof = ""
        notes = ""
        for arg in sys.argv[2:]:
            if arg.startswith("--revenue="):
                revenue = float(arg.split("=", 1)[1])
            elif arg.startswith("--cost="):
                cost = float(arg.split("=", 1)[1])
            elif arg.startswith("--source="):
                source = arg.split("=", 1)[1]
            elif arg.startswith("--experiment="):
                experiment = arg.split("=", 1)[1]
            elif arg.startswith("--proof="):
                proof = arg.split("=", 1)[1]
            elif arg.startswith("--notes="):
                notes = arg.split("=", 1)[1]
        add_entry(revenue=revenue, cost=cost, source=source, experiment=experiment, proof=proof, notes=notes)
    else:
        print("Unknown command")

if __name__ == "__main__":
    main()
