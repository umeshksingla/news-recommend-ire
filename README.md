# Personalized News Recommendation (Stream Data Based)

## Objective
The purpose of our project is to study reinforcement learning approaches to building a article recommender system. 

## Problem 
We formulate the problem of interactive recommendation as a contextual multi-armed bandit, learning user preferences recommending new articles and receiving their ratings. 

## Solution

We show that using reinforcement learning solves the problem of exploitation-exploration trade-off and the cold-start problem. We explore a content based approach as well as a collaborative filtering approach and both yield viable recommendation results. We implemented LinUCB, Hybrid LinUCB, ε-Greedy and Random Algorithms and also compared them. We also incoorporate data preprocessing by generating user dataset and then form feature vectors for user and article.

## Technical Details

### Algorithms

#### LinUCB
A state-of-art contextual bandit algorithm. It select arms based on an upper confidence bound of the estimated reward with given context vectors. LinUCB assume that users/bandits parameters are independent with each other. And LinUCB only works with the observed features and does not consider hidden features.

#### Hybrid LinUCB
Hybrid LinUCB works similar to LinUCB algorithm but the only difference lies in the fact that it incooporates the dependency between user and articles, i.e, user-article interaction is involved. They are not treated independently.

#### Comparisons
`ε-Greedy` algorithm always takes whatever action seems best at the present moment, even when that decision might lead to bad long term consequences. The ε-Greedy algorithm is almost a greedy algorithm because it generally exploits the best available option, but every once in a while the epsilon-Greedy algorithm explores the other available options. The best action is selected for a proportion `1 − ε` of the trials, and a action is selected at random (with uniform probability) for a proportion `ε`. A typical parameter value might be `ε = 0.1`, but this can vary widely depending on circumstances and predilections. This make no use of user-article information.

`Random` algorithm chooses randomly an artticle from the pool with equal probability. This doesn't require any parameter and also doesn't learn anything over time.

#### Simulation
* To run the code of algorithms:  
`jupyter notebook /src/LinUCB.ipynb`
* To get user feature vector:  
`python /src/user_feature_extraction.py`
* Similarly for article feature vector:  
`python /src/article_feature_extraction.py`

After executing the above commands you will find your article and user feature vector csv files in files folder and ipython notebook showcases the comparison of implemented algorithms based on certain parameter. To get the evaluation metric run python /src/evaluation.py which comprises of HIT@K, NDCG@K, MAP and many other mtrics for evaluation.

##### Note: 
* Use `python>=2.7.13`
* Not necessarily tested for script use
* Write to us for any implementation clarity at umeshksingla@gmail.com or shreyajainryp@gmail.com.
