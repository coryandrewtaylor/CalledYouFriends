# "I Have Called You Friends": Social Networks and Characterization in the Gospels

## Topic {#topic}

My dissertation uses social network analysis \(SNA\) to situate the New Testament Gospels within the context of other Greco-Roman biographies—works to which, Burridge has shown, the Gospels bear a “family resemblance” \(Burridge 2004, 37–43 _et passim_\). I examine the characterization in the four canonical Gospels, as well as Burridge’s sample of “later Graeco-Roman _bioi_” \(viz. Tacitus’ _Agricola_, Plutarch’s _Cato Minor_, Lucian’s _Demonax_, Philostratus’ _Apollonius of Tyana_, and Suetonius’ _Lives of the Caesars_\). More broadly, my goal is twofold: to propose new methods for the interpretation of the Gospels through an innovative “distant reading” \(Moretti 2013\) strategy for the analysis of literary characters and to make a contribution to the field of digital humanities by suggesting new ways of applying social network analysis to the study of literature.

The bulk of the dissertation will be devoted to testing current ideas about characterization in the Gospels and developing a theory of character that takes into account characters’ structural roles in each of the Gospels. As Bennema \(2014\) notes, very little work has been done to create a theory of character that applies to all four Gospels. This dissertation will fill that gap by 1\) measuring characters’ degree and centrality \(which are standard network measurements, well established in the literature\) to quantify characters’ plot functions, and 2\) developing a set of criteria that determine where a character falls on the spectrum/a of characterization. I will nuance that portrait by performing experiments on the networks to uncover circumstances under which a character’s role might change. Throughout, I will compare characterization in the Gospels and Burridge’s corpus, in order to expand my theory of character to Greco-Roman biography in general. The dissertation will conclude with an exploration of the Gospels’ genre. The genre of the Gospels is still largely an open question; however, as Ardanuy and Sporleder \(2014\) have recently shown, social networks are useful for classifying works according to genre. Incorporating my data on characters’ structural roles with additional measures of network structure \(e.g., small-world-ness and assortativity\), I test how far the Gospels’ resemblance to other biographies extends: whether it is primarily at the syntactic level, as in Burridge’s work, or if it also includes the structures of the works’ plots.

This dissertation will be an important contribution to New Testament Studies in several ways. For one, it is the first monograph-length network analysis—a methodology that has yielded concrete interpretive insights into other texts—of the Gospels. Second, because SNA provides a rigorous means of testing existing theories and developing new hypotheses, my dissertation will contribute to ongoing scholarly conversations about characterization in the Gospels, showing that plot function is a good index of a character’s role, but that it is insufficient simply to position characters along a continuum between minority and majority. Third, it will help to answer the longstanding question about the Gospels’ genre, which has been a matter of debate for decades.

## State of the Question {#state-of-the-question}

### Social Network Analysis of the New Testament {#social-network-analysis-of-the-new-testament}

Social network analysis has long been a productive methodology in NT studies, especially in Pauline studies. Chow’s _Patronage and Power_ \(1992\), which uses SNA to study the power relations in the church at Corinth, is seminal. Malina and Pilch’s _Social-Science Commentary on the Letters of Paul_ \(2006\) also uses SNA throughout, though social networks are not the main focus of the work. In addition, Malina has edited a series of monographs covering individual members of Paul’s social network.

Given how useful SNA has been to scholars of Paul, it is somewhat surprising that more Gospels scholars have not adopted it. As with Malina and Pilch’s commentary on Paul, Malina and Rohrbaugh have used SNA in their _Social-Science Commentaries_ on the Synoptic Gospels \(Malina and Rohrbaugh 2003\) and on John \(Malina and Rohrbaugh 1998\), though their analysis focuses exclusively on the “gossip network” surrounding Jesus. In addition, Duling has read his reconstruction of the historical Jesus movement through a network-analytical lens in a series of articles \(Duling 1999; Duling 2000; reprinted together as Duling 2002\). However, his argument treats SNA as a theory in itself, rather than—as has long been acknowledged in sociological network analysis—a means of testing and producing theories. Finally, Miyake has studied the Gospels’ networks in several presentations at Digital Humanities conferences \(Miyake 2007; Miyake 2008; Miyake 2009; Akama, Miyake, and Jung 2011\); however, her work focuses primarily on the semantic networks of NT Greek, with social networks only as a secondary emphasis. In all, no sustained analysis has been performed on the social networks of literary characters in the Gospels, leaving a sizeable gap that this dissertation hopes to fill.

