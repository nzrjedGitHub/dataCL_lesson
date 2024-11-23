import pandas as pd
df = pd.read_csv('GooglePlayStore_wild.csv')
print('___________')
print(df.info())

df['Rating'].fillna(-1, inplace = True)

print(df.info())

df['Reviews']= df['Reviews'].apply(int)

print(df.info())

def make_price(price):
   if price[0] == '$':
       return float(price[1:])
   return 0

df['Price']= df['Price'].apply(make_price)
 
print(df.info())

print(df['Size'].value_counts())

def set_size(size): # 122
   if size[-1] == 'M':
      return float(size[:-1])
   elif size[-1] == 'k':
      return float(size[:-1]) / 1024
   return -1
df['Size'] = df['Size'].apply(set_size)

def set_installs(installs):
   if installs == '0':
       return 0
   return int(installs[:-1].replace(',', ''))
df['Installs'] = df['Installs'].apply(set_installs)

print(df.info())