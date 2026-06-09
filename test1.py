import pandas as pd

po_det = pd.read_csv(r"C:\Users\DamlC\Downloads\CalDAA\PQ_dash\PO Spend - Details.csv", encoding="utf-8")
xlook_ref = pd.read_csv(r"C:\Users\DamlC\Downloads\CalDAA\PQ_dash\xlook_ref.csv", encoding="utf-8")
po_otd = pd.read_csv(r"C:\Users\DamlC\Downloads\CalDAA\PQ_dash\PO OTD - Details.csv", encoding="utf-8")
po_dpmo = pd.read_csv(r"C:\Users\DamlC\Downloads\CalDAA\PQ_dash\PO PPM - Supplier Quality Detail.csv", encoding="utf-8")


po_det["Supplier Name"] = po_det["Supplier Name"].str.strip().str.lower()
xlook_ref["Supplier Name"] = xlook_ref["Supplier Name"].str.strip().str.lower()
po_otd["Supplier Name"] = po_otd["Supplier Name"].str.strip().str.lower()
po_dpmo["Supplier Name"] = po_dpmo["Supplier Name"].str.strip().str.lower()

xlook_ref = xlook_ref.drop_duplicates(subset="Supplier Name")

merged_df = po_det.merge(
    xlook_ref[["Supplier Name", "SSM ", "Category"]],
    on="Supplier Name",
    how="left"
)

merged_df["SSM "] = merged_df["SSM "].fillna("UNKNOWN")
merged_df["Category"] = merged_df["Category"].fillna("UNKNOWN")

merged_otd = po_otd.merge(
    xlook_ref[["Supplier Name", "SSM ", "Category"]],
    on="Supplier Name",
    how="left"
)

merged_otd["SSM "] = merged_otd["SSM "].fillna("UNKNOWN")
merged_otd["Category"] = merged_otd["Category"].fillna("UNKNOWN")

merged_dpmo = po_dpmo.merge(
    xlook_ref[["Supplier Name", "SSM ", "Category"]],
    on="Supplier Name",
    how="left"
)

merged_dpmo["SSM "] = merged_dpmo["SSM "].fillna("UNKNOWN")
merged_dpmo["Category"] = merged_dpmo["Category"].fillna("UNKNOWN")

merged_df
merged_otd
merged_dpmo

