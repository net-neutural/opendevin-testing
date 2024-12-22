#!/bin/bash

# Fetch the Hacker News homepage HTML.
curl -s https://news.ycombinator.com > /workspace/hn.html

# Extract the title of the top story.
title=$(grep -o '<span class="rank">1.</span>.*<a href=".*" class="titlelink">.*<\/a>' /workspace/hn.html | grep -o '<a href=".*" class="titlelink">.*<\/a>' | sed -e 's/<a href=".*" class="titlelink">//; s/<\/a>//')

# Display the extracted information.
echo "Title: $title"