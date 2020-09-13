import urllib.request, json

def loadJson(json_subreddit):
    #input subreddit to extract posts from
    with open(str(json_subreddit)) as f:
        return json.load(f)


def getJson(subreddit_name, post_limit):
    #getting the json query result
    with urllib.request.urlopen("https://www.reddit.com/r/{}/top/.json?limit={}".format(subreddit_name, post_limit)) as url:
        return json.loads(url.read().decode())


def extractFromJson(post_data_json, post_limit):
    #extract post url out of json
    for post_number in range(post_limit):
        processed_data[len(processed_data)] = {
            "title" : post_data_json["data"]["children"][post_number]["data"]["title"],
            "content" : post_data_json["data"]["children"][post_number]["data"]["url"],
            "url" : "https://reddit.com" + post_data_json["data"]["children"][post_number]["data"]["permalink"]
        }


def storeJson(json_filename, json_content):
    # stores post url in json file
    with open(json_filename, 'w') as json_file:
        json.dump(json_content, json_file, indent=3) #post_links is json variable


processed_data = {} #dict stores extracted data
subreddits = loadJson('subreddits.json')
for v in subreddits.values():
    subreddit_name = v["subreddit"]
    post_limit = v["post_limit"]

    #skip empty subreddits
    if post_limit == 0:
        continue

    content_data = getJson(subreddit_name, post_limit)
    extractFromJson(content_data, post_limit)

storeJson('redditJsonOut.json', processed_data)




