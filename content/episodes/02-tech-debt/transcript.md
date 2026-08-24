---
headless: true
---

What's it going to be today?

Um, today the big uh sign on the wall says tech.

You wrote you wrote you wrote a you wrote a blog post about it.

I recently wrote a blog post about it. But I think more more importantly it's something that uh came um that I witnessed in my career so many times and um it was always the thing that someone approached me or there was this vague feeling inside an organization. behavior are too slow, some things off. We have bugs and if you look closer, it's always in most of the cases it's teched where someone tried to shortcut things which worked brilliantly brilliantly at the beginning and then after some time everything breaks down and I think that's an important topic

and and I heard that probably we will also talk about books again.

We're going to talk about books as always. We have many book recommendations for everyone and um we will do this of course. Yes.

Let's kick it off.

Let's kick this off.

Hi Raf.

We again.

It's this time of the day again. Yes.

Yay. Looking forward already.

Me too. So, what are we going to talk about today?

What topic?

As we as we said in the intro,

you wrote a you wrote a interesting article about technical depth.

No way.

Yes, you did.

I did.

I liked it.

That's true.

But I didn't understand it.

Of course. I also didn't understand it. It was totally written by Chad GPT. So, uh we have to investigate what it says.

both of us.

Let's look into it.

Let's look into it. So, um yeah. So um tech depth is the big theme and um tech depth can kill your can can kill your company. So this is how I how I phrased it and I I really mean it. So and I've seen this multiple times when working with clients and also with companies. Um companies start with software. Um they write software. They're eagerly trying to get product market fit. Um they prioritize um features and front-end development and getting something out of the door over fixing issues in the back end or creating tests or um yeah fixing getting the database schema correctly set up which isn't a big deal per se. So you of course if you don't write tests your software won't break down immediately. Um if you don't have the perfect database schema that's also fine won't impact you but what what I was able to witness is that at some point some something strange happens and that is um the feeling the strange feeling inside the company that we are very slow for whatever reason you know

um deploying something becomes very So classic example is you originally you deploy it maybe multiple times a day then this becomes too errorprone so it's once a month or it's once a week with the QA cycles then twice a month and then only one month and so if you only if you have the ability to deploy only once a month you have a problem because then you are not agile anymore as a business you cannot react to the market quickly enough and That's a huge problem. And even if you only deploy once a month, um you will still have bugs. You will still have to redeploy.

You still have this very bad side between QA engineers and so on. And that's that's a huge problem. This is tech debt. And I think the reason again the reason is tech debt. So if your company is low, one of the main reasons is tech debt. So um what I then what I think and so tech is something that's for a business person is very very abstract. So what's tech that I mean of course if you tell me that we can deploy faster without writing tests then deploy faster and write the software faster right um but um as you as an engineer or as an engineering manager your responsibility is to really highlight the downsides of uh accumulating tech depth that's the important part and um for for me it's it's four areas Again coming back to the blog post it's it's four things. First of all, you you lose your ability to hire good engineers, which is um not very obvious at the beginning, but if you don't maintain your frameworks, for instance, so if you have let's say you have Angular and you have outdated Angular versions, if you want to hire new Angular engineers and you have to tell them, hey, we using Angular that totally outdated version with security flaws um in a like in a state of eight years ago, you likely won't get um excitement in those um right

candidates, right? So that's that's one of the problems. Another problem which is um especially for backend frameworks but also for front end frameworks it's security. Security of course is always an afterthought and uh as long as you don't have any security incidents then everything is fine but um for you as a leader as an engine manager as a tech league as an CTO it's your responsibility to make sure that you don't have any security incidents and you have to invest in this heavily and you have to make sure that it doesn't happen as much as possible. It's a But one thing you don't want to have is outdated PHP versions running outdated PHP frameworks for instance or outdated Java versions. Java had al also many huge security issues with the logging frameworks recently. You don't want to have this. But if you have this in place, you have such a huge attack surface um that this can kill your company, your reputation.

