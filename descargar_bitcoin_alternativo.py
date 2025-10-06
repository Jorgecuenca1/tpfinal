"""
Descarga datos de Bitcoin usando multiples fuentes alternativas
"""
import urllib.request
import os
import json

def descargar_desde_coingecko():
    """Intenta descargar desde CoinGecko API"""
    print("Intentando descargar desde CoinGecko...")

    try:
        # CoinGecko API - datos historicos de Bitcoin
        url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=max&interval=daily"

        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())

        # Convertir a CSV
        os.makedirs('data/raw', exist_ok=True)

        with open('data/raw/bitcoin_historical.csv', 'w') as f:
            f.write('Date,Close,Volume\n')

            prices = data['prices']
            volumes = data['total_volumes']

            for i in range(len(prices)):
                timestamp = prices[i][0]
                price = prices[i][1]
                volume = volumes[i][1] if i < len(volumes) else 0

                # Convertir timestamp a fecha
                from datetime import datetime
                date = datetime.fromtimestamp(timestamp/1000).strftime('%Y-%m-%d')

                f.write(f'{date},{price},{volume}\n')

        print("OK - Datos descargados desde CoinGecko!")
        print("Archivo: data/raw/bitcoin_historical.csv")
        return True

    except Exception as e:
        print(f"Error con CoinGecko: {e}")
        return False

def descargar_desde_cryptocompare():
    """Intenta descargar desde CryptoCompare"""
    print("Intentando descargar desde CryptoCompare...")

    try:
        # Obtener datos historicos
        url = "https://min-api.cryptocompare.com/data/v2/histoday?fsym=BTC&tsym=USD&limit=2000"

        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read())

        if data['Response'] != 'Success':
            raise Exception("API response not successful")

        # Convertir a CSV
        os.makedirs('data/raw', exist_ok=True)

        with open('data/raw/bitcoin_historical.csv', 'w') as f:
            f.write('Date,Open,High,Low,Close,Volume\n')

            for item in data['Data']['Data']:
                from datetime import datetime
                date = datetime.fromtimestamp(item['time']).strftime('%Y-%m-%d')

                f.write(f"{date},{item['open']},{item['high']},{item['low']},{item['close']},{item['volumefrom']}\n")

        print("OK - Datos descargados desde CryptoCompare!")
        print("Archivo: data/raw/bitcoin_historical.csv")
        return True

    except Exception as e:
        print(f"Error con CryptoCompare: {e}")
        return False

def crear_datos_ejemplo():
    """Crea un dataset de ejemplo para probar"""
    print("Creando dataset de ejemplo...")

    os.makedirs('data/raw', exist_ok=True)

    # Crear datos de ejemplo (ultimos 365 dias)
    import random
    from datetime import datetime, timedelta

    with open('data/raw/bitcoin_historical.csv', 'w') as f:
        f.write('Date,Open,High,Low,Close,Volume\n')

        base_price = 30000
        current_date = datetime.now() - timedelta(days=365)

        for i in range(365):
            date_str = current_date.strftime('%Y-%m-%d')

            # Generar precios aleatorios con tendencia
            variation = random.uniform(-0.05, 0.05)
            open_price = base_price * (1 + variation)
            high_price = open_price * (1 + random.uniform(0, 0.03))
            low_price = open_price * (1 - random.uniform(0, 0.03))
            close_price = (high_price + low_price) / 2 + random.uniform(-500, 500)
            volume = random.randint(10000000, 50000000)

            f.write(f"{date_str},{open_price:.2f},{high_price:.2f},{low_price:.2f},{close_price:.2f},{volume}\n")

            base_price = close_price
            current_date += timedelta(days=1)

    print("OK - Dataset de ejemplo creado!")
    print("NOTA: Estos son datos simulados para pruebas")
    print("Archivo: data/raw/bitcoin_historical.csv")
    return True

if __name__ == "__main__":
    print("="*60)
    print("DESCARGA DE DATOS DE BITCOIN")
    print("="*60)

    # Intentar multiples fuentes
    if descargar_desde_coingecko():
        print("\nExito!")
    elif descargar_desde_cryptocompare():
        print("\nExito!")
    else:
        print("\nNo se pudo descargar de APIs publicas.")
        print("Creando dataset de ejemplo para que puedas probar...")
        crear_datos_ejemplo()
        print("\nPara datos reales, descarga manualmente desde:")
        print("  1. https://www.kaggle.com/datasets/mczielinski/bitcoin-historical-data")
        print("  2. https://finance.yahoo.com/quote/BTC-USD/history")
