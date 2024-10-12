import yfinance as yf
import pandas as pd
from difflib import get_close_matches
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

symbol_mapping = {
    # Top 100 Indian Stocks (NSE)
    'RELIANCE.NS': 'Reliance Industries Ltd.',
    'TCS.NS': 'Tata Consultancy Services Ltd.',
    'HDFCBANK.NS': 'HDFC Bank Ltd.',
    'INFY.NS': 'Infosys Ltd.',
    'ICICIBANK.NS': 'ICICI Bank Ltd.',
    'BAJFINANCE.NS': 'Bajaj Finance Ltd.',
    'SBIN.NS': 'State Bank of India',
    'HINDUNILVR.NS': 'Hindustan Unilever Ltd.',
    'ITC.NS': 'ITC Ltd.',
    'BHARTIARTL.NS': 'Bharti Airtel Ltd.',
    'KOTAKBANK.NS': 'Kotak Mahindra Bank Ltd.',
    'LT.NS': 'Larsen & Toubro Ltd.',
    'HCLTECH.NS': 'HCL Technologies Ltd.',
    'ASIANPAINT.NS': 'Asian Paints Ltd.',
    'MARUTI.NS': 'Maruti Suzuki India Ltd.',
    'AXISBANK.NS': 'Axis Bank Ltd.',
    'WIPRO.NS': 'Wipro Ltd.',
    'ULTRACEMCO.NS': 'UltraTech Cement Ltd.',
    'ONGC.NS': 'Oil & Natural Gas Corporation Ltd.',
    'TATAMOTORS.NS': 'Tata Motors Ltd.',
    'ADANIGREEN.NS': 'Adani Green Energy Ltd.',
    'POWERGRID.NS': 'Power Grid Corporation of India Ltd.',
    'HDFCLIFE.NS': 'HDFC Life Insurance Co. Ltd.',
    'M&M.NS': 'Mahindra & Mahindra Ltd.',
    'ADANIPORTS.NS': 'Adani Ports and SEZ Ltd.',
    'GRASIM.NS': 'Grasim Industries Ltd.',
    'SUNPHARMA.NS': 'Sun Pharmaceutical Industries Ltd.',
    'TITAN.NS': 'Titan Company Ltd.',
    'HINDALCO.NS': 'Hindalco Industries Ltd.',
    'JSWSTEEL.NS': 'JSW Steel Ltd.',
    'NTPC.NS': 'NTPC Ltd.',
    'DIVISLAB.NS': 'Divi’s Laboratories Ltd.',
    'SHREECEM.NS': 'Shree Cement Ltd.',
    'TATASTEEL.NS': 'Tata Steel Ltd.',
    'ADANITRANS.NS': 'Adani Transmission Ltd.',
    'BAJAJ-AUTO.NS': 'Bajaj Auto Ltd.',
    'EICHERMOT.NS': 'Eicher Motors Ltd.',
    'UPL.NS': 'UPL Ltd.',
    'PIDILITIND.NS': 'Pidilite Industries Ltd.',
    'HEROMOTOCO.NS': 'Hero MotoCorp Ltd.',
    'DRREDDY.NS': 'Dr. Reddy’s Laboratories Ltd.',
    'NESTLEIND.NS': 'Nestle India Ltd.',
    'SBICARD.NS': 'SBI Cards and Payment Services Ltd.',
    'INDUSINDBK.NS': 'IndusInd Bank Ltd.',
    'BRITANNIA.NS': 'Britannia Industries Ltd.',
    'COALINDIA.NS': 'Coal India Ltd.',
    'IOC.NS': 'Indian Oil Corporation Ltd.',
    'DABUR.NS': 'Dabur India Ltd.',
    'GAIL.NS': 'GAIL India Ltd.',
    'ICICIGI.NS': 'ICICI Lombard General Insurance Co. Ltd.',
    'SIEMENS.NS': 'Siemens Ltd.',
    'TECHM.NS': 'Tech Mahindra Ltd.',
    'DMART.NS': 'Avenue Supermarts Ltd.',
    'HAVELLS.NS': 'Havells India Ltd.',
    'MCDOWELL-N.NS': 'United Spirits Ltd.',
    'TORNTPHARM.NS': 'Torrent Pharmaceuticals Ltd.',
    'BERGEPAINT.NS': 'Berger Paints India Ltd.',
    'VOLTAS.NS': 'Voltas Ltd.',
    'LICI.NS': 'Life Insurance Corporation of India',
    'CIPLA.NS': 'Cipla Ltd.',
    'ONGC.NS': 'Oil and Natural Gas Corporation Ltd.',
    'BANDHANBNK.NS': 'Bandhan Bank Ltd.',
    'ADANIPOWER.NS': 'Adani Power Ltd.',
    'CANBK.NS': 'Canara Bank Ltd.',
    'ZOMATO.NS': 'Zomato Ltd.',
    'NYKAA.NS': 'FSN E-Commerce Ventures Ltd. (Nykaa)',
    'IRCTC.NS': 'Indian Railway Catering & Tourism Corp Ltd.',
    'NAUKRI.NS': 'Info Edge India Ltd.',
    'JUBLFOOD.NS': 'Jubilant FoodWorks Ltd.',
    'BHARATFORG.NS': 'Bharat Forge Ltd.',
    'TVSMOTOR.NS': 'TVS Motor Company Ltd.',
    'BANKBARODA.NS': 'Bank of Baroda',
    'PNB.NS': 'Punjab National Bank',
    'IDFCFIRSTB.NS': 'IDFC First Bank Ltd.',
    'DLF.NS': 'DLF Ltd.',
    'TATAPOWER.NS': 'Tata Power Company Ltd.',
    'SRF.NS': 'SRF Ltd.',
    'PFC.NS': 'Power Finance Corporation Ltd.',
    'BEL.NS': 'Bharat Electronics Ltd.',
    'GODREJCP.NS': 'Godrej Consumer Products Ltd.',
    'AUROPHARMA.NS': 'Aurobindo Pharma Ltd.',
    'LUPIN.NS': 'Lupin Ltd.',
    'BATAINDIA.NS': 'Bata India Ltd.',
    'PETRONET.NS': 'Petronet LNG Ltd.',
    'AMBUJACEM.NS': 'Ambuja Cements Ltd.',
    'RECLTD.NS': 'REC Ltd.',
    'ABB.NS': 'ABB India Ltd.',
    'MRF.NS': 'MRF Ltd.',
    'FEDERALBNK.NS': 'Federal Bank Ltd.',
    'ZEEL.NS': 'Zee Entertainment Enterprises Ltd.',
    'SUZLON.NS': 'Suzlon Energy Ltd.',


    # Top 100 Cryptocurrencies
    'BTC-USD': 'Bitcoin',
    'ETH-USD': 'Ethereum',
    'DOGE-USD': 'Dogecoin',
    'XRP-USD': 'Ripple',
    'BNB-USD': 'Binance Coin',
    'LTC-USD': 'Litecoin',
    'ADA-USD': 'Cardano',
    'SOL-USD': 'Solana',
    'DOT-USD': 'Polkadot',
    'AVAX-USD': 'Avalanche',
    'MATIC-USD': 'Polygon',
    'SHIB-USD': 'Shiba Inu',
    'UNI-USD': 'Uniswap',
    'XMR-USD': 'Monero',
    'ATOM-USD': 'Cosmos',
    'LINK-USD': 'Chainlink',
    'ALGO-USD': 'Algorand',
    'XLM-USD': 'Stellar',
    'ICP-USD': 'Internet Computer',
    'FIL-USD': 'Filecoin',
    'VET-USD': 'VeChain',
    'AAVE-USD': 'Aave',
    'SUSHI-USD': 'SushiSwap',
    'FTT-USD': 'FTX Token',
    'MKR-USD': 'Maker',
    'GRT-USD': 'The Graph',
    'RUNE-USD': 'THORChain',
    'KSM-USD': 'Kusama',
    'BAT-USD': 'Basic Attention Token',
    'ENJ-USD': 'Enjin Coin',
    'QNT-USD': 'Quant',
    'ZEC-USD': 'Zcash',
    'DASH-USD': 'Dash',
    'CRV-USD': 'Curve DAO Token',
    'COMP-USD': 'Compound',
    'SNX-USD': 'Synthetix',
    'ZIL-USD': 'Zilliqa',
    'NEO-USD': 'NEO',
    'WAVES-USD': 'Waves',
    'ONT-USD': 'Ontology',
    'STX-USD': 'Stacks',
    'CEL-USD': 'Celsius',
    'HT-USD': 'Huobi Token',
    'XDC-USD': 'XDC Network',
    'HNT-USD': 'Helium',
    'OKB-USD': 'OKB',
    'CRO-USD': 'Cronos',
    'KDA-USD': 'Kadena',

    # Forex Pairs
    'EURUSD=X': 'Euro/US Dollar',
    'GBPUSD=X': 'British Pound/US Dollar',
    'USDINR=X': 'US Dollar/Indian Rupee',
    'USDJPY=X': 'US Dollar/Japanese Yen',
    'AUDUSD=X': 'Australian Dollar/US Dollar',
    'NZDUSD=X': 'New Zealand Dollar/US Dollar',

}
def fetch_data(symbol):
    try:
        data = yf.download(symbol, period='1y', interval='1d')
        if data.empty:
            messagebox.showerror("Error", f"No data found for {symbol}. Please check the symbol.")
            return None
        return data
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching data for {symbol}: {e}")
        return None

