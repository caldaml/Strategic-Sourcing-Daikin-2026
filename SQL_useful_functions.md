# **SQL Useful Functions**

>[!IMPORTANT]
> This documentation is for more complicated SQL querying tasks which would other wise be done in excel or power query.
> This will include the syntax along with the logic behind it.


## XLOOKUP

Create a new table based on `data1` but adding ssm by referencing `xl_ref` with the consistent variable of `supplier`

```sql
SELECT data1.spend, data1.supplier, xl_ref.ssm -- what we are querying (we want to add ssm a table with data 1 categories)
FROM data1
LEFT JOIN xl_ref -- similar with python, the left join is the standard for xlookup extensions
    ON data1.supplier = xl_ref.supplier -- this is the common key among the 2 tables
```

## Currency Adjustment

Update `ext_ag` by adjusting the currency columns to match the USD exchange rate

```sql
UPDATE ext_ag
SET
    "Unit Price" = "Unit Price" * .0063,
    "Total Price" = "Total Price" * .0063,
    "Ext. Price" = "Ext. Price" * .0063,
    "Std. Cost" = "Std. Cost" * .0063,
    "Ext. PPV" = "Ext. PPV" * .0063
WHERE Currency ='JPY';
-- This is a past task I did where I had to adjust currency columns such that they would turn yen to USD.
--  (.0063 was the exchange rate at this point in time)
```

## Duplicate Reduction

Keep only one row per `org_id` + `year` combination, removing any duplicates.

```sql
DELETE FROM PART1_COMBINED
WHERE ROWID NOT IN (
    SELECT MIN(ROWID)
    FROM PART1_COMBINED
    GROUP BY org_id, year
);
```
>[!TIP]
> The task for a single variable duplicate reduction is much easier. Just do a GROUP BY function


## Dealing With Number Stored As Text

Query `revenue` based on an equivalent argument while the number is stored as text

```sql
SELECT *
FROM pro_publica
WHERE CAST(revenue AS DOUBLE) > 20000000
```

>[!TIP]
> Cast(... AS DOUBLE) or FLOAT / REAL depending on the dialect, explicitly converts a value from one data type into a double-precision floating-point number.
> This is useful when you need numeric operations or correct ordering on values stored as text or other types.


## Select Exclusive

Select `domain` if it doesn't exist in the seperate table

```sql
SELECT domain
FROM table_4110 -- the number denotes the amount of domains in each table
WHERE domain NOT IN (
    SELECT domain
    FROM table_3600
)
```
> [!NOTE]
> This should return the 510 domains which are missing in table 3600


## SELECT Top or Bottom

SELECT * of the top ten spend items

```SQL
SELECT *
FROM table
ORDER BY "Spend" DESC -- Denotes from high to low
LIMIT 10; -- Needed as it would order the entire table. Use TOP function for different dialects.
```

SELECT * of the bottom ten spend items\

```SQL
SELECT *
FROM table
ORDER BY "Spend" ASC -- Denotes low to high
LIMIT 10;
```