### Literary Social Network Analysis {#literary-social-network-analysis}

This project will engage with other fields beyond the highly specialized work in Gospels SNA, namely literary SNA \(including computer science fields such as natural language processing \[NLP\]\) and narrative criticism of the Gospels. Literary SNA is an active field, with many important works being published in the past decade. Moretti’s work has been especially important. He uses network analysis for book history in his _Graphs, Maps, Trees_ \(Moretti 2005\) and for literary criticism in his article/pamphlet “Network Theory, Plot Analysis” \(Moretti 2011a; expanded and republished as Moretti 2011b\); in the latter, he uses graph analysis to study the plots of _Hamlet_, _Our Mutual Friend_, and _The Story of the Stone_. Though Moretti was far from the first author to incorporate SNA into literary studies, he brought the methodology into the mainstream, tying it to his broader approach of distant reading.

Researchers at Columbia University have also been prolific in this area. Elson, Dames, and McKeown \(2010\) is particularly influential, due to the paper’s conclusions: the authors use social networks to disprove a longstanding theory about characterization in nineteenth-century novels set in rural, as opposed to urban, areas. More recently, Columbia-school SNA has focused on creating standalone tools for building and/or studying literary social networks \(for instance, `Scheherezade` \(Elson 2012\) and `SINNET` \(Agarwal et al. 2013\)\). The Columbia-school approach contrasts well with Moretti’s. Though Moretti manually draws the graphs in “Network Theory, Plot Analysis” and avoids the “stern adulthood of statistics” \(Moretti 2011b, 3\), his hand-crafted networks contain all the characters from the works he studies. The Columbia scholars, on the other hand, rely on automatic network extraction; as such, their analyses, while very powerful, suffer from incomplete data, due to the sheer difficulty of detecting unnamed characters \(Vala et al. 2015\). Elson, Dames, and McKeown’s approach, for example, only detected 51% of the speech in the books they examined \(though, among the speech it did detect, it attributed quotes to the correct characters 95% of the time\). My approach will strike a balance between the two extremes: initially, I will build the networks automatically, using a machine learning algorithm that I have developed to detect unnamed characters, but—because much of my focus will be on minor characters, which are predominantly unnamed—I will revise the networks by hand to ensure that they are complete.

### Characterization in the Gospels {#characterization-in-the-gospels}

Narrative criticism of the Gospels, and especially the study of characterization in them, is likewise thriving. Skinner and Bennema are the major recent scholars of Gospels characterization. Skinner’s revised dissertation \(Skinner 2009\) argues that many of John’s characters have imperfect faith in Jesus, as compared with the ideal faith set forth in John’s prologue \(Jn 1:1–18\). On that basis, he argues against Riley’s, DeConick’s, and Pagels’ views that John’s portrayal of Thomas was a polemic against a Gnostic community responsible for the Gospel of Thomas. Skinner has also edited or co-edited several important books on Markan and Johannine characterization \(Iverson and Skinner 2011; Skinner 2013; Hauge and Skinner 2014\).

Most of Bennema’s work \(e.g. Bennema 2009a; Bennema 2009b; Bennema 2013\) has been on John, with an emphasis on comparing Johannine characterization to other literature and attempting to quantify, by means of a rubric, where a given character falls on the spectrum between majority and minority. His most recent book \(Bennema 2014\) applies that same method to characters in Mark, John, and Acts, in order to develop a unified theory of characterization in NT narrative—the only work thus far with this goal.

In addition, many scholars have studied the minor characters in the Gospels \(for instance Williams 1994; Malbon 2000; Conway 2002; Howard 2006; Hylen 2009\). The most comprehensive approach, however, is Hunt, Tolmie, and Zimmermann \(2013\), which brings together studies of 70 characters in John. Their work stands in contrast to the rest of the literature, which tends to study either a single character \(as in Burnett \(1993\), which looks at Peter\) or a handful of characters \(as in the second half of Skinner \(2013\), which comprises chapters on eight characters in John\).

Bakhtinian theory \(part of the theoretical backbone of my dissertation; see below\) has also periodically made an appearance in studies of the Gospels’ characterization. The most relevant studies are McCracken \(1993\), which brings Bakhtin’s theory of interindividuality together with “the Kierkegaardian paradigm of self” \(McCracken 1993, 34\) to create a theory of the relationships between biblical characters; Barnet \(2003\) and Sung \(2008\), both of which examine characters’ roles in Matthew using Bakhtin’s aesthetics; and Webb \(2008\), which examines several Markan passages in light of Bakhtin’s concepts of dialogue, genre-memory, chronotopes, and carnivalesque.

