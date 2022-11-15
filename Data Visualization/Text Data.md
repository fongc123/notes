<span style = "color:lightblue">Text visualization</span> allows for quick understanding, grouping, comparison, and correlation of texts (e.g., articles, emails, messages).

There are various <span style = "color:lightblue">text mining</span> techniques that are used to analyze texts.

- <span style = "color:lightblue">information extraction</span>: obtaining structured information from unstructured or semi-structure text
	- <span style = "color:lightblue">named entity recognition</span>: extraction of proper nouns (e.g., organizations and specific people)
	- <span style = "color:lightblue">relation extraction</span>: extraction of relationship between entities
- <span style = "color:lightblue">text summarization</span>: short and concise information about a document or collection of documents (i.e., compressing multiple sentences to one sentence)
- <span style = "color:lightblue">opinion mining</span> and <span style = "color:lightblue">sentiment analysis</span>: extraction of opinions and emotions about entities or topics
- <span style = "color:lightblue">text clustering</span>: obtaining similar objects in text through similarity functions
	- <span style = "color:lightblue">term frequency-inverse document frequency (tf-idf)</span>: numerical statistic that reflects the importance of a term in a document with respect to a collection of documents
	- <span style = "color:lightblue">cosine similarity</span>
- <span style = "color:lightblue">text classification</span>: classification of texts with [[ML Basics|machine learning]]

The image below demonstrates how information and relations can be extracted from raw text.

![[data-vis-text-info-extraction.png|600]]

<span style = "color:lightblue">Text visualizations</span> generally do not represent the text directly. Instead, they represent the output of a language model (e.g., word count, sequences). It is important to match visualization tools with the abstraction and analysis task.
- <span style = "color:lightblue">node-link</span>: displays text as a **word tree**, where each node represents a term or a phrase
- <span style = "color:lightblue">cloud</span> or <span style = "color:lightblue">galaxy</span>: displays the most frequent words in a word cloud
- <span style = "color:lightblue">line plot</span> or <span style = "color:lightblue">river plot</span>: 