---
layout: default
---

Here's how to edit this website!

# Editing in Jekyll: The basics

Feel free to skip this section if you've already worked in Jekyll.

If anyone finds a good video explaining the basics of Jekyll please drop a link here!

This website is built in Jekyll. In order to edit it you should have at least some familiarity with basic HTML, CSS, and Liquid (https://shopify.github.io/liquid/basics/). HTML and CSS are used for web development. Liquid is a Jekyll specific syntax that helps create the site dynamically.

If you haven't worked with any of these programs before, read some basic descriptions of each language (some good intro to HTML/CSS links can be found in the lab wiki). Then, read this section. After that you should be able to follow the instructions on this readme and make the changes. But I also recommend following the instructions under "View changes locally/Troubleshooting" section and trying to play around with the code, making minor changes like changing an image, changing the color of an element, or anything else. This will give you a more intuitive sense of how the website works, which will help in case anything ever breaks.

This website is built in Jekyll rather than basic HTMl. If you've ever tried building a website using basic Jekyll you'll find that you have to copy and paste a lot of code—for example if you want the same menu bar at the top of the website, and you want the code for each website page to be written in separate html documents, you have to copy and paste the code for the menu in each of these separate documents. This can become quite inefficient and prone to error if you ever want to edit the contents of the menu items (because you would have to make the same edits in every html document)! Jekyll resolves this issue by dynamically building the website—meaning it takes code from different html files and combines it in any way you tell it to.

The basic framework is as follows. The html files that dictate how each of the pages looks like are stored in the _layouts folder. The base html file that all other files are based off of is default.html. All the other html files inherit the code from default.html, as specified by the header:
```
---
layout: default
---
```
The _layouts folder also contains html files for the other pages which specify the layout specific to that page. Home.html for the home page, publications.html for the publications page, etc. Open them to get a sense of their content. You'll notice that none of them actually have any content—just html and liquid code. This is where the structure of the Jekyll comes into play—all content is found in either markdown files (.md) in the root of the website or in the _data folder.

Non-repeating content found in markdown files is what is fed to the html files in order to populate the page with what will actually be printed. So for example, open the 00-index.md. You'll find content here specifying the image that should go on top (although technically that is an example of bad code as all html should be found in the home.html file and not in markdown...) and the text that will show up on the front page of the website. The header of this file looks like this:
```
---
layout: home
title: Home
permalink: index.html
---
```
Layout specifies which html file should be used as the layout format for this markdown content (i.e. home.html). Title specifies the title of the page (as it appears in the menu). Permalink creates an index.html file that will ultimately be printed on the webpage.

Repeating content is located in the _data folder in .yml (yaml) files. This is content that you want to repeat over and over again (for example entries on the publications page or people in the people page), but be populated using the same formatting. In order to do this, we give the information structure inside the yaml files, and then have the html files dynamically populate the same information for each entry (e.g. publication entry or person) using loops. That way each entry has the exact same layout, but the information differs. The markdown files associated with this type of data are empty, because there is no non-repeating information on these pages. If you wanted to add, for example, some kind of paragraph at the beginning of the people page, you would add this paragraph in the people.md file.


The repeating information is organized in yaml in a list format. A "-" symbol indicates a new entry. Every entry has information specified with keys and values in a new line  as [key]: [value] (e.g. name: Judith). Indentations in yaml files matter. If an entry is double indented (two tabs), it is nestled under the entry with only one tab (and so forth). The liquid for loops in the .html files iterate through all entries that are on the same level (have the same indentation). In order to enter a deeper level (e.g. go from iterating through entries with one tab to iterating through entries with two tabs) you can nestle a for loop in another for loop. Examples of this can be found in people.html and publications.html (the for loops are commented with what they are doing).   

In summary:
- .html = specifiying layout of of the page
- .md = specifying content that does not repeat
- .yml = specifying content that does repeat

This website code has been worked on by several people. Not all of it is well commented and you will find lots of legacy code that does nothing/parts of the code that are messy. While you are working on the website, please keep this in mind and try to comment/clean messy code/delete delete obsolete code as much as you can (always documenting your changes on git!).


# People Section
## Add a person to the website
You need:
- The person's name
- The person's personal website (optional)
- The person's photo
- The person's bio

1. Add the person's photo into the images/members folder and name it 'NAME.jpg'
2. Add the person's information to _data/alpslab.yml following the formatting shown there. Be sure to follow the formatting precisely, as missing spaces/incorrect line breaks may break the website. Add the person in the correct section (Graduate students, Masters Students, etc.)
3. Follow instructions under "publish changes"

## Change Lab member to Lab Alumni
1. Navigate to _data/alpslab.yml
2. Find their data entry, copy it, then delete it
3. Re-add their data entry to the "Lab Alumni" section, including only their name, webpage (if they have one), and image.
4. Follow instructions under "publish changes"

## Change the heading picture
You need:
- the new lab image

1. Go to images/ and rename the current 'lab_members.jpg' to 'lab_members[year photo was taken].jpg'.
2. Add your new image in this folder and name it 'lab_members.jpg'
3. Follow instructions under "publish changes"

# Publications

## Naming Nomenclature

Bibtex entry keys and pdf names should be identical in order to link the [preprint] button with the pdf. The bib.bib file is ordered chronolocially with "submitted" and "to appear" articles at the bottom.

The bib entry key and pdf name nomenclature used is: [year][AuthorLastName]
- use CamelCase
- Use the last names of the first two authors, if there are more than two append the string "EtAl" to the name
- if there are multiple articles from the same years and same authors, append the second article name with "B", the third with "C", etc.
- For "to appear" articles add the string "ToAppear" before the author last names
- For "submitted" articles add the string "Submitted" before the author last names

None of the keys use underscores in order to avoid parsing issues with certain programs which would interprate them as subscripts.

Please keep the bib.bib file organized, otherwise mistakes/missing information is harder to find!

## Add a publication entry
You need:
- the metadata of the publication
- to have the following things installed locally:
	- python
	- pyyaml (https://pyyaml.org/) (install it by running 'pip install pyyaml' in terminal)
	- bibtexparser (https://bibtexparser.readthedocs.io/en/master/) (install it by running 'pip install bibtexparser' in terminal)

1. Go to _data/bib.bib and add the new publication as a normal bibtex entry
2. Run the bib_to_yml.py python script found in _data/ locally. You can do so by navigating to the _data folder in the terminal and typing the command "python bib_to_yml.py"
3. Follow instructions under "publish changes"

Furter Notes:

Step (1): If the publication is not yet published, instead of including a year, write "to appear" (if its a manuscript that has been accepted already) or "submitted" (if its a manuscript that has been submitted but not yet accepted). In the Publication section, the "Pending", "To Appear", and "Submitted" headers will automatically appear if there is an entry in the bibtex where the year is set to "to appear" or "submitted".

Step (2): We want to have a bibtex file with all the bib entries of our bibliography. However, the website only knows how to interface with yaml files, not bibtex files. So the python script takes everything in the bibtex file and converts it to a yaml file that the website can then parse. On the Publications page there is a [bibtex] button which shows the bibtex entry. This button doesn't actually reference the bib.bib file but rather takes the information from the yaml and converts it to text which is formatted like a bibtex entry. (Technically, this means that the information about each paper in the bib.bib file can be in any order, as this script orders the information in a standardized way. But, again, try to stay organized when editing the bib.bib file or adding a new publication!).

## Change publication information
Do this if you found a mistake/missing link of a publication already published to the website, or if a publication has been published and needs to be moved from the "to appear" or "submitted" sections.

# View changes locally/Troubleshooting
You need:
- Install Jekyll locally

1. Navigate to the root of the ALPS website folder using terminal and execute command "bundle exec jekyll serve" (or "jekyll serve")
2. You will see an output that looks like this:
```
Configuration file: /Users/stefan/Desktop/repos/ALPS_website/_config.yml
            Source: /Users/stefan/Desktop/repos/ALPS_website
       Destination: /Users/stefan/Desktop/repos/ALPS_website/_site
 Incremental build: disabled. Enable with --incremental
      Generating...
       Jekyll Feed: Generating feed for posts
                    done in 0.536 seconds.
 Auto-regeneration: enabled for '/Users/stefan/Desktop/repos/ALPS_website'
    Server address: http://127.0.0.1:4000
  Server running... press ctrl-c to stop.
```
3. Copy the "server address" and paste it as a URL in your browser. This will take you to a local version of the website. Note that this is not accessible to anyone except you, so feel free to make any changes. The changes will only become visible when you push them to the github repo.

If in step (2) you do not see the above input, but an error message, this means that there was an error compiling your code. These are usually syntax errors. The messages that pop up in terminal are helpful in locating the syntax error.

If you make local changes with the website open locally on your browser, just hit save and the changes should automatically be reflected in your local browser. The fact that you saved the document will be reflected in the terminal in which you typed "jekyll serve". The terminal will also show you error messages that come up as you are editing the website. Be aware that if you make a change that is fatal to the website (e.g. a syntax error), terminal will show you a red message letting you know that this error message will keep the site from working, but the locally running website will not reflect that change (or any future changes until you fix the fatal error).

Final word of warning: the website that you see on the webpage is already compiled and entirely the output product of the jekyll framework, meaning it does not have access to the individual .html/.md/.yml files found in this repo nor does it have any access to the liquid syntax. So none of the that code will be visible in the web browser developer tools. In order to find and fix bugs, you have to use the terminal and the repo code and can't solely rely on the (locally running) webpage.

# Publish Changes
1. Commit + Add + Push changes to the github repo
2. Check that the changes were succesfully rendered on gitpages in the github repo
3. ??? ANything else, To be seen

# OLD STUFF
The rest is legacy documentation from when the website was published using the Stanford AFS servers (the original place where the website was hosted). It may prove useful while troubleshooting.

## Overview

1. Make changes and push to github (make sure you have collaborator privilages, and see later sections for details on specific kinds of changes)
2. Go to `/afs/ir.stanford.edu/group/alpslab/alpslab.stanford.edu` and pull your changes

		ssh [SUNetID]@cardinal.stanford.edu
		cd /afs/ir.stanford.edu/group/alpslab/alpslab.stanford.edu
		git pull

	There's a script on the server that makes the changes live after a successful merge.

## Specific kinds of changes

### How to add a new page to the website

1. make a markdown file, e.g. `new-file.md` in the top of the `alpslab.stanford.edu` directory

2. add this to the top of the markdown file:

		---
		layout: default
		---

3. if you want this page to appear in the navbar, add another value to the header:

		---
		layout: default
		title: New Page
		---

4. visit `alpslab.stanford.edu/new-page.html`.

### How to add a new entry to the "News" section

1. make a markdown file in the \_posts folder. give it a name according to these conventions: yyyy-mm-dd-title.md

2. give it a header of the following form:

		---
		layout: post
		title:  "YOUR TITLE"
		date:   2018-03-03 16:16:01 -0600 [your date/time goes here]
		categories: [a couple relevant tags]
		---

3. Write the body of your post below the header.

### How to add a person to the website

1. go to the file `_data/alpslab.yml`

2. find (or add) whatever role they play in the lab (e.g. Principal Investigator, Graduate Student, Alumni), and add a new person to that role.

		- role: [WHATEVER ROLE]
		  people:
		    - [OTHER PEOPLE]
		    - name: New Person
		      img: newPerson.jpg
		      webpage: //www.stanford.edu/~newP
		      bio:
		        - >
		          A paragraph of this person's bio.
		        - >
		          Another paragraph of this person's bio.
		    - [OTHER PEOPLE]

### How to add a publication to the website

1. go to the file `_bibliography/alpslab.bib` and add the publication.

If the publication is not appearing once you publish it to the website, this could be because of:
1. A typo in the alpslab.bib file. Make sure all the commas are in the right places!
2. You haven't published anything for this year yet and don't have the year header set up.

If (2) is the case, navigate to _config.yml at the root of the directory. Change line 12 as follows

`max_year: *insert new year*`

Then navigate to 02-publications.md at the root of the directory. Change line 18 as follows:

`...for year in (2011..*insert new year*)...`

### How to add an image to the front page carousel

1. got to the file `_data/carousel.yml`

2. add a new image to the end of the file

		- [OTHER IMAGES]
		- image: my-new-image.jpg
		  label: "A description of my new image"
		  alt: "if you want, you can add a line of alt text. otherwise, the label will be the alt text."


## Troubleshooting

If the website does not update within a minute or so of making these changes, this might be because the build script has stopped working. Run

	jekyll build
	rsync -r -a -v _site/* ../WWW/

in a terminal on the Stanford server in the `/afs/ir.stanford.edu/group/alpslab/alpslab.stanford.edu` directory.

### Setup

As of 9/25/2018, the website can be updated provided one has Ruby 2.5.1, Jekyll 3.8.4, Jekyll-Scholar 5.1.4, and Redcarpet 3.4.0 (back compatibility with earlier versions of the aforementioned software is possible but not guaranteed). Your Cardinal account comes with versions of Ruby and Jekyll that are incompatible with the website. First, update Ruby via rbenv:

```
# get rbenv
git clone https://github.com/sstephenson/rbenv.git ~/.rbenv

echo 'export PATH="$HOME/.rbenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(rbenv init -)"' >> ~/.bashrc
# run the updated .bashrc
source ~/.bashrc
# fetch the ruby-build installer plugin to make things easier
git clone https://github.com/sstephenson/ruby-build.git ~/.rbenv/plugins/ruby-build
# download Ruby 2.5.1. this will take some time.
rbenv install 2.5.1
# set your system's default ruby to 2.5.1
rbenv global 2.5.1
```

Next, get fresh Jekyll, and install Jekyll-Scholar and Redcarpet:

```
gem install redcarpet -v 3.4.0
gem install jekyll -v 3.8.4
gem install jekyll-scholar -v 5.14.0
```

Lastly, ensure that local encoding is set to UTF-8:

```
export LANG=en_US.UTF-8
export LANGUAGE=en_US.UTF-8
export LC_ALL=en_US.UTF-8
```

Note that while `jekyll` is compatible with [GitHub pages](https://help.github.com/articles/using-jekyll-as-a-static-site-generator-with-github-pages/), [`jekyll-scholar` is not](https://github.com/inukshuk/jekyll-scholar#github-pages).

For local debugging, one could run

```
jekyll build
```

and then navigate to `_site/index.html`.

<!-- Unfortunately, the links in this repo are currently hard-coded with the assumption that all files are present at the host (in the online version, `http://cocolab.stanford.edu/`, in the local version `file://`), so further abstraction and modifications would have to be made in order to actually navigate the site locally... --->
