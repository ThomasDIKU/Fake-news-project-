# Import libraries
import re
from cleantext import clean
from nltk.tokenize import word_tokenize 
from nltk.tokenize import MWETokenizer 
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer



# The function clean_text() does this:
#   - all words will be lowercased
#   - tabs, new lines and multiple white spaces will be set to single white space
#   - numbers, dates, emails, and URLs will be replaced by "\<NUM>", "\<DATE>", "\<EMAIL>" AND "\<URL>", respectively.
def clean_text(data):
  # Set dates with format DD/MM/YYYY or MM/DD/YYYY to "<date>"
  data = re.sub("[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}", "<date>", data) 

  # Set dates with the format DD/MM/YY or MM/DD/YY to "<date>"
  data = re.sub("[0-9]{1,2}/[0-9]{1,2}/[0-9]{2}", "<date>", data) 

  # Set dates with the format DD/MM/YYYY or MM/DD/YYYY to "<date>"
  data = re.sub("[0-9]{1,2}-[0-9]{1,2}-[0-9]{4}", "<date>", data) 

  # Set dates with the format DD/MM/YY or MM/DD/YY to "<date>"
  data = re.sub("[0-9]{1,2}-[0-9]{1,2}-[0-9]{2}", "<date>", data)

  # Consider adding other date formats, like "Sept 6", "September 6, 2019", etc.

  # Use clean() for remaining cleaning
  cleaned = clean(data,
      fix_unicode=False,           # fix various unicode errors
      to_ascii=False,              # transliterate to closest ASCII representation
      lower=True,                  # lowercase text
      no_line_breaks=True,         # fully strip line breaks as opposed to only normalizing them
      no_urls=True,                # replace all URLs with a special token
      no_emails=True,              # replace all email addresses with a special token
      no_phone_numbers=False,      # replace all phone numbers with a special token
      no_numbers=True,             # replace all numbers with a special token
      no_digits=False,             # replace all digits with a special token
      no_currency_symbols=False,   # replace all currency symbols with a special token
      no_punct=False,              # remove punctuations
      replace_with_punct="",       # instead of removing punctuations you may replace them
      replace_with_url="<URL>",
      replace_with_email="<EMAIL>",
      replace_with_phone_number="<PHONE>",
      replace_with_number="<NUM>",
      replace_with_digit="0",
      replace_with_currency_symbol="<CUR>",
      lang="en"                     # set to 'de' for German special handling
  )
  return cleaned


# Function that tokenize a string
def tokenize(data_string):

    # Word tokenize
    data_string = word_tokenize(data_string)

    # MAKE '<', 'num' and '>' into '<num>'. Same for <date>, <email> and <url>:
    multiWordsTokenizer = MWETokenizer([('<', 'num', '>'), ('<', 'date', '>'), ('<', 'email', '>'), ('<', 'url', '>')], separator='')
    data_string = multiWordsTokenizer.tokenize(data_string)

    return data_string


# Function that removes stop words from a string
def removeStopWords(words):
    
    stop_words = set(stopwords.words('english'))
    filteredWords = []

    for w in words:
        if w not in stop_words:
            filteredWords.append(w)
    return(filteredWords)


# Function that performs stemming on a string
def stemming(words):
    
    stemmer = PorterStemmer()
    stemmedWords = []

    for w in words:
        stemmedWords.append(stemmer.stem(w))
    
    return(stemmedWords)