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

## Description of data files
- `995,000_rows.csv` is the full dataset and is available on Absalon.
- `995,000_rows_preprocessed_train.csv` is the training data from the full preprocessed dataset and is available on Dropbox here: https://www.dropbox.com/scl/fi/ttvp5r1u2xiuo0isj7kk0/995-000_rows_preprocessed_train.csv?rlkey=ll0mhyrf6jvgde0wc7m7cs9ve&st=cw6fl84s&dl=0
- `995,000_rows_preprocessed_valid.csv` is the validation data from the full preprocessed dataset and is available on Dropbox here: https://www.dropbox.com/scl/fi/c8845w5vr2k087f7e1ii1/995-000_rows_preprocessed_valid.csv?rlkey=ao7se9oo8jfd53djdm32b83ju&st=7df2uig1&dl=0
- `995,000_rows_preprocessed_test.csv` is the training data from the full preprocessed dataset and is available on Dropbox here: https://www.dropbox.com/scl/fi/huzi9hmf26bjzi1s3z9qu/995-000_rows_preprocessed_test.csv?rlkey=x0cazpvn6vx8lx8zu2m1fefkc&st=2f1nvm15&dl=0
Alternatively you can run the preprocessing code on the full dataset and create the preprocessed dataset locally. It will take approximately two hours.
- `15,000_rows.csv` is a large sample of the full dataset that can be used when you want to run the preprocessing pipeline on a dataset of decent size, but you do not want it to take hours to run. 
- `15,000_rows_preprocessed_train.csv` is the training data from a preprocessed sample of the full dataset that can be used when we want to work with the preprocessed data, but the preprocessed full dataset is too heavy.
- `15,000_rows_preprocessed_valid.csv` is the validation data from a preprocessed sample of the full dataset that can be used when we want to work with the preprocessed data, but the preprocessed full dataset is too heavy.
- `15,000_rows_preprocessed_test.csv` is the test data from a preprocessed sample of the full dataset that can be used when we want to work with the preprocessed data, but the preprocessed full dataset is too heavy.
- `250_rows.csv` is a small sample of the full dataset that is used for part 1, task 1.

## Description of .ipynb files
- `part1_preprocessing.ipynb` is the code for part 1.
- `part2_logisticRegression.ipynb` is the code for part 2.
- `part3_advancedModel.ipynb` is the code for part 3.
- `part4_evaluationLogisticReg.ipynb` is the code for part 4, but only regarding the evaluation of the logistic regression model.
- `part4_evaluationAdvancedModel.ipynb` is the code for part 4, but only regarding the evaluation of the advanced model.

#### Disclaimer 
We used google colab to train and test the advanced model. The jypitor notebooks: "part3_advancedModel.ipynb" and "part4_evaluationAdvancedModel.ipynb" get the data from my personal drive when run on google colab. However if you wish to run it yourself, the data used is provided in the misc folder and the dropbox links.

## Description of other files
- `part1_preprocessing.pdf` is the output of `part1_preprocessing.ipynb` run on the full dataset (which includes the output of the 'exploration code' which plots and graphs).