If you have hackers that kind of get all the emails and send bogus emails out and uh if it's about payments, it's even worse. So security is another thing. The delivery speed, that's something I mentioned at the beginning. Um it will fall off a cliff. So um you simply very very slow, very buggy. Everything feels like a huge issue. And um you also see this especially when um you have to upgrade your your your frameworks. So I mentioned Angular at the beginning. If you have an outdated Angular version that's maybe as old as like 8 years upgrading this 8-year-old Angular version that's not just I will upgrade um this library. It's a huge amount of work. Like the whole framework will have changed. It will take maybe multiple months and it's a huge thing.

Breaking changes. Yeah. Yeah. And that's that's also like a a vicious cycle because you know it's painful, you won't do it. It will be even more painful then still painful. You won't do it and then you of will will accumulate all these huge problems not being able to hire top staff um security issues, slow delivery. It's, you know, it's a vicious cycle and that's what tech that is and you have to be very very vocal um about this as a tech leader and make sure that your teams don't um accumulate so much tech that because it might ultimately kill the business, right? So that's that's my my rough take on this and um yeah so I mean h what is tech for you? How do you manage this? Well, I I think you mentioned already um something interesting here that resonated immediately with me like how do I explain tech to people that are not from the from the technology uh department.

Um, I think that's that's the the most difficult thing for me. Like a a manager wouldn't tell a mason how to build a wall or a carpenter on how to uh fit the door into the wall and all of these things. But for some reason, there seems to be this possibility to tell software engineers on what part of their craftsmanship um they should do and what not. Like I don't know how often I heard then don't write tests or skip these tests or don't do this for like we don't need to upgrade our libraries and all of these things. We can just continue with what we have because it works.

Yeah. But if you if you're talking about tests, I mean tests, I kind of um the manager or the product manager whatever expecting not to not to write too many tests to make development faster because you can write tests until the end of your life and this won't won't benefit the business. So there is you have to have a good feeling how much it is worth testing and on what level

right? So, and of course you can kind of gorge this in one direction or in the

My my point is more towards the non- tech people are telling tech people on what's important and what's not important as part of their behaviors, their processes and their craftsmanship. From my perspective, this is craftsmanship that we have. And and when the same people would uh see their house that is being built uh and and all of the spec experts and craftsmen working on this, they probably will not feel as comfortable in telling them, oh no, you don't need this plumbing or no, you don't need this electrical line there. You can put it somewhere else. They wouldn't do that. So, so and explaining the concept of technical depth to these people is one of the let's say key success factors in being able to make progress. I mean, you can also make progress by ignoring all of these people and just doing your own thing. And if it's your own company, then probably you will be successful.

But if you are an employee and then you're going like people think that you go rogue because you're ignoring their requests or you're ignoring what they was were asking of you then there's a high chance that you won't belong inside the company. Rather the difficult part is how do you explain the concept of technical depth and the concept of interests and interests on interest. uh like this comes from the banking industry and everyone understands how interests work and how depth work but how does it re actually relate to what we're doing in technology that's I think a critical aspect of being successful as a manager as a leader and being able to make progress and make the make the environment and the system grow with the needs of the

and and what would what would you what would you recommend um when I mean you can write software in different ways and sometimes you just want to create a P you know want to try out if this like front end works what of course then happens is that the front end will be in production forever but if you want just want to try out how this works then you don't write too many tests right

correct right and how do you deal with th those situations because then you end up with untested software in production would you then

kind of demand hey my engineers need more time to kind of stabilize the development and add tests or would you just block this on my tech depth board and deal with it later or

so I will I will reply the way how you often reply to when I'm asking you a few things. It depends. It depends. There's there's there's some context necessary. Let's let's set the context. Um when you are an early startup and you're trying to find product market fit, technical depth is not something that you care too much about. I would say it depends on the on the product that you're building but like it needs to fulfill some minimal quality requirements so that the few customers that you have on your can show you yes you are on the right track or not right so a product where constantly your login fails so people can't even access your the value proposition that you're providing that's a no-go and you need to fix that and you need to keep that fixed all the time

