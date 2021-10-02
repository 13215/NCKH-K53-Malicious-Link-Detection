import pandas as pd

phishing = pd.read_csv("data\\phishing.csv")
legitimate = pd.read_csv("data\\legitimate.csv")
urldata = pd.concat([legitimate, phishing]).reset_index(drop=True)
urldata.to_csv('data\\urldata.csv', index=False)