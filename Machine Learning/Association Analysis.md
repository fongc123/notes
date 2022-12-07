<span style = "color:lightblue">Association analysis</span> finds **rules** that predict the occurrence of an item in a transaction based on the occurrences of other items.

<span style = "color:lightblue">Market basket analysis</span> is one such association mining technique that large retailers commonly use to predict groups of purchased items. An example of a list of grocery transactions is shown.

| ID  |           Items           |
|:---:|:-------------------------:|
|  1  |        Bread, milk        |
|  2  | Bread, diaper, beer, eggs |
|  3  | Milk, diaper, beer, coke  |
|  4  | Bread, milk, diaper, beer |
|  5  | Bread, milk, diaper, coke |

A strong rule that can be extracted is that **there is a strong relationship between the sale of beer and diapers together** (i.e., beer $\rightarrow$ diapers).

Association rule mining aims to achieve two things.
1. Find all frequent item sets (i.e., item sets that satisfy minimum support).
2. Generate strong association rules (i.e., find rules among the frequent item sets).

