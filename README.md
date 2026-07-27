# VenomStore-vuln-PoC

## Vulnerability Type
Race Condition / Replay Attack

## Affected Endpoint
OPTIONS /functions/v1/retail-mini-app-serve?action=spin_fortune_wheel&bot_id=4f0355aa-9791-4912-9136-917f2658188d&_t=<timestamp>

## Description
The Wheel of Fortune endpoint lacks idempotency checks. By intercepting and dropping confirmation requests, an attacker can replay successful spin results multiple times, accumulating unlimited rewards.

## Impact
- Unlimited in-app currency/rewards
- Financial loss for the platform
- Potential for abuse in other endpoints

## Credits
**Discovered by:** [CIVØ](https://t.me/+9UF1gyryCJw4ODk9) 
**Date:** 2026-07-24
**Bot username:** @VenomEuropeBot (https://t.me/VenomEuropeBot)
