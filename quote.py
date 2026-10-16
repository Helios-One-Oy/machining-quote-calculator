#!/usr/bin/env python3
"""Price a machined part at several quantities from a small JSON job file.

    python3 quote.py example-bracket.json
    python3 quote.py example-bracket.json --qty 1 5 25 100
"""
import argparse
import json


def price_table(job, quantities):
    material = job["material_price_per_lb"] * job["blank_weight_lb"]
    ops = job["operations"]
    setup_cost = sum(op["rate_per_hour"] * op["setup_min"] for op in ops) / 60
    run_cost = sum(op["rate_per_hour"] * op["run_min_per_part"] for op in ops) / 60
    lot = sum(o.get("lot_charge", 0) for o in job.get("outside_processing", []))
    per_part_outside = sum(o.get("per_part", 0) for o in job.get("outside_processing", []))
    markup = job.get("markup", 0.3)
    rows = []
    for q in quantities:
        cost = material + setup_cost / q + run_cost + lot / q + per_part_outside
        price = cost * (1 + markup)
        fixed_share = (setup_cost + lot) / q / cost
        rows.append((q, material, setup_cost / q, run_cost, lot / q + per_part_outside, cost, price, price * q, fixed_share))
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("job")
    ap.add_argument("--qty", type=int, nargs="+", default=[1, 10, 50])
    a = ap.parse_args()
    job = json.load(open(a.job))
    print(job.get("part", "part"))
    print(f"{'qty':>5} {'material':>9} {'setup':>9} {'run':>9} {'outside':>9} {'cost':>9} {'price':>9} {'job total':>11} {'fixed %':>8}")
    for q, m, s, r, o, c, p, t, f in price_table(job, a.qty):
        print(f"{q:>5} {m:>9.2f} {s:>9.2f} {r:>9.2f} {o:>9.2f} {c:>9.2f} {p:>9.2f} {t:>11.2f} {f:>7.0%}")


if __name__ == "__main__":
    main()
