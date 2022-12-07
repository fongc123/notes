<span style = "color:lightblue">Association analysis</span> finds **rules** that predict the occurrence of an item in a transaction based on the occurrences of other items.

<span style = "color:lightblue">Market basket analysis</span> is one such association mining technique that large retailers commonly use to predict groups of purchased items. An example of a list of grocery transactions is shown.

| ID  |           Items           |
|:---:|:-------------------------:|
|  1  |        Bread, milk        |
|  2  | Bread, diaper, beer, eggs |
|  3  | Milk, diaper, beer, coke  |
|  4  | Bread, milk, diaper, beer |
|  5  | Bread, milk, diaper, coke |

> [!INFO]
> The above table of transactions can be represented in a binary format.
> 
> ![[ml-assoc-binary.png|600]]
> 
> An entry of $1$ represents the presence of the item in the transaction, while an entry of $0$ represents the absence of the item.

A strong rule that can be extracted is that **there is a strong relationship between the sale of beer and diapers together** (i.e., beer $\rightarrow$ diapers).

Association rule mining aims to achieve two things.
1. Find all frequent item sets (i.e., item sets that satisfy minimum support).
2. Generate strong association rules (i.e., find rules among the frequent item sets).

> [!WARNING]
> Strong rules are not necessarily interesting (e.g., when item sets have an overwhelming probability of occurring).

# Support & Confidence
Both <span style = "color:lightblue">support</span> and <span style = "color:lightblue">confidence</span> are used to determine the strength of a rule. Given a rule $A\rightarrow B$, **support** is the fraction of transactions that contain **both** item sets $A$ and $B$ (i.e., **not** $A$ or $B$), where $A$ and $B$ are subsets of the entire set $I=\{I_1, I_2,\ldots,I_n\}$ of all transactional items.

$$\text{support}(A\rightarrow B)=\frac{\text{support\_count}(A\cup B)}{|T|}=P(A\cup B)$$

The <span style = "color:lightblue">support count</span> is the number of transactions that contain the item set $A$. For example, the item set  $\{\text{Milk}, \text{Diaper}, \text{Beer}\}$ occurs in two (i.e., support count) out of a total of five transactions.

$$
\text{support}(\{\text{Milk}, \text{Diaper}\}\rightarrow\{\text{Beer}\})=\frac{\text{support\_count}(\{\text{Milk},\text{Diaper},\text{Beer}\})}{5}=\frac{2}{5}=0.4
$$

>[!WARNING]
>Rules with low support may occur simply by chance and may not be interesting.

The **confidence** of a rule is the fraction of transactions containing $A$ that also contain $B$.

$$\text{confidence}(A\rightarrow B)=\frac{\text{support}(A\cup B)}{\text{support}(A)}=\frac{\text{support\_count}(A\cup B)}{\text{support\_count}(A)}=P(B|A)$$

It is equivalent to the [[Data Preprocessing#Probability & Independence|conditional probability]] of $B$ given $A$. For example, the item subset $\{\text{Milk}, \text{Diaper}, \text{Beer}\}$ appears in two out of a total of three transactions that contain the item set $\{\text{Milk}, \text{Diaper}\}$.

$$\text{confidence}(\{\text{Milk}, \text{Diaper}\}\rightarrow\{\text{Beer}\})=\frac{\text{support\_count}(\{\text{Milk},\text{Diaper},\text{Beer}\})}{\text{support\_count}(\{\text{Milk}, \text{Diaper}\})}=\frac{2}{3}=0.67$$

Confidence measures the reliability of the rule. 

**A strong rule satisfies a minimum support threshold $\text{min\_sup}$ (or minimum support count threshold) and a minimum confidence threshold $\text{min\_conf}$.**

> [!INFO]
> All association rules between combinations of item sets can be mined by **brute-force**, which may be computationally expensive.

## Generation of Rules from Frequent Item Sets
An item set $A$ is <span style = "color:lightblue">frequent</span> if it satisfies the minimum support threshold $\text{min\_sup}$. Additionally, a <span style = "color:lightblue">frequent k-item set</span> is a frequent item set that contains $k$ items.
1. Generate all **non-empty proper subsets** $A$ of a frequent item set $S$.
2. For each $A$, the rule $A\rightarrow(S-A)$ is a strong rule if the confidence of rule $A$ exceeds the minimum confidence threshold $\text{min\_conf}$.
3. Repeat the above steps for all frequent item sets.

Thus, new rules are generated from subsets of frequent item sets.

> [!INFO]
> Each subset of a frequent item set $A$ automatically satisfies the minimum support threshold, as they are derived from a frequent item set (i.e., **strong rule!**).

