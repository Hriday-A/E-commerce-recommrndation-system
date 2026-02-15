import os
import time
import pandas as pd
from dotenv import load_dotenv
from google import genai

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY not found.")

client = genai.Client(api_key=API_KEY)

SYSTEM_INSTRUCTION = """
You are a Senior Marketing strategist for Olist, a premium ecommerce platform. 
Your goal is to write high conversation, personalized re-engagement emails. 
Tone: Professional, appreciative and exclusive. 
Maximum 80 words. 
These are Champion customers. 
Offer a personalized reason to return without mentioning technical data points.
"""

def generate_emails():
    df = pd.read_csv('data/processed/rfm_features.csv')
    champions = df[df['monetary'] > 500].head(3)

    print(f"🚀 Found {len(champions)} Champions. Starting AI Outreach...\n")

    for _, row in champions.iterrows():
        cust_id = row['customer_unique_id'][:8]

        prompt = (
            f"Write an email for a customer who has spent ${row['monetary']:.2f} "
            f"but hasn't shopped in {int(row['recency'])} days."
        )

        try:
            print(f"--- Generating for Customer ID: {cust_id} ---")

            rresponse = client.models.generate_content(
    model="gemini-1.5-flash",
    contents=prompt,
    config={"system_instruction": SYSTEM_INSTRUCTION}
)


            print(response.text)
            print("-" * 50)

            time.sleep(2)

        except Exception as e:
            print(f"❌ Failed for {cust_id}: {e}")

    print("\n✅ Outreach campaign generation complete.")


if __name__ == "__main__":
    generate_emails()