## Theoretical Influences {#theoretical-influences}

My dissertation mainly relies on formalist theory. The most obvious connection is with the quantitative formalism espoused by the members of the Stanford Literary Lab and its alumni—especially Allison et al. \(2011\) and Moretti \(2011b\). In addition, I use formalist categories that lend themselves to interpreting social networks, namely Bakhtin’s \(Bakhtin 1982\) interindividuality and the longstanding formalist distinction between story and discourse—what Woloch describes as the contrast between “the fictional events that we reconstruct through the narrative” and “the narrative’s actual language and structure” \(Woloch 2003, 38\). Methodologically, I blend various approaches to social network analysis. Where much of the literature uses either co-occurrence or dialogue networks as the basis for analysis, I use both. In addition, I combine automatic network extraction—which reigns supreme in the computer science approaches to SNA—with manual network production, in order to ensure that all characters, both named and unnamed, are represented adequately.

Theory and method will be tightly intertwined in my dissertation. For instance, I take co-occurrence and dialogue networks, with the different information they encode, as a manifestation of story and discourse, respectively. Co-occurrence networks place links between all the characters who are present at an event; thus, it is straightforward to take them as the text’s story. In addition, I recast _discourse_ as “the words spoken by the characters in a text.” Following this redefinition, it is easy to use dialogue networks—which show the characters that speak to each other—as an abstraction of a work’s discourse.

This juxtaposition has already proven useful. In my research on Luke, I found that several kinds of minor and intermediate characters exist in that Gospel’s story, while the discourse is sharply divided between Jesus and a host of minor characters \(namely, every other speaking character in the book\). Moreover, after removing Jesus from the networks, the dialogue network dissolves significantly, as expected, while the co-occurrence network \(more specifically, the relationships between Jesus’ disciples and the book’s minor characters\) coheres. Extrapolating back to the text itself, a Jesus-less Luke tells the story of a beleaguered group of people who follow an itinerant, miracle-working preacher, who disperse when their leader is executed by political and religious authorities, but who come back together when they hear rumors of their leader’s resurrection. In other words, without Jesus, Luke’s story remains very nearly the same—suggesting that the disciples might be a class unto themselves: minor in terms of discourse, but major for the story. I will test this finding to determine whether it generalizes to the other works in my study.

As mentioned above, my dissertation will also extend current applications of Bakhtin’s thought to biblical characterization \(primarily McCracken \(1993\) and Webb \(2008\)\). Bakhtin’s notion that characters exist as a set of interactions between “character zones” applies directly to social networks, which are, at base, a set of relationships between nodes. SNA, I argue, thus provides a rigorous way to explore how a character’s majority or minority relates to their plot function. Take centrality and degree, for example: if a character has a high eigenvector centrality and high degree—that is, if that character’s node is connected to many other important nodes—it is intuitive that s/he will be a major character. On the other hand, a character with a high betweenness centrality, even if s/he has a low degree, will be an important link between different groups of characters; likewise, a high closeness centrality will indicate that a character is essential to the cohesion of a community within the text, even if s/he does not play a central role in the narrative.

Despite formalism’s prominence in my dissertation, I am sympathetic to critiques of it, especially that it is reductive \(as in de Man 1971, pp.; de Man 1973\) and that it relies on a fallacious understanding of the nature of data \(Drucker 2014\). Literary SNA certainly is reductive. However, reductiveness does not invalidate SNA as a methodology; rather, it simply indicates that SNA should be folded into the larger critical enterprise, so that it may benefit, and benefit from, other areas of criticism. Likewise, I acknowledge that my collecting and analyzing data is fundamentally an interpretive act, not a study of the objective nature of the text. As Drucker insists, “data are capta, taken not given, constructed as an interpretation of the phenomenal world, not inherent in it” \(Drucker 2014, 128, emphasis original\).

