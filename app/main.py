#import read_csv
import utils
import charts
import pandas as pd
import numpy as np

def run():
  '''
  data = read_csv.read_csv('data.csv') #lectura del archivo'''
  df= pd.read_csv('data.csv')
  opcion=utils.menu()
  while True:
    if opcion=='1':
      country = input('Type Country => ') 
      df=df[df['Country/Territory']==country]
      labels=df.columns.values
      labels=labels[5:13]
      print(labels)
      values1=df[df.columns[5:13]].values
      values2=values1[0]
      charts.generate_bar_chart(country,labels,values2)
    elif (opcion=='2'):
      countries=df['Country/Territory'].values
      percentages =df['World Population Percentage'].values
      charts.generate_pie_chart(countries,percentages)
    elif  opcion=='3':
      name_continent=input('Ingrese el nombre de continente:')
      #if (name_continent in df[df['Continent'] ==name_continent]):
      print(' Visualizacion de datos segun '+name_continent)
      df =df[df['Continent'] ==name_continent]
      countries =df['Country/Territory'].values
      percentages= df['World Population Percentage'].values
      print(percentages)
      print(type(percentages))
      charts.generate_pie_chart(countries,percentages)
      #else:
       # print('Opcion no valida')
    

if __name__ == '__main__':
  run()