def fetch_fundamental_data(symbol):
    try:
        asset = yf.Ticker(symbol)
        fundamentals = asset.info

        return {
            "P/E Ratio": fundamentals.get('forwardPE', 'N/A'),
            "Market Cap": fundamentals.get('marketCap', 'N/A'),
            "Dividend Yield (%)": (fundamentals.get('dividendYield', 0) * 100) if fundamentals.get('dividendYield') else 'N/A',
            "Debt to Equity Ratio": fundamentals.get('debtToEquity', 'N/A'),
            "Return on Equity (ROE)": fundamentals.get('returnOnEquity', 'N/A'),
            "Earnings Per Share (EPS)": fundamentals.get('trailingEps', 'N/A'),
        }
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching fundamental data for {symbol}: {e}")
        return None

def calculate_technical_indicators(data):
    data['MA20'] = data['Close'].rolling(window=20).mean()
    data['MA50'] = data['Close'].rolling(window=50).mean()
    data['EMA12'] = data['Close'].ewm(span=12, adjust=False).mean()
    data['EMA26'] = data['Close'].ewm(span=26, adjust=False).mean()
    data['MACD'] = data['EMA12'] - data['EMA26']
    data['ATR'] = data['High'].rolling(window=14).max() - data['Low'].rolling(window=14).min()

    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    data['RSI'] = 100 - (100 / (1 + rs))

    data['Bollinger High'] = data['MA20'] + (2 * data['Close'].rolling(window=20).std())
    data['Bollinger Low'] = data['MA20'] - (2 * data['Close'].rolling(window=20).std())