Finally, in addition to formalist literary theory, I will build heavily on quantitative and comparative approaches to the Gospels. Like Bennema \(2009a\), I will situate the Gospels’ characterization among other ancient works. And, in the same way that Bennema uses his \(quasi-quantitative\) continua of characterization, assigning scores to characters based on their “complexity,” “development,” and “inner life” \(Bennema 2009a; Bennema 2013\), I will use network measures to determine whether a character is major, minor, or somewhere in between. However, where Bennema collapses his continua into a single spectrum, I allow for the possibility that characters may be major in some ways but minor in others, and that those circumstances may not be reflected directly in the narrative. Moreover, unlike Bennema, who relies on close reading to classify his characters, my interpretation depends on distant reading. In this way, my approach is more like Burridge’s \(2004\) now classic study of Gospel genre, in fact a work of “proto-DH,” which studies patterns of structure and syntax instead of narratives proper.

## Methodology {#methodology}

No consensus exists yet on the best way to extract social networks from unstructured texts like books. Therefore, I will use an eclectic set of tools for producing social networks from my corpus.

Because English NLP far outstrips classical-language NLP, I begin with open-access translations of the works in my corpus. Next, I will run this corpus through AllPeople, a machine learning algorithm that I haved developed for named and non-named entity recognition, generating TEI XML copies of each text. These TEI documents contain metadata about the characters that AllPeople identified, encoded in such a way as to make computer-based analysis easier. Lastly, to account for any false positives or false negatives in AllPeople’s output, I manually clean and tune the entity metadata.

Once the entity-level work is complete, I manually chunk each text into “scenes,” encoding these scenes alongside the entity metadata in each TEI documents. I delimit scenes by location, such that the scene changes when the setting does, and I assume that, unless a character is explicitly recorded leaving a scene before others, the same cast of characters is present throughout an entire scene. With these scenes in hand, I generate the works’ affiliation networks \(viz. networks linking characters to the set of events in which they participate\), which I will use to test for correlation between characters’ structural functions and the number/importance of the scenes where they are present. Finally, I will reduce the affiliation networks into co-occurrence networks for analysis.

For dialogue networks, I follow a rule-based approach to quoted speech attribution \(Elson and McKeown 2010\). Afterwards, the process is the similar to building co-occurrence networks: manually cleaning the data and converting it into a network.

To ensure that I record network data consistently as I clean the data, I will follow a set of guidelines that I developed with Paul Dilley for a previous study. The guidelines are as follows.

I define _co-occurrence_ to be one of the following, differentiating between _direct_ and _indirect_ relationships:

1. When two \(or more\) characters are physically present in a scene \(a direct relationship\)
2. When a previously established relationship between two \(or more\) characters is brought into the scene \(a direct relationship\)
3. When an omniscient character speaks about another character while the second character is not present \(an indirect relationship\)
4. When a character speaks about another character on the basis of hearsay \(an indirect relationship\)

Each unidirectional spoken address counts as a separate _instance of dialogue_. For example, if Jesus addresses Peter, and then Peter addresses Jesus, these are two separate events, each recorded as one instance of dialogue for the purposes of weighting. The same rule holds even when the character being addressed is incapable of understanding or responding to the speaker.

As with co-occurrences, I will distinguish between direct and indirect speech. I consider _indirect speech_ to be any instance of dialogue that is not a direct quotation, including occurrences where the topic or content of the dialogue is unknown.

If a character is explicitly identified in the narrative, I will take that character as an actor in the network. In the same way, I will treat collective characters \(e.g., “Disciples,” “Pharisees”\) as a single actor.

In the Gospels, I infer that a named disciple \(e.g., “Peter,” “Andrew”\) is part of the collective character “Disciples,” and I will make this inference explicit in the network. However, I will include the character only after s/he is introduced within the network. Because John does not give names for each of the twelve apostles, I include “The Twelve” as a collective character. However, in the Synoptics, each of the twelve apostles are given names, so I will not include that character. In Luke, I will treat the 72 disciples as a collective character \(“The Seventy-Two”\). Moreover, once they are introduced in Lk 10, I will treat them like a named disciple and infer that they are part of the collective character “Disciples.”

## Structure {#structure}

I divide my dissertation into four chapters. The first chapter covers the theory of literary SNA and the ways it may be applied to the Gospels. Chapter two uses well-established network-analytic concepts to measure characterization in the Gospels and compare it to the biographies in Burridge’s corpus. Chapters three and four move into experimental territory, using relational algebra to map out the relationships implicit in each text, and, as mentioned above, removing the protagonist from each network to gain insight into the plot functions of the other characters. Finally, I conclude by determining the extent to which comparative characterization can inform us about the Gospels’ genre. I also include two appendices: a brief introduction to SNA and a detailed description of the methodology I followed in creating the networks.

