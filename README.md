# 52-Week Fight or Rest — A Text Simulation Game

## 1. About the Game

### Core Concept

A lightweight text-based simulation game where you make weekly choices between **resting** and **fighting** over 52 weeks. Balance your energy and inspiration to accumulate the highest possible achievement score. Minimal controls — just text input — perfect for quick sessions.

### Design Philosophy

The game is built around the principle of **work-life balance**: burning out leads to inefficiency, while too much rest means no progress. It also incorporates a "guaranteed minimum + state-dependent bonus" model — effort always pays off, but *how much* depends on your current state and a bit of luck.

## 2. Setup

- **Duration**: 52 weeks (one decision per week)
- **Resources**: Energy and Inspiration, both start at 20 (max 20)
  - **Energy**: The cost of fighting. If it drops to 0, the game ends.
  - **Inspiration**: Affects fight rewards. Acts as both a resource and a "reward multiplier."
- **Achievement**: 52 slots (one per week), all start at 0. Fight results are recorded in real time.

## 3. How to Play

### Display

Each week shows three pieces of information:
- **Achievement timeline**: All 52 weeks displayed, current week highlighted in yellow
- **Resource status**: Energy and Inspiration shown in blue (out of 20)
- **Week counter**: Current week number (e.g., Week 12/52) in blue

### Actions

Each week, choose one of two actions:

| Action | Input | Energy | Inspiration | Achievement |
|--------|-------|--------|-------------|-------------|
| **Rest** | `r` | +5 | +3 | None |
| **Fight** | `f` | -5 | -3 | +7 + random(0, current inspiration) |

> The random bonus means higher inspiration = higher potential rewards. The fixed +7 guarantees that effort always produces *something*, while the random component mirrors real-life uncertainty.

### Game Over

The game ends in one of two ways:
- **Forced end**: Energy or Inspiration drops to 0 or below. **Watch out when energy is at 5 — unless it's the final week, you must rest or the game ends!**
- **Natural end**: All 52 weeks completed.

At the end, you'll see your total weeks played and cumulative achievement score.

## 4. Tips

The key is **balance**: over-fighting drains your resources, but over-resting wastes potential. Keep inspiration high for better fight rewards. Rest when resources are low, fight when they're full.

> Inspiration is your "reward multiplier" and the random bonus is your "reality simulator" — effort has a guaranteed floor, but returns depend on your state. Balance both to maximize your score.

## 5. Running the Game

```bash
python main.py
```

Requires Python 3.x. No external dependencies — uses only the standard library.

## License

GPL-3.0 — see [LICENSE](LICENSE).
