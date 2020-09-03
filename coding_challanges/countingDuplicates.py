def duplicate_count(text):
    text = list(text)
    text = [item.lower() for item in text]
    count = 0
    for e in text:
        if text.count(e) > 1:
            count = count + 1
            for i in range(text.count(e)-1):
                text.remove(e)
    return  count

print(duplicate_count(""))