# “I Have Called You Friends”: Social Networks and Characterization in the Gospels

## Topic

My dissertation uses social network analysis (SNA) to situate the New
Testament Gospels within the context of other Greco-Roman
biographies–works to which, Burridge has shown, the Gospels bear a
“family resemblance” (Burridge [2004](#ref-Burridge2004WhatAre), 37–43
*et passim*). I examine the characterization in the four canonical
Gospels, as well as Burridge’s sample of “later Graeco-Roman *bioi*”
(viz. Tacitus’ *Agricola*, Plutarch’s *Cato Minor*, Lucian’s *Demonax*,
Philostratus’ *Apollonius of Tyana*, and Suetonius’ *Lives of the
Caesars*).[^1] More broadly, my goal is twofold: to propose new methods
for the interpretation of the Gospels through an innovative “distant
reading” (Moretti [2013](#ref-Moretti2013DistantReading)) strategy for
the analysis of literary characters and to make a contribution to the
field of digital humanities by suggesting new ways of applying social
network analysis to the study of literature.

The bulk of the dissertation will be devoted to testing current ideas
about characterization in the Gospels and developing a theory of
character that takes into account characters’ structural roles in each
of the Gospels. As Bennema ([2014](#ref-Bennema2014Theory)) notes, very
little work has been done to create a theory of character that applies
to all four Gospels. This dissertation will fill that gap by 1)
measuring characters’ degree and centrality (which are standard network
measurements, well established in the literature) to quantify
characters’ plot functions, and 2) developing a set of criteria that
determine where a character falls on the spectrum/a of characterization.
I will nuance that portrait by performing experiments on the networks to
uncover circumstances under which a character’s role might change.
Throughout, I will compare characterization in the Gospels and
Burridge’s corpus, in order to expand my theory of character to
Greco-Roman biography in general. The dissertation will conclude with an
exploration of the Gospels’ genre. The genre of the Gospels is still
largely an open question; however, as Ardanuy and Sporleder
([2014](#ref-ArdanuySporleder2014Clustering)) have recently shown,
social networks are useful for classifying works according to genre.
Incorporating my data on characters’ structural roles with additional
measures of network structure (e.g., small-world-ness and
assortativity), I test how far the Gospels’ resemblance to other
biographies extends: whether it is primarily at the syntactic level, as
in Burridge’s work, or if it also includes the structures of the works’
plots.

This dissertation will be an important contribution to New Testament
Studies in several ways. For one, it is the first monograph-length
network analysis—a methodology that has yielded concrete interpretive
insights into other texts—of the Gospels. Second, because SNA provides a
rigorous means of testing existing theories and developing new
hypotheses, my dissertation will contribute to ongoing scholarly
conversations about characterization in the Gospels, showing that plot
function is a good index of a character’s role, but that it is
insufficient simply to position characters along a continuum between
minority and majority. Third, it will help to answer the longstanding
question about the Gospels’ genre, which has been a matter of debate for
decades.

[^1]: For ease of expression, I refer to these five works as “Burridge’s
    corpus.”

## State of the Question

### Social Network Analysis of the New Testament

Social network analysis has long been a productive methodology in NT
studies, especially in Pauline studies. Chow’s *Patronage and Power*
([1992](#ref-Chow1992Patronage)), which uses SNA to study the power
relations in the church at Corinth, is seminal. Malina and Pilch’s
*Social-Science Commentary on the Letters of Paul*
([2006](#ref-MalinaPilch2006SocSciPaul)) also uses SNA throughout,
though social networks are not the main focus of the work. In addition,
Malina has edited a series of monographs covering individual members of
Paul’s social network.

Given how useful SNA has been to scholars of Paul, it is somewhat
surprising that more Gospels scholars have not adopted it. As with
Malina and Pilch’s commentary on Paul, Malina and Rohrbaugh have used
SNA in their *Social-Science Commentaries* on the Synoptic Gospels
(Malina and Rohrbaugh [2003](#ref-MalinaRohrbaugh2003SocSciSynoptics))
and on John (Malina and Rohrbaugh
[1998](#ref-MalinaRohrbaugh1998SocSciJohn)), though their analysis
focuses exclusively on the “gossip network” surrounding Jesus. In
addition, Duling has read his reconstruction of the historical Jesus
movement through a network-analytical lens in a series of articles
(Duling [1999](#ref-Duling1999SNA1); Duling [2000](#ref-Duling2000SNA2);
reprinted together as Duling [2002](#ref-Duling2002SNACombo)). However,
his argument treats SNA as a theory in itself, rather than–as has long
been acknowledged in sociological network analysis–a means of testing
and producing theories.[^2] Finally, Miyake has studied the Gospels’
networks in several presentations at Digital Humanities conferences
(Miyake [2007](#ref-Miyake2007Network); Miyake
[2008](#ref-Miyake2008Investigating); Miyake
[2009](#ref-Miyake2009Capturing); Akama, Miyake, and Jung
[2011](#ref-AkamaMiyakeJung2011Automatic)); however, her work focuses
primarily on the semantic networks of NT Greek, with social networks
only as a secondary emphasis. In all, no sustained analysis has been
performed on the social networks of literary characters in the Gospels,
leaving a sizeable gap that this dissertation hopes to fill.

[^2]: On SNA as method vs. theory, see Wasserman and Faust
    ([1994](#ref-WassermanFaust1994SNA)), p. 5.

### Literary Social Network Analysis

This project will engage with other fields beyond the highly specialized
work in Gospels SNA, namely literary SNA (including computer science
fields such as natural language processing \[NLP\]) and narrative
criticism of the Gospels. Literary SNA is an active field, with many
important works being published in the past decade. Moretti’s work has
been especially important. He uses network analysis for book history in
his *Graphs, Maps, Trees* (Moretti
[2005](#ref-Moretti2005GraphsMapsTrees)) and for literary criticism in
his article/pamphlet “Network Theory, Plot Analysis” (Moretti
[2011](#ref-Moretti2011NewLeft)[a](#ref-Moretti2011NewLeft); expanded
and republished as Moretti
[2011](#ref-Moretti2001LitLab)[b](#ref-Moretti2001LitLab)); in the
latter, he uses graph analysis to study the plots of *Hamlet*, *Our
Mutual Friend*, and *The Story of the Stone*. Though Moretti was far
from the first author to incorporate SNA into literary studies, he
brought the methodology into the mainstream, tying it to his broader
approach of distant reading.

Researchers at Columbia University have also been prolific in this area.
Elson, Dames, and McKeown ([2010](#ref-ElsonDamesMcKeown2010Extracting))
is particularly influential, due to the paper’s conclusions: the authors
use social networks to disprove a longstanding theory about
characterization in nineteenth-century novels set in rural, as opposed
to urban, areas. More recently, Columbia-school SNA has focused on
creating standalone tools for building and/or studying literary social
networks (for instance, `Scheherezade` (Elson
[2012](#ref-Elson2012Modeling)) and `SINNET` (Agarwal et al.
[2013](#ref-Agarwal2013SINNET))). The Columbia-school approach contrasts
well with Moretti’s. Though Moretti manually draws the graphs in
“Network Theory, Plot Analysis” and avoids the “stern adulthood of
statistics” (Moretti
[2011](#ref-Moretti2001LitLab)[b](#ref-Moretti2001LitLab), 3), his
hand-crafted networks contain all the characters from the works he
studies. The Columbia scholars, on the other hand, rely on automatic
network extraction; as such, their analyses, while very powerful, suffer
from incomplete data, due to the sheer difficulty of detecting unnamed
characters (Vala et al. [2015](#ref-ValaEtAl2015MrBennet)). Elson,
Dames, and McKeown’s approach, for example, only detected 51% of the
speech in the books they examined (though, among the speech it did
detect, it attributed quotes to the correct characters 95% of the time).
My approach will strike a balance between the two extremes: initially, I
will build the networks automatically, using a machine learning
algorithm that I have developed to detect unnamed characters,
but–because much of my focus will be on minor characters, which are
predominantly unnamed–I will revise the networks by hand to ensure that
they are complete.

### Characterization in the Gospels

Narrative criticism of the Gospels, and especially the study of
characterization in them, is likewise thriving. Skinner and Bennema are
the major recent scholars of Gospels characterization. Skinner’s revised
dissertation (Skinner [2009](#ref-Skinner2009Conflict)) argues that many
of John’s characters have imperfect faith in Jesus, as compared with the
ideal faith set forth in John’s prologue (Jn 1:1-18). On that basis, he
argues against Riley’s, DeConick’s, and Pagels’ views that John’s
portrayal of Thomas was a polemic against a Gnostic community
responsible for the Gospel of Thomas. Skinner has also edited or
co-edited several important books on Markan and Johannine
characterization (Iverson and Skinner
[2011](#ref-IversonSkinner2011MarkStory); Skinner
[2013](#ref-Skinner2013Characters); Hauge and Skinner
[2014](#ref-HaugeSkinner2014CharacterStudies)).

Most of Bennema’s work (e.g. Bennema
[2009](#ref-Bennema2009Theory)[a](#ref-Bennema2009Theory); Bennema
[2009](#ref-Bennema2009Encountering)[b](#ref-Bennema2009Encountering);
Bennema [2013](#ref-Bennema2013Comprehensive)) has been on John, with an
emphasis on comparing Johannine characterization to other literature and
attempting to quantify, by means of a rubric, where a given character
falls on the spectrum between majority and minority. His most recent
book (Bennema [2014](#ref-Bennema2014Theory)) applies that same method
to characters in Mark, John, and Acts, in order to develop a unified
theory of characterization in NT narrative–the only work thus far with
this goal.

In addition, many scholars have studied the minor characters in the
Gospels (for instance Williams [1994](#ref-Williams1994Other); Malbon
[2000](#ref-Malbon2000Company); Conway [2002](#ref-Conway2002Speaking);
Howard [2006](#ref-Howard2006Significance); Hylen
[2009](#ref-Hylen2009Imperfect)). The most comprehensive approach,
however, is Hunt, Tolmie, and Zimmermann
([2013](#ref-HuntTolmieZimmerman2013Seventy)), which brings together
studies of 70 characters in John. Their work stands in contrast to the
rest of the literature, which tends to study either a single character
(as in Burnett ([1993](#ref-Burnett1993Characterization)), which looks
at Peter) or a handful of characters (as in the second half of Skinner
([2013](#ref-Skinner2013Characters)), which comprises chapters on eight
characters in John).

Bakhtinian theory (part of the theoretical backbone of my dissertation;
see below) has also periodically made an appearance in studies of the
Gospels’ characterization. The most relevant studies are McCracken
([1993](#ref-McCracken1993Interdividuality)), which brings Bakhtin’s
theory of interindividuality together with “the Kierkegaardian paradigm
of self” (McCracken [1993](#ref-McCracken1993Interdividuality), 34) to
create a theory of the relationships between biblical characters; Barnet
([2003](#ref-Barnet2003Aesthetics)) and Sung
([2008](#ref-Sung2008Infants)), both of which examine characters’ roles
in Matthew using Bakhtin’s aesthetics; and Webb
([2008](#ref-Webb2008Threshold)), which examines several Markan passages
in light of Bakhtin’s concepts of dialogue, genre-memory, chronotopes,
and carnivalesque.[^3]

[^3]: For Bakhtin, “at a fundamental level, all language and thought is
    dialogical: each word or thought presupposes an answer. . . .
    \[E\]ach person, although having irreducible moral status, cannot be
    considered to have a consciousness in isolation” (Webb
    [2008](#ref-Webb2008Threshold), 19). In the same vein, he conceives
    of genres as constantly evolving, with each writer engaging in
    dialogue with previous manifestations of the genre.

    His “chronotopes” are the way space and time meld together in
    literature: “Time, as it were, thickens, takes on flesh, becomes
    artistically visible; likewise, space becomes charged and responsive
    to the movements of time, plot and history. This intersection of
    axes and fusion of indicators characterizes the artistic chronotope”
    (Bakhtin, Medvedev, and Wehrle
    [1991](#ref-BakhtinMedvedev1991FormalMethod), 131).

    Finally, he sees the medieval religious carnival, in which the
    established order is upended, as continuing after the Renaissance in
    the literary “carnivalesque”:

    > an irresolvable paradox that is seemingly universal and
    > archetypal, that subverts an established value system in order to
    > institute one of its own, that corrupts language and behavioural
    > codes in the work of creating new ones seemingly designed
    > exclusively to displace old ones, and that superimposes one
    > paradox upon another until the original remains forever hidden,
    > undisturbed and unseen (Danow [1995](#ref-Danow1995Spirit), 63;
    > cited in Webb [2008](#ref-Webb2008Threshold), 54).

## Theoretical Influences

My dissertation mainly relies on formalist theory. The most obvious
connection is with the quantitative formalism espoused by the members of
the Stanford Literary Lab and its alumni–especially Allison et al.
([2011](#ref-AllisonEtAl2011Quantitative)) and Moretti
([2011](#ref-Moretti2001LitLab)[b](#ref-Moretti2001LitLab)).[^4] In
addition, I use formalist categories that lend themselves to
interpreting social networks, namely Bakhtin’s (Bakhtin and Emerson
[1982](#ref-Bakhtin1982Dialogic)) interindividuality and the
longstanding formalist distinction between story and discourse–what
Woloch describes as the contrast between “the fictional events that we
reconstruct through the narrative” and “the narrative’s actual language
and structure” (Woloch [2003](#ref-Woloch2003OneVsMany), 38).
Methodologically, I blend various approaches to social network analysis.
Where much of the literature uses either co-occurrence or dialogue
networks as the basis for analysis, I use both.[^5] In addition, I
combine automatic network extraction–which reigns supreme in the
computer science approaches to SNA–with manual network production, in
order to ensure that all characters, both named and unnamed, are
represented adequately.

Theory and method will be tightly intertwined in my dissertation. For
instance, I take co-occurrence and dialogue networks, with the different
information they encode, as a manifestation of story and discourse,
respectively. Co-occurrence networks place links between all the
characters who are present at an event; thus, it is straightforward to
take them as the text’s story.[^6] In addition, I recast *discourse* as
“the words spoken by the characters in a text.” Following this
redefinition, it is easy to use dialogue networks–which show the
characters that speak to each other–as an abstraction of a work’s
discourse.

This juxtaposition has already proven useful. In my research on Luke, I
found that several kinds of minor and intermediate characters exist in
that Gospel’s story, while the discourse is sharply divided between
Jesus and a host of minor characters (namely, every other speaking
character in the book). Moreover, after removing Jesus from the
networks, the dialogue network dissolves significantly, as expected,
while the co-occurrence network (more specifically, the relationships
between Jesus’ disciples and the book’s minor characters) coheres.
Extrapolating back to the text itself, a Jesus-less Luke tells the story
of a beleaguered group of people who follow an itinerant,
miracle-working preacher, who disperse when their leader is executed by
political and religious authorities, but who come back together when
they hear rumors of their leader’s resurrection. In other words, without
Jesus, Luke’s story remains very nearly the same–suggesting that the
disciples might be a class unto themselves: minor in terms of discourse,
but major for the story. I will test this finding to determine whether
it generalizes to the other works in my study.

As mentioned above, my dissertation will also extend current
applications of Bakhtin’s thought to biblical characterization
(primarily McCracken ([1993](#ref-McCracken1993Interdividuality)) and
Webb ([2008](#ref-Webb2008Threshold))). Bakhtin’s notion that characters
exist as a set of interactions between “character zones” applies
directly to social networks, which are, at base, a set of relationships
between nodes. SNA, I argue, thus provides a rigorous way to explore how
a character’s majority or minority relates to their plot function. Take
centrality and degree, for example: if a character has a high
eigenvector centrality and high degree–that is, if that character’s node
is connected to many other important nodes–it is intuitive that s/he
will be a major character. On the other hand, a character with a high
betweenness centrality, even if s/he has a low degree, will be an
important link between different groups of characters; likewise, a high
closeness centrality will indicate that a character is essential to the
cohesion of a community within the text, even if s/he does not play a
central role in the narrative.

Despite formalism’s prominence in my dissertation, I am sympathetic to
critiques of it, especially that it is reductive (as in Man
([1971](#ref-deMan1971DeadEnd)) and Man
([1973](#ref-deMan1973Semiology))) and that it relies on a fallacious
understanding of the nature of data (Drucker
[2014](#ref-Drucker2014Graphesis)).[^7] Literary SNA certainly is
reductive. However, reductiveness does not invalidate SNA as a
methodology; rather, it simply indicates that SNA should be folded into
the larger critical enterprise, so that it may benefit, and benefit
from, other areas of criticism. Likewise, I acknowledge that my
collecting and analyzing data is fundamentally an interpretive act, not
a study of the objective nature of the text. As Drucker insists, “data
are capta, taken not given, constructed as an interpretation of the
phenomenal world, not inherent in it” (Drucker
[2014](#ref-Drucker2014Graphesis), 128, emphasis original).

Finally, in addition to formalist literary theory, I will build heavily
on quantitative and comparative approaches to the Gospels. Like Bennema
([2009](#ref-Bennema2009Theory)[a](#ref-Bennema2009Theory)), I will
situate the Gospels’ characterization among other ancient works. And, in
the same way that Bennema uses his (quasi-quantitative) continua of
characterization, assigning scores to characters based on their
“complexity,” “development,” and “inner life” (Bennema
[2009](#ref-Bennema2009Theory)[a](#ref-Bennema2009Theory); Bennema
[2013](#ref-Bennema2013Comprehensive)), I will use network measures to
determine whether a character is major, minor, or somewhere in between.
However, where Bennema collapses his continua into a single spectrum, I
allow for the possibility that characters may be major in some ways but
minor in others, and that those circumstances may not be reflected
directly in the narrative. Moreover, unlike Bennema, who relies on close
reading to classify his characters, my interpretation depends on distant
reading. In this way, my approach is more like Burridge’s
([2004](#ref-Burridge2004WhatAre)) now classic study of Gospel genre, in
fact a work of “proto-DH,” which studies patterns of structure and
syntax instead of narratives proper.

[^4]: The authors of Allison et al.
    ([2011](#ref-AllisonEtAl2011Quantitative))–all scholars then working
    at, or otherwise affiliated with, the Stanford Literary Lab–coined
    the term “quantitative formalism.” By it, they mean using
    “precise–ideally, measurable–ways” (Allison et al.
    [2011](#ref-AllisonEtAl2011Quantitative), 6) to answer traditional
    formalist questions about genre, with the connotation that their
    tools were digital.

[^5]: Ardanuy and Sporleder
    ([2014](#ref-ArdanuySporleder2014Clustering)) and Jayannavar et al.
    ([2015](#ref-JayannavarEtAl2015Validating)) are notable exceptions
    to this trend.

[^6]: E.g. at the Sermon on the Mount (Mt 5-7), links would be recorded
    between Jesus, each of the disciples, and the crowd that was
    present.

[^7]: I am less sympathetic to critiques such as Mitchell’s, who writes
    that “everyone knows that the concept of form has outlived its
    usefulness in discussions of literature, the arts, and media,” that
    “formalists, as we know, are harmless drudges who spend their days
    counting syllables, measuring line lengths, and weighing emphases
    (Trotsky), or they are decadent aesthetes who waste their time
    celebrating beauty and other ineffable, indefinable qualities of
    works of art,” and laments his “own misspent career as a formalist”
    ([2003](#ref-Mitchell2003StillCrazy), 321, 325 n. 1).

## Methodology

No consensus exists yet on the best way to extract social networks from
unstructured texts like books. Therefore, I will use an eclectic set of
tools for producing social networks from my corpus.

Because English NLP far outstrips classical-language NLP, I begin with
open-access translations of the works in my corpus.[^8] Next, I will run
this corpus through AllPeople, a machine learning algorithm that I haved
developed for named and non-named entity recognition, generating TEI XML
copies of each text.[^9] These TEI documents contain metadata about the
characters that AllPeople identified, encoded in such a way as to make
computer-based analysis easier. Lastly, to account for any false
positives or false negatives in AllPeople’s output, I manually clean and
tune the entity metadata.

Once the entity-level work is complete, I manually chunk each text into
“scenes,” encoding these scenes alongside the entity metadata in each
TEI documents. I delimit scenes by location, such that the scene changes
when the setting does, and I assume that, unless a character is
explicitly recorded leaving a scene before others, the same cast of
characters is present throughout an entire scene. With these scenes in
hand, I generate the works’ affiliation networks (viz. networks linking
characters to the set of events in which they participate), which I will
use to test for correlation between characters’ structural functions and
the number/importance of the scenes where they are present. Finally, I
will reduce the affiliation networks into co-occurrence networks for
analysis.

For dialogue networks, I follow a rule-based approach to quoted speech
attribution (Elson and McKeown
[2010](#ref-ElsonMcKeown2010Attribution)). Afterwards, the process is
the similar to building co-occurrence networks: manually cleaning the
data and converting it into a network.

To ensure that I record network data consistently as I clean the data, I
will follow a set of guidelines that I developed with Paul Dilley for a
previous study. The guidelines are as follows.

I define *co-occurrence* to be one of the following, differentiating
between *direct* and *indirect* relationships:

1.  When two (or more) characters are physically present in a scene (a
    direct relationship)

2.  When a previously established relationship between two (or more)
    characters is brought into the scene (a direct relationship)

3.  When an omniscient character speaks about another character while
    the second character is not present (an indirect relationship)

4.  When a character speaks about another character on the basis of
    hearsay (an indirect relationship)

Each unidirectional spoken address counts as a separate *instance of
dialogue*. For example, if Jesus addresses Peter, and then Peter
addresses Jesus, these are two separate events, each recorded as one
instance of dialogue for the purposes of weighting. The same rule holds
even when the character being addressed is incapable of understanding or
responding to the speaker.

As with co-occurrences, I will distinguish between direct and indirect
speech. I consider *indirect speech* to be any instance of dialogue that
is not a direct quotation, including occurrences where the topic or
content of the dialogue is unknown.

If a character is explicitly identified in the narrative, I will take
that character as an actor in the network. In the same way, I will treat
collective characters (e.g., “Disciples,” “Pharisees”) as a single
actor.

In the Gospels, I infer that a named disciple (e.g., “Peter,” “Andrew”)
is part of the collective character “Disciples,” and I will make this
inference explicit in the network. However, I will include the character
only after s/he is introduced within the network. Because John does not
give names for each of the twelve apostles, I include “The Twelve” as a
collective character. However, in the Synoptics, each of the twelve
apostles are given names, so I will not include that character. In Luke,
I will treat the 72 disciples as a collective character (“The
Seventy-Two”). Moreover, once they are introduced in Lk 10, I will treat
them like a named disciple and infer that they are part of the
collective character “Disciples.”

[^8]: I will use Conybeare’s ([1912](#ref-Conybeare1912Philostratus))
    translation of the *Life of Apollonius*, Long’s
    ([1892](#ref-StewartLong1892Plutarch)) translation of *Cato Minor*,
    Brooks’ ([1897](#ref-Brooks1897Tacitus)) translation of *Agricola*,
    Fowler and Fowler’s ([1905](#ref-FowlerFowler1905Lucian))
    translation of *Demonax*, and Forester’s
    ([1893](#ref-Forester1893Suetonius)) translation of the *Lives of
    the Caesars*. The first work is available on the Internet Archive;
    the rest are on Project Gutenberg.

    For the Gospels, I will use the 1910 edition of the Revised Version
    (Moulton et al. [1910](#ref-MoultonEtAl1910RV)). I make this choice
    for practical reasons: since the syntax of the RV is similar to that
    of the other translations I will use, I will not need to develop a
    separate set of rules for my processing to follow, like I would if I
    used a more modern translation.

[^9]: On the usefulness of machine learning for SNA, see e.g. De,
    Dehuri, and Wang ([2012](#ref-DeEtAl2012MLforSNA))

## Structure

I divide my dissertation into four chapters. The first chapter covers
the theory of literary SNA and the ways it may be applied to the
Gospels. Chapter two uses well-established network-analytic concepts to
measure characterization in the Gospels and compare it to the
biographies in Burridge’s corpus. Chapters three and four move into
experimental territory, using relational algebra to map out the
relationships implicit in each text, and, as mentioned above, removing
the protagonist from each network to gain insight into the plot
functions of the other characters. Finally, I conclude by determining
the extent to which comparative characterization can inform us about the
Gospels’ genre. I also include two appendices: a brief introduction to
SNA and a detailed description of the methodology I followed in creating
the networks.

### Chapter 1: Literary SNA, Characterization, and the Gospels

Since Forster distinguished between “flat” and “round” characters in his
*Aspects of the Novel* (Forster [1927](#ref-Forster1927Aspects)),
theorists have been concerned with the differences between major and
minor characters. However, no consensus has emerged on what roles minor
characters play–or, indeed, even how to determine whether a character is
minor or major. This chapter provides a survey of existing studies of
characterization, both from within and without ancient studies, before
exploring some theoretical complications of literary SNA as a
methodology, both in terms of the limitations of the current technology
and the tension between algorithmic precision and the latent
constructedness inherent in the results.

### Chapter 2: Observing Characterization in Social Networks

I begin my analysis by calculating several standard network measures for
each network: the degree distribution; the small-world-ness; and the
closeness, betweenness, and eigenvector centrality scores for each node.
I use these various measures to lay out structural criteria to determine
1) whether a character is major, minor, or somewhere in between; 2)
whether cohesive types of minor character exist; and 3) ways in which
minor characters can be structurally important (especially in terms of
information flow between groups in the text). Building on these results,
I show that majority and minority are multi-faceted. That is, a
character may be minor in terms of the text’s discourse, but major for
its story (e.g. the disciples in the Gospels).

### Chapter 3: Extending the Networks: Role Algebras

This chapter will use role algebras (Pattison
[1993](#ref-Pattison1993AlgebraicModels)) combined from the
co-occurrence and dialogue networks for each work. For each compound
relation, beginning with the highest ranked, I will examine the
resulting networks to see how minor characters’ roles change, if at all,
documenting and attempting to systematize the circumstances under which
a minor character may become major. This technique has the potential for
significant interpretive payoff, rounding out characters who are
otherwise so flat as to be “animated scenery” (Galef
[1993](#ref-Galef1993Supporting), 11).

### Chapter 4: Deforming the Networks: Removing Key Characters

Researchers sometimes remove nodes from a network in order to determine
the resilience of a network’s structure against an attack. In this
chapter, I do the same–removing the protagonist (i.e. the subject of
each biography) from each network. However, instead of determining the
network’s robustness, my goal is to determine how much of the story
coheres in the protagonist’s absence, and which character(s), if any,
may be the focus of that story. A significant coherence would indicate a
sub-story within the text, with its own (sub-)protagonist(s) and
narrative arc, which would otherwise be very difficult to detect.

### Conclusion

I will conclude the dissertation by looking at the Gospels’ genre, which
is still a matter of debate (despite the general consensus that they are
Greco-Roman biography, as in Aune ([1987](#ref-Aune1987NTLiterary)) and
Burridge ([2004](#ref-Burridge2004WhatAre))). I follow Ardanuy and
Sporleder ([2014](#ref-ArdanuySporleder2014Clustering)) in using my
social networks to cluster the Gospels and Burridge’s corpus by genre,
in order to provide an additional data about the question. Later
research will expand the scope to include other genres, such as
Greco-Roman novels (as in Tolbert ([1990](#ref-Tolbert1990Gospel))) or
Jewish biography (as outlined in Aune
([1987](#ref-Aune1987NTLiterary))).

### Appendix

The appendix will describe the methodology I followed in producing and
analyzing my network data.

## Works Cited [works-cited]

Agarwal, Apoorv, Anup Kotalwar, Jiehan Zheng, and Owen Rambow. 2013.
“SINNET: Social Interaction Network Extractor from Text.” In *Sixth
International Joint Conference on Natural Language Processing*, 33–36.

Akama, Hiroyuki, Maki Miyake, and Jaeyoung Jung. 2011. “Automatic
Extraction of Hidden Keywords by Producing ’Homophily’ within Semantic
Networks.” In *Digital Humanities 2011: Conference Abstracts*, 71–74.
Stanford University Library.

Allison, Sarah Danielle, Ryan Heuser, Matthew Jockers, Franco Moretti,
and Michael Witmore. 2011. “Quantitative Formalism: An Experiment.”
Literary Lab Pamphlets. Stanford, CA: Stanford Literary Lab.
<http://litlab.stanford.edu/LiteraryLabPamphlet1.pdf>.

Ardanuy, Mariona Coll, and Caroline Sporleder. 2014. “Structure-Based
Clustering of Novels.” In *Proceedings of the 3rd Workshop on
Computational Linguistics for Literature (Clfl 2014)*, 31–39.

Aune, David E. 1987. *The New Testament in Its Literary Environment*.
Philadelphia: Westminster.

Bakhtin, Mikhail Mikhailovich, and Caryl Emerson. 1982. *The Dialogic
Imagination: Four Essays*. Edited by Michael Holquist. Reprint ed. 1.
Austin, TX: University of Texas Press.

Bakhtin, Mikhail Mikhailovich, Pavel Nikolaevich Medvedev, and Albert J.
Wehrle. 1991. *The Formal Method in Literary Scholarship: A Critical
Introduction to Sociological Poetics*. Baltimore: Johns Hopkins
University Press.

Barnet, John. 2003. *Not the Righteous but Sinners: M. M. Bakhtin’s
Theory of Aesthetics and the Problem of Reader-Character Interaction in
Matthew’s Gospel*. 246. London: T & T Clark.

Bennema, Cornelis. 2009a. “A Theory of Character in the Fourth Gospel
with Reference to Ancient and Modern Literature.” *Biblical
Interpretation* 17 (4): 375–421.

———. 2009b. *Encountering Jesus: Character Studies in the Gospel of
John*. Minneapolis: Augsburg Fortress.

———. 2013. “A Comprehensive Approach to Understanding Character in the
Gospel of John.” In *Characters and Characterization in the Gospel of
John*, edited by Christopher W Skinner, 36–58. London: T&T Clark.

———. 2014. *A Theory of Character in New Testament Narrative*.
Minneapolis: Fortress.

Burnett, Fred W. 1993. “Characterization and Reader Construction of
Characters in the Gospels.” *Semeia* 63: 3–28.

Burridge, Richard A. 2004. *What are the Gospels?: A Comparison with
Graeco-Roman Biography*. 2nd ed. Grand Rapids: Eerdmans.

Chow, John K. 1992. *Patronage and Power: A Study of Social Networks in
Corinth*. 75. Sheffield: JSOT Press.

Conway, Colleen M. 2002. “Speaking through Ambiguity: Minor Characters
in the Fourth Gospel.” *Biblical Interpretation* 10: 324–41.

Danow, David K. 1995. *The Spirit of Carnival: Magical Realism and the
Grotesque*. Lexington, KY: University Press of Kentucky.

De, Sagar S., Satchidananda Dehuri, and Gi-Nam Wang. 2012. “Machine
Learning for Social Network Analysis: A Systematic Literature Review.”
*IUP Journal of Information Technology* 8 (4): 30–51.

Drucker, Johanna. 2014. *Graphesis: Visual Forms of Knowledge
Production*. Cambridge, MA: Harvard University Press.

Duling, Dennis C. 1999. “The Jesus Movement and Social Network Analysis
(Part I: The Spatial Network).” *Biblical Theology Bulletin* 29: 156–75.
doi:[10.1177/014610799902900404](https://doi.org/10.1177/014610799902900404).

———. 2000. “The Jesus Movement and Social Network Analysis (Part II: The
Social Network).” *Biblical Theology Bulletin* 30: 3–14.
doi:[10.1177/014610790003000102](https://doi.org/10.1177/014610790003000102).

———. 2002. “The Jesus Movement and Network Analysis.” In *The Social
Setting of Jesus and the Gospels*, edited by Wolfgang Stegemann, Bruce J
Malina, and Gerd Theissen, 301–32. Minneapolis: Augsburg Fortress.

Elson, David K. 2012. “Modeling Narrative Discourse.” PhD thesis, New
York: Columbia University.
[http://www.cs.columbia.edu/{\~}delson/pubs/Modeling-Narrative-Discourse{\\\_}Elson{\\\_}R4.pdf](http://www.cs.columbia.edu/{~}delson/pubs/Modeling-Narrative-Discourse{\_}Elson{\_}R4.pdf).

Elson, David K., and Kathleen R. McKeown. 2010. “Automatic Attribution
of Quoted Speech in Literary Narrative.” In *Proceedings of the 24th
Aaai Conference on Artificial Intelligence*, 1013–9. AAAI.

Elson, David K., Nicholas Dames, and Kathleen R. McKeown. 2010.
“Extracting Social Networks from Literary Fiction.” In *Proceedings of
the 48th Annual Meeting of the Association for Computational
Linguistics*, 138–47. Association for Computational Linguistics.

Forster, Edward Morgan. 1927. *Aspects of the Novel*. New York:
Harcourt, Brace & Company.

Galef, David. 1993. *The Supporting Cast: A Study of Flat and Minor
Characters*. University Park, PA: Pennsylvania State University Press.

Hauge, Matthew Ryan, and Christopher W. Skinner, eds. 2014. *Character
Studies and the Gospel of Mark*. London: Bloomsbury T&T Clark.

Howard, James M. 2006. “The Significance of Minor Characters in the
Gospel of John.” *Bibliotheca Sacra* 163: 63.

Hunt, Steven A., D François Tolmie, and Ruben Zimmermann. 2013.
*Character Studies in the Fourth Gospel: Narrative Approaches to Seventy
Figures in John*. Tübingen: Mohr Siebeck.

Hylen, Susan. 2009. *Imperfect Believers: Ambiguous Characters in the
Gospel of John*. Louisville: Westminster John Knox.

Iverson, Kelly R., and Christopher W. Skinner, eds. 2011. *Mark as
Story: Retrospect and Prospect*. 65. Atlanta: Society of Biblical
Literature.

Jayannavar, Prashant Arun, Apoorv Agarwal, Melody Ju, and Owen Rambow.
2015. “Validating Literary Theories Using Automatic Social Network
Extraction.” In *Proceedings of Naacl-Hlt Fourth Workshop on
Computational Linguistics for Literature*, 32–41.

Lucian. 1905. *The Works of Lucian of Samosata*. Translated by H. W.
Fowler and F. G. Fowler. Vol. 3. Oxford: Clarendon Press.
<http://www.gutenberg.org/cache/epub/6829/pg6829.txt>.

Malbon, Elizabeth Struthers. 2000. *In the Company of Jesus: Characters
in Mark’s Gospel*. Louisville: Westminster John Knox Press.

Malina, Bruce J., and John J. Pilch. 2006. *Social-Science Commentary on
the Letters of Paul*. Minneapolis: Fortress.

Malina, Bruce J., and Richard L. Rohrbaugh. 1998. *Social-Science
Commentary on the Gospel of John*. Minneapolis: Fortress.

———. 2003. *Social-Science Commentary on the Synoptic Gospels*. 2nd ed.
Minneapolis: Fortress.

Man, Paul de. 1971. “The Dead-End of Formalist Criticism.” In *Blindness
and Insight: Essays in the Rhetoric of Contemporary Criticism*, 229–45.
Minneapolis: University of Minnesota Press.

———. 1973. “Semiology and Rhetoric.” *Diacritics* 3 (3): 27–33.

McCracken, David. 1993. “Character in the Boundary: Bakhtin’s
Interdividuality in Biblical Narratives.” *Semeia* 63: 29–42.

Mitchell, W. J. T. 2003. “The Commitment to Form; or, Still Crazy after
All These Years.” *Publications of the Modern Language Association of
America* 118: 321–25.

Miyake, Maki. 2007. “A Network Structure of the Synoptic Gospels
Employing Clustering Coefficients.” In *Digital Humanities 2007:
Conference Abstracts*, 135–37. University of Illinois, Urbana-Champaign:
Graduate School of Library and Information Science.

———. 2008. “Investigating Word Co-Occurrence Selection with Extracted
Sub-Networks of the Gospels.” In *Digital Humanities 2008: Book of
Abstracts*, 258–60. English Philology, University of Oulu.

———. 2009. “Capturing the Social Networks of the Gospels through a Graph
Clustering.” In *Digital Humanities 2009: Conference Abstracts*, 373–75.
Maryland Institute for Technology in the Humanities.

Moretti, Franco. 2005. *Graphs, Maps, Trees: Abstract Models for a
Literary History*. London: Verso.

———. 2011a. “Network Theory, Plot Analysis.” *New Left Review* 68:
80–102.

———. 2011b. “Network Theory, Plot Analysis.” Literary Lab Pamphlets.
Stanford, CA: Stanford Literary Lab.
<https://litlab.stanford.edu/LiteraryLabPamphlet2.pdf>.

———. 2013. *Distant Reading*. London: Verso.
doi:[10.1093/llc/fqu010](https://doi.org/10.1093/llc/fqu010).

Moulton, W. F., James Hope Moulton, A. W. Greenup, and Frederick Henry
Ambrose Scrivener, trans. 1910. *The New Testament, in the revised
version of 1881, with fuller references*. Oxford: Oxford University
Press. <http://archive.org/details/cu31924029309717>.

Pattison, Philippa. 1993. *Algebraic Models for Social Networks*. 7.
Cambridge: Cambridge University Press.

Philostratus. 1912. *The Life of Apollonius of Tyana*. Translated by F.
C. Conybeare. Vol. 1. L016. London: William Heinemann.
<http://archive.org/details/LoebClassicalLibraryL016>.

Plutarch. 1892. *The Project Gutenberg EBook of Plutarch’s Lives Volume
III.* Translated by Aubrey Stewart and George Long. Vol. 3. London:
George Bell & Sons. <http://www.gutenberg.org/files/14140/14140-0.txt>.

Skinner, Christopher W. 2009. *John and Thomas: Gospels in Conflict?:
Johannine Characterization and the Thomas Question*. 115. Eugene, OR:
Pickwick.

———, ed. 2013. *Characters and Characterization in the Gospel of John*.
London: T&T Clark.

Suetonius. 1893. *The Lives of the Twelve Caesars*. Translated by
Alexander Thomson Forester. London: George Bell & Sons.
<http://www.gutenberg.org/cache/epub/6400/pg6400.txt>.

Sung, Baek-Yong. 2008. “‘Revealed to Infants, Not to the Wise and
Intelligent’: Reader, Character, and Dialogic Interaction—A Bakhtinian
Reading of the Gospel of Matthew.” PhD thesis, Madison, NJ: Drew
University.

Tacitus. 1897. *The Germany and the Agricola of Tacitus*. Translated by
Edward Brooks, Jr. Philadelphia: David McKay.
<http://www.gutenberg.org/cache/epub/7524/pg7524.txt>.

Tolbert, Mary Ann. 1990. “The Gospel in Greco-Roman Culture.” In *The
Book and the Text: The Bible and Literary Theory*, edited by Regina M
Schwartz, 258–75. Cambridge, MA: Blackwell.

Vala, Hardik, David Jurgens, Andrew Piper, and Derek Ruths. 2015. “Mr.
Bennet, His Coachman, and the Archbishop Walk Into a Bar but Only One of
Them Gets Recognized: On The Difficulty of Detecting Characters in
Literary Texts.” *Proceedings of the 2015 Conference on Empirical
Methods in Natural Language Processing*. Association for Computational
Linguistics, 769–74.

Wasserman, Stanley, and Katherine Faust. 1994. *Social Network Analysis:
Methods and Applications*. 8. Cambridge: Cambridge University Press.

Webb, Geoff R. 2008. *Mark at the Threshold: Applying Bakhtinian
Categories to Markan Characterisation*. Leiden: Brill.

Williams, Joel F. 1994. *Other Followers of Jesus: Minor Characters as
Major Figures in Mark’s Gospel*. 102. Sheffield: JSOT Press.

Woloch, Alex. 2003. *The One vs. the Many: Minor Characters and the
Space of the Protagonist in the Novel*. Princeton: Princeton University
Press.
