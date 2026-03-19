# Swift 100 – RWA Section Update (March 2026)

_Date: 2026-03-18_

## Scope

This note documents the first structured update to the **RWA (Real World Assets)** slice of the Swift 100 list.

Goals:

- Keep the RWA section focused on:
  - Tokenized Treasuries / conservative on-chain yield
  - On-chain credit with real traction
  - Regulated RWA infrastructure and supply-chain data
- Reduce exposure to fragile or overlapping credit experiments
- Preserve CPOOL as the on-chain credit name we want to keep watching

Current RWA-heavy names in Swift 100:

- ONDO – RWA / Tokenized Treasuries
- OM – MANTRA (RWA)
- CFG – Centrifuge (RWA Credit)
- POLYX – Polymesh (Regulated RWA Chain)
- TRAC – OriginTrail (RWA / Supply Data)
- MPL – Maple (Onchain Credit)
- CPOOL – Clearpool (Onchain Credit)
- GFI – Goldfinch (Emerging-Market Credit)
- ALGO – Algorand (L1 / RWA Infra)
- VET – VeChain (Supply Chain / Enterprise)

---

## Decisions

### 1. Remove GFI (Goldfinch)

**Verdict:** Remove from Swift 100.

**Rationale:**

- Goldfinch is focused on emerging-market private credit. In practice, multiple high-profile pool issues (e.g. Tugende and others) have severely damaged trust.
- The token has suffered a major drawdown and the on-chain credit risk has not translated into a sustainable, diversified on-chain lending market.
- For a curated “flagship 100” list, the risk/reward profile and track record no longer justify a dedicated slot.

**Impact:**

- Reduces exposure to fragile EM credit experiments.
- Frees a slot for stronger or more differentiated RWA names.

---

### 2. Remove OM (MANTRA)

**Verdict:** Remove from Swift 100.

**Rationale:**

- OM (MANTRA) is a high-beta RWA + staking narrative token with significant overlap to other RWA exposures already present (notably ONDO and CFG/MPL for yield and credit).
- Execution and product-market fit are less clear than our RWA anchors, and the token is more narrative-driven than infrastructure-driven at this stage.
- For Swift 100, we prefer to anchor RWA exposure in protocols with clearer usage, infra roles, and transparency.

**Impact:**

- Reduces narrative overlap in the RWA slice.
- Keeps the section centered around better-defined RWA infrastructure and credit platforms.

---

### 3. Explicitly Keep CPOOL (Clearpool)

**Verdict:** Keep in Swift 100.

**Rationale:**

- Clearpool remains one of the recognizable on-chain credit brands, with pools targeting institutional borrowers.
- While on-chain credit is still an emerging and volatile space, CPOOL offers a differentiated view of unsecured or partially-secured credit relative to CFG/MPL.
- Lucky explicitly wants to **keep CPOOL** as the on-chain credit name to watch alongside CFG/MPL, rather than removing it in this update.

**Impact:**

- Swift 100 maintains CPOOL as a key on-chain credit exposure.
- RWA credit representation becomes: CFG + CPOOL (+ MPL if retained after further review).

---

## Resulting RWA Core (post-update)

After this update, the RWA-focused slice of Swift 100 is anchored around:

- **Treasuries / On-chain Yield**
  - ONDO – tokenized Treasuries & yield products

- **On-chain Credit**
  - CFG – Centrifuge (RWA credit pools)
  - CPOOL – Clearpool (institutional on-chain credit)
  - MPL – Maple (on-chain credit) — *kept for now, pending deeper comparative review*

- **Regulated / Infrastructure / Data**
  - POLYX – Polymesh (regulated RWA chain)
  - TRAC – OriginTrail (supply chain / provenance for RWAs)
  - ALGO – Algorand (L1 often used in RWA/institutional discussions)
  - VET – VeChain (enterprise supply chain / RWA-adjacent infra)

This keeps the RWA slice reasonably diversified across:

- Yield (Treasuries)
- Credit (secured/unsecured)
- Regulated infra and supply-chain data

while pruning weaker/overlapping names.

---

## Next Candidates to Monitor (Not Yet Added)

These are **watchlist** candidates for future RWA rotations, not immediate additions:

- SYRUP (or similar retail RWA yield aggregator)
  - Potential retail front-end on top of issuer protocols like ONDO.
  - Would strengthen the Treasuries / fixed-income angle for non-institutional users.

- A refined “second credit protocol” choice
  - Decide between MPL and any newer credit protocols based on:
    - Pool performance
    - Default history
    - On-chain AUM
    - Risk controls and transparency.

- A second regulated RWA infra or issuer token alongside POLYX
  - Must be tied to real tokenization rails, not just whitepapers.
  - Should show up on RWA dashboards with non-trivial AUM.

No watchlist token is added until it clears these checks and a full Swift 100 thesis is written.

---

## Notes for Future Updates

- This RWA update is intentionally conservative: we remove two weaker names (GFI, OM) and explicitly keep CPOOL at Lucky's request.
- Future RWA updates should:
  - Re-check RWA.xyz / equivalent dashboards for AUM and asset composition.
  - Re-run a light threat / trust analysis on any new RWA candidates (Clawtrust-style).
  - Only promote watchlist names into Swift 100 after both data and narrative are compelling.
