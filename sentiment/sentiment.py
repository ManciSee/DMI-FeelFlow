import pandas as pd
import json
import numpy as np
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from translate import Translator
from feel_it import EmotionClassifier, SentimentClassifier

# ------------------ Sentiment Analysis by traslating text from it to en ------------------
'''
df = pd.read_csv('../data.csv', sep=',')
print(df.head())

nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()

translator = Translator(to_lang="en", from_lang="it")

res = {}
for i, row in df.iterrows():
    text = row['Comments']
    id = row['Message ID']

    translated_text = translator.translate(text)
    #print(translated_text)
    sentiment = sia.polarity_scores(translated_text)
    res[id] = sentiment

result_df = pd.DataFrame(res).T
print(result_df.head())

vaders = pd.DataFrame(res).T
vaders = vaders.reset_index().rename(columns={'index': 'Message ID'})
vaders = vaders.merge(df, how='left')

print("Add polarity scores to dataset")
vaders.to_csv('DMI_sentiment.csv', index=False)
print("Done!")
'''
# ------------------------------------------------------------------------------------------


# ------------------ Sentiment Analysis by using Bert - Italian ----------------------------
sentiment = SentimentClassifier()
emotion = EmotionClassifier()

data = pd.read_csv('../data.csv', sep=',')

print("Calculating sentiment and emotion...")
data['Sentiment'] = sentiment.predict(data['Comments'].values.tolist())
data['Emotion'] = emotion.predict(data['Comments'].values.tolist())
print("Done!")
print(data)

print("Saving dataset...")
data.to_csv('DMI_sentiment_emotion.csv', index=False)
print("Done!")

# ------------------------------------------------------------------------------------------