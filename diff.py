import json

def parse_instagram_json(followers_file, following_file):
    try:
        with open(followers_file, 'r') as file:
            followers_data = json.load(file)
        with open(following_file, 'r') as file:
            following_data = json.load(file)
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None

    # Extract followers from JSON
    followers = set()
    for entry in followers_data:
        string_list_data = entry.get("string_list_data", [])
        for item in string_list_data:
            followers.add(item.get("value", ""))

    # Extract following from JSON
    following = set()
    for entry in following_data.get("relationships_following", []):
        string_list_data = entry.get("string_list_data", [])
        for item in string_list_data:
            following.add(item.get("value", ""))

    return following, followers

def find_differences(following, followers):
    not_following_back = following - followers
    not_followed_by_you = followers - following
    return not_following_back, not_followed_by_you

def save_results_to_html(not_following_back, not_followed_by_you):
    with open("result.html", "w") as file:
        file.write("<html><head><style>")
        file.write("""
            body {
                background-color: black;
                color: white;
                font-family: sans-serif;
                margin: 0;
                padding: 20px;
            }
            .container {
                display: flex;
                justify-content: space-between;
            }
            .column {
                width: 48%;
            }
            .user {
                margin: 5px 0;
            }
            a {
                color: cyan;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        """)
        file.write("</style></head><body>\n")

        file.write("<div class='container'>\n")
        # First column: Users you follow but don't follow you back
        file.write("<div class='column'>\n")
        file.write("<h2>Users you follow but don't follow you back:</h2>\n")
        for user in not_following_back:
            file.write(f"<div class='user'><a href='https://instagram.com/{user}' target='_blank'>{user}</a></div>\n")
        file.write("</div>\n")

        # Second column: Users who follow you but you don't follow back
        file.write("<div class='column'>\n")
        file.write("<h2>Users who follow you but you don't follow back:</h2>\n")
        for user in not_followed_by_you:
            file.write(f"<div class='user'><a href='https://instagram.com/{user}' target='_blank'>{user}</a></div>\n")
        file.write("</div>\n")

        file.write("</div>\n")
        file.write("</body></html>\n")


def main():
    followers_file = "connections/followers_and_following/followers_1.json"  
    following_file = "connections/followers_and_following/following.json"  

    result = parse_instagram_json(followers_file, following_file)

    if result:
        following, followers = result

        # Find differences
        not_following_back, not_followed_by_you = find_differences(following, followers)

        # Save results to an HTML file
        save_results_to_html(not_following_back, not_followed_by_you)
        print("Done! result.html is ready")

if __name__ == "__main__":
    main()
