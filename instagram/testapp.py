from instapy import InstaPy

session = InstaPy(username="le_wiseman", password="************")
session.login()

session.like_by_tags(['love', 'gainwithmcharming'], amount=10)
#session.like_by_feed(amount=100, randomize=True, unfollow=True, interact=True)

session.set_do_follow(True, percentage=10)

session.set_do_comment(True, percentage=25)
session.set_comments(['lit', 'wow', u'lit 🔥'])

session.end()