### Chapter 1: Literary SNA, Characterization, and the Gospels {#chapter-1-literary-sna-characterization-and-the-gospels}

Since Forster distinguished between “flat” and “round” characters in his _Aspects of the Novel_ \(Forster 1927\), theorists have been concerned with the differences between major and minor characters. However, no consensus has emerged on what roles minor characters play—or, indeed, even how to determine whether a character is minor or major. This chapter provides a survey of existing studies of characterization, both from within and without ancient studies, before exploring some theoretical complications of literary SNA as a methodology, both in terms of the limitations of the current technology and the tension between algorithmic precision and the latent constructedness inherent in the results.

### Chapter 2: Observing Characterization in Social Networks {#chapter-2-observing-characterization-in-social-networks}

I begin my analysis by calculating several standard network measures for each network: the degree distribution; the small-world-ness; and the closeness, betweenness, and eigenvector centrality scores for each node. I use these various measures to lay out structural criteria to determine 1\) whether a character is major, minor, or somewhere in between; 2\) whether cohesive types of minor character exist; and 3\) ways in which minor characters can be structurally important \(especially in terms of information flow between groups in the text\). Building on these results, I show that majority and minority are multi-faceted. That is, a character may be minor in terms of the text’s discourse, but major for its story \(e.g. the disciples in the Gospels\).

### Chapter 3: Extending the Networks: Role Algebras {#chapter-3-extending-the-networks-role-algebras}

This chapter will use role algebras \(Pattison 1993\) combined from the co-occurrence and dialogue networks for each work. For each compound relation, beginning with the highest ranked, I will examine the resulting networks to see how minor characters’ roles change, if at all, documenting and attempting to systematize the circumstances under which a minor character may become major. This technique has the potential for significant interpretive payoff, rounding out characters who are otherwise so flat as to be “animated scenery” \(Galef 1993, 11\).

### Chapter 4: Deforming the Networks: Removing Key Characters {#chapter-4-deforming-the-networks-removing-key-characters}

Researchers sometimes remove nodes from a network in order to determine the resilience of a network’s structure against an attack. In this chapter, I do the same—removing the protagonist \(i.e. the subject of each biography\) from each network. However, instead of determining the network’s robustness, my goal is to determine how much of the story coheres in the protagonist’s absence, and which character\(s\), if any, may be the focus of that story. A significant coherence would indicate a sub-story within the text, with its own \(sub-\)protagonist\(s\) and narrative arc, which would otherwise be very difficult to detect.

### Conclusion {#conclusion}

I will conclude the dissertation by looking at the Gospels’ genre, which is still a matter of debate \(despite the general consensus that they are Greco-Roman biography, as in Aune \(1987\) and Burridge \(2004\)\). I follow Ardanuy and Sporleder \(2014\) in using my social networks to cluster the Gospels and Burridge’s corpus by genre, in order to provide an additional data about the question. Later research will expand the scope to include other genres, such as Greco-Roman novels \(as in Tolbert \(1990\)\) or Jewish biography \(as outlined in Aune \(1987\)\).

### Appendix {#appendix}

The appendix will describe the methodology I followed in producing and analyzing my network data.

## Works Cited {#works-cited}

