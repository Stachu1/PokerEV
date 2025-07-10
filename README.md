# 🃏 PokerEV — Poker Expected Value Calculator

**PokerEV** is a command-line tool written in Python that estimates your **chances of winning a Texas Hold'em hand** based on your current cards, the visible community cards, and the pot size. It performs **Monte Carlo simulations** (default: 200,000 games) to compute your **expected value (EV)** when deciding whether to call a bet.

---

## 🚀 Features

- Simulates thousands of poker games to estimate:
  - 🟢 **Win** probability
  - 🟡 **Tie** probability
  - 🔴 **Loss** probability
- Calculates **expected value (EV)** of calling a bet given:
  - Your hand
  - Community cards
  - Pot size and bet to call
- Fast console output with real-time updates
- Interactive prompt interface
- Supports variable number of opponents

---

## 📦 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/pokerev.git
   cd pokerev
   ```

2. Install dependencies:
   ```bash
   pip install colorama
   ```

---

## 🧠 How It Works

PokerEV simulates random hands for other players and completes the board (if necessary), then scores each hand to determine win/tie/loss counts. Based on the outcomes and input pot/to-call values, it calculates the expected value:

EV = P_win × pot + P_tie × (pot / 2) - P_loss × to_call

This helps answer the question:  
👉 _Is it worth risking a given bet for the current pot?_  
For example, risking 100 to win a 900 pot is break-even at just 10% win probability (ignoring ties).

---

## 🧪 Example Usage

```bash
python main.py
```
<img width="500" height="700" alt="image" src="https://github.com/user-attachments/assets/f58082a4-d0d1-4ca7-adaf-997e3e5889cd" />

Output format:  
`EV: <value> [Win% Tie% Loss%]`

---

## ⚙️ Options

You can pass the number of simulation iterations as a command-line argument:

```bash
python main.py 500000
```

Default: `200000`
