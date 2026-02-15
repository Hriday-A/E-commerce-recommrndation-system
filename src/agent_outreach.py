import pandas as pd 

df = pd.read_csv('data/processed/rfm_features.csv')

champions = df[df['monetary'] > 500]
for index,row in champions.head(3).iterrows():
    monetary=row['monetary']
    recency=row['recency']

    prompt=f"Write a VIP email to customer {row['customer_unique_id']}. " \
             f"They have spent ${monetary:.2f} but haven't shopped in {int(recency)} days. " \
             f"Offer a personalized incentive to return."
    print("-"*30)
    print(prompt) 