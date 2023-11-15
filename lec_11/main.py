import requests

base_url = "https://jsonplaceholder.typicode.com/"

fetched_posts_response = requests.get(f"{base_url}/posts")

if fetched_posts_response.status_code == 200:
    posts = fetched_posts_response.json()

    filtered_titles = []
    for post in posts:
        if len(post['title'].split()) <= 6:
            filtered_titles.append(post['title'])

    print("Titles with less than or equal to 6 words:")

    for title in filtered_titles:
        print(title)

    filtered_posts = []

    for post in posts:
        if len(post['body'].split('\n')) <= 3:
            filtered_posts.append(post)

    print("\nPosts with body containing 3 or fewer lines:")
    for post in filtered_posts:
        print(f"\nTitle: {post['title']}")
        print(f"Body:\n{post['body']}")
else:
    print("Failed to fetch posts.")

my_new_post = {"title": "My Title", "body": "Some text"}
create_post_response = requests.post(f"{base_url}/posts", json=my_new_post)

if create_post_response.status_code == 201:
    my_new_post_id = create_post_response.json()['id']
    print(f"ID of my_new_post: {my_new_post_id}")

my_updated_post = {"title": "Updated title", "body": "Some updated text"}
update_post_response = requests.put(f"{base_url}/posts/{my_new_post_id}", json=my_updated_post)

if update_post_response.status_code == 200:
    print("The post my_new_post updated successfully")

delete_post_response = requests.delete(f"{base_url}/posts/{my_new_post_id}")
if delete_post_response.status_code == 200:
    print("The post my_new_post deleted successfully")

