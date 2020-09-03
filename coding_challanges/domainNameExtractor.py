def domain_name(url):
    url = url.split(".")
    if "www" in url[0]:
        return url[1]
    elif "http" not in url[0]:
        return url[0]
    else:
        url = url[0].split("//")
        return url[1]

print(domain_name("https://cnet.com"))