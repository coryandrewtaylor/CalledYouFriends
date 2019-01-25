# “I Have Called You Friends”: Social Networks and Characterization in the Gospels {#i-have-called-you-friends-social-networks-and-characterization-in-the-gospels}

## Topic {#topic}

My dissertation uses social network analysis (SNA) to examine characterization in the four New Testament Gospels. More broadly, my goal is threefold: to propose new methods for the interpretation of the Gospels through an innovative “distant reading” strategy for the analysis of literary characters (Moretti 2013); to make a contribution to the field of Digital Humanities by suggesting new ways of applying social network analysis to the study of literature; and to advance digital New Testament Studies through open-source, online tool-building.

Rather than following the traditional monograph format for my dissertation, I plan to develop an interactive web application. This format has precedent within Digital Humanities; the seminal work is Visconti’s dissertation (2015a), the body of which comprised the website [Infinite Ulysses](http://infiniteulysses.com) (Visconti 2015b). Moreover, most digital tools for Biblical Studies are proprietary, closed-source software packages, the contents of which are driven by potential for profit rather than scholarly utility. My dissertation will contribute to a nascent counter-trend among scholars in Digital Biblical Studies, where interconnected, open-source web applications allow scholarship to flourish more quickly than under the current model (Hobson 2014, 269).

The bulk of the dissertation will be devoted to testing current ideas about characterization in the Gospels and developing a theory of character that takes into account characters’ structural roles in each of the Gospels. As Bennema (2014) notes, very little work has been done to create a theory of character that applies to all four Gospels. This dissertation will fill that gap by 1) measuring characters’ degree and centrality (which are standard network measurements, well established in the literature) to quantify characters’ plot functions, and 2) developing a set of criteria that determine where a character falls on the spectrum/a of characterization. Incorporating my data on characters’ structural roles with additional measures of network structure (e.g., small-world-ness and assortativity), I will nuance that portrait by performing experiments on the networks to uncover circumstances under which a character’s role might change.

This dissertation will be an important contribution to New Testament Studies in several ways. For one, it is the first full-length network analysis—a methodology that has yielded concrete interpretive insights into other texts—of the Gospels. Second, because SNA provides a rigorous means of testing existing theories and developing new hypotheses, the dissertation will contribute to ongoing scholarly conversations about characterization in the Gospels, showing that plot function, as expressed through social network measurements, is a good index of character’s role within a narrative.

## State of the Question {#state-of-the-question}

### Social Network Analysis of the New Testament {#social-network-analysis-of-the-new-testament}

Social network analysis has long been a productive methodology in NT studies, especially in Pauline studies. Chow’s *Patronage and Power* (1992), which uses SNA to study the power relations in the church at Corinth, is seminal. Malina and Pilch’s *Social-Science Commentary on the Letters of Paul* (2006) also uses SNA throughout, though social networks are not the main focus of the work. In addition, Malina has edited a series of monographs covering individual members of Paul’s social network.

Given how useful SNA has been to scholars of Paul, it is somewhat surprising that more Gospels scholars have not adopted it. As with Malina and Pilch’s commentary on Paul, Malina and Rohrbaugh have used SNA in their *Social-Science Commentaries* on the Synoptic Gospels (2003) and on John (1998), though their analysis focuses exclusively on the “gossip network” surrounding Jesus. In addition, Duling has read his reconstruction of the historical Jesus movement through a network-analytical lens in a series of articles (Duling 1999; Duling 2000; reprinted together as Duling 2002). However, his argument treats SNA as a theory in itself, rather than as a means of testing and producing theories, as social scientists acknowledge (Wasserman and Faust 1994, 5.). Finally, Miyake has studied the Gospels’ networks in several presentations at the annual Digital Humanities conference (Miyake 2007; Miyake 2008; Miyake 2009; Akama, Miyake, and Jung 2011); however, her work focuses primarily on the semantic networks of NT Greek, with social networks only as a secondary emphasis. In all, no sustained analysis has been performed on the social networks of literary characters in the Gospels, leaving a gap that this dissertation hopes to fill, if only in part.

### Literary Social Network Analysis {#literary-social-network-analysis}

