import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/insurance_customers.csv")

print("Rows:", len(df))
print("\nPolicy mix:")
print(df["policy_type"].value_counts())

summary = df.groupby("policy_type").agg(
    customers=("customer_id", "count"),
    avg_premium=("annual_premium", "mean"),
    claim_rate=("claim_flag", "mean"),
    avg_claim_cost=("claim_amount", "mean"),
    renewal_rate=("renewed", "mean"),
    avg_satisfaction=("satisfaction_score", "mean")
).round(3)

print("\nPolicy summary:")
print(summary)

channel = df.groupby("purchase_channel").agg(
    customers=("customer_id", "count"),
    renewal_rate=("renewed", "mean"),
    claim_rate=("claim_flag", "mean"),
    avg_premium=("annual_premium", "mean")
).round(3)

print("\nChannel summary:")
print(channel)

# Opportunity sizing: illustrative scenario only, not a forecast.
auto_claim_cost = df.loc[df["policy_type"].eq("Auto"), "claim_amount"].sum()
scenario_savings = auto_claim_cost * 0.05
print(f"Illustrative 5% reduction in Auto claim costs: £{scenario_savings:,.2f}")

summary["claim_rate"].plot(kind="bar", title="Claim Rate by Policy Type")
plt.ylabel("Claim rate")
plt.tight_layout()
plt.savefig("claim_rate_by_policy.png", dpi=150)
plt.show()
