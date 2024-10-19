from db_connection import insert_data_to_mongo
from learning_model import df

documents = df.to_dict(orient='records')

insert_data_to_mongo(documents)
print("Data inserted into MongoDB!")