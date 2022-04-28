# Finding Illegal Wildlife Trade on Twitter

## Abstract

Example:
Experts combating wildlife trafficking manually sift through articles about seizures and
arrests, which is time consuming and makes identifying trends difficult. In this project, we
applied natural language processing techniques to extract data from reports published by the Eco
Activists for Governance and Law Enforcement. We expanded on spaCy’s pre-trained pipeline
and added custom named entities which enabled us to identify approximately 40% of wildlife
trafficking events. We created visualizations to display trends in the extracted data, which are
accessible on our website, Wildlife Trafficking in Africa. This project is an initial solution to
automatically extract, collect, and display, wildlife trafficking data for experts to easily analyze.


The illegal ivory trade (abbreviated as IIT) is a major concern in the world today. It is estimated that over 30,000 African elephants are killed each year by illegal trade. The population is decreasing by about 0.6% per year. To help stop IIT, we are investigating the use of Twitter to identify IIT and potentially remove the offending tweets. We worked under the assumption that if poachers have no clients, they have no incentive to participate in IIT. There has been work done before about automatically detecting offending Tweets, but they were using a basic biterm clustering algorithm since they were limited by having limited training data. In this paper we are making two contributions, a BERT based machine learning model for identifying IIT and the largest dataset of IIT tweets. We will also discuss the potential impact of this project on the world of wildlife trade.

## Introduction 

Example:
The International Consortium on Combating Wildlife Crime, a leading expert in the field,
defines wildlife trafficking as “the taking, trading (supplying, selling, or trafficking), importing,
exporting, and processing, possessing, obtaining and consumption of wild fauna and flora,
including timber and other forest products, in contravention of national or international law”
(Wildlife Crime | CITES, n.d.). The United Nations Office of Drugs and Crime (UNODC)
recognized nearly 6,000 species being illegally traded as of 2019 (UNODC, 2020). Pangolins,
tigers, elephants, and their associated products, such as scales, skins, and tusks, are examples of
commonly trafficked commodities. As of 2018, illegal wildlife trade impacts at least 149
countries and territories (UNODC, 2020). The World Wildlife Fund valued wildlife trade to be at
least $19 billion per year, making it the fourth largest illegal global trade (WWF, 2012). Wildlife
trafficking is a global issue that endangers the targeted flora and fauna, ecosystems, and human
welfare (Wildlife, Forest & Fisheries Crime Module 1 Key Issues, 2019).
Many organizations work to combat illegal wildlife trafficking and to conserve wildlife
including the World Wildlife Fund, International Union for Conservation of Nature, and the Eco
Activists for Governance and Law Enforcement, also known as EAGLE. EAGLE aims to
impede wildlife trafficking and related corruption through civic activism and collaborating with
governments. They do so through investigations, arrests, prosecutions, and publicity (EAGLE
Network, 2022). As a result of EAGLE’s efforts, more than 2,000 wildlife traffickers have been
jailed. The organization covers nine countries, Cameroon, Congo, Gabon, Togo, Senegal, Benin,
Côte D’Ivoire, Burkina Faso, and Uganda. EAGLE releases monthly briefings containing details
of their recent work including seizures and wildlife trafficker arrests. This data could be
leveraged to identify trends and insights about wildlife trafficking.

* Introduction:
 * What is ivory trade?
 * Why is IIT a concern?
 * How are people addressing IIT?
 * What is the problem with their solutions?
 * 

The Fish and Wildlife Service (FWS) prohibits the "import and export of African elephant ivory with limited exceptions for: Musical instruments, items that are part of a traveling exhibition, and items that are part of a household move or inheritance when specific criteria are met; and ivory for law enforcement or genuine scientific purposes." (5) Even with bans in several countries, the African elephant is still being poached. According to National Geographic there are 30,000 African elephants poached each year with a continent-wide population of only 400,000 (6). The population of African elephants is decreasing by about 0.6% per year. We are focusing on elephants, but it is being affected by IIT. It is also happening to the rhinos(11) and walruses. There have been some past attempts to address this issue by using a biterm clustering model (12). Using a clustering model inherently has a very low accuracy. In fact, 4 out of 9 tweets they report as illegal ivory trade we do not agree with since the items being sold are referring to the color ivory or ivory lookalike(12). They were also limited by not having an initial dataset (12). We address these problems in two ways:
* We built the largest ever dataset of IIT Tweets Our Dataset contains XX IIT Tweets.
* Created the first BERT based model for IIT. This allowed us to obtain an accuracy of about XX%.

