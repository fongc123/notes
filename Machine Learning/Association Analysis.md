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
> ```text
> for each transaction t in database do:
> 	for each candidate contained in t do:
> 		increment the support count;
> 	end
> end
> ```

## Generation of New Rules
An item set $A$ is <span style = "color:lightblue">frequent</span> if it satisfies the minimum support threshold $\text{min\_sup}$. Additionally, a <span style = "color:lightblue">frequent k-item set</span> is a frequent item set that contains $k$ items.
1. Generate all **non-empty proper subsets** $A$ of a frequent item set $S$.
2. For each $A$, the rule $A\rightarrow(S-A)$ is a strong rule if the confidence of rule $A$ exceeds the minimum confidence threshold $\text{min\_conf}$.
3. Repeat the above steps for all frequent item sets.

Thus, new rules are generated from subsets of frequent item sets.

> [!INFO]
> Each subset of a frequent item set $A$ automatically satisfies the minimum support threshold, as they are derived from a frequent item set (i.e., **strong rule!**).

# Apriori Algorithm
From [[#Generation of New Rules|the previous section]], association rule mining is reduced to finding frequent item sets. To avoid the computationally expensive brute-force method, item set candidates must be pruned.
1. **Any subset of a frequent item set must be frequent.**
2. **If there is any item set which is infrequent, its superset should not be tested or generated** (i.e., <span style = "color:lightblue">antimonotone</span> property of the support measure).

The steps of the algorithm are shown below.
1. Enumerate the candidate **1-item sets** by incrementing their [[#Support & Confidence|support count]].
2. Remove the candidate 1-item sets that are **infrequent** by a minimum support count threshold.
3. [[#Generation of Candidates|Generate]] the candidate **2-item sets** based on the remaining **frequent 1-item sets**.
4. Remove the candidate 2-item sets that are infrequent.
5. Repeat for $n$-item sets until no other item sets can be generated.

In general, frequent $(k-1)$-item sets generate new candidate $k$-item sets.

## Generation of Candidates
A smart generation method does not generate candidates that are guaranteed to be infrequent.

> [!WARNING]
> Generation of new candidates only aims to **reduce duplicates** and **remove any $k$-item sets that are guaranteed to be infrequent** (*the superset of an infrequent item set is also infrequent*). The new $k$-item set candidates must still be checked if they themselves are frequent.

## Example
An example of the algorithm is shown below, where the minimum support count is $3$ and a frequent 3-item set is generated.
- $k=1$: Sum of support counts ($\text{coke}$ and $\text{eggs}$ are infrequent).
- $k=2$: Self-join frequent item sets for ${4\choose2}$ or $6$ combinations.
- $k=3$: Self-join frequent item sets.
	- Only the item sets $A=\{\text{Bread},\text{Diaper}\}$ and $B=\{\text{Bread},\text{Milk}\}$ are joined.
	- The first $k-2$ or $1$ items are identical, ensuring that the subsets of the new item set are frequent.
	- For $i=1,2$, $a_i$ is lexicographically smaller than $b_i$, avoiding duplicates.

![[ml-apriori-ex.png|600]]

A brute-force approach would produce $41$ candidates up to size $3$.

$${6\choose1}+{6\choose2}+{6\choose3}=41$$

The <span style = "color:lightblue">Apriori algorithm</span> will only generate $13$ candidates up to size $3$.

$${6\choose1}+{4\choose2}+1=13$$

> [!INFO]
> The total number of combinations can be calculated with the following formula.
> $$_nC_r=\dfrac{n!}{r!(n-r)!}$$
> For example, the number of combinations from picking $2$ out of $4$ items is $_4C_2$.