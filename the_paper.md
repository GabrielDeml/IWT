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


The illegal ivory trade (IIT) is a major concern in the world today. It is estimated that over XX billion animals are killed each year by illegal trade. Of that, XX are poached for their ivory.  Some of these poached species include the African Elephant, Walrus, and X. To help stop IWT, we are investigating the use of Twitter to identify illegal wildlife trade and potentially remove the offending tweets. We worked under the assumption that if poachers have no clients, they have no incentive to participate in IIT. In this paper we are making two contributions a BERT based machine learning model for identifying IWT and the largest dataset of IIT tweets. We will also discuss the potential impact of this project on the world of wildlife trade.

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

The Fish and Wildlife Service (FWS) prohibits the "import and export of African elephant ivory with limited exceptions for: Musical instruments, items that are part of a traveling exhibition, and items that are part of a household move or inheritance when specific criteria are met; and ivory for law enforcement or genuine scientific purposes." (5) Even with bans in several countries, the African elephant is still being poached. According to national geographic there are 30,000 African elephants poached each year with a continent-wide population of only 400,000 (6). The population of African elephants is decreasing by about XX. Our goal is to create a framework that would make it harder for sellers of IIT to find clients. We believe that if poachers have no clients, they have no incentive to participate in IIT. There have been some past attempts to address this issue, but they were not very successful since they were using clustering instead of a strong machine learning model like BERT. We even found that 4 out of the 9 tweets they found were not actually ivory, but ivory replicas. Using our BERT we were able to identify IIT tweets with XX accuracy. This allows us to create a large dataset of IIT tweets that could be used by future researchers. 

## Motivation 

Example:
The motivation behind this project arose from discussion with domain experts Patricia
Raxter, PhD and Meredith Gore PhD, who emphasized the issue of wildlife trafficking especially
within Africa. Patricia Raxter, PhD is a Subject Matter Expert on transnational wildlife crime.
Meredith Gore, PhD is an associate professor at the University of Maryland whose expertise is in
the human dimensions of wildlife management, and environment and resource policy.
There is a need for an easy process to read through wildlife trafficking reports and media
stories to find trends across illegal wildlife trade seizures. Currently this is a manual process, as
investigators often have to sift through data manually. Experts interviewed acknowledged the
current process is tedious and articles often are not shared between all the experts. Since the
information in these briefings is disjointed it can be difficult for experts to parse through and
identify insights. The reports, as seen in Figure 1, contain descriptions of wildlife trafficking
seizures within different countries across a certain period.

* Motivation:
 * What questions do we want to answer?
 * A brief review of the literature  
 * A short outline of the paper


There were two motivations for this project. The first motivation is to demonstrate that it is possible to automatically classify user generated content. We believe that this model could potentially be applied to a dynamic and high speed platform. this paper focuses on twitter, but the same principles should apply to other platforms as well. We hope that it will demonstrates to media platforms that it is possible and practical to implement an algorithm that automatically removes post that are promoting the sale of IIT. We also hope that this paper would be a good starting point for any platform setting out to implement such an algorithm. The second motivation is to build a large enough dataset of IIT texts that that such platforms can use it as a seed dataset. One of our worst problems was generating our initial dataset to seed the model. We believe that this dataset will be large enough to be used by researchers in the future. 

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

* 






# Citations
Used:

Might be useful:
1. https://onlinelibrary.wiley.com/doi/epdf/10.2307/1244594?saml_referrer
2. https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0076539
3. https://www.animallaw.info/article/international-strategy-ivory-trade-ban-united-states-and-china#sintro
Laws:
4. https://www.animallaw.info/article/international-strategy-ivory-trade-ban-united-states-and-china#sintro
5. https://www.federalregister.gov/documents/2016/06/06/2016-13173/endangered-and-threatened-wildlife-and-plants-revision-of-the-section-4d-rule-for-the-african?utm_campaign=subscription+mailing+list&utm_medium=email&utm_source=federalregister.gov
6. https://www.nationalgeographic.com/newsletters/animals/article/is-elephant-poaching-declining-june-25