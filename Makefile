
.PHONY: run build install

run:
	bundle exec jekyll serve --livereload
build:
	JEKYLL_ENV=production bundle exec jekyll build

build_gh:
	JEKYLL_ENV=production bundle exec jekyll build --config "_config.yml,_config.gh.yml"