def analyze_data(data):
    if data is None or data.empty:
        return

    calculate_technical_indicators(data)
    last_price = data['Close'].iloc[-1]

    analysis_result = f"Current Price: {last_price:.2f}\n"
    
    if data['MA20'].iloc[-1] > data['MA50'].iloc[-1]:
        analysis_result += "Signal: Buy\n"
    elif data['MA20'].iloc[-1] < data['MA50'].iloc[-1]:
        analysis_result += "Signal: Sell\n"
    else:
        analysis_result += "Signal: Hold\n"

    analysis_result += f"\nTechnical Indicators:\n"
    analysis_result += f"20-day MA: {data['MA20'].iloc[-1]:.2f}\n"
    analysis_result += f"50-day MA: {data['MA50'].iloc[-1]:.2f}\n"
    analysis_result += f"12-day EMA: {data['EMA12'].iloc[-1]:.2f}\n"
    analysis_result += f"26-day EMA: {data['EMA26'].iloc[-1]:.2f}\n"
    analysis_result += f"MACD: {data['MACD'].iloc[-1]:.2f}\n"
    analysis_result += f"ATR: {data['ATR'].iloc[-1]:.2f}\n"
    analysis_result += f"RSI: {data['RSI'].iloc[-1]:.2f}\n"
    analysis_result += f"Bollinger High: {data['Bollinger High'].iloc[-1]:.2f}\n"
    analysis_result += f"Bollinger Low: {data['Bollinger Low'].iloc[-1]:.2f}\n"

    high_52_week = data['Close'].max()
    low_52_week = data['Close'].min()
    analysis_result += f"52-week High: {high_52_week:.2f}\n"
    analysis_result += f"52-week Low: {low_52_week:.2f}\n"

    return analysis_result

