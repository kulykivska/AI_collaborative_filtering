from learning_model import model, df

def get_recommendations(user_id, modelSVD, dataFrame, top_n=5):
    # List of all items
    all_items = dataFrame['item_id'].unique()

    # Items that the user has already rated
    rated_items = dataFrame[dataFrame['user_id'] == user_id]['item_id'].unique()

    # Items that the user has not rated yet
    items_to_predict = [item for item in all_items if item not in rated_items]

    # Predicting ratings
    predictions = [
        (item, modelSVD.predict(user_id, item).est)
        for item in items_to_predict
    ]

    # Sorting by rating
    predictions.sort(key=lambda x: x[1], reverse=True)

    return predictions[:top_n]

recommendations = get_recommendations(1, model, df)
print("Recommendations for user 1:")
print("Recommendations", recommendations)
for item, rating in recommendations:
    print(f"Item {item} with predicted rating {rating:.2f}")