if you are in established company, you have your hundreds and thousands of customers already. Um, then constantly delivering quality that is being expected from these hundreds of thousands of customers is a different aspect than if you are a startup and you have a few hundred or maybe just a few dozen. Um, so that aspect is something that is influencing how I'm answering. So now I'm going into the into into my answer mode. I'm assuming you already have an an established product. I'm assuming that you already have uh a significant number of of of of customers and you are continuing to develop your pro your product. In that case, I need to differentiate between what is it that we're trying to achieve here? Are we trying to build a pro proof of concept?

Then there are there's a rule set behind or around this proof of concept process that allows people more flexibility but it's also very clear this will not go to production or if it goes to production it will be restricted to I don't know 1% of the customers or 0.5% of the customers so that we can gain the information that we want from the proof of concept. If this is on the other hand something that needs to go to production because it went through all the tests and it went off through all of the processes that make us sure that that help us understand that we're developing the product in the right direction. Then it needs to fulfill a few requirements that we have. We call them something like there's a concept of a definition of a definition of done which is not to be mixed up with acceptance criteria. Two different things.

Yeah. Uh the definition of done is uh something that says oh we wrote the test that we need. Oh it's running in the with the with the um uh technologies that we have agreed on. So it it also has a a runbook so that the people that are on on on call in the middle of the night know what to do and how to do it. Uh we have our locks where they belong to. We have the metrics and so on and so on. That's it's all part of the definition of done. So I need to clarify first before people start working on something that is it is it proof of concept and you can do whatever you want like wild west kind of approach or is it going to production now it's not always so easy and so clear and and uh we are here to support the business to be successful so I I don't feel that being dogmatic about these things is is um helping me and being successful and helping the company being successful. So if there is this gray area in between where oh this proof of concept was went really well and we want to expand it what do we do. So what normally happens is that there is a conversation ongoing like how urgent is it how much time do we have to make this like there's this very very important customer that is really wanting to use this feature now that is a P actually in production and if we don't do this we lose X amount of revenue.

Our job as engineering is to support that. But it's a negotiation that then starts and that is okay if we do this then you have to promise and we will get the capacity and the time to fix this at a later point. We will define the later point and it will make us slower later because if we don't then we have collected technical depth. We made a conscious decision to take a shortcut to to use a workaround whatever and now we need to pay the interest on this because it it will make us slower for the next feature and the next feature and the next feature. It's like building balconies on balconies. There's a limit of balconies that you can build on each

Do you track your tech debt somewhere or how much time you invest in in certain areas? So building new products versus maintaining old ones or do you track this and do you see some kind of tendencies or some

Yes. So

there are metrics that that I'm tracking. I'm starting very simple with Dora metrics. Um coming from the book accelerate we like books talking about books.

Accelerate one of the main books everyone should read I Um and there are some metrics that help me understand on how how good we are and with regards to our let's say deployment phase.

But these metrics are a resulting um metric of things that are also happening before. So for instance, I don't only look at the at the cycle time for a release. I actually look at the whole lead time that um a certain feature takes in from the development until the release. Yeah. So I expanded that metric for for my teams and then if I see that a certain like threshold oh it's something is taking more than two um I have a metric where I can see like a dot uh going higher and higher on the on the list like a colleague of mine says like oh we have balloons that are like ballooning up into the sky

that's when we are able to look into and figure out what's going on like what's happening by wises.

That's that's wonderful. And of course, if you have an organization, as I said at the beginning, that is only able to deploy once a month, you will see those bubbles quite a lot.

Yeah, exactly. That's good. Yeah, that's also why I like these accelerate metrics. That's always what I keep on saying, hey, we have to have the ability to deploy multiple times a day. And then everyone says, yeah, but we don't need to deploy multiple times a day, you know. And the answer is of course no. We don't need to. But we have to have the ability because if you have the ability then everything is okay. But if you don't have this ability anymore, you will have problems like missing tests, missing automated tests, strange QA setup, buggy software, whatever. And we don't want to have this

the whole class of problems. We don't want to have that.

