# ------ PITCHFORK SCRAPING LOGIC BELOW ------
from bs4 import BeautifulSoup
import requests

# gets the review page
# soupifies the response
# extracts p/span elements that contain the album score
# tests whether a score is present
# returns the score if one is found
def get_score(release):
    page = get_pitchfork_review_page(release)
    soup = BeautifulSoup(page.content, 'html.parser')
    p = soup.find('p') # score sometimes in the first 'p' element
    span = soup.find('span', {'class': 'score'}) # score sometimes in span element named 'score'
    score = test_elements_for_score(p, span)
    return score

# ------------- HELPER METHODS -------------

# compiles the elements of a pitchfork review url
def get_pitchfork_review_page(release):
    release_text = clean_string(release['title'])
    url = "https://pitchfork.com/reviews/albums/" + release_text
    return requests.get(url)

# formats title string for pitchfork review url
def clean_string(string):
    word_list = string.split()
    new_list = []
    for word in word_list:
        clean_word = "".join(filter(str.isalnum, word))
        if clean_word:
            new_list += [clean_word]
    clean_str = "-".join(new_list)
    return clean_str.lower()

# checks if the scrape actually pulled a score and,
# if so, returns it.
def test_elements_for_score(p, span):
    if span:
        try:
            return float(span.text)
        except:
            print('span is not a valid score')
    try:
        return float(p.text)
    except:
        print('No Pitchfork score found')