Project Goal:
There were two goals for this project. The first goal is to demonstrate that it is possible to automatically classify user generated content. We believe that this model could potentially be applied to a dynamic and high speed platform. This paper focuses on Twitter, but the same principles should apply to other platforms as well. We hope that it will demonstrate to media platforms that it is possible and practical to implement an algorithm that automatically removes post that are promoting the sale of IIT. We also hope that this paper would be a good starting point for any platform setting out to implement such an algorithm. The second goal is to build a large enough dataset of IIT texts that such platforms can use it as a seed dataset. One of our biggest challenge was generating our initial dataset to seed the model. We believe that this dataset will be large enough to be used by researchers in the future.

# Background

Example:

Wildlife trafficking market supply chains involve many people assuming various roles. In
their 2016 article, Phelps et al., developed a typology framework of the key actors involved in
wildlife trafficking. The three main roles were harvesters, intermediaries, and consumers.
Harvesters gather the plants and animals from the wild. There are a variety of reasons people
choose to harvest such as for individual use, recreation, and commercial gain. Intermediaries
transport and sell goods and consist of seven sub-roles: logistician, specialized smuggler,
government colluder, third party, processor, launderer, and vendor. Logistician’s responsibilities
include financing and planning the transportation of goods. This may be done directly or at a
distance. Specialized smugglers excel at moving illegal goods across borders without being
intercepted. Smugglers may involve government colluders through bribery, and other third
parties such as for transportation. Most of these actors intentionally get involved, however
sometimes the third parties unknowingly support trade. Processors convert the wildlife into other

3
products such as by skinning animals. Launderers and vendors sell the products to consumers
and other intermediaries. They may complete sales in person through markets or digitally
through online platforms. Intermediaries are typically the ones embroiled in wildlife trafficking
seizures. The last category of actors that Phelps et al. (2016) identified were consumers, which
use the final goods. An example of a supply chain an illicit good may pass through can be seen
below in Figure 2.

* Background
 * The basic structure of the supply chain
 * Why someone would be involved in IIT
   * Why would someone sell IIT
     * What type ot people would sell IIT
   * Why would someone buy IIT
     * What type of people would be buying IIT
 * What the cost on the environment is
 * What punishment would be given to the perpetrator



Paragraph 1:
 * Who poaches the elephants?
Paragraph 2:
 * Who is it being sold to?
   * https://www.sciencedirect.com/science/article/pii/S0006320714003371?casa_token=jxfHglTOhI0AAAAA:DtE4ATQ7-t6Bd_P4n22P7TFnXRffCkoh9AFDibarJnjfDc4-j2X5j3YarHZfx3BpMw-XKJSX
Paragraph 3:
 * What type of market would it go through?
Paragraph 4:
* What is the punishment given to the perpetrator?
  * https://www.traffic.org/site/assets/files/2544/w-traps-elephant-rhino-report.pdf
Paragraph 5:
 * What is the cost on the environment/economy?
   * https://www.nature.com/articles/s41467-019-09993-2




Paragraph 1:
There is a monetary incentive for poaching elephants. Each the ivory on a single elephant is worth about $18,000 or about $1,800 per kg (13). Even that is just the wholesale value on the street, it is worth about $6,000 per Kg of carved ivory or about 60,000 per elephant(13). African ivory is more valuable than Asian ivory, since Asian ivory yellows over time(19). Ivory poaching is much more professional than it used to be (16). Poachers are now well-equipped to catch the elephants, using everything between rocket launchers and helicopters (16). Most recruits come from rural areas, and they are often hired by organized crime syndicates (16). Frequently, even the military is involved in the poaching of elephants (16).

It is hard for law enforcement to catch the poachers (16). This is for a couple of reasons. The first is, once ivory enters the supply chain, it is not hard to know if it is legal or not (7).i  Elephants are outside of reserves and are constantly crossing boarders (16).