There's this saying like if it hurts, do it more often. Um, so if it's so hurtful to to deploy the software, then try to do it more often because then the engineers you hired very intelligent and smart and and capable engineers, they will figure out a way on how to make it less painful because like one of the skills that an engineer has, at least I'm I'm now looking at myself, is I'm lazy and I don't want to have this

That's that's a leadership um trait, not an engineering trait.

Oh, okay. I'll I'll take it. I also seen engineers that are like removing just around of course.

Yeah. So um having metrics is is is one way uh how to look at technical depth. Um we also have something like architectural records like decision

That's nice.

Uh we're using them whenever we're taking shortcuts. Um and they're owned by the CTO. So the CTO is overseeing them. I'm not the CTO. and working very closely with the CTO on this and therefore um this group of people that are like taking care about our architecture and the way how the system is evolving they are paying attention to these things and uh at some point we make decisions. So for instance we made a decision like when we were moving from our monoliths to from our monolith excuse me uh into a serviceoriented architecture microser etc. Like there was a decision by by the CTO and me where we said like every change that goes into the monolith needs to be going through our desk because we don't want any changes in the monolith anymore. we want you to think about how we can expand this into this serviceoriented architecture which made it more painful for them. They had to move it or they voluntarily moved into the different direction because they didn't want to wait for

uh getting the okay from the SVP or from the CTO.

Yeah. So going back to the to the tickets or to the Yeah. to the ticketing structure you're using, do you like do you uh label the tickets? um in what area these tickets are like removing tech depth, improving existing stuff, new stuff. Do you have an over do you have an oversight there?

Yes, we're using Jira like probably 80% of of the rest of the engine.

That's what everyone is using Jira

Yeah, because like Jira is a jugger of all trades or you can also give it different names. Um still um uh we're using labels for this uh and we're labeling uh the G each ticket. Uh we also have a few let's say components that allow us like the labels and components help us understand and we also have ticket types. So we have like maintenance tickets for instance when we when we're updating or upgrading um libraries because they got outdated. There's a rule where I'm saying like I don't want any of our third party uh libraries to be behind more than three minor versions because I don't want to have this pain of like what you described like having like an 8-year-old I I I used to work in a company where we were still working with PHP.

Uh but it was like at times where we I think PHP 5 was out and we still had code that wasn't PHP 3.

Okay. And we had exactly those those moments where engineers were like we're in interviews and telling them this is what we had to do and they were like

yeah we don't want to join your company.

I don't want that.

Yeah. So for the so this um like labeling of tickets that's um super interesting and also an approach I'm using when uh I want to communicate what the engineering department is actually doing and also get the buy in from the uh and to get the let's say the the allowance to spend time fixing bugs because what we're using in the end you have to have some kind of investment framework with which actually is related to capitalization ation which is a different topic now um but the CFO will love this but what I want to know when I'm looking at the department is um how much of the work is dedicated to like new products improving existing features

improving productivity and keeping the lights on and um you should have a certain percentages what you um uh what you spend on each area. So and if you say that's let's say keeping the lights on these are things like upgrading libraries um yeah doing daily work business such kind of things fixing bugs that's also keeping the lights on but if this if this area where you maybe initially said this should be not more than 20% of our ticket volume or time we spend is growing to 40 50% then this tells you something you see the graph like going up going up more tech depth people are fixing box box and then it's time to really improve this. And this is also an a good um a good graph that you can show to management. Okay, this is what we're having right now. Um and we have to um invest in like reducing the keeping lights keeping the lights on type of um area and stuff and things we're doing there. So that's why you have another area which is improved productivity and improved productivity would mean reducing keeping the lights on. That's a very simple investment framework that was I think a couple of years ago published by Dropbox. Dropbox is using this and this is very very helpful to actively manage tech depth make it visible and also reduce it later are at the spot.

Do you have a do you have a number in mind? You just said uh 20%. No, you said no 20%.

Yeah, 20%. I think it depends. It depends um on the company where you are. But being cautious uh conscious about these numbers is I think the important

