
.PHONY: run build install

run:
	bundle exec jekyll serve --livereload
build:
	JEKYLL_ENV=production bundle exec jekyll build