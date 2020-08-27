from instapy import InstaPy

# Load user info from file
with open('.uinfo', 'r') as infile:
    username = infile.readline().strip()
    password = infile.readline().strip()

# Init session and login
session = InstaPy(username=username, password=password, headless_browser=True)
session.login()

# Load list of target users
userfile = open('target_accounts.txt', 'r')
userList = [line for line in userfile.readlines()]

# Like posts of target users
session.set_do_like(True, percentage=100)
num_recent_posts_to_like = 3 # Likes last 3 posts
session.interact_by_users(userList, amount=num_recent_posts_to_like, randomize=False)

# End session
session.end()