Because of course most of your of your of the time of your engineers should be spent on creating new products and improving existing products. Right. So product work. So this should be I don't know 60 70% and fixing bugs should not take most of your time and um but if fixing bugs becomes a huge amount of time or a huge block then uh you have to you have to act you can make this visible but if you don't know what the people are working on you can't make this visible so you have a hard time using tech circle again so making this visible important and then also getting the me message across the board or the the C level is then um very easy and it's also your duty as CTO or leadership position doing that.

Yeah, I I uh I agree with you. So I using a similar concept but I'm I'm giving a fixed number. I'm saying like 25% of the of the engineering capacity belongs to me.

You're doing this differently. Okay. It's it's it's similar because it's not that I'm like very rigid about oh it needs to be 25%. like I'm not I'm I'm tracking this on a monthly basis, but in the end of the year I want to see like roughly where did we end up because like it's always a a taking a giving and taking and and um sometimes we have maybe a few more bucks and therefore like we need to invest a little bit more but sometimes uh product wants to deliver this one feature because of a deadline or because of a trade fair or whatever and then it's totally fine that it gets reduced to like 15% Um I think the important part is we have to track it. We have to we have to track it and we need to get an understanding when it's when is something healthy and acceptable and when does it go to something that is unacceptable and unhealthy.

I would even say like if you are ending up into 40% or even higher then you already are in an unhealthy and unhealthy mix.

That's true.

It's maybe then sorry too late.

Yeah. you have to yeah change gears then I guess but um if you're using like 25% for 25% me time in terms of me the SVP or the CTO time um this is basically what I would call then keeping the lights on time or andor improved productivity time of my department so you would say this is like 25% and the rest is then product improvement product feature work

correct and I would even put the bugs in there because like bugs

okay that's also different are not ne necessarily something that uh the technology department decided to put in there. Maybe they are a side effect on how the feature was uh designed to work and and maybe it's an edge case that that we missed or some something like from my perspective product work needs to contain the bugs that that are dealt with because in the end someone needs to also make a decision what bug is worth fixing and what bug is not worth fixing. That should be a product manager doing that kind of decision, not the technology department.

Yeah, I'm not sure if I would agree to be honest. I for me it's I know what you mean. Uh for me it's helpful to see this and like budgeting this or um

Oh, absolutely.

bucketing this into keeping the lights on, then you see it immediately. But you're right because not not every bug is made equal, right? So there are bugs and there are bugs. There are outages and there are bugs and there are nice to have things like I want the color to be a little bit more lighter.

That's a bug,

Yeah. So, you're right. I mean, maybe I should revisit that.

So, I I I have the visibility on the on the on the bugs. I I don't think that number of bugs is is a good performance metric by the way, but it's just like for me it's still it's a metric. It's a metric. It's not a KPI or something like that. But it it gives me a feeling on what's going on in our system. Um still the decision on which bugs are worked on and how many uh a team is taking into into their system into their development like flow um is completely up to them. Um up to a point where I say like okay this is too much we need to look at this differently. We need to approach it differently. That's when the the interest rates are becoming too expensive. You said something else which I find intriguing and that is you said that it will be easy for the CTO to talk to the rest of the business.

I have to say that this is from my perspective one of the most difficult conversations and the most difficult part in the managing technical depth because like I know my jargon. I know I I can talk to engineers all day and I will mostly understand what they talk about and they hopefully will also understand what what I talk about. But that's not the same jargon that I can use when I'm talking to business people, when I'm talking to the CFO and explaining why things are becoming more expensive, when I'm talking to the CEO and telling them why things are as slow as they are. By the way, we're never fast enough. no matter how many people you have and how how good your process is.

I'm always being told, "Please develop a little slower. That's too fast."

I'm just joking.

I never heard that.

I'm just joking.

Good one. Um so so from my perspective a very important aspect of getting your point across on on how to handle and how to manage technical depth is that you're speaking the right language that you're using the words and the and the maybe you're able to create uh examples like I just did in the very beginning talking about building a house and you know telling someone how to

that's wonderful

um and that's I think that's really I'm pretty sure you have been in that

Yeah. Yeah. You have you have to do this totally. So always like I always try to um explain tech in terms of hey um if you have a car you of course can run the car without doing any maintenance but it will show up and at some point your car will break down. So and we have to do the maintenance because we want to run the car for a long time. I like it.