Paragraph 2:
The ivory on the black market is being sold in two different forms, raw and carved ivory. It also goes through several people before being sold to the end consumer (14). The poachers are the first people in the chain. They take the ivory, sell it to carvers(14). In this stage, the ivory is in a raw form (14). Carvers are the second people in the chain. They are the artisans who take the ivory and carve it into works of art (14). The ivory often turned into items such as pendants, rings, bangles, guru beads, and simple figurines (17). From there, a trader is the third person in the chain. In this stage, the ivory is carved. The traders are the people who sell the ivory to the end consumer (14).

Consumers want ivory for a couple of reasons. The first is ivory is typically used in traditional Chinese medicine (17). They believe that the ivory will remove toxins from the body (17). The second reason is decorative purposes, either as jewelry or ornamental (17). The third is as an investment. Some think that the price of ivory will continue to rise, thus making it a good investment (17). Lastly, it has religious significance. The ivory is made believed to bring good fortune, and it is made of in intelligence (17).

Paragraph 3:

There are three different states of legality that ivory is being sold in. White, black, and gray markets.

The first is the white or legal markets (17). These are usually factories or retail outlets and are well established (17). All white markets must hold licenses for the ivory being sold and be operating within the law (17). The white markets are regulated by the government (17).

The second, Black markets, are split up into two types online and unauthorized outlets (17). These markets are not regulated and unauthorized (17). In online markets, the seller typically directs the client to customer to contact them directly (17). They then sell and transfer the ivory to the buyer (17).

For the third, Gray markets, the ivory is frequently sold in live auctions (17) The legality of these are questionable. They may be completely legit, but there is a good chance that they are not (17). The questionability comes from items claiming that they predate the ban on ivory harvesting (17).

Paragraph 4:

It is hard to quantify the punishment for poaching elephants or trading ivory since there are so many countries involved. Also, some countries are corrupt, so the laws are not enforced (19). The punishment for poaching elephants ranges from a couple of thousand dollars to a lifetime in prison (19). Generally the punishment is towards a couple of thousand dollars side of the spectrum (19).

Paragraph 5:



Notes:
* Once ivory enters the supply chain, it is not hard to know if it is legal or not. (7)


# Related Work

There is one paper is particularly relevant to this paper. 

# Methodology

In this section, we will discuss three things. First, we will talk about filtering through the corpus of tweets to create the dataset. Secondly, the creation and cleaning of the dataset. Thirdly, we will discuss the creation of the model.

Our starting point was 9 IIT Tweets from X paper. Upon further investigation, we realized that 4 of them were not IIT which we will discuss in detail later. For each of the nine tweets’ users, we manually went through the first 100 tweets in their timeline. This gave us another 62 IIT tweets to add to our dataset totaling 71 IIT tweets.

We needed a way to further expand the dataset since fine tuning models like BERT require lots of training data. Finding IIT is essentially like looking through a needle in a haystack, so manually going through every tweet would have been impossible. We needed a way to automatically classify tweets. The tweets that the model had the highest confidence in could be manually labeled by a human. We came up with four ways to resolve this problem: using a corpus of tweets that are known to have IIT, iteratively create a better classifier, and use keyword filtering.

To start, we needed a corpus of tweets that we thought to have a higher likelihood of containing IIT. We wondered if the followers of the 9 IIT sellers from paper X would also be selling IIT. This intuitively would make sense, since groups of people tend to follow each other. We collected the first 100 tweets from all the 9 seed users' followers. The number of followers worked out to be X. Since not all the followers posted 100 tweets, we ended up with 52,911 individual tweets. We then filtered for the keyword of ivory. This left us with X number of tweets. We then manually went through and found X IIT tweets. This demonstrated that the followers did have some IIT tweets.

To get more tweets, we decided to try training a BERT model. We knew that the model would not be accurate, but we thought that it would help filter out non IIT Tweets. For a model we used the huggingface uncased BERT model. We figured that we could then manually go through the tweets that the model was most confident in and filtered by the keyword ivory. If we found tweets that were IIT, we would add them to the dataset. We repeated this process 4 times. Each time we would add the tweets that the previous model found. We also varied the negative examples. We added the false positive from the previous model. We also tried adding negative examples from random users. The number of negative examples varied from a couple hundred to a couple thousand. We realized that having many more negative examples biased the model to predict negative results. If the model was not biased, then we would have had a harder time manually going through the tweets due to the sheer number of tweets.

