# cautious-invention
A foolish application for browsing articles and commenting on them.

```
git clone https://github.com/mishalbishal/cautious-invention
cd cautious-invention
docker-compose up
```

Configuration settings
======================

*ARTICLES_COMMENT_MODERATION_ANONYMOUS* defaults to False. Setting this to true would require
moderation for all non-logged in users. I kept it as False so that it would be easier to test
when reviewing the implementation.

Thoughts
========

The git history and chat history should have more details on my development process.
My first step was getting a "working" site with the provided data and then configuring the
commenting system. The content_api.json dump is quite complicated and I was originally
thinking of storing the documents in something like mongodb so that I could have document
search without having to worry about the schema. I went with a simpler solution of just
loading from a file.
I decided to add database support for the articles as a way of showing familiarity with
Django's ORM, and incorporating third-party applications. Below are some additional features
that I would have liked to work on.

Improvements
============

* Make a more robust front-end.
  * Add image fallback: currently, quotes images have the fool placeholder image in some cases. 
  * Default views when relevant articles don't exist. For example, if a featured article doesn't exist should
    have a fallback or make some strategy to prevent issues on the mainpage.
  * Have a less hardcoded way of setting the featured article. Possibly something like having a "featured"
    table that gets curated and the latest item in that table is shown on the homepage.
  * Add testing using selenium to test rendered html.
* Implement captcha for preventing spam bots.
* Have the article page be static with Javascript that dynamically loads the comment form.
  This allows for caching of the page either via django's caching or an http accelerator like Varnish,
  but loads the comment form (and associated security features like a csrf token) when a user goes to make a comment.
* Increase database guarantees. I used blank=True for many fields because it made it easier to
  develop quickly. But I would have liked to have stronger guarantees.
* Develop the admin site to support a WYSIWYG editor for writing articles.
* Configure docker
  * Use docker conventions (using an unprivilaged user instead of root)
  * Allow easy access to manage.py commands. Currently, I just 'docker exec -it container bash'
    and then ran whatever commands I needed.