So this this is like one example but you are totally right. What is sometimes very helpful is when like the delivery speed when when you have problems. So if the CEO comes to you and says you know what um we cannot obso the product because it takes forever to kind of upgrade licenses and nobody's knows how to improve the situation. It's like killing us. We are super slow. How does that happen? So if if you have this this this feeling in the whole organization that something is strangely off, this will ease your job. Um of course if you're not responsible for this off thing but um if you have to improve an organization and have to support there then it's always good if there is already some kind of um urgency attached to the topic. So if people know okay there is something is not good we have to change this and then the discussion becomes easy and if you have then good examples with the car for instance or so what you mentioned at the beginning then this um facilitates the discussion and of course and that's another thing um if it of course always helps if the CEO or if the sea level or if the board is kind of technical right so if you are the only technical person in the room

and Everything else is about insurance and ma mathematics or business or

e-commerce it's yeah I don't know that is hard but even the best e-commerce companies let's say u Shopify I mean Shopify is an e-commerce company but um Toby so the CEO for sure knows about tech and he knows when to fix this and that's very very important so it's it always depends but if you have good people also on the CEO level on the C level on the board this helps um just a recommendation you should hire there. But yeah, think of Toby. Toby knows what's going on inside those organizations and in his organization and he's a technical person and it's um very very helpful. And what if you don't

good examples and um yeah that's that's your duty as CTO to really articulate the challenges and make sure that lay out a plan if there's a like a challenge lay out a plan how you can improve that

that is understandable to everyone else that's not very technical. So communication is important and um it's and the same applies as with security. if you don't have any security issues, it either means you are lucky or you have enough security consciousness inside the organization that people just don't let security or it prioritize security. So people prioritize security and they don't have any security issues. so either of the two two is true. And with tech, it's the same. So, if you're at a point where you have a security issue, um it means something was wrong before. And if you have a problem where you have tech that and tech that becomes this item of discussion in the board level, then something went wrong way before. So it's the same same thing with security and you don't want to have tech that as a discussion topic in board and the board level or with the CEO and you don't want to have um security as a discussion item there as well. And um yeah this means you have to deal with it up front. That's your duty as CTO.

If it's if it becomes a problem it actually means your job was not done properly or you didn't do your job properly likely. I think there's a third option and it reminds me on something that Martin Fer um when you when you posted that um blog article I also had to look it up again what Martin Fer wrote about um technical depth um because he created this four quadrant uh um um I think you you've seen that

um what if you don't know that you have technical depth is that still technical depth and and why is it important to know if you have technical depth

did did you already talk about the Dunning Kruger effect.

I think there was like like one podcast we did a long time ago that very talked about the Dunning Kruger effect. Yeah. But this would be the like the Dunning Kruger effect of tech, right? So, um

what's the effect?

Yeah. You think you're writing awesome code at the same time you are accumulating tech that will kill your company. Very simple. And you don't even know that you're accumulating. So, you don't even know that you're even killing the company at that point of time.

Yeah. So, the absence of you not knowing doesn't mean that it doesn't exist.

Um, but this basically means you have to understand where and when your teams are cutting corners or accepting maybe subpar quality and you need to actively manage that.

And looking at bugs and the number of bugs is one way how to do that.

Um, taking tracking these things these decisions in architectural decision records is another way on how to do that. Maybe there are other ways and probably there are many other ways but like like the responsibility and the accountability for making yourself and your environment where there is technical depth and where it is and what to do about it. What are the options that we have? That's a responsibility of the leadership.

Yes, absolutely. And it's a skill issue as well. So if you have um also something I've I've witnessed um if you have like very junior teams or junior developers they will just accept if a product manager says hey we need to go faster please don't write any tests okay we don't write any tests

but that's not technical depth

um it will become technical depth at some point if um development slows down and so on but this is like the root cause of it

and so if the workforce is very junior um it's not their fault I guess you know just they can be overridden. They just think it's the normal way of working and they just write the code the way they've been told and but then of course it's as you've said it's a failure of management. It's a failure of the CTO. It's a failure of the whole organization. So it's a skill issue as

