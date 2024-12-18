def from_txt_to_slug(slug: str) -> str:
    result = ""
    for i in slug.lower():
        if i.isalnum():
            result += i
        elif i == " ":
            result += "-"
    return result
