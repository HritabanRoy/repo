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
        post_links.append(post_data_json["data"]["children"][post_number]["data"]["url_overridden_by_dest"])


def storeJson(json_filename):
    # stores post url in json file
    with open(json_filename, 'w') as json_file:
        json.dump(post_links, json_file, indent=3) #post_links is json variable



subreddits = loadJson('subreddits.json')
post_links = [] #list to store output links
for v in subreddits.values():
    subreddit_name = v["subreddit"]
    post_limit = v["post_limit"]

    #skip empty subreddits
    if post_limit == 0:
        continue

    post_json = getJson(subreddit_name, post_limit)
    extractFromJson(post_json, post_limit)

storeJson('redditJsonOut.json')