We don't we don't we don't talk about technical depth because we want to find the guilty person. I I once heard that uh guilt is not investigated but guilt is assigned and and you just did it. You assigned it by default to the leadership team. um because it's their it's their accountability and their responsibility to to to figure this out. But they can delegate it obviously, right? They can delegate like tell me where where you see technical depth

to the team. But in the end making the decision on what to do with this and how to approach that is something that is uh lies within the leadership, technical leadership, organizational leadership. We talked about that also.

That's right. So if um if it's always the case for instance that the product or the CPO overrides what the CTO has said if the CTO said you know we can't we can't develop software like that we have to have like a minimum test coverage of let's say 60% or something and then everyone else overrides the CTO or the teams hey please don't write any tests all the time yeah you know where this leads towards so this will generate tech depths and will kill the company potentially but then it's also the fault of either of course the CTO because the CTO accepted it but also of the CPO and of the whole power structure inside the organization. Huge problem. I can't imagine shopify uh doing this but I've seen other companies doing that and that's very very painful. So if leadership doesn't understand the concept and um as also as we've said at the beginning um tries to be to do the job of the CTO right if the CPO tries to do the job of the CTO and know everything better you will have a problem. It's a power structure.

And the CEO let this let that slip. And it just makes me think that we should talk about some at some point maybe in a different uh episode on on on communication especially in technology communicating is is is an art because like the language that we're using the concepts that we have in mind and like it's it's it's very unique. I I have a background in in in economics also in addition also some psychology

um but also in computer science. um which makes me feel more comfortable in in in let's say changing my language. I'm still speaking English but I will like speak the techie English and then the business English and what what not

and not everybody I'm not saying that I'm able to that I'm doing this in a good way. This is for other people to judge but I believe that technical depth highly depends also on how you're commun you're able to communicate on these things. It's absolutely absolutely true and I also think that at some point if you are consultant or if you are want to become CTO it makes sense to learn the language of the business. What language does the CO use? What language does the CEO use? What does HR use? Um and they use also their own language. And at some point in your career you have to get a budget for something. And then you have to know how those budget discussions work. how labor is being calculated and so I think it makes sense at some point to really do kind of an MBA or something where you acquire that knowledge which is then big fun and will facilitate your communication skills and also your path in such such an organization that's the MBA part I think economics and having like a business background economics background is very very important if you want to succeed in in in this area it facilitates it you can also do it yourself it's like not very complicated But yeah, a comprehensive way would be getting an MBA.

I don't have it, but you don't need it, of course. Um, okay. So, let's wrap up, I guess. Um, so main takeaways, tech. what are the main takeaways? Main takeaways would be something like, um, it will kill your company. That's my takeaway because you cannot hire people.

You can read it up.

Yeah. you cannot hire any anyone anymore. Um becomes hiring becomes super hard. Um security issues piled up which can also kill your company in isolation. Upgrading your software is painful and development speed goes down painfully down. So that's why what tech means for me and like I would just shout to everyone please don't accumulate tech depth. Please don't in most of the cases sometimes it's okay but like in most of the cases don't

don't accumulate this which is my takeaway like um it's it's something that we have to negotiate and it's something that we have to track and there's I think there's a limit there's a limit

and who is defining the limit you as the technical leader uh or your your technical leadership group you are defining this together and you need to keep track of this um like it's a it's a giving and taking I I've have not seen a single company so far in my career that doesn't have somewhere some technical depth and it's okay but if you accumulate it like you are describing then it will has a potential to kill to kill your company 100% agree

yes and if you use this uh investment framework that we just briefly discussed your CFO will love you because he can then capitalize the costs and you can use the same framework to really measure how much time goes into keeping the lights on into bucklike kind of work and if this goes um out control you can steer it into the right direction again and make this visible also board level for everyone else

right and last but not least communication is important just just telling the CEO that there is tech nobody will listen to you right

so phrase this differently cool

cool thanks Marco

that was great thank you for a
