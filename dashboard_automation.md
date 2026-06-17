# Complete Dashboard Automation Guide
> (note) Before starting, the process laid out is entirely skipping an dataset manipulation via excel be it even power query. However, there are some needed extensions to streamline the process. 



## **Step 1: Download Python**

> (note) Don't be intimidated by the fact we will be utilizing python for the process. There won't be any coding involved besides the parsing which will be highly simplified by this markdown. The most complicated step in the process is actually downloading python and setting the dependencies.

We first go to this website :point_right: https://www.python.org/downloads/

![alt text](<Screenshot 2026-06-02 135952-1.png>)

As seen in the red highlighted area, we want to pick our respective OS. (E.g. macOS, Windows, etc.)

![alt text](<Screenshot 2026-06-02 140215-1.png>)

In this example we picked windows. We always want to pick the 64-bit. And just to play it safe, we should download a past release such that we don't run into any issues. (as seen python 3.13.13)

Run the installer and a little pop up should show up. 

**Extremely Important** 

:warning: We must make sure to click the "Add Python to Path" box. Failing to do so will likely place python in an obscure specific location on your device which leads to a lot complications later on.

Once this is checked, we can Install Now

> [!TIP]
> For a little sanity check in bash or command prompt

```bash
python --version
```
If it shows a version we are good.

## **Step 2: Download Dependency**

> (note) Any operating system should have some shell program. This is the point in which we can download extensions or packages for python. For macOS this may be bash, and for windows this is "command prompt". For windows, just search this in the little windows search bar.

![alt text](<Screenshot 2026-06-03 090755-1.png>)

Since we added python to path in step 1, we don't need to change the directory.

```bash
pip install pandas
```

Type the following and press enter. That is literally it.

## **Step 3: Getting the Data in PBI**

> (note) You can copy paste the code for this step, however make sure you change the file paths such that they match with your own device.

![alt text](<Screenshot 2026-06-02 142701-1.png>)

As seen in the picture above, in "Get Data", go more, and we search python and select python scripting.

When selected, we should see a script pop up

```python
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

po_spend_files = [r"PO Spend - Jun.csv",
                  r"PO Spend - May.csv",
                  r"PO Spend - Apr.csv"
                  ]

po_otd_files =  [r"PO OTD - Jun.csv",
                    r"PO OTD - May.csv",
                    r"PO OTD - Apr.csv"
                    ]

po_dpmo_files = [r"PO PPM - Jun.csv",
                    r"PO PPM - May.csv",
                    r"PO PPM - Apr.csv"
                    ]

    
xlook_ref_file = r"C:\Users\DamlC\Downloads\CalDAA\PQ_dash\xlook_ref.csv"



merged_df, merged_otd, merged_dpmo = union_paths(po_spend_files, po_otd_files, po_dpmo_files, xlook_ref_file)


merged_df, merged_otd, merged_dpmo
```

![alt text](<Screenshot 2026-06-03 090151-2.png>)


Paste the above code in the scripting area. Make sure you put in the correct file paths for the po data (the po jun, may, apr are just place holders) and xlookup_ref. Remember to add new monthly data into the assignment.


> (note) Know that the only varying part of this loop is the file paths. Just copy the path in your files and paste in the respective location.

Now all you have to do is select and load the merged tables as your data. 

![alt text](<Screenshot 2026-06-04 101419-1.png>)

And you're done :thumbsup: