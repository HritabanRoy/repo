import urllib.request, json

def loadJson(json_subreddit):
    #input subreddit to extract posts from
    with open(str(json_subreddit)) as f:
        return json.load(f)


def getJson(subreddit_name, post_limit):
    #getting the json query result
    with urllib.request.urlopen("https://www.reddit.com/r/{}/top/.json?limit={}".format(subreddit_name, post_limit)) as url:
        return json.loads(url.read().decode())


def processData(post_data_json, post_limit, processed_data):
    #extract post url out of json
    for post_number in range(post_limit):
        processed_data[len(processed_data)] = {
            "title" : post_data_json["data"]["children"][post_number]["data"]["title"],
            "content" : post_data_json["data"]["children"][post_number]["data"]["url"],
            "url" : "https://reddit.com" + post_data_json["data"]["children"][post_number]["data"]["permalink"]
        }


def storeJson(json_filename, json_content): #regressed
    # stores post url in json file
    with open(json_filename, 'w') as json_file:
        json.dump(json_content, json_file, indent=3) #post_links is json variable


def scrape():
    processed_data = {}
    subreddits_to_scrape = loadJson('subreddits_to_scrape.json')
    for subreddit in subreddits_to_scrape.values():
        subreddit_name = subreddit["subreddit"]
        post_limit = subreddit["post_limit"]

        if post_limit == 0:
            continue
        
        raw_data = getJson(subreddit_name, post_limit)
        processData(raw_data, post_limit, processed_data)
    return processed_data






