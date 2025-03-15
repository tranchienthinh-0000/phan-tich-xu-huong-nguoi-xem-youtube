import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Đọc dữ liệu
df = pd.read_csv("top_category_results_clean.txt", sep="\t")

# Chuyển đổi dữ liệu
df["ViewCount"] = df["ViewCount"].astype(int)

# ====== 1. Biểu đồ cột (Bar Plot) ======
plt.figure(figsize=(10, 5))
sns.barplot(x="Category", y="ViewCount", data=df, palette="coolwarm")
plt.xticks(rotation=45)
plt.xlabel("Danh mục")
plt.ylabel("Lượt xem")
plt.title("Biểu đồ cột: Xu hướng xem YouTube")
plt.show()  # Hiển thị từng biểu đồ một

# ====== 2. Biểu đồ tròn (Pie Chart) ======
df_sorted = df.sort_values(by="ViewCount", ascending=False)[:10]  # Chọn 10 danh mục cao nhất
plt.figure(figsize=(8, 8))
plt.pie(df_sorted["ViewCount"], labels=df_sorted["Category"], autopct="%1.1f%%", colors=sns.color_palette("coolwarm", len(df_sorted)))
plt.title("Biểu đồ tròn: Phân bố lượt xem theo danh mục")
plt.show()

# ====== 3. Biểu đồ đường (Line Plot) ======
df_sorted = df.sort_values(by="ViewCount", ascending=False)
plt.figure(figsize=(10, 5))
sns.lineplot(x="Category", y="ViewCount", data=df_sorted, marker="o", color="b")
plt.xticks(rotation=45)
plt.xlabel("Danh mục")
plt.ylabel("Lượt xem")
plt.title("Biểu đồ đường: Xu hướng danh mục phổ biến")
plt.show()

# ====== 4. Biểu đồ tần suất (Histogram) ======
plt.figure(figsize=(10, 5))
sns.histplot(df["ViewCount"], bins=20, kde=True, color="purple")
plt.xlabel("Lượt xem")
plt.ylabel("Tần suất")
plt.title("Biểu đồ tần suất: Phân bố lượt xem")
plt.show()
