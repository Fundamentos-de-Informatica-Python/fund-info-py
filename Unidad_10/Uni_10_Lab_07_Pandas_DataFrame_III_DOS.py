import pandas as pd

data = {
    'color': ['blue','green','yellow','red','white'],
    'object': ['red', 'yellow', 'green', 'orange', 'blue'],
    'price': [1.2, 1.0, 0.6, 0.9, 1.7]
}

frame = pd.DataFrame(data)

menores = frame[frame['price'] < 1]


print(menores)