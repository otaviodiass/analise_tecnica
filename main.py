import pandas as pd
from matplotlib import pyplot as plt
import talib

df_historico_diario = pd.read_csv('historicos\\historico_bitcoin_diario.csv')

df_historico_diario['data'] = pd.to_datetime(df_historico_diario['data'], unit='ms')

df_historico_diario['MMS_5'] = talib.SMA(df_historico_diario['fechamento'], timeperiod=5)

df_historico_diario['MMS_20'] = talib.SMA(df_historico_diario['fechamento'], timeperiod=20)

df_historico_diario['EMA_5'] = talib.EMA(df_historico_diario['fechamento'], timeperiod=5)

df_historico_diario['EMA_20'] = talib.EMA(df_historico_diario['fechamento'], timeperiod=20)

df_historico_diario['MACD'], df_historico_diario['MACD_Signal'], df_historico_diario['MACD_Histograma'] = talib.MACD(
    df_historico_diario['fechamento'], fastperiod=12, slowperiod=26, signalperiod=9
)

df_historico_diario['rsi'] = talib.RSI(df_historico_diario['fechamento'], timeperiod=9)

df_historico_diario.dropna(inplace=True)
print(df_historico_diario.head())

plt.figure(figsize=(10, 5))

plt.subplot(2, 1, 1)

plt.plot(df_historico_diario['data'], df_historico_diario['fechamento'], label='Preço de Fechamento')
plt.plot(df_historico_diario['data'], df_historico_diario['MMS_5'], label='MMS_5')
plt.plot(df_historico_diario['data'], df_historico_diario['MMS_20'], label='MMS_20')
plt.ylabel('Preço')
plt.xlabel('Período')
plt.legend()
plt.title('Médias Moveis Simples')

plt.subplot(2, 1, 2)
plt.plot(df_historico_diario['data'], df_historico_diario['fechamento'], label='Preço de Fechamento')
plt.plot(df_historico_diario['data'], df_historico_diario['EMA_5'], label='EMA_5')
plt.plot(df_historico_diario['data'], df_historico_diario['EMA_20'], label='EMA_20')
plt.ylabel('Preço')
plt.xlabel('Período')
plt.legend()
plt.title('Médias Moveis Exponenciais')
plt.subplots_adjust(hspace=0.5)
plt.gcf().canvas.manager.set_window_title('Médias Móveis')

plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(df_historico_diario['data'], df_historico_diario['fechamento'], label='Preço de Fechamento')
plt.ylabel('Preço')
plt.xlabel('Período')
plt.title('Preço')
plt.subplot(2, 1, 2)
plt.plot(df_historico_diario['data'], df_historico_diario['MACD'], label='MACD')
plt.plot(df_historico_diario['data'], df_historico_diario['MACD_Signal'], label='Linha de Sinal')
plt.bar(df_historico_diario['data'], df_historico_diario['MACD_Histograma'], label='Histograma MACD', color='gray')
plt.ylabel('MACD')
plt.xlabel('Período')
plt.legend()
plt.title('MACD')
# plt.subplots_adjust(hspace=0.5)
plt.gcf().canvas.manager.set_window_title('MACD')

plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.plot(df_historico_diario['data'], df_historico_diario['fechamento'], label='Preço de Fechamento')
plt.ylabel('Preço')
plt.xlabel('Período')
plt.title('Preço')
plt.subplot(2, 1, 2)
plt.plot(df_historico_diario['data'], df_historico_diario['rsi'], label='RSI')
plt.axhline(y=30, color='red')
plt.axhline(y=70, color='red')
plt.xlabel('Período')
plt.title('RSI')
plt.gcf().canvas.manager.set_window_title('RSI')
plt.subplots_adjust(hspace=0.3)

plt.show()
