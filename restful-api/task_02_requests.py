#!/usr/bin/env python3

import requests
import csv


def fetch_and_print_posts():

    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code != 200:
        return
    else:
        print("Status Code: {}".format(r.status_code))
        data = r.json()
        for post in data:
            print(post['title'])


def fetch_and_save_posts():

    posts_list = []
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    if r.status_code != 200:
        return
    data = r.json()
    for i in data:
        posts_list.append({"id": i["id"],
                           "title": i["title"],
                           "body": i["body"]
                           })
    with open("posts.csv", "w") as p:
        fieldnames = ["id", "title", "body"]
        writer = csv.DictWriter(p, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(posts_list)
