import pandas as pd

def load_union(file_list):

    dfs = []
    for file in file_list:
        try:
            df = pd.read_csv(file, encoding="utf-8")
            dfs.append(df)
        except Exception as e:
            print(f"Error loading file {file}: {e}")
    return pd.concat(dfs, ignore_index=True) if dfs else pd.DataFrame()



def merge_lookup(df, xlook_ref):
    xlook_ref = xlook_ref.drop_duplicates(subset="Supplier Name")
    merged_df = df.merge(
        xlook_ref[["Supplier Name", "SSM ", "Category"]],
        on="Supplier Name",
        how="left"
    )
    merged_df["SSM "] = merged_df["SSM "].fillna("UNKNOWN")
    merged_df["Category"] = merged_df["Category"].fillna("UNKNOWN")
    return merged_df

def union_paths(po_spend_files, po_otd_files, po_dpmo_files, xlook_ref_file):
    po_spend = load_union(po_spend_files)
    po_otd = load_union(po_otd_files)
    po_dpmo = load_union(po_dpmo_files)
    xlook_ref = pd.read_csv(xlook_ref_file, encoding="utf-8")

    merged_spend = merge_lookup(po_spend, xlook_ref)
    merged_otd = merge_lookup(po_otd, xlook_ref)
    merged_dpmo = merge_lookup(po_dpmo, xlook_ref)

    return merged_spend, merged_otd, merged_dpmo



def otd_task(merged_otd):
    total = len(merged_otd)

    if total == 0:
        return 0.0
    
    otd_count = merged_otd[
        merged_otd["Delivery Result"].isin(["On-Time", "Early"])
    ].shape[0]
    
    return otd_count / total


po_spend_files = [r"C:\Users\null\PO Spend - Jun.csv",
                  r"C:\Users\null\PO Spend - May.csv",
                  r"C:\Users\null\PO Spend - Apr.csv"
                  ]

po_otd_files = [r"C:\Users\null\PO OTD - Jun.csv",
                    r"C:\Users\null\PO OTD - May.csv",
                    r"C:\Users\null\PO OTD - Apr.csv"
                    ]

po_dpmo_files = [r"C:\Users\null\PO PPM - Jun.csv",
                    r"C:\Users\null\PO PPM - May.csv",
                    r"C:\Users\null\PO PPM - Apr.csv"
                    ]

    
xlook_ref_file = r"C:\Users\null\xlook_ref.csv"



merged_df, merged_otd, merged_dpmo = union_paths(po_spend_files, po_otd_files, po_dpmo_files, xlook_ref_file)

def otd_task2(merged_otd):
    print("function is running")
    merged_otd["OTD"] = (
        merged_otd["Delivery Result"]
        .isin(["Early", "On-Time"])
        .astype(int)
    )

    return merged_otd

merged_otd = otd_task2(merged_otd)


merged_df, merged_otd, merged_dpmo