After the 4 iterations, we had a dataset of 168 unique IIT tweets.

We needed to formalize the dataset so that we could demonstrate that it was possible to build a model that could accurately classify IIT tweets.

Our initial dataset came from four sources:
* 168 tweets we thought contained IIT
* 240 tweets from random users that we thought were not IIT
* 131 tweets that one of the models got as a false positive
* 100 tweets that we thought were good from seed users

This totaled 515 initial number of tweets.

Before labeling the dataset, we needed to clean the text. We wanted to respect the user's privacy so we needed to make it harder for the labelers to find the original tweets. There was a second motivation for cleaning the dataset. We wanted to make it easier for the model to learn from the dataset by adding special tokens.

Before labeling all text in the dataset was cleaned using the following steps:
* Replace all URLs with a {{URL}} token.
* Replace all @mentions with a {{MENTION}} token.
* Replace all email addresses with a {{EMAIL}} token.
* Removing all tweets that were not in English.
* Removing all tweets that have duplicate tweet IDs.
  * There were some duplicate texts that were not removed. We latter removed them before training the model.
* Replaced all tweet ids with fake tweet ids so that the labelers would have a harder time finding the original tweet.
  * We created a mapping between the original tweet ids and the fake tweet ids.


The dataset was then converted to a CSV file to upload to share with the labelers. The CSV was in the following format:
*Fake Tweet ID, Tweet Text, User description, labelers label*

* Fake Tweet ID: The fake tweet id that was created to make it harder for the labelers to find the original tweet.
* Tweet Text: The text of the tweet.
* User description: The description of the user from their Twitter profile.
* Labelers Label: The label that the labeler gave to the tweet in a binary value. 1 means that the tweet is IIT, and 0 means that it is not IIT.

The labelers were also given the images associated with the tweets. Sometimes there were more than one image per tweet and other times there were none. All tweets were labeled with fake tweet id followed by an image counter for that tweet id. This allowed the labelers to look at the images while labeling the tweets. 

The criteria that the labelers used to label the tweets were:
* The item looks like it could potentially be bought 
  * The user says to go to their website to buy it  
  * The user says to contact them for details
  * The user is a business that the item can be bought at based on the user description, E.g. auctioneer, antique dealer
* The person is trying to or already bought ivory
  * The user is asking buy ivory
  * The user said that they bought a piece of ivory
* Not selling an item, but pointing users to a website place to buy/sell ivory  
  * Buy ivory at this website
  * Buy ivory at this location
* The item is ivory
  * The user claims it is made of ivory and the item could potentially be made of ivory
  * The item has schreger lines in the image and looks like ivory


The dataset was labeled by three volunteers. Labeling happened in two stages. The first stage was each labeler labeled each tweet individually. The labels from all three labelers agreed 85.8% of the time from this stage. In the second stage, the labelers worked together.  When the labelers disagreed on a tweet, each person would explain why they picked a label they did. The labelers then relabeled the tweet if they decided that the argument changed their opinion. After stage 2, the labelers agreed on 99.6% of the tweets. There were only two tweets that the labelers disagreed on. The final labels for these tweets were decided by majority voting.

The final dataset had 315 tweets without IIT and 177 tweets with IIT totaling 492 tweets.

The dataset then needed to be cleaned a second time before being converted to a format that the model could understand. The dataset was cleaned in the following steps:
* Remove all &amp; characters using beautiful soup These were fragments of HTML that were not removed.
* Remove all Tweets with duplicate text. Some duplicate tweets were not removed before labeling because they had different tweet ids which we were checking for.

We wanted to try training the model on three variations of the dataset. The first variation, with just the tweets text. The second variation with the tweets text and the user description. The third variation with the tweets text, the user description, and optical character recognition (OCR) of the images. 
To obtain the OCR of the images, we used the following steps:
* Run teseract on each image.
* If the tweet has more that one image combine the text from all the images using spaces.
* Replace all URLs with a {{URL}} token.
* Replace all @mentions with a {{MENTION}} token.
* Replace all email addresses with a {{EMAIL}} token.
* Clean using beautiful soup.

The first variation with just the tweets text was used to train the model. We used a train, validation, and test split of 80%, 10%, and 10% respectively. The data was split using a stratified split. The token length was set to 95 since that was the max token length in the dataset. The model was run on a tenfold cross validation. The model was trained on the training data and tested on the test data. The model was then saved.

