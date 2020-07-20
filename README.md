# OiT_Twitter_Bot_2020

Overview: In Summer 2020, I had the opportunity to intern with Out in Tech as their Programs and Communications Intern. My primary objective was to brainstorm and execute strategies to grow the Out in Tech community. The OiT_Twitter_Bot_2020 is a Twitter bot that favorites and replies to tweets involving the phrase "outintech". Ideally, this would be associated with the Out in Tech Twitter account and deployed onto Heroku. Tweets related to Out in Tech would be supported, a ripple effect across Twitter's platform would be curated, and additional exposure would be created.

Follow Out in Tech on Twitter: https://twitter.com/OutInTech

For more information about Out in Tech: https://outintech.com/

Upon testing out my code, I tried to like tweets with different variations of the phrase "outintech" to find the intersection of efficiency and effectiveness.
![](images/tweet_one.png)

I discovered here that searching for the phrase "@outintech" is not effective, it practically does nothing. However, when searching for the phrase "outintech", the tweets involving "@outintech" is liked.
![](images/tweet_two.png)

In this scenario, I tried to search for the phrase "out in tech" and as you can see the results were not promising at all. Looking up "out in tech" translated to liking tweets that contained "out", "in", and "tech". Interestingly enough none of my tweets were liked therefore, I removed this as a search option.
![](images/tweet_three.png)

The same situation evolving around "@outintech" applies to the phrase "#outintech". In conclusion, searching for the phrase "outintech" captures a large scope and is very versatile.
![](images/tweet_four.png)

Along with favoriting tweets associated with Out in Tech, the Twitter bot also responds to tweets. An issue I came across was when I ran the code in small batches; a thread of replied tweets began to form. This occurs because in the comment itself mentions "outintech". This can be easily prevented by avoiding using the search phrase in the tweet. At this time the best workaround is to run big batch less frequently versus small batches frequently.
![](images/comment_one.png)
