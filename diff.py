import re

def parse_instagram_file(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("Error: insta_folks.txt File not found.")
        return None

    # Locate section headers
    try:
        following_index = lines.index("Following\n")
        followers_index = lines.index("Followers\n")
    except ValueError:
        print("Error: 'Following' or 'Followers' headers not found in the file.")
        return None

    # Separate Following and Followers sections
    following = set()
    followers = set()

    # Regex to identify date patterns
    date_pattern = re.compile(r'^[A-Za-z]{3} \d{2}, \d{4} \d{1,2}:\d{2} (am|pm)$')

    # Extract Following usernames
    for line in lines[following_index + 1:followers_index]:
        username = line.strip()
        if username and not date_pattern.match(username):  # Skip dates and empty lines
            following.add(username)

    # Extract Followers usernames
    for line in lines[followers_index + 1:]:
        username = line.strip()
        if username and not date_pattern.match(username):  # Skip dates and empty lines
            followers.add(username)

    return following, followers

def find_differences(following, followers):
    not_following_back = following - followers
    not_followed_by_you = followers - following
    return not_following_back, not_followed_by_you

def save_results_to_html(not_following_back, not_followed_by_you):
    with open("result.html", "w") as file:
        file.write("<html><head><style>")
        file.write("body { background-color: black; color: white; font-family: Arial, sans-serif; }\n")
        file.write(".container { display: flex; justify-content: space-between; }\n")
        file.write(".column { width: 48%; }\n")
        file.write("a { color: #1E90FF; text-decoration: none; }\n")
        file.write("a:hover { text-decoration: underline; }\n")
        file.write("</style></head><body>\n")

        file.write("<div class='container'>\n")

        file.write("<div class='column'>\n")
        file.write("<h2>Users you follow but don't follow you back:</h2>\n<ul>\n")
        for user in not_following_back:
            file.write(f"<li><a href='https://instagram.com/{user}' target='_blank'>{user}</a></li>\n")
        file.write("</ul>\n</div>\n")

        file.write("<div class='column'>\n")
        file.write("<h2>Users who follow you but you don't follow back:</h2>\n<ul>\n")
        for user in not_followed_by_you:
            file.write(f"<li><a href='https://instagram.com/{user}' target='_blank'>{user}</a></li>\n")
        file.write("</ul>\n</div>\n")

        file.write("</div>\n")
        file.write("</body></html>\n")

def main():
    file_path = "insta_folks.txt"  # Change the file name here
    result = parse_instagram_file(file_path)

    if result:
        following, followers = result

        # Find differences
        not_following_back, not_followed_by_you = find_differences(following, followers)

        # Save results to an HTML file
        save_results_to_html(not_following_back, not_followed_by_you)

        print("Done! result.html is ready.")


if __name__ == "__main__":
    main()
