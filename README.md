# Veritas AI: Fake News Detection Prototype

Veritas AI is a modern, full-stack web application designed to demonstrate the power of Machine Learning in identifying potential misinformation in news articles. This project serves as a **functional prototype** and educational tool for NLP-based classification.

> [!IMPORTANT]
> This is a **prototype project**. To train the model for real-time news detection in a production environment, you must replace the synthetic dataset with a larger, verified dataset (e.g., from Kaggle or news agencies).

---

## 📊 Prototype Dataset
The model is currently trained on a curated synthetic dataset of 60 examples (30 Real, 30 Fake).

### Real News Examples (Training Set)
1. The Federal Reserve chair announced a slight increase in interest rates to combat inflation.
2. New research suggests that a Mediterranean diet can significantly reduce the risk of heart disease.
3. The city council approved a new budget for public transportation improvements and infrastructure.
4. SpaceX successfully landed its Falcon 9 rocket on a drone ship in the Atlantic Ocean.
5. The Tokyo Stock Exchange saw a 2% rise following positive corporate earnings reports.
6. Global temperatures in July were the highest ever recorded, according to weather authorities.
7. The World Health Organization officially declared the end of the recent public health emergency.
8. A group of archaeologists discovered a lost city in the Amazon rainforest dating back 1,000 years.
9. The national park service is implementing new conservation measures to protect endangered species.
10. Electric vehicle sales increased by 40% globally in the last fiscal year.
11. The Nobel Prize in Physics was awarded to three scientists for their work on quantum mechanics.
12. The local bridge will be closed for maintenance starting next Monday for two weeks.
13. New agricultural techniques have helped farmers in dry regions double their crop yields.
14. The tech company announced its latest smartphone featuring a revolutionary battery technology.
15. Olympic athletes are beginning their final training cycles ahead of the summer games.
16. UN reports show a decrease in global poverty levels over the past decade in several regions.
17. A major software update was released today to fix security vulnerabilities in popular browsers.
18. The annual film festival announced its lineup featuring several independent international movies.
19. Recent census data shows an increase in the urban population across the country.
20. The university opened a new research center dedicated to renewable energy solutions.
21. Automakers are transitioning more production lines to fully electric models by 2030.
22. The local library is launching a new digital literacy program for seniors in the community.
23. Mars Rover sends back high-resolution images of the planet's rocky surface and craters.
24. Standardized test scores for high school students showed improvement in mathematics this year.
25. A new treaty for international maritime safety was signed by over fifty nations today.
26. Healthcare providers are adopting tele-health services at an unprecedented rate.
27. The museum is hosting a special exhibit on the history of ancient Egyptian civilization.
28. Financial analysts suggest that the tech sector will lead the market recovery this quarter.
29. Recent breakthroughs in battery storage are making solar energy more viable for households.
30. The national weather service issued a thunderstorm warning for the coastal counties.

### Fake News Examples (Training Set)
1. Secret government files reveal that the moon landing was filmed in a Hollywood basement.
2. Drinking lemon juice every morning will grant you the ability to speak to dolphins.
3. Breaking: Chocolate has been proven to cure all types of viruses instantly.
4. NASA whistleblower claims that Mars is actually a giant projection in the sky.
5. Scientists find that walking backwards for 20 minutes a day restores your youth.
6. The world's richest man is secretly a lizard from the fourth dimension.
7. Leaked documents show that gravity is a hoax used to keep people from floating away.
8. A new pill allows humans to live without oxygen for up to three hours at a time.
9. The Eiffel Tower was originally built as a long-range communication antenna for aliens.
10. Eating pizza once a day has been shown to increase your IQ by 50 points.
11. Breaking: The Earth is actually shaped like a giant donut, say conspiracy theorists.
12. Water has been discovered to have a secret memory of everywhere it has been.
13. New law requires citizens to wear tinfoil hats to prevent mind-reading by satellites.
14. Scientists have discovered a portal to a parallel universe inside a coffee shop in London.
15. The internet will be permanently shut down starting tomorrow at midnight.
16. A secret forest in Siberia is home to talking trees that predict the future.
17. The sun is actually a giant electric lightbulb designed by 19th-century inventors.
18. Your smartphone can now charge its battery using the power of your thoughts.
19. Ancient scrolls suggest the Great Pyramids were actually grain silos for giants.
20. Rainwater in some cities now contains liquid gold worth millions of dollars.
21. A new study proves that pets are actually spies sent from the planet Orion.
22. The government is secretly replacing all birds with high-tech surveillance drones.
23. Eating at midnight is the best way to lose weight and gain muscle instantly.
24. Scientists find ancient city under Antarctica that is still populated by Vikings.
25. A new app can translate the language of insects into English in real-time.
26. The clouds in the sky are actually giant sponges soaking up toxic chemicals.
27. Famous actor reveals he has been replaced by a holographic projection for years.
28. Breaking: Gravity will be turned off for 15 minutes today for maintenance.
29. New research shows that sleeping for 12 hours a day makes you a genius.
30. A hidden island in the Pacific is where all the missing socks from laundry go.

---

## 🛠️ Technology Stack
- **Frontend**: React (Vite), CSS3 (Glassmorphism), Lucide Icons, Axios.
- **Backend**: FastAPI (Python), Uvicorn.
- **ML Engine**: Scikit-Learn (TF-IDF Vectorizer + Logistic Regression).

---

## 🚀 Getting Started

### Prerequisites
- Node.js (v18+)
- Python (3.10+)

### Setup Instructions
1. Navigate to the project root:
   ```powershell
   cd FakeNewsDetectionApp
   ```
2. Run the automated startup script:
   ```powershell
   ./start.ps1
   ```

### Training Your Own Data
If you wish to train the model on real-world news:
1. Replace the lists in `backend/train_model.py` with your own dataset or load a `.csv` file using Pandas.
2. Run the training script:
   ```powershell
   cd backend
   python train_model.py
   ```
3. Restart the backend server.

---

## ⚖️ License
This project is for educational and prototype purposes only.
