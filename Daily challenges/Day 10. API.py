import requests
import json


def get_response_json(url:str, item_only=True) -> list:
    ROOT_URL = "https://api.stackexchange.com"
    response = requests.get(ROOT_URL + url)
    if item_only:
        return response.json()['items']
    return response.json()


def save_to_file(func):
    def wrapper(filename, *args):
        result = func(*args)
        with open(filename, 'w') as f:
            f.write(json.dumps(result))
    return wrapper


# find the 10 most highly voted posts in the last day. How many upvotes do they have?
@save_to_file
def highly_voted_top_10():
    return get_response_json("/2.2/posts?pagesize=10&fromdate=1622851200&order=desc&sort=votes&site=stackoverflow")


# find the first 3 badges by alphabetical order of their name
@save_to_file
def first_3_badges():
    return get_response_json("/2.2/badges?pagesize=3&order=asc&sort=name&site=stackoverflow")


#  find the most recent 3 users to be awarded each of these badges
@save_to_file
def recent_3_recipients():
    with open('first_3_badges') as f:
        badges = json.loads(f.read())
    # Create a dictionary with badge name: recipients(list of users)
    recipients = {b['name']: get_response_json(f"/2.2/badges/{b['badge_id']}/recipients?pagesize=3&site=stackoverflow") for b in badges}
    return recipients
    

# find the first 5 pages of posts from this month
@save_to_file
def posts_by_pages(pageNum=5):
    result = []
    for pIdx in range(pageNum):
        result.extend(get_response_json(f"/2.2/posts?page={pIdx}&pagesize=1&fromdate=1622505600&todate=1622937600&order=desc&sort=activity&site=stackoverflow"))
    return result



# create a function which gets all of the responses from an endpoint by paginating through them (essentially put your solution to the prev question in a function)
@save_to_file
def paginate_to_end(param, queries):
    
    page_idx = 1
    has_next_page = True
    result = []
    
    while has_next_page:
        response = get_response_json(f"/2.2/{param}?page={page_idx}&{queries}", item_only=False)
        result.extend(response['items'])
        has_next_page = response.get('has_more', False)
    
    return result



# find the 5 users with the most questions posted in the last week
# [hint] what does the “page” query param do? What is on the “Paging” section of the website?

def users_questioned_most_top_5():
    
    paginate_to_end('questions.txt', 'questions', 'pagesize=50&fromdate=1622937600&order=desc&sort=hot&site=stackoverflow')
    
    with open('questions.txt') as f:
        questions = json.loads(f.read())

    questioned_users = {}

    for q in questions:
        owner_id = q['owner']['user_id']
        num_question = questioned_users.get(owner_id, 0)
        questioned_users[owner_id] = num_question + 1

    top_5 = sorted(questioned_users.items(), key=lambda x:x[1], reverse=True)[:5]
    return top_5


# find the question with the most comments from today
def most_commented_today():
    #1. find questions today
    #paginate_to_end('questions.txt', 'questions', 'pagesize=50&fromdate=1622937600&order=desc&sort=hot&site=stackoverflow')
    with open('questions.txt') as f:
        questions = json.loads(f.read())

    #2. get each question id
    #3. get comments from id
    #4. length
    comments = {q['question_id']: len(paginate_to_end('question_comments.txt', f"questions/{q['question_id']}", 'order=desc&sort=creation&site=stackoverflow')) for q in questions}
    most_commented = sorted(comments.items(), key = lambda x:x[1], reverse=True)[0]
    return most_commented[0]



if __name__ == '__main__':
    #first_3_badges('first_3_badges.txt')
    #recent_3_recipients('recent_3.txt')
    most_commented_today()
