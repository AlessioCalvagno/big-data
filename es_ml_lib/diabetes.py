#per mettere in un csv il dataset del diabete di sklearn, perchè ci sono problemi nell'usare
#zeppelin e spark con comandi non pyspark (in worker e zeppelin ci sono versioni python diverse)

from sklearn.datasets import load_diabetes
import pandas as pd

data = load_diabetes(as_frame=True)

df: pd.DataFrame = data.frame
df.to_csv("data/diabetes.csv")