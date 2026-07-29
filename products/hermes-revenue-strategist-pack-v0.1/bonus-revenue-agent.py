#!/usr/bin/env python3
"""
Bonus: Minimal Revenue Agent starter (Hermes Revenue Experiment)
This is a tiny harness you can run to structure your own revenue sessions using the prompt pack.

Usage:
    python bonus-revenue-agent.py "I need ideas for making money as an AI with $0 capital"
"""

import sys
from pathlib import Path

def main():
    if len(sys.argv) < 2:
        print("Usage: python bonus-revenue-agent.py \"your goal here\"")
        print("\nExample: python bonus-revenue-agent.py \"Create my first $10 digital product\"")
        return

    goal = " ".join(sys.argv[1:])
    
    print("=" * 60)
    print("HERMES REVENUE AGENT — v0.1")
    print(f"Goal: {goal}")
    print("=" * 60)
    
    print("\n[PHASE 1] Load full context (README + ledger + this pack)")
    print("→ In a real session, paste the main experiment README + current ledger here.\n")
    
    print("[PHASE 2] Run 02-ideation-engine on the goal")
    print("Prompt to use:")
    print("  Use the ideation engine from this pack on the following goal...")
    print(f"  Goal: {goal}\n")
    
    print("[PHASE 3] Validate top idea with 03-validation-scanner")
    print("[PHASE 4] Forge MVP using 04-mvp-forger")
    print("[PHASE 5] Plan distribution with 05-distribution-cannon")
    print("[PHASE 6] Write offers with 06-monetization-closer")
    print("[PHASE 7] Log everything with 07-ledger-accountant\n")
    
    print("Full playbook available in: full-playbook.md")
    print("All modules are in this folder.")
    print("\nNext step: Feed the relevant module + this goal into your LLM.")
    print("=" * 60)

if __name__ == "__main__":
    main()
