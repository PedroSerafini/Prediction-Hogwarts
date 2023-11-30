import pandas as pd
import random

random.seed(42)  

data = {
    'NumQuartos': [random.randint(1, 5) for _ in range(100)],
    'NumBanheiros': [random.randint(1, 4) for _ in range(100)],
    'NumGaragens': [random.randint(0, 2) for _ in range(100)],
    'MetrosQuadrados': [random.randint(50, 200) for _ in range(100)],
    'NumEncantamentos': [random.randint(0, 10) for _ in range(100)],
    'QuadraQuadribol': [random.choice([True, False]) for _ in range(100)],
    'AluguelSugerido': [random.randint(1000, 3000) for _ in range(100)],
    'VendaSugerida': [random.randint(50000, 200000) for _ in range(100)]
}

df = pd.DataFrame(data)

df.to_csv('hogwarts_dataset.csv', index=False)