This project will engage with other fields beyond the highly specialized work in Gospels SNA, namely literary SNA (including computer science fields such as natural language processing \[NLP\]) and narrative criticism of the Gospels. Literary SNA is an active field, with many important works being published in the past decade. Moretti’s work has been especially important.[^1] He uses network analysis for book history in his *Graphs, Maps, Trees* (2005) and for literary criticism in his article/pamphlet “Network Theory, Plot Analysis” (2011a; expanded and republished as 2011b); in the latter, he uses graph analysis to study the plots of *Hamlet*, *Our Mutual Friend*, and *The Story of the Stone*. Moretti manually drew all the graphs in his analysis, meaning that his hand-crafted networks contain all the characters from the works he studies. However, his analysis ultimately suffers, as he focuses entirely on his visualizations, avoiding the “stern adulthood of statistics” (Moretti 2011b, 3).

Researchers at Columbia University have also been prolific in literary SNA. Elson, Dames, and McKeown (2010) are particularly influential, due to their paper’s conclusions. They use social networks in an attempt to disprove a longstanding theory about characterization in nineteenth-century novels set in rural, as opposed to urban, areas. Columbia-school SNA has also focused on creating standalone tools for building and/or studying literary social networks.[^2] The upshot is that the Columbia scholars, in contrast to Moretti, rely on automatic network extraction. As such, their analyses, while very powerful, suffer from incomplete data, due to the sheer difficulty of detecting unnamed characters (Vala et al. 2015). Elson and his colleagues’ approach, for example was highly precise but had poor recall, only detecting 51% of the speech in the books they examined. In other words, their algorithm had essentially the same performance as picking quotes from a text at random. Among the speech it did detect, however, it attributed quotes to the correct characters 95% of the time.

My approach to data collection will strike a balance between the two extremes. Initially, I will build the networks automatically, using machine learning algorithms to detect named and unnamed characters within the texts (Honnibal and Montani 2017; Taylor 2018) that I have developed to detect unnamed characters. However, to counteract the shortcomings inherent in automatic parsing, I will revise the networks by hand to ensure that they are complete.

### Characterization in the Gospels {#characterization-in-the-gospels}

Narrative criticism of the Gospels, and especially the study of characterization in them, is likewise thriving. Skinner and Bennema are the major recent scholars of Gospels characterization. Skinner’s revised dissertation (Skinner 2009) argues that many of John’s characters have imperfect faith in Jesus, as compared with the ideal faith set forth in John’s prologue (Jn 1:1–18). On the basis of his analysis, he argues against Riley’s (1995), DeConick’s (1996; 1997), and Pagels’ (1999) view that John’s portrayal of Thomas was a polemic against a Gnostic community responsible for the Gospel of Thomas. Skinner has also edited or co-edited several important books on Markan and Johannine characterization (Iverson and Skinner 2011; Skinner 2013; Hauge and Skinner 2014).

Most of Bennema’s work in NT characterization (e.g. 2009a; 2009b; 2013) has been on John, with an emphasis on comparing Johannine characterization to other literature and attempting to quantify, by means of a rubric, where a given character falls on a (quasi-quantitative) spectrum of characterization, assigning scores to characters based on their “complexity,” “development,” and “inner life” (Bennema 2009a; Bennema 2013). His most recent book (Bennema 2014) applies that same method to characters in Mark, John, and Acts, in order to develop a unified theory of characterization in NT narrative—the only work thus far with this goal.

In addition, many scholars have studied the minor characters in the Gospels (for instance Williams 1994; Malbon 2000; Conway 2002; Howard 2006; Hylen 2009). The most comprehensive approach, however, is Hunt, Tolmie, and Zimmermann (2013), which brings together studies of 70 characters in John. Their work stands in contrast to the rest of the literature, which tends to study either a single character (as in Burnett (1993), a study of Peter) or a handful of characters (as in the second half of Skinner (2013), which comprises chapters on eight characters in John).

## Theoretical Influences {#theoretical-influences}

My approach relies heavily on formalist theory. The most obvious connection is with the quantitative formalism espoused by the members of the Stanford Literary Lab and its alumni—especially Allison et al. (2011) and Moretti (2011b).[^3] In addition, I use formalist categories that lend themselves to interpreting social networks, namely Bakhtin’s interindividuality (Bakhtin 1982) and the longstanding formalist distinction between story and discourse.

