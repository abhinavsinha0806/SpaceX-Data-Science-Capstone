# SpaceX Falcon 9 First Stage Landing Prediction

## 🚀 Project Overview
SpaceX advertises Falcon 9 rocket launches on its website with a cost of **$62 million**; other providers cost upward of **$165 million** each, much of the savings is because SpaceX can reuse the first stage. Therefore, if we can determine if the first stage will land, we can determine the cost of a launch. This project aims to predict the landing outcome of the Falcon 9 first stage using machine learning pipelines.

## 📂 Project Structure
The project follows a standard Data Science methodology:

### 1. Data Collection
- **API Request:** Fetched launch data from the SpaceX API.
- **Web Scraping:** Scraped Falcon 9 historical launch data from Wikipedia using BeautifulSoup.

### 2. Data Wrangling
- Filtered data to include only Falcon 9 launches.
- Handled missing values (e.g., calculated mean for payload mass).
- Converted categorical outcomes into binary classification (1 = Success, 0 = Failure).

### 3. Exploratory Data Analysis (EDA)
- **SQL:** Used SQL queries to analyze payload mass vs. booster versions and launch sites.
- **Visualization:** Created scatter plots and bar charts to analyze relationships between flight number, orbit, and success rate using Matplotlib and Seaborn.

### 4. Interactive Visual Analytics
- **Folium Map:** Built interactive maps to visualize launch sites and their proximity to coastlines, railways, and highways.
- **Plotly Dash:** Developed a real-time dashboard to filter launches by site and payload mass.

### 5. Predictive Analysis (Machine Learning)
- **Models Trained:** Logistic Regression, Support Vector Machine (SVM), Decision Tree, K-Nearest Neighbors (KNN).
- **Results:** Achieved **83.33% accuracy** on the test set across all models.
- **Best Model:** Decision Tree was identified as the robust model for this dataset.

## 📊 Key Insights
1. **Flight Experience:** Success rate significantly increases as the Flight Number increases.
2. **Orbit:** Launches to ES-L1, GEO, HEO, and SSO orbits have a 100% success rate.
3. **Payload:** Heavy payloads (>8,000 kg) have a higher success rate than lighter payloads for specific orbits.
4. **Location:** All launch sites are strategically located near coastlines for safety.

## 🛠️ Technologies Used
- **Languages:** Python, SQL
- **Libraries:** Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, Folium, Plotly Dash, BeautifulSoup, Requests
- **Tools:** Jupyter Notebooks, IBM Watson Studio

## 🏁 How to Run the Dashboard
1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `python spacex_dash_app.py`
4. Open your browser at `http://127.0.0.1:8050/`

## 📜 License
This project is part of the IBM Data Science Professional Certificate Capstone.
