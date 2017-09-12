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

test:
	@echo "This is a test!\n"

refresh:
	@echo "Updating repo from GitHub..."
	git pull

	@echo "Deleting all posts..."
	rm -r _posts/*

	@echo "Generating posts..."
	tools/generate_posts.py

	@echo "Adding any new posts to git..."
	git add _posts/*

	@echo "Committing changes..."
	git commit -a -m 'Refreshed links from Pinboard.'

	@echo "Pushing to GitHub..."
	git push

	@echo "Done."