Bakhtinian theory has periodically made an appearance in studies of the Gospels’ characterization. The most relevant studies are McCracken (1993), which brings Bakhtin’s theory of interindividuality together with “the Kierkegaardian paradigm of self” (McCracken 1993, 34) to create a theory of the relationships between biblical characters; Barnet (2003) and Sung (2008), both of which examine characters’ roles in Matthew using Bakhtin’s aesthetics; and Webb (2008), which examines several Markan passages in light of Bakhtin’s concepts of dialogue, genre-memory, chronotopes, and carnivalesque.[^4]

Where most studies uses either co-occurrence or dialogue networks as the basis for literary SNA, I use both.[^5] I take co-occurrence and dialogue networks, with the different information they encode, as a manifestation of the classic formalist dichotomy between story and discourse—what Woloch describes as the contrast between “the fictional events that we reconstruct through the narrative” and “the narrative’s actual language and structure” (Woloch 2003, 38). Co-occurrence networks place links between all the characters who are present at an event; thus, it is straightforward to take them as the text’s story.[^6] In addition, I take a narrow view of “the narrative’s actual language and structure,” interpreting it as “the words spoken by the characters in a text.” Following this redefinition, it is easy to use dialogue networks—which model how characters speak to each other—as an abstraction of a work’s discourse.

This juxtaposition has already proven useful. In my research on Luke, I found that several kinds of minor and intermediate characters exist in that Gospel’s story, while the discourse is sharply divided between Jesus and a host of minor characters (namely, every other speaking character in the book). Moreover, after removing Jesus from the networks, the dialogue network dissolves significantly, as expected, while the co-occurrence network (more specifically, the relationships between Jesus’ disciples and the book’s minor characters) coheres. Extrapolating back to the text itself, a Jesus-less Luke tells the story of a beleaguered group of people who follow an itinerant, miracle-working preacher, who disperse when their leader is executed by political and religious authorities, but who come back together when they hear rumors of their leader’s resurrection. In other words, without Jesus, Luke’s story remains very nearly the same. This finding suggests that the disciples might be a class unto themselves: minor in terms of discourse, but major for the story. I will test this hypothesis against the other three Gospels to determine the extent to which it generalizes to works besides Luke. This line of investigation promises significant exegetical payoff.

As mentioned above, my dissertation will also extend current applications of Bakhtin’s thought to biblical characterization.[^7] Bakhtin’s notion that characters exist as a set of interactions between “character zones” applies directly to social networks, which are, at base, a set of relationships between actors. Social network analysis, I argue, thus provides a rigorous way to explore how a character’s majority or minority relates to their plot function. Take centrality and degree, for example: if a character has a high eigenvector centrality—that is, if that character’s node is connected to many other important nodes—it is intuitive that s/he will be a major character. On the other hand, a character with a high betweenness centrality, even if s/he has a low degree, will be an important link between different groups of characters. Likewise, a high closeness centrality could indicate that a character is essential to the cohesion of a community within the text, even if s/he does not play a central role in the narrative.

Despite formalism’s prominence in my dissertation, I am sympathetic to critiques of it, especially that it is reductive (as in de Man (1971) and de Man (1973)) and that it relies on a fallacious understanding of the nature of data (Drucker 2014). Literary SNA certainly is reductive. However, reductiveness does not invalidate SNA as a methodology; rather, it simply indicates that SNA should be folded into the larger critical enterprise, so that it may benefit, and benefit from, other areas of criticism.

Finally, in addition to formalist theory, I will build heavily on quantitative and comparative approaches to the Gospels. In the same way that Bennema uses his continua of characterization, I will use network measures to determine whether a character is major, minor, or somewhere in between. However, where Bennema collapses his continua into a single spectrum, I allow for the possibility that characters may be major in some ways but minor in others, and that those circumstances may not be reflected directly in the narrative. Moreover, unlike Bennema, who relies on close reading to classify his characters, my interpretation depends on distant reading. In this way, my approach is more like Burridge’s (2004) now classic study of Gospel genre, in fact a work of proto-DH, which studies patterns of structure and syntax instead of narratives proper.

## Methodology {#methodology}

No consensus exists yet on the best way to extract social networks from unstructured texts like books. Therefore, I will use an eclectic set of tools for producing social networks from my corpus.

