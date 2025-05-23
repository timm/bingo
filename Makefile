# Default is show help; e.g.
#
#    make 
#
# prints the help text.   

SHELL     := bash
MAKEFLAGS += --warn-undefined-variables
.SILENT:

LOUD = \033[1;34m##
HIGH = \033[1;33m#
SOFT = \033[0m#

Top=$(shell git rev-parse --show-toplevel)
Tmp  ?= $(HOME)/tmp 

.PHONY: help

help: ## Show this help.
	@gawk '\
		BEGIN {FS = ":.*?##"; printf "\nUsage:\n  make \033[36m<target>\033[0m\n\nHelp:\n"} \
    /^[a-zA-Z_-]+:.*?##/ {printf "  \033[36m%-25s\033[0m %s\n", $$1, $$2 } \
	' $(MAKEFILE_LIST)
	
pull: ## update from main
	git pull

push: ## commit to main
	echo -en "$(LOUD)Why this push? $(SOFT)" 
	read x ; git commit -am "$$x" ;  git push
	git status

sh: ## run my shell
	here="$(Top)" bash --init-file  $(Top)/etc/init.sh -i

nvimcolors:
	mkdir -p ~/.config/nvim/pack/plugins/start/
	git clone https://github.com/catppuccin/nvim.git ~/.config/nvim/pack/plugins/start/catppuccin

lint: ## lint all python in this directory
	export PYTHONPATH="..:$$PYTHONPATH"; \
	pylint --disable=W0311,C0303,C0116,C0321,C0103 \
		    --disable=C0410,C0115,C3001,R0903,E1101 \
		    --disable=E701,W0108,W0106,W0718,W0201   bingo.py

docs/%.html : %.py
	docco -o docs  $^
	echo "pre { font-size: small;} p { text-align:right; }" >> docs/docco.css
	gawk '/<h1>/ {print "<div class=docs>";                       \
                while(getline x < "etc/head.html") {print x}; \
                print "<h1>'$^'</h1></div>";                  \
                next} 1' $@ > tmp.tmp
	mv tmp.tmp $@

~/docs/%.pdf: %.py  ## make doco: .py ==> .pdf
	echo "pdf-ing $@ ... "
	a2ps                 \
		-Br                 \
		--chars-per-line=90 \
		--file-align=fill      \
		--line-numbers=1        \
		--pro=color               \
		--left-title=""            \
		--borders=no             \
	    --left-footer="$<  "               \
	    --right-footer="page %s. of %s#"               \
		--columns 3                 \
		-M letter                     \
		-o - $< | ps2pdf - $@
	open $@
