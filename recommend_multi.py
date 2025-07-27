import pandas as pd

# Load data
products = pd.read_csv("products.csv")
users = pd.read_csv("users.csv")

# Build user profile from their past clicks
def build_user_profile(user_clicks_df):
    tags = set()
    categories = set()
    for _, row in user_clicks_df.iterrows():
        product = products[products["product_id"] == row["product_id"]].iloc[0]
        tags.update(tag.strip() for tag in product["tags"].split(","))
        categories.add(product["category"])
    return {"preferred_tags": list(tags), "preferred_categories": list(categories)}

# Generate recommendations
def get_personalized_recommendations(user_profile, clicked_ids, top_n=3):
    def compute_score(row):
        tag_match = len(set(row["tags"].split(",")).intersection(user_profile["preferred_tags"]))
        cat_match = 1 if row["category"] in user_profile["preferred_categories"] else 0
        return tag_match + cat_match + 0.2 * row["popularity_score"]

    candidate_products = products[~products["product_id"].isin(clicked_ids)].copy()
    candidate_products["score"] = candidate_products.apply(compute_score, axis=1)
    return candidate_products.sort_values("score", ascending=False).head(top_n)


for user_id in users["user_id"].unique():
    print(f"\n=== Recommendations for User {user_id} ===")

    user_clicks = users[(users["user_id"] == user_id)]
    clicked_ids = user_clicks["product_id"].tolist()

    print(f"Clicked products: {clicked_ids}")

    user_profile = build_user_profile(user_clicks)
    print(f"User profile: {user_profile}")

    recommendations = get_personalized_recommendations(user_profile, clicked_ids)
    print("\nTop Recommendations:")
    print(recommendations[["product_id", "title", "score"]])

