


## 📁 Files

- `products.csv`: A sample dataset containing product details such as ID, tags, categories, and popularity scores.
- `users.csv`: Simulated interaction data of multiple users and the products they clicked.
- `recommend_multi.py`: The main script that builds user profiles and recommends personalized products.

## 🛠️ How It Works

### 1. Load User Clicks
- Reads `users.csv` to find which products each user clicked on.

### 2. Build User Profiles
- For each user, extract the **tags** and **categories** of the clicked products.
- These preferences are stored as a profile dictionary:
  ```python
  {
      "preferred_tags": [...],
      "preferred_categories": [...]
  }
  ```

### 3. Personalized Recommendations
- For each product (not already clicked), compute a **recommendation score**:
  - +1 for each matching tag
  - +1 if category matches
  - +0.2 × popularity_score (to simulate hybrid logic)
- Recommend the top 3 products with the highest score.

## 📊 Example Output

```text
=== Recommendations for User 101 ===
Clicked products: [1, 9]
User profile: {'preferred_tags': ['boho', 'pastel', 'summer'], 'preferred_categories': ['tops', 'skirts']}

Top Recommendations:
   product_id          title  score
5            6     Maxi Skirt    4.58
2            3   Denim Jacket    3.80
4            5  Summer Dress    3.64
```

## ✅ To Run

# Run the below command after entering into root directory

python recommend_multi.py


# This will print recommendations for each user found in `users.csv`.

---


