# Default is show help; e.g.
#
#    make 
#
# prints the help text.   

SHELL     := bash
MAKEFLAGS += --warn-undefined-variables
.SILENT:
VPATH = .:..

LOUD = \033[1;34m##
HIGH = \033[1;33m#
SOFT = \033[0m#

Top=$(shell git rev-parse --show-toplevel)
Tmp ?= $(HOME)/tmp 

.PHONY: help

help: ## show help.
	@gawk '\
		BEGIN {FS = ":.*?##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nHelp:\n"} \
    /^[a-zA-Z_%\.\/-]+:.*?##/ {printf("  \033[36m%-15s\033[0m %s\n", $$1, $$2) | "sort" } \
	' $(MAKEFILE_LIST)

loc: ## REport loc
	cat bingo.py \
	| gawk '!/^#/ && !/^\f#/' \
	| gawk 'BEGIN {RS="";FS="\n"} /def eg_/ {next} {print $$0 "\n"}' |wc

pull: ## update from main
	git pull

push: ## commit to main
	echo -en "$(LOUD)Why this push? $(SOFT)" 
	read x ; git commit -am "$$x" ;  git push
	git status

sh: ## run my shell
	here="$(Top)" bash --init-file  $(Top)/etc/init.sh -i

lint: ## lint all python in this directory
	export PYTHONPATH="..:$$PYTHONPATH"; \
	pylint --disable=W0311,C0303,C0116,C0321,C0103 \
		     --disable=C0410,C0115,C3001,R0903,E1101,E1120,R1726 \
		     --disable=W0108,W0106,W0718,W0201,W0102,W0212,R1710  *.py

docs/%.html: %.py $(Top)/Makefile $(Top)/etc/head.html ## make doco: .py ==> .html
	cat $< | gawk '{gsub(/-------[-]*/,"\n#  \n#   \n\n"); print}' > $(Top)/docs/$<
	cd $(Top)/docs; docco -o .  $<; 
	rm $(Top)/docs/$<
	echo "pre { font-size: small;} h2 {border-top: 1px solid #CCC;}" >> $(Top)/docs/docco.css
	echo "p { text-align:right;}" >> $(Top)/docs/docco.css
	gawk '/<h1>/ {print "<div class=docs>";                       \
                while(getline x < "$(Top)/etc/head.html") {print x}; \
                print "<h1>'$<'</h1></div>";                  \
                next} 1' $@ > tmp.tmp
	mv tmp.tmp $@
	open $@

docs/%.pdf: %.py Makefile ## make doco: .py ==> .pdf
	echo "pdf-ing $@ ... "
	a2ps                  \
		-Br                  \
		--portrait            \
		--file-align=fill      \
		--line-numbers=1        \
		--pro=color              \
		--left-title=""           \
		--borders=no               \
	    --left-footer="$<  "      \
	    --right-footer="page %s. of %s#"  \
		--columns 2                          \
		-M letter                             \
		-o - $< | ps2pdf - $@
	open $@


# push:
# 	git add -A ../LICENSE.md *.md # Or more specific files
# 	git commit -m "docs: Update headers and license" # Or prompt for message
# 	git push

# # Redefine ONE and TWOPLUS for standard Markdown spacing (one blank line)
# ONE_CMD = awk 'BEGIN {RS=""; ORS="\n\n"} {print $$0; exit}' $<
# TWOPLUS_CMD = awk 'BEGIN {RS=""; ORS="\n\n"} NR > 1 {print $$0}' $@
# # Note: ORS="\n\n" means one paragraph, then two newlines (so one blank line follows)
#
# # Then in your rules:
# # ...
# @($(ONE_CMD); $(TWOPLUS_CMD)) > .tmp; mv .tmp $@
# # ...