def on_fetch():
    asset_type = asset_type_var.get().lower()
    symbol = symbol_entry.get().upper()

    closest_match = get_close_matches(symbol, symbol_mapping.keys(), n=1)
    if closest_match:
        symbol = closest_match[0]
    else:
        messagebox.showerror("Error", f"Invalid symbol: {symbol}. Please enter a valid symbol.")
        return

    if asset_type == 'stock' and not symbol.endswith('.NS'):
        messagebox.showerror("Error", f"{symbol} is not a valid stock symbol. Please select 'Crypto' or 'Forex' instead.")
        return
    elif asset_type == 'crypto' and not symbol.endswith('-USD'):
        messagebox.showerror("Error", f"{symbol} is not a valid crypto symbol. Please select 'Stock' or 'Forex' instead.")
        return
    elif asset_type == 'forex' and not symbol.endswith('=X'):
        messagebox.showerror("Error", f"{symbol} is not a valid forex symbol. Please select 'Stock' or 'Crypto' instead.")
        return

    data = fetch_data(symbol)
    fundamental_data = fetch_fundamental_data(symbol)

    output_text.delete(1.0, tk.END)  # Clear previous output

    if data is not None:
        output_text.insert(tk.END, f"Fetched Data for {symbol_mapping[symbol]}:\n")
        output_text.insert(tk.END, str(data.tail()) + "\n")
        
        analysis_result = analyze_data(data)
        output_text.insert(tk.END, analysis_result + "\n")

    if fundamental_data:
        output_text.insert(tk.END, "Fundamental Data:\n")
        for key, value in fundamental_data.items():
            output_text.insert(tk.END, f"{key}: {value}\n")

root = tk.Tk()
root.title("Financial Data Fetcher v1.0 - By Navjot Singh Panesar")
root.geometry("800x600")

asset_type_var = tk.StringVar(value="stock")
asset_type_label = tk.Label(root, text="Select Asset Type:", font=("Arial", 16))
asset_type_label.pack(pady=10)

asset_type_combobox = ttk.Combobox(root, textvariable=asset_type_var, font=("Arial", 14))
asset_type_combobox['values'] = ['Stock', 'Crypto', 'Forex']
asset_type_combobox.pack(pady=10)

symbol_label = tk.Label(root, text="Enter Symbol (e.g., AAPL, BTC-USD):", font=("Arial", 16))
symbol_label.pack(pady=10)

symbol_entry = tk.Entry(root, font=("Arial", 14), width=30)
symbol_entry.pack(pady=10)

fetch_button = tk.Button(root, text="Fetch Data", command=on_fetch, font=("Arial", 16))
fetch_button.pack(pady=20)

root.bind('<Return>', lambda event: on_fetch())

output_text = scrolledtext.ScrolledText(root, font=("Arial", 12), width=90, height=25)
output_text.pack(pady=10)

root.mainloop()
