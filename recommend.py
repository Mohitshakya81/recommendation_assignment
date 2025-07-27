
import pandas as pd
import random

# Load product data
products = pd.read_csv("products.csv")

# --- ROUND 1: Initial Recommendations ---
def get_initial_recommendations(df, top_n=3):
    return df.sort_values("popularity_score", ascending=False).head(top_n)

# --- Simulate User Clicks ---
def simulate_user_clicks(recommended_df, click_n=2):
    return recommended_df.sample(n=click_n, random_state=1)

# --- Build User Profile from Clicked Products ---
def build_user_profile(clicked_df):
    tags = set()
    categories = set()
    for _, row in clicked_df.iterrows():
        tags.update(tag.strip() for tag in row["tags"].split(","))
        categories.add(row["category"])
    return {"preferred_tags": list(tags), "preferred_categories": list(categories)}

# --- Generate Personalized Recommendations ---
def get_personalized_recommendations(df, user_profile, clicked_ids, top_n=3):
    def compute_score(row):
        tag_match = len(set(row["tags"].split(",")).intersection(user_profile["preferred_tags"]))
        category_match = 1 if row["category"] in user_profile["preferred_categories"] else 0
        return tag_match + category_match + 0.2 * row["popularity_score"]

    filtered_df = df[~df["product_id"].isin(clicked_ids)].copy()
    filtered_df["score"] = filtered_df.apply(compute_score, axis=1)
    return filtered_df.sort_values("score", ascending=False).head(top_n)

# --- Main Flow ---
def main():
    print("=== ROUND 1: Cold Start Recommendations ===")
    round1 = get_initial_recommendations(products)
    print(round1[["product_id", "title"]])

    clicked = simulate_user_clicks(round1)
    clicked_ids = clicked["product_id"].tolist()
    print("\nUser clicked:", clicked_ids)

    print("\n=== UPDATED USER PROFILE ===")
    user_profile = build_user_profile(clicked)
    print(user_profile)

    print("\n=== ROUND 2: Personalized Recommendations ===")
    round2 = get_personalized_recommendations(products, user_profile, clicked_ids)
    print(round2[["product_id", "title", "score"]])

if __name__ == "__main__":
    main()
