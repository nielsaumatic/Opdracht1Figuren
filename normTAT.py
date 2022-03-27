import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


fcfsData = pd.read_csv('resultsCSV 50000/fcfs.csv', sep=',')
sjfData = pd.read_csv('resultsCSV 50000/sjf.csv', sep=',')
srtData = pd.read_csv('resultsCSV 50000/srt.csv', sep=',')
rr2Data = pd.read_csv('resultsCSV 50000/rr2.csv', sep=',')
rr4Data = pd.read_csv('resultsCSV 50000/rr4.csv', sep=',')
rr8Data = pd.read_csv('resultsCSV 50000/rr8.csv', sep=',')
hrrnData = pd.read_csv('resultsCSV 50000/hrrn.csv', sep=',')
mlfb25Data = pd.read_csv('resultsCSV 50000/mlfb25.csv', sep=',')
mlfb50Data = pd.read_csv('resultsCSV 50000/mlfb50.csv', sep=',')


plt.plot(fcfsData['percentage'], fcfsData['gemiddeldNormTAT'], label='FCFS')
plt.plot(sjfData['percentage'], sjfData['gemiddeldNormTAT'], label='SJF')
plt.plot(srtData['percentage'], srtData['gemiddeldNormTAT'], label='SRT')
plt.plot(rr2Data['percentage'], rr2Data['gemiddeldNormTAT'], label='RR2')
plt.plot(rr4Data['percentage'], rr4Data['gemiddeldNormTAT'], label='RR4')
plt.plot(rr8Data['percentage'], rr8Data['gemiddeldNormTAT'], label='RR8')
plt.plot(hrrnData['percentage'], hrrnData['gemiddeldNormTAT'], label='HRRN')
plt.plot(mlfb25Data['percentage'], mlfb25Data['gemiddeldNormTAT'], label='MLFB25')
plt.plot(mlfb50Data['percentage'], mlfb50Data['gemiddeldNormTAT'], label='MLFB50')
plt.xlabel('Bedieningstijd percentiel')
plt.ylabel('Genormaliseerde omlooptijd')
plt.ylim(0, 30)
plt.legend()
plt.title('Genormaliseerde omlooptijd in functie van bedieningstijd')
plt.savefig('normTAT50000.svg')
