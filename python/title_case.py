def title_case(title, minor_words):
    words = title.split()
    result = []
    exception = minor_words.split()
    for w in words:
        if w in exception:
            result.append(w)
        else:
            result.append(w.capitalize())

    result[0] = result[0].capitalize()
    return " ".join(result)

