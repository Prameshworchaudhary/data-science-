#A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.

import pandas as pd

data={
    'Books':["math","science","nepali","english"],
    'price':[800,565,605,475]
}
result=pd.DataFrame(data)
print(result)

#index
data = {
    'Books':["math","science","nepali","english"],
    'price':[800,565,605,475]
  
}
df = pd.DataFrame(data, index = ["B1", "B2", "B3","B4"])
print(df) 