Because English NLP far outstrips classical-language NLP, I will begin with open-access translations of the Gospels, namely the 1881 edition of the Revised Version (Moulton et al. 1910). Next, I will run this corpus through the named-entity recognition algorithm in `spaCy`, an open-source NLP library (Honnibal and Montani 2017), followed by AllPeople, a machine learning model that I have developed for non-named entity recognition (Taylor 2018).[^8] After these steps, I will generate TEI markup of each text. These TEI documents will contain metadata about the characters that AllPeople identified, encoded in such a way as to make computer-based analysis easier. Lastly, to account for any false positives or false negatives in the entity-recognition tasks, I will manually clean and tune the entity metadata.

Once the entity-level work is complete, I will manually chunk each text into “scenes,” encoding these scenes alongside the entity metadata in each TEI document. I delimit scenes by location, such that the scene changes when the setting does, and I assume that, unless a character is explicitly recorded leaving a scene before others, the same cast of characters is present throughout an entire scene. With these scenes in hand, I will generate the works’ co-occurrence networks for analysis.

For dialogue networks, I follow a rule-based approach to quoted speech attribution, as in Elson and McKeown (2010). Afterwards, the process is the similar to building co-occurrence networks: encoding the dialogue relationships in TEI, manually cleaning the data, and converting it into a network.

To ensure that I record network data consistently as I clean the data, I will follow a set of guidelines that I developed with Paul Dilley for a previous study. The guidelines are as follows.

I define *co-occurrence* to be one of the following, differentiating between *direct* and *indirect* relationships:

1.  Two or more characters who are physically present together, at the same time, in a scene (a direct relationship)

2.  A previously established co-occurrence relationship between two or more characters being referenced in a scene (a direct relationship)

3.  An omniscient character speaking about another character while the second character is not present (an indirect relationship)

4.  A character speaking about another character on the basis of hearsay (an indirect relationship)

Through this extended definition of “co-occurrence,” I aim to encode all the social relationships in each work, not simply those where two characters appear beside each other.

Each unidirectional, spoken address constitutes an *instance of dialogue*. For example, if Jesus addresses Peter, and then Peter addresses Jesus, these are two separate events, each recorded as a separate instance of dialogue. The same rule holds even when the character being addressed is incapable of understanding or responding to the speaker.

As with co-occurrences, I distinguish between direct and indirect speech. I consider *indirect speech* to be any instance of dialogue that is not a direct quotation, including occurrences where the topic or content of the dialogue is unknown

If a character is explicitly identified in the narrative, I take that character as an actor in the network. I treat collective characters (e.g., “Disciples,” “Pharisees”) as a single actor. Any actor who is contemporary to the events in the narrative is eligible to be included in the network. Thus, natural and supernatural characters are both valid actors, while historical figures and characters in parables are not, since they are touchstones, not members of the text’s imagined society.

I infer that a named disciple (e.g., “Peter,” “Andrew”) is part of the collective character “Disciples,” and I will make this inference explicit in the network data. However, I will include the character only after s/he is introduced within the text. Because John does not give names for each of the twelve apostles, I will include “The Twelve” as a collective character. However, in the Synoptics, each of the twelve apostles has a name, so I will not include that character. In Luke, I will treat the 72 disciples as a collective character (“The Seventy-Two”). Moreover, once they are introduced in Lk 10, I will treat them like a named disciple and infer that they are part of the collective character “Disciples.”

## Structure {#structure}

I divide my dissertation into a prologue and three interactive sections. The prologue covers the theory of literary SNA and the ways it may be applied to the Gospels. The first section uses well-established network-analytic concepts to measure characterization in the Gospels. sections two and three present analyses of a more experimental sort. Section 2 maps out the relationships implicit in each text by means of relational algebra (Pattison 1993). Section 3 removes Jesus from each network to gain insight into the plot functions of the other characters, as described above. I will also include an appendix, detailing the methodology I followed in creating the networks.

### Prologue: Literary SNA, Characterization, and the Gospels {#prologue-literary-sna-characterization-and-the-gospels}

Since Forster distinguished between “flat” and “round” characters in his *Aspects of the Novel* (Forster 1927), theorists have been concerned with the differences between major and minor characters. However, no consensus has emerged on what roles minor characters play—or, indeed, even how to determine whether a character is minor or major. This chapter provides a survey of existing studies of characterization, both from within and without ancient studies, before exploring some theoretical complications of literary SNA as a methodology, both in terms of the limitations of the current technology and the tension between algorithmic precision and the latent constructedness inherent in the results.

