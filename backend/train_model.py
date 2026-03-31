import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle
import os

# 1. Create a small synthetic dataset for demonstration
# In a real scenario, you would use a large dataset like Fake.csv/True.csv
data = {
    'text': [
        # --- 30 Real News ---
        "The Federal Reserve chair announced a slight increase in interest rates to combat inflation.",
        "New research suggests that a Mediterranean diet can significantly reduce the risk of heart disease.",
        "The city council approved a new budget for public transportation improvements and infrastructure.",
        "SpaceX successfully landed its Falcon 9 rocket on a drone ship in the Atlantic Ocean.",
        "The Tokyo Stock Exchange saw a 2% rise following positive corporate earnings reports.",
        "Global temperatures in July were the highest ever recorded, according to weather authorities.",
        "The World Health Organization officially declared the end of the recent public health emergency.",
        "A group of archaeologists discovered a lost city in the Amazon rainforest dating back 1,000 years.",
        "The national park service is implementing new conservation measures to protect endangered species.",
        "Electric vehicle sales increased by 40% globally in the last fiscal year.",
        "The Nobel Prize in Physics was awarded to three scientists for their work on quantum mechanics.",
        "The local bridge will be closed for maintenance starting next Monday for two weeks.",
        "New agricultural techniques have helped farmers in dry regions double their crop yields.",
        "The tech company announced its latest smartphone featuring a revolutionary battery technology.",
        "Olympic athletes are beginning their final training cycles ahead of the summer games.",
        "UN reports show a decrease in global poverty levels over the past decade in several regions.",
        "A major software update was released today to fix security vulnerabilities in popular browsers.",
        "The annual film festival announced its lineup featuring several independent international movies.",
        "Recent census data shows an increase in the urban population across the country.",
        "The university opened a new research center dedicated to renewable energy solutions.",
        "Automakers are transitioning more production lines to fully electric models by 2030.",
        "The local library is launching a new digital literacy program for seniors in the community.",
        "Mars Rover sends back high-resolution images of the planet's rocky surface and craters.",
        "Standardized test scores for high school students showed improvement in mathematics this year.",
        "A new treaty for international maritime safety was signed by over fifty nations today.",
        "Healthcare providers are adopting tele-health services at an unprecedented rate.",
        "The museum is hosting a special exhibit on the history of ancient Egyptian civilization.",
        "Financial analysts suggest that the tech sector will lead the market recovery this quarter.",
        "Recent breakthroughs in battery storage are making solar energy more viable for households.",
        "The national weather service issued a thunderstorm warning for the coastal counties.",

        # --- 30 Fake News ---
        "Secret government files reveal that the moon landing was filmed in a Hollywood basement.",
        "Drinking lemon juice every morning will grant you the ability to speak to dolphins.",
        "Breaking: Chocolate has been proven to cure all types of viruses instantly.",
        "NASA whistleblower claims that Mars is actually a giant projection in the sky.",
        "Scientists find that walking backwards for 20 minutes a day restores your youth.",
        "The world's richest man is secretly a lizard from the fourth dimension.",
        "Leaked documents show that gravity is a hoax used to keep people from floating away.",
        "A new pill allows humans to live without oxygen for up to three hours at a time.",
        "The Eiffel Tower was originally built as a long-range communication antenna for aliens.",
        "Eating pizza once a day has been shown to increase your IQ by 50 points.",
        "Breaking: The Earth is actually shaped like a giant donut, say conspiracy theorists.",
        "Water has been discovered to have a secret memory of everywhere it has been.",
        "New law requires citizens to wear tinfoil hats to prevent mind-reading by satellites.",
        "Scientists have discovered a portal to a parallel universe inside a coffee shop in London.",
        "The internet will be permanently shut down starting tomorrow at midnight.",
        "A secret forest in Siberia is home to talking trees that predict the future.",
        "The sun is actually a giant electric lightbulb designed by 19th-century inventors.",
        "Your smartphone can now charge its battery using the power of your thoughts.",
        "Ancient scrolls suggest the Great Pyramids were actually grain silos for giants.",
        "Rainwater in some cities now contains liquid gold worth millions of dollars.",
        "A new study proves that pets are actually spies sent from the planet Orion.",
        "The government is secretly replacing all birds with high-tech surveillance drones.",
        "Eating at midnight is the best way to lose weight and gain muscle instantly.",
        "Scientists find ancient city under Antarctica that is still populated by Vikings.",
        "A new app can translate the language of insects into English in real-time.",
        "The clouds in the sky are actually giant sponges soaking up toxic chemicals.",
        "Famous actor reveals he has been replaced by a holographic projection for years.",
        "Breaking: Gravity will be turned off for 15 minutes today for maintenance.",
        "New research shows that sleeping for 12 hours a day makes you a genius.",
        "A hidden island in the Pacific is where all the missing socks from laundry go."
    ],
    'label': ['Real'] * 30 + ['Fake'] * 30
}


df = pd.DataFrame(data)

# 2. Vectorize the text
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['text'])
y = df['label']

# 3. Train a simple model
model = LogisticRegression()
model.fit(X, y)

# 4. Save the model and vectorizer
if not os.path.exists('models'):
    os.makedirs('models')

with open('models/model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('models/tfidf.pkl', 'wb') as f:
    pickle.dump(vectorizer, f)

print("Model and vectorizer trained and saved successfully in /models directory.")
