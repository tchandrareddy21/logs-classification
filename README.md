<h1 align="center">LOGS Classification</h1>

## Project Overview
- This project builds a hybrid log classification system that incorporates three complementary approaches to manage varying complexities in log patterns. The classification techniques ensure adaptability and efficiency in processing predictable, intricate, and poorly-labeled data patterns.

### Problem Statement
- A company has different software, each generating logs. The goal is to classify logs into specific categories based on their function, making it easier to identify issues and streamline troubleshooting. This classification will be particularly helpful in detecting critical problems when something goes wrong.

### Solution Proposed
- Regular Expression (Regex):
  - Handles simple and predictable log patterns.
  - Ideal for cases where patterns can be effectively captured using predefined rules.

- Sentence Transformer + Logistic Regression:
  - Manages more complex patterns when sufficient training data is available.
  - Utilizes Sentence Transformer embeddings with Logistic Regression as the classification layer.

- Large Language Models (LLMs):
  - Used for highly complex patterns when labeled training data is insufficient.
  - Acts as a fallback or complementary approach to enhance classification.

### Log Classification Examples:

- **Security Alert**  
  ├── Cybersecurity Team  

- **Resource Usage**  
  ├── DevOps Team  

- **User Action**  
  ├── Analytics Team  


### Benefits of Hybrid Classification:
1. Cost Efficiency – Reduces expenses by minimizing reliance on LLMs for all classifications.
2. Performance – Regex-based classification is fast and efficient.
3. Improved Accuracy – Combines multiple approaches for more precise classification.
4. Scalability – Adapts to increasing data volumes and complexity effectively.


## Architectures
### Project Architecture
![High Level Project View](flowcharts/Technical%20Architecture%20High%20Level.png)

### Prediction Architecture
![Prediction Architecture](flowcharts/Prediction%20Architecture.png)
## How to run?

### Running the app locally using GitHub repository

#### Step 1: Clone the repository
```pycon
git clone https://github.com/tchandrareddy21/logs-classification.git
```
#### Step 2: Create the conda environment and activate the environment
```pycon
conda create -n logs-classification python=3.11 -y
```
```pycon
conda activate logs-classification
```

#### Step 3: Install the requirements
```pycon
pip install -r requirements.txt
```

#### Step 4: Create .env file and add the secrets
```pycon
touch .env
```
-  Replace empty codes with you API key
```python
GROQ_API_KEY = ""
```

#### Step 5: Run the application
```pycon
streamlit run app.py
```
- Go to below url to predict the new data.
```pycon
http://localhost:8501/
```

## UI Screenshots
![Streamlit UI](UI%20Screenshots/Streamlit%20UI.png)
![CSV Upload](UI%20Screenshots/CSV%20upload.png)
![Prediction Started](UI%20Screenshots/Prediction%20Started.png)
![Prediction Completed](UI%20Screenshots/Prediction%20completed.png)