### Section 1: Observing Characterization in Social Networks {#section-1-observing-characterization-in-social-networks}

I begin my analysis by calculating several standard network measures for each network: the degree distribution; the small-world-ness; and the closeness, betweenness, and eigenvector centrality scores for each node. I use these various measures to lay out structural criteria to determine 1) whether a character is major, minor, or somewhere in between; 2) whether cohesive types of minor character exist; and 3) ways in which minor characters can be structurally important (especially in terms of information flow between groups in the text). Building on these results, I show that majority and minority are multi-faceted. That is, a character may be minor in terms of the text’s discourse, but major for its story (e.g. the disciples in the Gospels).

### Section 2: Extending the Networks: Role Algebras {#section-2-extending-the-networks-role-algebras}

This section will use role algebras (Pattison 1993) combined from the co-occurrence and dialogue networks for each work. For each compound relation, beginning with the highest ranked, I will examine the resulting networks to see how minor characters’ roles change, if at all, documenting and attempting to systematize the circumstances under which a minor character may become major. This technique has the potential for significant interpretive payoff, rounding out characters who are otherwise so flat as to be “animated scenery” (Galef 1993, 11).

### Section 3: Deforming the Networks: Removing Key Characters {#section-3-deforming-the-networks-removing-key-characters}

Researchers sometimes remove nodes from a network in order to determine the resilience of a network’s structure against an attack. In this section, I do the same—removing the protagonist (i.e. the subject of each biography) from each network. However, instead of determining the network’s robustness, my goal is to determine how much of the story coheres in the protagonist’s absence, and which character(s), if any, may be the focus of that story. A significant coherence would indicate a sub-story within the text, with its own (sub-)protagonist(s) and narrative arc, which would otherwise be very difficult to detect.

### Appendix {#appendix}

The appendix will describe the methodology I followed in producing and analyzing my network data.

## Works Cited {#works-cited}

Agarwal, Apoorv, Anup Kotalwar, Jiehan Zheng, and Owen Rambow. 2013. “SINNET: Social Interaction Network Extractor from Text.” In *The Companion Volume of the Proceedings of Ijcnlp 2013: System Demonstrations*, 33–36. Nagoya, Japan: Asian Federation of Natural Language Processing. <http://www.aclweb.org/anthology/I13-2009>.

Akama, Hiroyuki, Maki Miyake, and Jaeyoung Jung. 2011. “Automatic Extraction of Hidden Keywords by Producing ’Homophily’ within Semantic Networks.” In *Digital Humanities 2011: Conference Abstracts*, 71–74. Stanford University Library.

Allison, Sarah Danielle, Ryan Heuser, Matthew Jockers, Franco Moretti, and Michael Witmore. 2011. “Quantitative Formalism: An Experiment.” Literary Lab Pamphlets. Stanford, CA: Stanford Literary Lab. <http://litlab.stanford.edu/LiteraryLabPamphlet1.pdf>.

Bakhtin, M. M. 1982. *The Dialogic Imagination: Four Essays*. Edited by Michael Holquist. Translated by Caryl Emerson. Reprint ed. Austin, TX: University of Texas Press.

Bakhtin, M. M., and P. N. Medvedev. 1991. *The Formal Method in Literary Scholarship: A Critical Introduction to Sociological Poetics*. Translated by Albert J. Wehrle. Baltimore: Johns Hopkins University Press.

Barnet, John. 2003. *Not the Righteous but Sinners: M. M. Bakhtin’s Theory of Aesthetics and the Problem of Reader-Character Interaction in Matthew’s Gospel*. Library of New Testament Studies 246. London: T & T Clark.

