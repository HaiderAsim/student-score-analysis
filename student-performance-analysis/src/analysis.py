import pandas as pd

df = pd.read_csv("study_performance.csv")
print(df.head())
print(df.info())
print(df.shape)

print(df.isnull().sum())
print(df.groupby("gender")[["math_score", "reading_score", "writing_score"]].mean())
print(df["test_preparation_course"].value_counts())
print(df.groupby("parental_level_of_education")["reading_score"].mean())
print(df.groupby("race_ethnicity")["writing_score"].mean())

print(df.groupby("lunch")[["math_score", "reading_score", "writing_score"]].mean())
df["average_score"] = (df["math_score"] + df["reading_score"] + df["writing_score"]) / 3
df["result"] = df["average_score"].apply(lambda x: "Pass" if x >=55 else "Fail")


print(df[["average_score", "result"]].head())
df.to_csv("study_performance_cleaned.csv", index=False)
print("Clean file saved!")






# cols = ["city", "listing_type", "rating_overall" , "ttm_revenue", "superhost" ]
# # print(df[cols].isnull().sum())

# df["city"] = df["city"].fillna("Unknown")
# # print(df["city"].isnull().sum())
# df["listing_type"] = df["listing_type"].fillna("Unknown")
# df["rating_overall"] = df["rating_overall"].fillna(df["rating_overall"].mean())
# df["ttm_revenue"] = df["ttm_revenue"].fillna(df["ttm_revenue"].mean())
# df["superhost"] = df["superhost"].fillna("Unknown")

# print(df[cols].isnull().sum())

# print(df["city"].value_counts().head(10))
# print(df["listing_type"].value_counts())
# print(df["superhost"].value_counts())
# print(df["rating_overall"].mean())
# print(df.groupby("listing_type")["ttm_revenue"].mean())
      











