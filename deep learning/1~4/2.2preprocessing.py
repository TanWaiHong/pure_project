import os
import pandas as pd
from mxnet import np

os.makedirs(os.path.join('../..', 'data'), exist_ok=True)
data_file = os.path.join('../..', 'data', 'house_tiny.csv')
with open(data_file, 'w') as f:
    f.write('NumRooms,Alley,Price\n')  # Column names
    f.write('NA,Pave,127500\n')  # Each row represents a data example
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA,NA,140000\n')


data = pd.read_csv(data_file)
print(data)

inputs, outputs = data.iloc[:, 0:2], data.iloc[:, 2]
inputs['NumRooms'] = inputs['NumRooms'].fillna(inputs['NumRooms'].mean())
print(inputs)

inputs = pd.get_dummies(inputs, dummy_na=True)
print(inputs)

X, y = np.array(inputs.values), np.array(outputs.values)
print(X, y)

inputs = inputs.drop(0)
print(inputs)

z = np.array(inputs.values)
print(z)