Bennema, Cornelis. 2009a. “A Theory of Character in the Fourth Gospel with Reference to Ancient and Modern Literature.” *Biblical Interpretation* 17: 375–421. doi:[10.1163/156851508X329700](https://doi.org/10.1163/156851508X329700).

———. 2009b. *Encountering Jesus: Character Studies in the Gospel of John*. Minneapolis: Augsburg Fortress.

———. 2013. “A Comprehensive Approach to Understanding Character in the Gospel of John.” In *Characters and Characterization in the Gospel of John*, edited by Christopher W. Skinner, 36–58. London: T & T Clark.

———. 2014. *A Theory of Character in New Testament Narrative*. Minneapolis: Fortress.

Burnett, Fred W. 1993. “Characterization and Reader Construction of Characters in the Gospels.” *Semeia* 63: 3–28.

Burridge, Richard A. 2004. *What are the Gospels?: A Comparison with Graeco-Roman Biography*. 2nd ed. Grand Rapids: Eerdmans.

Chow, John K. 1992. *Patronage and Power: A Study of Social Networks in Corinth*. Journal for the Study of the New Testament Supplement Series 75. Sheffield: JSOT Press.

Coll Ardanuy, Mariona, and Caroline Sporleder. 2014. “Structure-Based Clustering of Novels.” In *Proceedings of the 3rd Workshop on Computational Linguistics for Literature (CLFL)*, 31–39. Gothenburg, Sweden: Association for Computational Linguistics. <http://www.aclweb.org/anthology/W14-0905>.

Conway, Colleen M. 2002. “Speaking through Ambiguity: Minor Characters in the Fourth Gospel.” *Biblical Interpretation* 10: 324–41. doi:[10.1163/156851502760226293](https://doi.org/10.1163/156851502760226293).

De, Sagar S., Satchidananda Dehuri, and Gi-Nam Wang. 2012. “Machine Learning for Social Network Analysis: A Systematic Literature Review.” *IUP Journal of Information Technology* 8: 30–51. <http://papers.ssrn.com/abstract=2187186>.

de Man, Paul. 1971. “The Dead-End of Formalist Criticism.” In *Blindness and Insight: Essays in the Rhetoric of Contemporary Criticism*, 229–45. Minneapolis: University of Minnesota Press.

———. 1973. “Semiology and Rhetoric.” *Diacritics* 3 (3): 27–33. doi:[10.2307/464524](https://doi.org/10.2307/464524).

DeConick, April. 1996. *Seek to See Him: Ascent and Vision Mysticism in the Gospel of Thomas*. Leiden: Brill.

———. 1997. “’Blessed are those who have not seen’ (John 20:29): Johannine Dramatization of an Early Christian Discourse.” In *The Nag Hammadi Library After Fifty Years*, edited by John D. Turner and Ann McGuire, 381–400. Leiden.

Drucker, Johanna. 2014. *Graphesis: Visual Forms of Knowledge Production*. Cambridge, MA: Harvard University Press.

Duling, Dennis C. 1999. “The Jesus Movement and Social Network Analysis (Part I: The Spatial Network).” *Biblical Theology Bulletin* 29: 156–75. doi:[10.1177/014610799902900404](https://doi.org/10.1177/014610799902900404).

———. 2000. “The Jesus Movement and Social Network Analysis (Part II: The Social Network).” *Biblical Theology Bulletin* 30: 3–14. doi:[10.1177/014610790003000102](https://doi.org/10.1177/014610790003000102).

———. 2002. “The Jesus Movement and Network Analysis.” In *The Social Setting of Jesus and the Gospels*, edited by Wolfgang Stegemann, Bruce J. Malina, and Gerd Theissen, 301–32. Minneapolis: Augsburg Fortress.

Elson, David K. 2012. “Modeling Narrative Discourse.” PhD thesis, New York: Columbia University. [http://www.cs.columbia.edu/{~}delson/pubs/Modeling-Narrative-Discourse{\\\_}Elson{\\\_}R4.pdf](http://www.cs.columbia.edu/{~}delson/pubs/Modeling-Narrative-Discourse{\_}Elson{\_}R4.pdf).

Elson, David K., and Kathleen R. McKeown. 2010. “Automatic Attribution of Quoted Speech in Literary Narrative.” In *Proceedings of the 24th AAAI Conference on Artificial Intelligence*, 1013–9. AAAI. <https://www.aaai.org/ocs/index.php/AAAI/AAAI10/paper/view/1945>.

Elson, David K., Nicholas Dames, and Kathleen R. McKeown. 2010. “Extracting Social Networks from Literary Fiction.” In *Proceedings of the 48th Annual Meeting of the Association for Computational Linguistics*, 138–47. Uppsala, Sweden: Association for Computational Linguistics. <http://www.aclweb.org/anthology/P10-1015>.

Forster, Edward Morgan. 1927. *Aspects of the Novel*. New York: Harcourt, Brace & Company.

Galef, David. 1993. *The Supporting Cast: A Study of Flat and Minor Characters*. University Park, PA: Pennsylvania State University Press.

Hauge, Matthew Ryan, and Christopher W. Skinner, eds. 2014. *Character Studies and the Gospel of Mark*. London: Bloomsbury T & T Clark.

Hobson, Russell. 2014. “Does Biblical Studies Deserve to Be an Open Source Discipline?” In *Digital Humanities in Biblical, Early Jewish and Early Christian Studies*, edited by Claire Clivaz, Andrew Gregory, and David Hamidović, 261–70. Boston: Brill.

Honnibal, Matthew, and Ines Montani. 2017. “spaCy 2: Natural language understanding with Bloom embeddings, convolutional neural networks and incremental parsing.” *To Appear*. <https://github.com/explosion/spaCy>.

Howard, James M. 2006. “The Significance of Minor Characters in the Gospel of John.” *Bibliotheca Sacra* 163: 63.

Hunt, Steven A., D. François Tolmie, and Ruben Zimmermann. 2013. *Character Studies in the Fourth Gospel: Narrative Approaches to Seventy Figures in John*. Tübingen: Mohr Siebeck.

Hylen, Susan. 2009. *Imperfect Believers: Ambiguous Characters in the Gospel of John*. Louisville: Westminster John Knox.

Iverson, Kelly R., and Christopher W. Skinner, eds. 2011. *Mark as Story: Retrospect and Prospect*. Atlanta: Society of Biblical Literature.

Jayannavar, Prashant Arun, Apoorv Agarwal, Melody Ju, and Owen Rambow. 2015. “Validating Literary Theories Using Automatic Social Network Extraction.” In *Proceedings of the Fourth Workshop on Computational Linguistics for Literature*, 32–41. Denver, CO: Association for Computational Linguistics. <https://www.aclweb.org/anthology/W15-0704>.

Malbon, Elizabeth Struthers. 2000. *In the Company of Jesus: Characters in Mark’s Gospel*. Louisville: Westminster John Knox Press.

Malina, Bruce J., and John J. Pilch. 2006. *Social-Science Commentary on the Letters of Paul*. Minneapolis: Fortress.

Malina, Bruce J., and Richard L. Rohrbaugh. 1998. *Social-Science Commentary on the Gospel of John*. Minneapolis: Fortress.

———. 2003. *Social-Science Commentary on the Synoptic Gospels*. 2nd ed. Minneapolis: Fortress.

McCracken, David. 1993. “Character in the Boundary: Bakhtin’s Interdividuality in Biblical Narratives.” *Semeia* 63: 29–42.

Miyake, Maki. 2007. “A Network Structure of the Synoptic Gospels Employing Clustering Coefficients.” In *Digital Humanities 2007: Conference Abstracts*, 135–37. University of Illinois, Urbana-Champaign Graduate School of Library; Information Science.

———. 2008. “Investigating Word Co-Occurrence Selection with Extracted Sub-Networks of the Gospels.” In *Digital Humanities 2008: Book of Abstracts*, 258–60. English Philology, University of Oulu.

———. 2009. “Capturing the Social Networks of the Gospels through a Graph Clustering.” In *Digital Humanities 2009: Conference Abstracts*, 373–75. Maryland Institute for Technology in the Humanities.

Moretti, Franco. 2005. *Graphs, Maps, Trees: Abstract Models for a Literary History*. London: Verso.

———. 2011a. “Network Theory, Plot Analysis.” *New Left Review* 68: 80–102.

———. 2011b. “Network Theory, Plot Analysis.” Literary Lab Pamphlets. Stanford, CA: Stanford Literary Lab. <https://litlab.stanford.edu/LiteraryLabPamphlet2.pdf>.

———. 2013. *Distant Reading*. London: Verso. doi:[10.1093/llc/fqu010](https://doi.org/10.1093/llc/fqu010).

Moulton, W. F., James Hope Moulton, A. W. Greenup, and Frederick Henry Ambrose Scrivener. 1910. *The New Testament, in the Revised Version of 1881, with Fuller References*. Oxford: Oxford University Press. <http://archive.org/details/cu31924029309717>.

Pagels, Elaine H. 1999. “Exegesis of Genesis 1 in the Gospels of Thomas and John.” *Journal of Biblical Literature* 118: 477–96. doi:[10.2307/3268185](https://doi.org/10.2307/3268185).

Pattison, Philippa. 1993. *Algebraic Models for Social Networks*. Structural Analysis in the Social Sciences 7. Cambridge: Cambridge University Press.

Riley, Gregory J. 1995. *Resurrection Reconsidered: Thomas and John in Controversy*. Minneapolis: Fortress.

Skinner, Christopher W. 2009. *John and Thomas: Gospels in Conflict?: Johannine Characterization and the Thomas Question*. Princeton Theological Monograph Series 115. Eugene, OR: Pickwick.

———, ed. 2013. *Characters and Characterization in the Gospel of John*. London: T & T Clark.

Sung, Baek-Yong. 2008. “‘Revealed to Infants, Not to the Wise and Intelligent’: Reader, Character, and Dialogic Interaction—A Bakhtinian Reading of the Gospel of Matthew.” PhD thesis, Drew University.

Taylor, Cory. 2018. “AllPeople: A Named- and Non-Named Entity Recognition Tool for Unstructured Text.” <https://github.com/coryandrewtaylor/AllPeople>.

Vala, Hardik, David Jurgens, Andrew Piper, and Derek Ruths. 2015. “Mr. Bennet, His Coachman, and the Archbishop Walk Into a Bar but Only One of Them Gets Recognized: On The Difficulty of Detecting Characters in Literary Texts.” In *Proceedings of the 2015 Conference on Empirical Methods in Natural Language Processing*, 769–74. Association for Computational Linguistics. <http://www.aclweb.org/anthology/D15-1088>.

Visconti, Amanda. 2015a. “’How Can You Love a Work If You Don’t Know It?’: Critical Code and Design Toward Participatory Digital Editions.” PhD thesis, University of Maryland, College Park. <http://dr.amandavisconti.com/>.

———. 2015b. “Infinite Ulysses.” <http://infiniteulysses.com/>.

Wasserman, Stanley, and Katherine Faust. 1994. *Social Network Analysis: Methods and Applications*. Structural Analysis in the Social Sciences 8. Cambridge: Cambridge University Press.

Webb, Geoff R. 2008. *Mark at the Threshold: Applying Bakhtinian Categories to Markan Characterisation*. Leiden: Brill.

Williams, Joel F. 1994. *Other Followers of Jesus: Minor Characters as Major Figures in Mark’s Gospel*. Journal for the Study of the New Testament Supplement Series 102. Sheffield: JSOT Press.

Woloch, Alex. 2003. *The One vs. the Many: Minor Characters and the Space of the Protagonist in the Novel*. Princeton: Princeton University Press.

## Notes {#notes}

[^1]: Though Moretti was far from the first author to incorporate SNA into literary studies, he brought the methodology into the mainstream, tying it to his broader approach of distant reading.

[^2]: For instance, `Scheherezade` (Elson 2012) and `SINNET` (Agarwal et al. 2013).

[^3]: Allison and her colleagues—all scholars then working at, or otherwise affiliated with, the Stanford Literary Lab—coined the term “quantitative formalism” (Allison et al. 2011). By it, they mean using “precise—ideally, measurable—ways” (2011, 6) to answer traditional formalist questions about genre, with the connotation that their tools were digital.

[^4]: For Bakhtin, “at a fundamental level, all language and thought is dialogical: each word or thought presupposes an answer. . . . \[E\]ach person, although having irreducible moral status, cannot be considered to have a consciousness in isolation” (Webb 2008, 19). In the same vein, he conceives of genres as constantly evolving, with each writer engaging in dialogue with previous manifestations of the genre. <br/><br/>His “chronotopes” are the way space and time meld together in literature: “Time, as it were, thickens, takes on flesh, becomes artistically visible; likewise, space becomes charged and responsive to the movements of time, plot and history. This intersection of axes and fusion of indicators characterizes the artistic chronotope” (Bakhtin and Medvedev 1991, 131).

[^5]: Coll Ardanuy and Sporleder (2014) and Jayannavar et al. (2015) are notable exceptions to this trend.

[^6]: E.g. at the Sermon on the Mount (Mt 5–7), links would be recorded between Jesus, each of the disciples, and the crowd that was present.

[^7]: cf. McCracken (1993) and Webb (2008).

[^8]: On the usefulness of machine learning for SNA, see e.g. De, Dehuri, and Wang (2012).