Agarwal, Apoorv, Anup Kotalwar, Jiehan Zheng, and Owen Rambow. 2013. “SINNET: Social Interaction Network Extractor from Text.” In _The Companion Volume of the Proceedings of Ijcnlp 2013: System Demonstrations_, 33–36. Nagoya, Japan: Asian Federation of Natural Language Processing. [https://www.aclweb.org/anthology/I13-2009](https://www.aclweb.org/anthology/I13-2009).

Akama, Hiroyuki, Maki Miyake, and Jaeyoung Jung. 2011. “Automatic Extraction of Hidden Keywords by Producing ‘Homophily’ within Semantic Networks.” In _Digital Humanities 2011: Conference Abstracts_, 71–74. Stanford University Library.

Allison, Sarah Danielle, Ryan Heuser, Matthew Jockers, Franco Moretti, and Michael Witmore. 2011. “Quantitative Formalism: An Experiment.” Literary Lab Pamphlets. Stanford, CA: Stanford Literary Lab. [https://litlab.stanford.edu/LiteraryLabPamphlet1.pdf](https://litlab.stanford.edu/LiteraryLabPamphlet1.pdf).

Ardanuy, Mariona Coll, and Caroline Sporleder. 2014. “Structure-Based Clustering of Novels.” In _Proceedings of the 3rd Workshop on Computational Linguistics for Literature \(Clfl\)_, 31–39. Gothenburg, Sweden: Association for Computational Linguistics. doi:[10.3115/v1/W14-0905](https://doi.org/10.3115/v1/W14-0905).

Aune, David E. 1987. _The New Testament in Its Literary Environment_. Philadelphia: Westminster.

Bakhtin, M. M. 1982. _The Dialogic Imagination: Four Essays_. Edited by Michael Holquist. Translated by Caryl Emerson. Reprint ed. University of Texas Press Slavic Series 1. Austin, TX: University of Texas Press.

Bakhtin, M. M., and P. N. Medvedev. 1991. _The Formal Method in Literary Scholarship: A Critical Introduction to Sociological Poetics_. Translated by Albert J. Wehrle. Baltimore: Johns Hopkins University Press.

Barnet, John. 2003. _Not the Righteous but Sinners: M. M. Bakhtin’s Theory of Aesthetics and the Problem of Reader-Character Interaction in Matthew’s Gospel_. Library of New Testament Studies 246. London: T&T Clark.

Bennema, Cornelis. 2009a. “A Theory of Character in the Fourth Gospel with Reference to Ancient and Modern Literature.” _Biblical Interpretation_, no. 4: 375–421. doi:[10.1163/156851508X329700](https://doi.org/10.1163/156851508X329700).

———. 2009b. _Encountering Jesus: Character Studies in the Gospel of John_. Minneapolis: Augsburg Fortress.

———. 2013. “A Comprehensive Approach to Understanding Character in the Gospel of John.” In _Characters and Characterization in the Gospel of John_, edited by Christopher W. Skinner, 36–58. London: T&T Clark.

———. 2014. _A Theory of Character in New Testament Narrative_. Minneapolis: Fortress.

Burnett, Fred W. 1993. “Characterization and Reader Construction of Characters in the Gospels.” _Semeia_ 63: 3–28.

Burridge, Richard A. 2004. _What are the Gospels?: A Comparison with Graeco-Roman Biography_. 2nd ed. Grand Rapids: Eerdmans.

Chow, John K. 1992. _Patronage and Power: A Study of Social Networks in Corinth_. Journal for the Study of the New Testament Supplement Series 75. Sheffield: JSOT Press.

Conway, Colleen M. 2002. “Speaking through Ambiguity: Minor Characters in the Fourth Gospel.” _Biblical Interpretation_ 10: 324–41. doi:[10.1163/156851502760226293](https://doi.org/10.1163/156851502760226293).

Danow, David K. 1995. _The Spirit of Carnival: Magical Realism and the Grotesque_. Lexington, KY: University Press of Kentucky.

de Man, Paul. 1971. “The Dead-End of Formalist Criticism.” In _Blindness and Insight: Essays in the Rhetoric of Contemporary Criticism_, 229–45. Minneapolis: University of Minnesota Press.

———. 1973. “Semiology and Rhetoric.” _Diacritics_ 3: 27–33. doi:[10.2307/464524](https://doi.org/10.2307/464524).

De, Sagar S., Satchidananda Dehuri, and Gi-Nam Wang. 2012. “Machine Learning for Social Network Analysis: A Systematic Literature Review.” _IUP Journal of Information Technology_ 8 \(4\): 30–51.

Drucker, Johanna. 2014. _Graphesis: Visual Forms of Knowledge Production_. Cambridge, MA: Harvard University Press.

Duling, Dennis C. 1999. “The Jesus Movement and Social Network Analysis \(Part I: The Spatial Network\).” _Biblical Theology Bulletin_ 29: 156–75. doi:[10.1177/014610799902900404](https://doi.org/10.1177/014610799902900404).

———. 2000. “The Jesus Movement and Social Network Analysis \(Part II: The Social Network\).” _Biblical Theology Bulletin_ 30: 3–14. doi:[10.1177/014610790003000102](https://doi.org/10.1177/014610790003000102).

———. 2002. “The Jesus Movement and Network Analysis.” In _The Social Setting of Jesus and the Gospels_, edited by Wolfgang Stegemann, Bruce J. Malina, and Gerd Theissen, 301–32. Minneapolis: Augsburg Fortress.

Elson, David K. 2012. “Modeling Narrative Discourse.” PhD thesis, New York: Columbia University. [http://www.cs.columbia.edu/{~}delson/pubs/Modeling-Narrative-Discourse{\\_}Elson{\\_}R4.pdf](http://www.cs.columbia.edu/{~}delson/pubs/Modeling-Narrative-Discourse{_}Elson{_}R4.pdf).

Elson, David K., and Kathleen R. McKeown. 2010. “Automatic Attribution of Quoted Speech in Literary Narrative.” In _Proceedings of the Twenty-Fourth Aaai Conference on Artificial Intelligence_, 1013–9. Association for the Advancement of Artificial Intelligence.

Elson, David K., Nicholas Dames, and Kathleen R. McKeown. 2010. “Extracting Social Networks from Literary Fiction.” In _Proceedings of the 48th Annual Meeting of the Association for Computational Linguistics_, 138–47. Uppsala, Sweden: Association for Computational Linguistics. [http://www.aclweb.org/anthology/P10-1015](http://www.aclweb.org/anthology/P10-1015).

Forster, E. M. 1927. _Aspects of the Novel_. New York: Harcourt, Brace & Company.

Galef, David. 1993. _The Supporting Cast: A Study of Flat and Minor Characters_. University Park, PA: Pennsylvania State University Press.

Hauge, Matthew Ryan, and Christopher W. Skinner, eds. 2014. _Character Studies and the Gospel of Mark_. Library of New Testament Studies. London: Bloomsbury T&T Clark.

Howard, James M. 2006. “The Significance of Minor Characters in the Gospel of John.” _Bibliotheca Sacra_ 163: 63–78.

Hunt, Steven A., D. François Tolmie, and Ruben Zimmermann. 2013. _Character Studies in the Fourth Gospel: Narrative Approaches to Seventy Figures in John_. Tübingen: Mohr Siebeck.

Hylen, Susan. 2009. _Imperfect Believers: Ambiguous Characters in the Gospel of John_. Louisville: Westminster John Knox.

Iverson, Kelly R., and Christopher W. Skinner, eds. 2011. _Mark as Story: Retrospect and Prospect_. Resources for Biblical Study 65. Atlanta: Society of Biblical Literature.

Jayannavar, Prashant Arun, Apoorv Agarwal, Melody Ju, and Owen Rambow. 2015. “Validating Literary Theories Using Automatic Social Network Extraction.” In _Proceedings of Naacl-Hlt Fourth Workshop on Computational Linguistics for Literature_, 32–41. Denver, Colorado: Association for Computational Linguistics. [http://www.aclweb.org/anthology/W15-0704](http://www.aclweb.org/anthology/W15-0704).

Lucian. 1905. _The Works of Lucian of Samosata_. Translated by H. W. Fowler and F. G. Fowler. Vol. 3. Oxford: Clarendon Press. [http://www.gutenberg.org/cache/epub/6829/pg6829.txt](http://www.gutenberg.org/cache/epub/6829/pg6829.txt).

Malbon, Elizabeth Struthers. 2000. _In the Company of Jesus: Characters in Mark’s Gospel_. Louisville: Westminster John Knox Press.

Malina, Bruce J., and John J. Pilch. 2006. _Social-Science Commentary on the Letters of Paul_. Minneapolis: Fortress.

Malina, Bruce J., and Richard L. Rohrbaugh. 1998. _Social-Science Commentary on the Gospel of John_. Minneapolis: Fortress.

———. 2003. _Social-Science Commentary on the Synoptic Gospels_. 2nd ed. Minneapolis: Fortress.

McCracken, David. 1993. “Character in the Boundary: Bakhtin’s Interdividuality in Biblical Narratives.” _Semeia_ 63: 29–42.

Mitchell, W. J. T. 2003. “The Commitment to Form; or, Still Crazy after All These Years.” _Publications of the Modern Language Association of America_ 118: 321–25. doi:[10.1632/003081203X67703](https://doi.org/10.1632/003081203X67703).

Miyake, Maki. 2007. “A Network Structure of the Synoptic Gospels Employing Clustering Coefficients.” In _Digital Humanities 2007: Conference Abstracts_, 135–37. University of Illinois, Urbana-Champaign: Graduate School of Library and Information Science.

———. 2008. “Investigating Word Co-Occurrence Selection with Extracted Sub-Networks of the Gospels.” In _Digital Humanities 2008: Book of Abstracts_, 258–60. English Philology, University of Oulu.

———. 2009. “Capturing the Social Networks of the Gospels through a Graph Clustering.” In _Digital Humanities 2009: Conference Abstracts_, 373–75. Maryland Institute for Technology in the Humanities.

Moretti, Franco. 2005. _Graphs, Maps, Trees: Abstract Models for a Literary History_. London: Verso.

———. 2011a. “Network Theory, Plot Analysis.” _New Left Review_ 68: 80–102.

———. 2011b. “Network Theory, Plot Analysis.” Literary Lab Pamphlets. Stanford, CA: Stanford Literary Lab. [https://litlab.stanford.edu/LiteraryLabPamphlet2.pdf](https://litlab.stanford.edu/LiteraryLabPamphlet2.pdf).

———. 2013. _Distant Reading_. London: Verso. doi:[10.1093/llc/fqu010](https://doi.org/10.1093/llc/fqu010).

Moulton, W. F., James Hope Moulton, A. W. Greenup, and Frederick Henry Ambrose Scrivener, trans. 1910. _The New Testament, in the Revised Version of 1881, with Fuller References_. Oxford: Oxford University Press. [http://archive.org/details/cu31924029309717](http://archive.org/details/cu31924029309717).

Pattison, Philippa. 1993. _Algebraic Models for Social Networks_. Structural Analysis in the Social Sciences 7. Cambridge: Cambridge University Press.

Philostratus. 1912. _The Life of Apollonius of Tyana_. Translated by F. C. Conybeare. Vol. 1. Loeb Classical Library L016. London: William Heinemann. [http://archive.org/details/LoebClassicalLibraryL016](http://archive.org/details/LoebClassicalLibraryL016).

Plutarch. 1892. _Plutarch’s Lives_. Translated by Aubrey Stewart and George Long. Vol. 3. London: George Bell & Sons. [http://www.gutenberg.org/files/14140/14140-0.txt](http://www.gutenberg.org/files/14140/14140-0.txt).

Skinner, Christopher W. 2009. _John and Thomas–Gospels in Conflict?: Johannine Characterization and the Thomas Question_. Princeton Theological Monograph Series 115. Eugene, OR: Pickwick.

———, ed. 2013. _Characters and Characterization in the Gospel of John_. Library of New Testament Studies. London: T&T Clark.

Suetonius. 1893. _The Lives of the Twelve Caesars_. Translated by Alexander Thomson Forester. London: George Bell & Sons. [http://www.gutenberg.org/cache/epub/6400/pg6400.txt](http://www.gutenberg.org/cache/epub/6400/pg6400.txt).

Sung, Baek-Yong. 2008. “‘Revealed to Infants, Not to the Wise and Intelligent’: Reader, Character, and Dialogic Interaction—A Bakhtinian Reading of the Gospel of Matthew.” PhD thesis, Madison, NJ: Drew University.

Tacitus. 1897. _The Germany and the Agricola of Tacitus_. Translated by Edward Brooks, Jr. Philadelphia: David McKay. [http://www.gutenberg.org/cache/epub/7524/pg7524.txt](http://www.gutenberg.org/cache/epub/7524/pg7524.txt).

Tolbert, Mary Ann. 1990. “The Gospel in Greco-Roman Culture.” In _The Book and the Text: The Bible and Literary Theory_, edited by Regina M. Schwartz, 258–75. Cambridge, MA: Blackwell.

Vala, Hardik, David Jurgens, Andrew Piper, and Derek Ruths. 2015. “Mr. Bennet, His Coachman, and the Archbishop Walk Into a Bar but Only One of Them Gets Recognized: On The Difficulty of Detecting Characters in Literary Texts.” In _Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing_, 769–74. Lisbon, Portugal: Association for Computational Linguistics. [http://aclweb.org/anthology/D15-1088](http://aclweb.org/anthology/D15-1088).

Wasserman, Stanley, and Katherine Faust. 1994. _Social Network Analysis: Methods and Applications_. Structural Analysis in the Social Sciences 8. Cambridge: Cambridge University Press.

Webb, Geoff R. 2008. _Mark at the Threshold: Applying Bakhtinian Categories to Markan Characterisation_. Leiden: Brill.

Williams, Joel F. 1994. _Other Followers of Jesus: Minor Characters as Major Figures in Mark’s Gospel_. Journal for the Study of the New Testament Supplement Series 102. Sheffield: JSOT Press.

Woloch, Alex. 2003. _The One vs. the Many: Minor Characters and the Space of the Protagonist in the Novel_. Princeton: Princeton University Press.

## Notes {#notes}

