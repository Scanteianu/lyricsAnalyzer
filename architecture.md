# LyricsTheme Architecture

## Purpose

LyricsTheme aims to identify thematic elements within the lyrics of various musical artists. 

Thematic elements:
- Niche topics: things that this artist talks about the most, compared to other artists (unique themes)
- Main topics - things that this artist talks about the most overall (even if other artists also discuss the same subjects) (top themes)

Other takeaways - which artist has the biggest vocabulary? What is the average vocabulary size of a rock band's lyrics?
What words are unique to the artist?
## Approach

As a first cut, a naive tfidf is done - each artist is considered to be a document, the more a term occurs in each artist's lyrics, and the fewer times it appears in a different 

## Data Layout
Input is provided within the lyrics directory. The lyrics directory is expected to have subdirectories for each artist. Within each subdirectory, a separate text file (utf-8 encoded) is expected for each separate song.

## Data Processing pipeline

First, the lyrics for each artist are taken and collected into one document. cases are normalized, special characters are removed

Then, as an optional step, we can try to stem the words in order to eliminate plurals/different verb conjugations/etc

then, a mapping is constructed per artist for each term and the number of times it occurs in the artist's vocabulary

afterwards, for all words, a mapping is constructed between each word globally and the number of artists' songs it appears in (the artist's most unique themes).

Finally, the top tfidf terms for each artist are displayed along with scores. Top term frequency words can also be displayed, perhaps with stopwords removed (the artist's top themes)

After this is done, the top themes and top unique themes can possibly be clustered to get higher level artist interests and topics

Words with a high inverse document frequency (or unique to the artist only) can also be displayed. These are subjects on which the artist has monopoly, even if they only fleetingly discussed the subject.
