
.PHONY: run build install

run:
	bundle exec jekyll serve --livereload
build:
	JEKYLL_ENV=production bundle exec jekyll build

build_gh:
	JEKYLL_ENV=production bundle exec jekyll build --config "_config.yml,_config.gh.yml"

build_archive:
	JEKYLL_ENV=production bundle exec jekyll build --config "_config.yml,_config.gh.yml,_config.archive.yml"

archive: build_archive
	zip -r site.zip _site/