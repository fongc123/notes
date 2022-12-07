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

Item set is a subset of $I$. $I=\{I_1, I_2, \ldots, I_n\}$.

<span style = "color:lightblue">Support count</span>: number of transactions that contain the item set $A$
<span style = "color:lightblue">Support</span>: fraction of transactions that contain the item set $A$

$$\text{support}(A)=\frac{\text{support\_count}(A)}{|T|}=P(A)$$

For example, the support count of the item set $\{\text{Milk}, \text{Diaper}, \text{Beer}\}$ occurs in two (i.e., support) out of a total of five transactions.

$$\text{support}(A)=\frac{2}{5}=0.4$$

# Support & Confidence
Both <span style = "color:lightblue">support</span> and <span style = "color:lightblue">confidence</span> are used to determine the strength of a rule. Given a rule $A\rightarrow B$, **support** is the fraction of transactions that contain **both** item sets $A$ and $B$ (i.e., **not** $A$ or $B$).

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