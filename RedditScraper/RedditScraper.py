import praw
import csv

# Initialize Reddit API
reddit = praw.Reddit(
    client_id='IpMzF_gs_btkR0hnQJTSMA',
    client_secret='KEivnh4jhpHEASFMBs9HS-Dh6VwQ2w',
    user_agent='horror_scraper by u/Maleficent-Eye-804'
)

# Target subreddit
subreddit_name = "nosleep"
subreddit = reddit.subreddit(subreddit_name)

# Set number of posts to fetch
post_limit = 20

# CSV setup
csv_filename = f"{subreddit_name}_posts.csv"
fields = ["Title", "Author", "Score", "URL", "Text"]

with open(csv_filename, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(fields)  # Write header

    for post in subreddit.top(limit=post_limit):
        # Skip stickied posts (like rules or pinned megathreads)
        if post.stickied:
            continue

        writer.writerow([
            post.title,
            str(post.author),
            post.score,
            post.url,
            post.selftext.replace('\n', ' ')
        ])

print(f"Saved {post_limit} posts from r/{subreddit_name} to {csv_filename}")