The second variation with the tweets text and the user description was used to train the model. In between the text and user description we added the token [sep] to tell the model we were transitioning to the next section of the dataset. If there was no user description (not all Twitter users have descriptions), we put [nodes] which we added as a custom token to the model.   We used a train, validation, and test split of 80%, 10%, and 10% respectively. The data was split using a stratified split. The token length was set to 137 since that was the max token length in the dataset. The model was run on a tenfold cross validation. The model was trained on the training data and tested on the test data. The model was then saved.

The third variation with the tweets text, the user description, and optical character recognition (OCR) of the images from the tweet was used to train the model. In between the text and user description, we added the token [sep] to tell the model we were transitioning to the next section of the dataset. If there was no user description (not all Twitter users have descriptions), we put [nodes] which we added as a custom token to the model. In between the user description and the OCR, we added the token [sep] to tell the model we were transitioning to the next section of the dataset. If there was no OCR, we put [noocr] which we added as a custom token to the model.   We used a train, validation, and test split of 80%, 10%, and 10% respectively. The data was split using a stratified split. The token length was set to 476 since that was the max token length in the dataset. We also tried a token length of 313 since there was only one tweet with a token length of 476 and we thought it was an outlier. The model was run on a tenfold cross validation. The model was trained on the training data and tested on the test data. The model was then saved.


Finally, the BERT model that we used was bert-uncased from huggingface. We fine-tuned the model using the huggingface glue_run example code. We also added the custom tokens to the model: [nodes], [noocr], {{URL}}, {{MENTION}}, and {{EMAIL}}.

# Results

To get our final results, we ran tenfold cross validation on the model. We ran the model on all three variations of the dataset with the parameters listed above. The results can be seen in figures 1-5. For OCR we used a token length of 476 since that was the max token length in the dataset. We also tried a token length of 313 since there was only one tweet with a token length of 476 and we thought it was an outlier. 




* F1 scores
* 
Classification reports
Which component is useful

First part is the best 

What needs to go in
The final scores of the model
How the data was cleaned/prepared
What OCR was used


Talk about whether text/user/ocr is better

Followers were selling IIT 
https://docs.google.com/presentation/d/1gzPUlcziiGEmOf_Mx2C0TlcWHTWMnB6cIyZkayEW0wU/edit#slide=id.g10f0465fa01_0_2
https://docs.google.com/presentation/d/1rQ46gBQMZT4DFS7VAlO30CEwS22B2gNyk_FBatZnBTk/edit#slide=id.g10f0465fa01_0_2



BERT model
Model that is being used
Hyperparameters
Token length
Ten-fold results
What tokenizer is being used
Custom words
Dataset
What the final split ended up being
What our agreement ratio is
How many tweets are in the dataset
How the dataset was cleaned
What format the dataset is stored in
The token length for each result
How the strings were put together for the user description/OCR

# Analysis

## Seed Tweets

Originally, we took the seed Tweets at face value and assumed that their labels were correct. When we were labeling the dataset, we discovered that 4 out if the 9 seed tweets were labeled incorrectly. They were not IIT. We will discuss the analysis of these tweets in this section.

### Figure 7.
In the figure 7 the Tweet clearly states that the item is made of “french ivory”. French ivory is a term for plastic that is made to resemble ivory. It is a plastic, not an ivory. Furthermore, looking at the image, there are no schreger lines. This is what makes us believe that the item is made of plastic, not ivory.

We realized that the tweet text and image in Figure 7 was identical to a second tweet in the seed tweets. The user that posted the tweets were different accounts, along with the tweet IDs being different. This makes us believe that the two accounts might be the same person due to the fact that they posted the same tweet.

The tweet in Figure 7 along with its duplicate tweet were what accounted for two of the incorrectly labeled seed tweets.

### Figure 8.

In Figure 8 we find no evidence that the tweet contains ivory. The text does not state that the item is made of ivory. The image also does not show any signs of ivory. We believe that the original labelers might have gotten confused by the white clock face. Upon further inspection, though, it is clear that it is made of wood. This is because of the following reasons:
* The clock face shows no signs of schreger lines.
* The clock face is too large to be made of ivory.

For those reasons, we believe that the tweet in Figure 8 is not an IIT tweet.

