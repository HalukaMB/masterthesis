This is the CorEA corpus v1.

the data is property of corrieredellasera and university of trento.
DO NOT redistribute the data.

the corpus contains 2 tab-separated files:

-CorEA-message-level.csv
-CorEA-sentence-level.csv

the message level contains the following fields:

0Mid		message id
1Pid		participant id
2Pname		participant name
3type		message type (article/comment)
4under		id of the article under which is the comment 
5manual-topics		set of topics manually annotated
6text		message text
7timestamp		message timestamp
8category		news category of the article
9refer-to-Pname	reply to (by participant name)
10refer-to-M		reply to (by message id)
11avatar		url of the participant profile picture (most use a default one)
12replies-count	count of replies to the message
13likes		count of message likes
14agree-disagree	agree (1), disagree (-1), neutral (0), not applicable (NA)
15Pday_activity	participant's activity score
16Pinterests		participant's interests
17Ptotal_views		participant's page views
18Ptotal_comments	participant's total comments
19Ptotal_shares	participant's total shares
20Ptotal_comments_votes	participant's likes received
21Emo_indig		overall emotion declared by the participant after reading articles
22Emo_disapp		overall emotion declared by the participant after reading articles
23Emo_worried		overall emotion declared by the participant after reading articles
24Emo_amused		overall emotion declared by the participant after reading articles
25Emo_satisfied	overall emotion declared by the participant after reading articles
26_APIobjectID		not used
27_title		article title
28_externalID		not used


the sentence level contains the following fields:

Sentence 1 M-ID	sentence 1 id
Sentence 1 text	sentence 1 text
Sentence 2 M-ID	sentence 2 id
Sentence 2 text	sentence 2 text
Annotated Topic	automatically extracted topics (used for pairing sentences)
Agreement		agree (1), disagree (-1), neutral (0), not applicable (NA)
Start milliseconds	start time of the annotation
End milliseconds	end time of the annotation
Annotator		annotator id
Notes		annotator's free notes
Original Topics	original topics
Tags		tags 
Merged Tags		tags from the message level



please refer and cite the works attached to the corpus:


@inproceedings{celli2014corea,
  title={CorEA: Italian News Corpus with Emotions and Agreement.},
  author={Celli, Fabio and Riccardi, Giuseppe and Ghosh, Arindam},
  booktitle={CLIC-it 2014},
  pages={98--102},
  year={2014}
}




