import pandas as pd
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer
import re
ps = PorterStemmer()
lemmatizer = WordNetLemmatizer()

text = """Steve was born in Tokyo, Japan in 1950. He moved to London with his parents when he
was 5 years old. Steve started school there and his father began work at the hospital.
His mother was a house wife and he had four brothers.
He lived in England for 2 years then moved to Amman, Jordan where he lived there for
10 years. Steve then moved to Cyprus to study at the Mediterranean University.
Unfortunately, he did not succeed and returned to Jordan. His parents were very
unhappy so he decided to try in America.
He applied to many colleges and universities in the States and finally got some
acceptance offers from them. He chose Wichita State University in Kansas. His major
was Bio-medical Engineering. He stayed there for bout six months and then he moved
again to a very small town called Greensboro to study in a small college."""

##To loweer case
text  = text.lower()


# remove punctuations and special characters
clean_sentences = pd.Series(text).str.replace("[^a-zA-Z]", " ")

#removing whitespace
text = clean_sentences.str.strip()

stop_words = stopwords.words('english')
# function to remove stopwords
def remove_stopwords(sen):
    sen_new = " ".join([i for i in sen if i not in stop_words])
    return sen_new

#Remove stop words
text = remove_stopwords(text)


#Stemming
text1 = [ps.stem(word) for word in text]

text = ' '.join(text1)

print("after stemming", text)
#Lemmatize
text2 = [lemmatizer.lemmatize(word) for word in text]

text = ' '.join(text2)

print("after lemmatization",text)
