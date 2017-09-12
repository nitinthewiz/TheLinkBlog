#J=bundle exec jekyll
J=jekyll

all: site

site: clean
	$J build #--lsi
	chmod -R a+rx ./_site/

clean:
	rm -rf _site/

local_all:
	$J serve --watch --drafts

local:
	$J serve --watch --drafts --limit_posts 100

refresh:
	@echo "Updating repo from GitHub..."
	git pull

	@echo "\nDeleting all posts..."
	rm -r _posts/*

	@echo "\nGenerating posts..."
	tools/generate_posts.py

	@echo "\nAdding any new posts to git..."
	git add _posts/*

	@echo "\nCommitting changes..."
	git commit -a -S -m 'Refreshed links from Pinboard.'

	@echo "\nPushing to GitHub..."
	git push

	@echo "\nDone."