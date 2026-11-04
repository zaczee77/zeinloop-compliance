# Demo: real estate compliance summary pattern

This demo is a small reference implementation of the Zeinloop workflow pattern in plain Python with no external packages. It calls no real model and uses no network.

## How to run it

1. Open a terminal in this folder.
2. Run the command: python3 compliance_demo.py

## What it does

1. It loads three synthetic sample buildings.
2. It validates each building for required fields: building identifier, square footage, and emissions data, with square footage required to be positive.
3. It computes emissions per square foot for each validated building.
4. It flags incomplete buildings for human review, naming the missing fields.
5. It prints a summary of summarized and flagged buildings.

## Expected output

1. BLDG001: 0.0160 kg per square foot, within threshold.
2. BLDG002: flagged for review, missing emissions_kg.
3. BLDG003: 0.0300 kg per square foot, above threshold.
4. Summary: 2 summarized, 1 flagged for review.

## Notes on honesty

The sample data is invented for illustration only. It is not building data, not utility data, and not employer data. The threshold is illustrative only. It is not a legal limit and it is not a New York City rule. The demo does not reproduce any employer system.
