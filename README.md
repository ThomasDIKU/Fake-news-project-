## Required libraries
Make sure that the following libraries are installed: ```pandas```, ```numpy```, ```cleantext```, ```matplotlib```, ```ast```, ```re```, ```joblib```, ```collections```, ```scipy```, ```tensorflow```, ```json```, ```nltk```. If they are not installed, they can be installed in the terminal using these commands:

```
pip install pandas
pip install numpy
pip install cleantext
pip install matplotlib
pip install ast
pip install re
pip install joblib
pip install collections
pip install scipy
pip install tensorflow
pip install json
pip install nltk
```

## How to run the code
1. Clone the repo `Fake-news-project-` to your local machine by running this command in your terminal:
```
git clone https://github.com/ThomasDIKU/Fake-news-project-.git
```

2. Make sure Jupyter Notebook is installed. If not, run this command in your terminal:

```
pip install jupyter notebook
```

3. Navigate to the `Fake-news-project-` repo and run this command in your terminal:

```
jupyter notebook
```

4. Open the .ipynb file that you want to run (e.g. `part1_preprocessing.ipynb`). Run either a selected kode cell by pressing the 'play' icon, or run the entire script by clicking `Run -> Run All Cells`.

#### Disclaimer 
We used google colab to train and test the advanced model. The jypitor notebooks: "part3_advancedModel.ipynb" and "part4_evaluationAdvancedModel.ipynb" get the data from my personal drive when run on google colab. However if you wish to run it yourself, the data used is provided in the misc folder and the dropbox links. https://www.dropbox.com/scl/fi/xpzzii0mns4f2vtzptq82/tokenizer.pkl?rlkey=o6umee4gaeyqet2ryooq3cmka&st=3fpxc9cn&dl=0

## Description of data in `BBC_data` folder
- `BBC_preprocessed.csv` is the BBC articles that was scraped as part of individuel assignment 2, which has been preprocessed in our preprocessing pipeline. 

## Description of data in `fakenewscorpus_data` folder
- `15,000_rows.csv` is a large sample of the full dataset that can be used when you want to run the preprocessing pipeline on a dataset of decent size, but you do not want it to take hours to run. 
- `15,000_rows_preprocessed.csv` is the preprocessed sample of the full dataset that can be used when we want to work with the preprocessed data, but the preprocessed full dataset is too heavy.
- `15,000_rows_preprocessed_train.csv` is the training data from a preprocessed sample of the full dataset that can be used when we want to work with the preprocessed data, but the preprocessed full dataset is too heavy.
- `15,000_rows_preprocessed_valid.csv` is the validation data from a preprocessed sample of the full dataset that can be used when we want to work with the preprocessed data, but the preprocessed full dataset is too heavy.
- `15,000_rows_preprocessed_test.csv` is the test data from a preprocessed sample of the full dataset that can be used when we want to work with the preprocessed data, but the preprocessed full dataset is too heavy.
- `250_rows.csv` is a small sample of the full dataset that is used for part 1, task 1.

## Description of data in `liar_data` folder
- `liar_data_full.tsv` is the full unprocessed LIAR dataset where train, validation and test data has been combined.
- `liar_full_dataset_preprocessed.csv` is the preprocessed full LIAR dataset where train, validation and test data has been combined.

## Description of data in `misc` folder
- `logistic_model.joblib` is our logistic regression model from part 2.
- `scaler.pkl` is the scaler created based on `995,000_rows_preprocessed_train.csv`.
- `top_10000_words.json` is the 10,000 most common words (tokens) in the preprocessed FakeNewsCorpus training data. 
- `X_test_scaled.npz` is the scaled BoW of the test data. 
- `y_test.csv` is the labels for the test data.

## Description of .ipynb files
- `part1_preprocessing.ipynb` is the code for part 1.
- `part2_logisticRegression.ipynb` is the code for part 2.
- `part3_advancedModel.ipynb` is the code for part 3.
- `part4_evaluationLogisticReg.ipynb` is the code for part 4, but only regarding the evaluation of the logistic regression model.
- `part4_evaluationAdvancedModel.ipynb` is the code for part 4, but only regarding the evaluation of the advanced model.
- `preprocessingFunctions.ipynb` is the function used for preprocessing: `clean_text()`, `tokenize()`, `removeStopWords()` and `stemming()`.

## Description of data on `dropbox`
- `995,000_rows_preprocessed_train.csv` is the training data from the full preprocessed dataset and is available on Dropbox here: https://www.dropbox.com/scl/fi/ttvp5r1u2xiuo0isj7kk0/995-000_rows_preprocessed_train.csv?rlkey=ll0mhyrf6jvgde0wc7m7cs9ve&st=te2juxnc&dl=0
- `995,000_rows_preprocessed_valid.csv` is the validation data from the full preprocessed dataset and is available on Dropbox here: https://www.dropbox.com/scl/fi/c8845w5vr2k087f7e1ii1/995-000_rows_preprocessed_valid.csv?rlkey=ao7se9oo8jfd53djdm32b83ju&st=7df2uig1&dl=0
- `995,000_rows_preprocessed_test.csv` is the training data from the full preprocessed dataset and is available on Dropbox here: https://www.dropbox.com/scl/fi/huzi9hmf26bjzi1s3z9qu/995-000_rows_preprocessed_test.csv?rlkey=x0cazpvn6vx8lx8zu2m1fefkc&st=2f1nvm15&dl=0