### Figure 9.

In figure 9 it clearly states that the item is made of French ivory. For the same reasons as in Figure 7, we believe that the tweet in Figure 9 is not an IIT tweet.




# Citations
Used:

Might be useful:
1. https://onlinelibrary.wiley.com/doi/epdf/10.2307/1244594?saml_referrer
   1. ECONOMICS OT ANTIPOACHING ENFORCEMENT AND THE IVORY TRADE BAN
2. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0076539
   1. Dissecting the Illegal Ivory Trade: An Analysis of Ivory Seizures Data
3. https://www.animallaw.info/article/international-strategy-ivory-trade-ban-united-states-and-china#sintro
   1. The (Inter)national Strategy: An Ivory Trade Ban In The United States And China
4. https://www.animallaw.info/article/international-strategy-ivory-trade-ban-united-states-and-china#sintro
   1. The (Inter)national Strategy: An Ivory Trade Ban In The United States And China
5. https://www.federalregister.gov/documents/2016/06/06/2016-13173/endangered-and-threatened-wildlife-and-plants-revision-of-the-section-4d-rule-for-the-african?utm_campaign=subscription+mailing+list&utm_medium=email&utm_source=federalregister.gov
   1. Endangered and Threatened Wildlife and Plants; Revision of the Section 4(d) Rule for the African Elephant (Loxodonta africana
6. https://www.nationalgeographic.com/newsletters/animals/article/is-elephant-poaching-declining-june-25
   1. Is elephant poaching really declining?
7. https://conbio.onlinelibrary.wiley.com/doi/epdf/10.1111/cobi.12377?saml_referrer
   1. Legal ivory trade in a corrupt world and its impact on African elephant populations
8. https://link.springer.com/content/pdf/10.1007/s10745-004-6097-7.pdf
   1. The Human Ecology of World Systems in East Africa: The Impact of the Ivory Trade
9.  https://cites.org/eng/news/pr/African_elephant_poaching_down_ivory_seizures_up_and_hit_record_high_24102017
    1. CITES: African elephant poaching down, ivory seizures up and hit record high
10. https://esajournals.onlinelibrary.wiley.com/doi/full/10.1002/fee.1325?casa_token=0ARyyjyH4BkAAAAA%3AR2LPO7naoeZZao9VQaOPRFOM4cND_bgj8OkqmTmSkJhyfMhZeohax1-5T3v0CDMy-mDP-qbGQB0LvQc
    1.  Tools and terms for understanding illegal wildlife trade
11. https://www.sciencedirect.com/science/article/pii/S2351989420306867
    1.  Will legal international rhino horn trade save wild rhino populations?
12. https://www.frontiersin.org/articles/10.3389/fdata.2019.00028/full
    1.  Use of Machine Learning to Detect Wildlife Product Promotion and Sales on Twitter
13. https://awionline.org/awi-quarterly/2013-winter/elephant-slaughter-escalates-illegal-ivory-market-thrives
    1.  Elephant Slaughter Escalates as Illegal Ivory Market Thrives
14. https://savetheelephants.org/wp-content/uploads/2016/11/2000IvoryMarketsAfrica.pdf
    1.  Ivory markets in Africa
15. https://academic.oup.com/bjc/article/49/4/451/325177?login=true
    1.  The International Ban on Ivory Sales and its Effects on Elephant Poaching in Africa 
16. https://ciaotest.cc.columbia.edu/journals/wpj/v30i2/f_0032841_26713.pdf
    1.  Rethinking Ivory: Why Trade in Tusks Won't Go Away
17. https://www.sciencedirect.com/science/article/pii/S0006320714003371?casa_token=mPIoUMnwWKsAAAAA:SUYLf-WeIuLUkIFUx_WScNW9AVW9kMGYTidrIdNzMTBprz9xXk0h7qNvdnR5oj27X_dBo4jW
    1.  Elephant ivory trade in China: Trends and drivers
18. https://www.traffic.org/site/assets/files/2544/w-traps-elephant-rhino-report.pdf
    1.  ILLEGAL TRADE IN IVORY AND RHINO HORN
19. https://www.animallaw.info/article/detailed-discussion-elephants-and-ivory-trade
    1.  Detailed Discussion of Elephants and the Ivory Trade