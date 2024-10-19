import pandas as pd
from surprise import SVD, Dataset, Reader, accuracy
from surprise.model_selection import train_test_split

data_dict = {
    'user_id': [1, 1, 1, 2, 2, 3, 3, 3, 4],
    'item_id': [101, 102, 103, 101, 104, 102, 103, 105, 101],
    'rating': [5, 4, 3, 5, 4, 2, 5, 4, 3],
}
df = pd.DataFrame(data_dict)

reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['user_id', 'item_id', 'rating']], reader)

trainset, testset = train_test_split(data, test_size=0.2)

model = SVD()
model.fit(trainset)

predictions = model.test(testset)

print("RMSE:", accuracy.rmse(predictions))


__all__ = ['model', 'df']