import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


fcfsData = pd.read_csv('resultsCSV 10000/fcfs.csv', sep=',')
sjfData = pd.read_csv('resultsCSV 10000/sjf.csv', sep=',')
srtData = pd.read_csv('resultsCSV 10000/srt.csv', sep=',')
rr2Data = pd.read_csv('resultsCSV 10000/rr2.csv', sep=',')
rr4Data = pd.read_csv('resultsCSV 10000/rr4.csv', sep=',')
rr8Data = pd.read_csv('resultsCSV 10000/rr8.csv', sep=',')
hrrnData = pd.read_csv('resultsCSV 10000/hrrn.csv', sep=',')
mlfb5Data = pd.read_csv('resultsCSV 10000/mlfb5.csv', sep=',')
mlfb25Data = pd.read_csv('resultsCSV 10000/mlfb25.csv', sep=',')


plt.plot(fcfsData['percentage'], fcfsData['gemiddeldWait'], label='FCFS')
plt.plot(sjfData['percentage'], sjfData['gemiddeldWait'], label='SJF')
plt.plot(srtData['percentage'], srtData['gemiddeldWait'], label='SRT')
plt.plot(rr2Data['percentage'], rr2Data['gemiddeldWait'], label='RR2')
plt.plot(rr4Data['percentage'], rr4Data['gemiddeldWait'], label='RR4')
plt.plot(rr8Data['percentage'], rr8Data['gemiddeldWait'], label='RR8')
plt.plot(hrrnData['percentage'], hrrnData['gemiddeldWait'], label='HRRN')
plt.plot(mlfb5Data['percentage'], mlfb5Data['gemiddeldWait'], label='MLFB5')
plt.plot(mlfb25Data['percentage'], mlfb25Data['gemiddeldWait'], label='MLFB25')
plt.xlabel('Bedieningstijd percentiel')
plt.ylabel('Wachttijd')
plt.ylim(0, 2000)
plt.legend()
plt.title('Wachttijd in functie van bedieningstijd')
plt.savefig('wait10000.svg')
