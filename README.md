## Setup & Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Muskan-Tarafder/Trading_Bot.git
   cd Trading_Bot
   ```
2. **Set Up Environment**:

```bash
  python -m venv venv
  # Windows:
  venv\Scripts\activate 
  # Mac/Linux:
  source venv/bin/activate
```
4. **Install Dependencies**:

```bash
pip install -r requirements.txt
```

5. **API Configuration**:
Create a .env file in the root directory and add Binance Testnet credentials:

```bash
API=testnet_api_key
SEC=testnet_api_secret
```
## Usage Examples

Run in terminal

1. Place a Market Order

```bash
python cli.py --symbol BTCUSDT --side BUY --order-type MARKET --quantity 0.01
```

2. Place a Limit Order

```bash
python cli.py --symbol BTCUSDT --side SELL --order-type LIMIT --quantity 0.01 --price 68000
```


## Assumptions

1. **Security & Environment Variables**:
For security, API credentials are not hardcoded. The application expects a .env file in the root directory. This file is included in .gitignore to prevent sensitive data from being committed to the repository.
