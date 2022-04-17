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

Example: 
This project was divided into three phases as shown in Figure 5. The first phase was to
create a custom natural language processing (NLP) pipeline using spaCy (SpaCy, 2021) to
process EAGLE reports and apply named entity recognition (NER) and relation extraction to
identify information valuable to wildlife trafficking analysts. The second phase was creating a
database to organize and store the extracted information. The third phase was to effectively
visualize the contents of the database (Tableau, 2021).

Phase 1:
* Create a dataset large enough to seed the BERT model. 
Phase 2:    
* 







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