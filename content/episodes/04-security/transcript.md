---
headless: true
---

What's the topic for today?

Security and uh specifically application security. I think that's something that as a as a leader as a tech leader everybody needs to think of and uh probably in different stages uh your appetite for risk is different. And uh I hope that we can shed some light on this on at least how we are understanding this.

Yeah, that's that's an important topic and um I mean what what types of security do we have? So, you already mentioned application security. This is a CTO business like um the application developers pulling some libraries, assembling some code, sending data between I don't know, the user and the back end, you know, HTTPS, those kind of things. Is that correct?

This is what I would like to spend most of the time on, but application security is only a subset of something that I would rather call information security. And probably you could even extend it uh through like physical like access security like oh, who do I let into my Um but it's it starts with like yeah. Not just who I let into my building, but um what do I do with my computers? Who has access to my computers? Do I need to have like an uh physical key or um uh do I have a username and password is already something that is part of information security.

And that it all has different let's say easiness on how to exploit that. Uh I don't know if you are aware of this, but I I I think like currently the most um let's say dangerous uh um activities that we have are not that oh, somebody sends a worm or a Trojan or whatever that is, but rather that people are like, I don't finding a USB stick somewhere on the streets and then just plugging it into their computer to see what's on it and boom, there's a security breach. And ideally, you don't do this at home, but you do this of course into in the companies' uh computer because like you wouldn't never do this at home, would you?

And then the whole network suddenly is infected. So, at least that's that's my last standing. But with the rise of AI, um maybe application security will will soon be the one that becomes even um dangerous.

So, USB stick stays as relevant as ever, but then you have application security and someone creating like very bad tools using AI um on top of that. But coming back to the USB key, I mean, we are now all now trained to just a click on hey, accept um this device to access my computer. Yes, no. Yes, accept. Yes, accept. I accept the cookie. I accept the USB key. I accept the USB whatever {question mark} accesses my device because of course you can also embed like a USB attack device inside a USB cable, right? So, you have just a USB cable, looks like a USB cable, works as a USB cable, but it's basically uh like a like a Trojan virus um built into the USB cable as a controller, but then forwards everything to the cable, which looks normal, but then you have something stored in your laptop.

Super easy and um do you have like training courses or how do you train your workforce against those kind of threats?

Because like that's that's real, right? You find those devices on parking spaces next to Google, next to Apple, next to maybe your company. Um how do you raise awareness?

Yeah. So, let me maybe start a little bit differently because what you just said is already an implication in there that there is a training. And and I 100% believe in this because I believe that security is not something that you bolt on to something that is existing. But it's rather something that you have to instill into the mindset of every individual. Like, is what I'm planning to do now a secure action? Am I Am I endangering myself or others if I do this? And then application security, where sometimes we're saying we're trying to move security We're We're shifting security to the left. Uh to the left meaning that we want to integrate security considerations already very, very early into the design process and and basically embed it into the whole software development life cycle. So, that's why we're calling it a secure software development life cycle.

And the way how to do that is through you start with a mindset like like create the mindset of like the world, as much as we want to be a a a beautiful and and and non-dangerous place, is actually a dangerous place, and there are threat actors or malicious people with malicious intent, and they try to exploit things that you are using and you're doing. And first thing that we're doing is create um there is like a very very simple but mandatory training for all of our engineers. Every year it gets repeated, where we ask some some I would say simple questions, but very, very important questions. And that's why we're we're doing this to create the awareness that these things exist. Let me be careful the things because it's also evolving.

Yeah, and is it only engineers, or is it the whole company that has um to notice?

Yeah, and that's the difference between application security and information security. Information security is relevant like for for the whole company. Like, oh, you get an email. What do you do with this email? There's somebody like a you're finding out that you have a rich uncle from Nigeria that wants that that's unfortunately passed, but now is giving you all of the millions of dollars that they have and you click on the link and then that's already a point where you need some training that if it sounds too good to be true, then probably it is too good to be true and somebody else just wants to mess with you.

So, we have So, we have the information security for all the company and then you like we zoom into the engineering departments, which then is the application security. Right, that's how you see this. Right. Yeah, this makes total sense. for the application security, I mean, how do you raise the awareness that it is actually important because the nasty thing about security is that you don't you don't notice immediately when it's not secure, right? It's just I mean, you know, unsafe passwords or missing security best practices in your front end development or back end development. Yeah, you you don't notice this immediately, but how do you preemptively raise awareness and as a CTO, you have to basically get money and resources to spend on security. So, um how would you do this?

And yeah, how how would you do this?

It depends. I'm repeating myself here. It depends because I I believe that I think I've mentioned this in one of the other episodes is like there's a there's a risk that everyone's taking when they're building a product and by investing into this or let's say by defining how much you're investing into this. And when you're a startup and you didn't find product market fit yet, um and you are active maybe in the I don't know. Uh dating industry or something or it's not something that is highly regulated like finance or or medical environment and maybe your appetite for for risk and also the appetite of your customers for using your product because they know you're a startup and they don't really think too much or don't care so much about if their personally identifiable data gets leaked or then you may not invest so much in this and you don't care so much about this in the very beginning because you care about finding a product that is actually loved by the customers so that you can actually generate some money but the moment that you have found this and I'm not saying this is the way how you should do it but I I I I got to learn quite a few are thinking in that way and I'm not blaming them I'm not saying that this is the way how I would do it but it's it's it's the reality that I see and when you're coming to a position where you're saying now security is important now suddenly something happened which needs needs you to rethink this whole thing well you already mentioned one thing providing money for this providing time for this is already a very important part because like if you're asking people to do something but you're not giving them a mandate or giving them resources to to to to to work in this way it's already a bad signal so you have to provide these this mandate and the resources and then is the question what do you do with this money and there's a lot of tooling there's tooling that you can use and there's like a lot of support that you can already get out there like let's let's let's look at something like supply chain attacks what's a supply chain attack what's a supply chain attack so look this up it's when a logistics company no that's wrong the supply chain I mean they were in the press lately quite frequently right they I mean, all of software kind we depend on each other, right? We depend on open source libraries and we have to pull them somewhere from the internet, right? Somewhere.

Uh and that's true for like that's true for us, that's true for Go, that's true for Java, that's true for like Python as well. Uh and of course uh JavaScript as

Especially Java.

Especially JavaScript, yeah. And uh in the news we had a lot of um instances where for instance JavaScript um we had malicious actors replacing libraries that thousands of um of companies use uh and pull each and every day, replace those libraries with for instance, let's say a Bitcoin Bitcoin mining library that then mines Bitcoin instead of rendering I don't know what. That's not too bad. It's just Bitcoin, you know, it's slower and whatever. But when it becomes really malicious is when this library is used to um just copy and paste your env environment, your passwords, and sends them to a server in a very strange uh nation, right?

Um right.

And we have to face it. If you have if you're developing software, you're developing software, and um you have secrets somewhere. And maybe you have your AWS AWS secrets in your root folder of your user directory, and this is then yeah, this is very a very nice target for hackers and supply chain attacks. Libraries you you that's uh one of the prime ways how you can how you can do this. And I have to also admit that one thing that has changed is that I was always told don't execute anything that you get from the internet, be very cautious about this. Yes, um and what we do nowadays is we have um bash scripts that execute uh bash so bash scripts in the internet, right? So we just say, "Hey, curl bash, do this." So we execute um stuff that installed something on our laptop on some kind distance server. And I think this is very very don't do this and find this very strange way, but most of the libraries or many of the of the applications these days work that way. Just execute a distant a best script. I think this is very dangerous because if you change one line it has full access to your laptop, right? It just execute something. You don't know what it does. Very very interesting approach.

But yeah, so this this is basically a supply chain attack. And the question is how can we guard against supply chain attacks? And there are tools for that.

There there is I mean the ecosystem of our or let's say software engineering has become an ecosystem. It's it's more using Legos and and instead of rewriting something that somebody else has already done, we have these libraries so that we're that we're including. It makes us faster and it's it's a good thing, but we have to somehow ensure that what we are in in doesn't have any vulnerabilities and is doing actually what we're what what we want it to do. And there is like there are tools that are helping us identifying this. Like first of all, there's a central database which is like keeping track of vulnerabilities, so-called CVEs. And the maintainers of the libraries are are paying attention because like when somebody finds a vulnerability, obviously they want to close it as fast as possible as a serious developer of a such a library.

And then they create a new new version of it. And then this new version is available but you don't know about it. You don't know that the the version that you have been using of this library is outdated and it has a vulnerability. And there are tools in the in the market that are helping you to identify that.

What what tools?

Oh, there are many tools. I'm not being paid by any one of them just as a disclaimer here, but so far I've I've worked with with sneak with a Y and I've also worked with GitHub dependabot. Um and while they're like promising and delivering way more than that like the two thing the one thing that I used with them the most is is the is the the scanning of all of our libraries and finding out if we have vulnerabilities because it checks against the version that we have installed with the library and if there's a newer version and if there's a if there's a vulnerability in there. And then if there's a vulnerability it tells me hey there's a vulnerability and it if there is a patch if there is a newer version of it it also tells me hey you need to install this new version.

It even can go as far as to provide you the pull request with everything prepared to to just you need to click a button you merge it and then you can deploy it. And if you're super fancy you just automate the whole thing because you created enough tests in your system that allows you to sleep sleep deeply overnight because you trust your system that if there's something broken it won't ship it to production.

Yeah, but that's not where it is sneak and dependabot those two things. And then again both services cost money at scale and actually fixing those things also cost you money because it's not sometimes it's just a pull request and you do something. But more often than that it's hey you have to look at some changed APIs that come with the upgraded library and something that you have to adapt and then you have to test if it's really working and that's still it working that way. So so it costs you real money and so this is actually when we when we go back to where where we started. So at some point as a CTO you have to really you have your road map and you have to have a you have a task on your open pay we have to upgrade X and Y. And then your CEO or your product colleague comes and says hey, this sounds like this has no business value at all, right? So, why do we do this at all? And then it's like, yeah, you know, we have to increase security. But, yeah, I mean, we are secure enough. We don't have any security breaches right now.

But, what I found quite useful, and this is something I've learned from from a colleague Robin who founded Sadia in London, is really pricing the impact of CVEs. So, if you say, "Okay, we have this CVE in that library if this gets exploited, we will have this amount of damage, right? So, you have a price tag. You say, "Okay, if we don't do this, there is this damage, this amount of damage is basically invisible in our P&L, but it's there. So, we have to really get rid of that. Wow." And so, you get some Yeah, you get some monetary values, and this is how you can communicate very easily with a business and also a board.

Do you know how he how he calculates these? Yeah, that's a good question, and this is where it gets tricky when the board asks questions. How do you calculate why is this like Yeah, there is some value. I mean, you have security you you you have security breaches that happened in the past, and you can clearly see what influence these security breaches had on the company valuation in terms of stock market value, in terms of lost revenue, and so on. So, you have kind of a feeling what it will cost you not to fix this. And these values, you can average them, and you can turn them around and mix them, and then you have something if it's kind of similar to that, then we have that amount of damage that's lurking And this is roughly how it works.

And what I've also learned is that like owners of companies, especially if it's if it comes to let's say private equity companies, they are very very interested in having in reducing the risk because they want to sell the company after a couple of years, and if the company value drops massively because you had a security that's not really good for PE. That's not how a PE wants so PE companies are very interested in in those numbers and they want to have um like a high um awareness of security. And um so that's why these companies are very very supportive in establishing a good posture for a company.

So it's more like an approximate Um the the the money value. It's not like you don't you can't take it like as as is. But it's based on findings from similar similar vulnerabilities and the damage that they

Exactly. You you have a company of of with a revenue of X and you have a security uh vulnerability that allows you to have uh remote access under certain circumstances. Like in a similarly real um security incident, this has cost a company of similar size Y or US dollars Y and so you can translate this to your company and can clearly communicate this will cost us this amount of money. I would recommend not paying this and not having this in our invisible P&L but rather fixing

This is um a good way. And usually again the board is on your side if you do this as a CTO.

That's that's kind of interesting. Um Yes, but and then you also get the money and this is where we started. This is this is how you get the money for tools like sneak and and dependabot and a ton of other tools.

There are many tools.

They will cost you money. You get the money if you reduce um this risk for your for the owners and for your company.

Have you heard me say a fool with a tool is still a fool?

It is. It is. It is. I heard you saying

The thing that I always tell people to do first and I learned this is a good friend of mine, who's a very, very, uh, deeply into the security, uh, uh, uh, area, and as a disclaimer, I'm not. But, he always tells me, you first have to know what you have. You need to have something like an asset inventory. You have to understand what are the artifacts that actually are that you are running in production. And then, as a second step, you need to figure out how important are they for your business. And so, what he tells me is credit hearing. Credit hearing system, it can be as simple as is it is it is it containing PII, personal identifiable information. Thank you.

Um, and is it exposed to the internet? And then, you have like, basically, four quadrants, and the if you answer yes to both of these things, then probably this should go into your tier one, which means like the most important thing. And if you find some vulnerability in there, fix it first. And then, if if the answer yes, it runs in production, but it's not exposed to the internet, and no, it doesn't run doesn't run any personal identifiable information, PII, then it has the the lowest tier, tier And that's the thing where many people are like already struggling with, because they don't know, because they have engineers, and many engineers are building a lot of things, and we need to get production running, we need to build this feature, we need to ship it, it needs to work. But, then if you ask them, like, what's actually going on you sometimes get crickets, or, uh, maybe only half of the reality. So, when you are serious about understanding the security posture that you have and improving it, you have to start with understanding what you have.

Yeah, I totally I would totally agree. What's, um, what also helped me quite a lot is making things visible and this is also what you mentioned. So, I mean because you don't do this only on your own. You know that hey, we have like five servers that aren't not really well maintained. Ah, that's super super bad. But hey, write down the servers, use the tearing system. That's a really really good remark. Use the tearing system and then if you have like servers that are super super important to you and you mentioned that hey, we have to fix them. So, we have five servers, like zero of them is fixed you can use this to manage this. You put it on the wall, you tell this like your team in the first quarter we want to fix like 30% of the unmaintained services. Um manage this, but you can also use this in with your C-level colleagues or on the board, right? So, right now we have like 0% of the services unmaintained and then over time first month, second month, third month, you go to hey, 100% of the of our services are now well maintained. We don't have any security risks or known with security risks right now. Went from zero to 100, big success.

So, um super super important thing. What I also found quite interesting is you told us about your friend that is that knows a lot more about security. Yes, that would That's Does this actually mean that modern companies need So, is it a is it a task of the CTO or the let's say the SVP engineering to own security or is it Do you always need like a to manage this and to own this and to have someone that keeps you on your toes as a CTO and as application engineers is kind of the annoying person that always tells you hey, we looked into that this and that service.

How do you do this? What's the Can we CTOs and technical people do this? I I think there's a I think there's a Short answer is I think there's an um that I see with us as a software engineering leaders. Um we have to build security in just that we need to have testability and quality needs to be built in um just like we need to make sure that things are running reliably and can Um that's all within our accountability. Just how do we get there? I believe we need experts and and uh I'm I have never worked with a CISO, chief information security officer. That that's the I've never worked with one but I've worked with security experts.

Um in the past they were reporting to me or they were reporting directly to the CTO. Um but their job was to figure out um what we want and also to support the teams and the training and support the teams in building these things because like um as I said, I don't want security to be bolted on. There's there's there's maybe the possibility that you have like your engineering teams over here. They build stuff and then they throw it over the fence to the quality engineers or the quality assurance people and then they test it and then they move on to the security people and they laugh at what you have built and say like you have to go start from scratch because uh you missed I don't know a cross-site scripting uh uh vulnerability or something or you built built something in that shouldn't be built in there.

I don't want this. I want this to be built in from the very beginning. So having experts that are training the engineers that are maybe also together with engineering creating policies. Like we want to achieve this. Okay, let's write it down. This is what we want to achieve so that we can hold ourselves accountable against it. That needs to be done and supported by I don't know if I really answered your question because I'm kind of dodging it.

No, no, that's I think I think that's a really good answer. So, first of all, it's of course um the responsibility of the CTO. I think it also depends on the size of the company. So, if you have hundreds of thousands of um of employees, um you likely will have um like a chief information security officer. Um if you have like 10 engineers, you likely don't need one, right? So, there is a difference. And like in your case, um if you have a smaller engine Well, if you have an engine organization of let's say 100 engineers, what I found quite useful is um having someone that is responsible for um security, maybe as part as part-time job as part that is a as a leader um of the let's say security um chapter.

And then you have security champions inside each of the teams, and they talk to the security champion that leads the um and or to the security expert, sorry. They talk to each other. And so, you have um the security awareness in all the teams, and you have in each of the teams you have one person responsible for that. We have a sync up to the CTO, and this is one way how you can like, you know, softly introduce security as a topic in the awareness inside these organizations. Really useful.

I love that.

Is is the security champion a a separate role? Like, are you are you hiring a security champion or or how do you do

Yeah, good question. So, in um I I think you can do both. Both can work. It depends on the capabilities of the person. Um in that case, uh this So, the the the security So, security champion is in most of the cases, a security champion is a regular engineer that's kind of interested in the topic of security and where I am in one of the teams. All right, so it's any other person that knows about OWASP, but likes to hack around a little bit, and knows how you can exploit uh HTTP requests from the front end to the back end, and has this kind of awareness.

So, these are your champions inside of the teams. And then you have a security expert that kind of leads them leads them or like a at least syncs with them.

Influential leader and a like a I have the mandate because I have the stripe on my shoulder.

I mean, maybe going back what is a chapter? You have you have teams that um contribute to one of the product areas, stream aligned teams. And then sometimes you have concerns that um are important across all the

Like right, period. Security is something that's important for all the

And so you have um maybe a regular meeting once a week, 1 hour, where all the security um kind of champions uh one person they meet uh with uh in one room, and they have an agenda, they talk about um important news. Let's say um a supply chain attacks that happened in in um JavaScript last week. They make sure that uh that's not a case or an issue for us in each of the teams, And so, often we have the security champions inside the teams, and then you have one person leading those security champions, like influential leader. And that person can be either the uh chief information security officer, or in smaller companies this can be actually the CTO sometimes. Sometimes it's um it's one of the security champions that does this because he's more experienced, and sometimes this is um like a slightly, let's say lower role, not a chief information security officer, but um someone that is on a like let's say VP level, and has to focus on security.

Not only application security, and in our case, but also on the whole uh security posture of the of the company.

This includes the USB keys and the parking lots, right?

Right. So,

that's one way I can do this, but if you don't have um a chief information security officer, uh having the security champions, having the security chapter can be beneficial and a soft way and a good way to introduce this.

Right. I am doing something similar. So, I I can relate.

You just mentioned uh something that uh I think we have not explained yet. You said some I think you said OWASP.

OWASP, yeah.

What's OWASP?

What's OWASP? I don't know if I if you have even pronounced this correctly, but so, um the OWASP top 10 are very important top 12. Is it top 10 or top 12?

Normally, I would talk I talk about the top 10, yeah.

It's uh there are more to them, but uh these are the prime ways our software gets compromised. And it's an organization that

a yearly basis updates the most important security vulnerabilities of software and how you can guide against And so, you have this top 10 list. You have more to them, and you have them for different areas. You have them for software, you have them for um hardware, you have them for different areas. And um this is something you can use as a as a as a boilerplate, so to say, to harden your systems. So, are we really like considering the top 10 security vulnerabilities of software, um are we actually safe um against them, against being hacked? And a good it's a very good starting

So, that's where your training could Train the people to understand the top 10 OWASP vulnerabilities. I think cross-site scripting is still on there, SQL injection is still on there. Like stuff that probably many people have heard about, and if you start training them in how to avoid this or how to identify this in their artifacts, I think you're already on a good on a good road.

And you don't have to reinvent the wheel, so OWASP is really well known and there are um security trainings based on OWASP, so you can just buy the security training. It's not very expensive and you have an very positive impact on your whole organization. Yeah. So, yeah.

So, a fool with a tool is still a fool. That's something that I said. And there are many, many other tools that people can use. Uh I don't know if you've heard about the Burp Suite.

The Burp Suite? I heard about him. Do you use it?

I personally don't use it. My friend is using it and and he tells me great things about it, but there are many, many tools that help you in increasing or improving your security And some of them are more defensive. Um have you heard about this blue teaming and red teaming?

And some of them are more on the offensive side and some of them are trying to find these vulnerabilities actively and tell you about them before someone else does and then help you in identifying and closing them. So, what's red teaming and blue teaming? Red teaming and blue teaming is something that that is being used in the sense of understanding who is an attacker and who is a defender. Normally, the blue teams are the defending teams and the red teams are the are the attacking teams. And when you're looking for uh people that are helping you in your security posture, normally you would start for blue teamers. You would start for people that are on the defending side. But there are many companies, especially big companies, that also have their own red teams. And they they basically ask them to attack and try to breach security within defined uh poss- defined areas.

Thank you. Thank you. Uh but still they're asking them to like okay, see if you can find find a vulnerability, see if you can breach our system so that we can fix it as as fast as possible. And normally like if you're starting with this whole thing, I would rather look for people that are like on the blue team. Um and there are people actually that you can hire um that would do the red teaming for you. It's called penetration testing. Have you heard about penetration testing

I'm joking. Of course I know about

penetration testing. So this is exactly this is uh one of the I guess best practices to have uh someone external testing our systems right in a hopefully good way. And to give you an independent list of things that are actually not okay that you can then fix uh proactively. Um and I think the rule of thumb is to have a penetration test um being done once a year, right?

Once a year. I like that.

And uh another uh rule of thumb is to not always use the same penetration test agency, but uh to use my so to always use a new one. So you get new perspective because if one penetration test agency that does it every year, they get kind of used to it, right? They do always the same stuff. But if you have a different agency doing um each and every year, then you have different angles, different attack vectors, and and different things you can learn from that. So super important, I guess.

That's sound advice. I'm working with an agency which is actually switching the the penetration testers. So I'm still working with the same company, but it's different people um doing the penetration test so that they go they don't get used to to exactly what you just said about. So

And I mean the next step that is also very important for companies is having uh like a security certification that you can uh pin on your website. So there is ISO 27001, there is SOC 2 and a couple of others. And the nice thing about this is first of all some companies need this. So if you have business customers or if you're supplying stuff to the military you will have to have those certifications, right? And but on the other hand it's also very nice for the company yourself and for your CTO they will tell you what to implement what kind of documentation you have to have um um making sure that you are up to date each and every year and get re-certified successfully each and every year means that you have a certain kind of minimal security posture in place that you can post somewhere that has a positive business impact and then it also is also very visible on the let's say board level and in in the end of the for the company valuation, right?

Uh some things right if you get the certification and that's a good thing. So I would always recommend doing this and getting the certifications this always sounds like a huge amount of work. But it's actually not. You can prepare for that and there are also agencies that help you to get the initial certifications up and running, right? And it's really not a huge amount of work you have to put into if you have the right people helping you and the business outcome is very tangible.

Have you done this already?

Yes, I've done this.

Yeah, so you're speaking out of

Yeah, I've done this and um I've also had some help of some great people that supported me in the first certifications and it's actually then smooth more or less smooth going. Depends a little bit what you have in place. But um yeah. Doesn't have to be crazy. if we look into the security sector yeah, there's so many things that we can discuss so many things that we we haven't even not even lightly. but we wanted to give an overview on on what's possible and we wanted to dig deeper in the application security area. I think I hope we did that, but let's find out. If you have to summarize or I will help you with the

There's actually There's actually one thing I guess like the big thing that we didn't talk about, which is AI.

You forgot one.

Oh, yeah.

Mythos and Mythos, I don't even

know how that's pronounced.

Um I think this is I mean, do you think that AI changes something for security? I guess

I was too fast.

It does, right?

Yeah, it does.

This Mythos thing is I don't know if it's only just marketing and I think it's marketing um that hey, our model our new model is so capable we can't actually release it in into the wild because it's so capable, right? But on the other hand, it's actually true. Um if you have those AI agents, um they can automatically find security vulnerabilities. And there's also like good parts and bad parts of AI. The bad parts is that you can use AI tooling and agents in a very easy manner to just search for CVEs and try to exploit your production systems. And not only you can do this, bad actors can do this as well. Right, so and automate this and um I think that's a hypothesis, but I think the amount of security incidents that we're going to see will go up because of that, because it's so easy to have an army of very well capable hackers and uh hacking into systems. We had this before, but then it was like scripts and stuff and now it's even more capable.

Um but on the other hand, um what you can also use, you mentioned this with Snyk um and with um pull requests that get reviewed you can have this with AI as well. So, AI I look into your code, the code you generate, and can find whether this code is actually secure or not secure. Um I've recently talked with a friend of mine, so I also have friends. Oh, don't you? You have friends? I also have friends, and he also told me that they're using um

I'm your friend.

Yeah, of course. Are you? That's good. Um but they used um really good tool to read through the pull request regarding the security vulnerabilities. Like many of of the alerts that the tool gives you are actually false alerts. But then again, there are some really good remarks about stuff that might have a security impact. And um I guess we as companies should and can use that tooling um to make sure that we are not uh we don't have that large attack surface against these new hacking things, I guess. And that's AI.

We're closing the loop again because you're you're We're talking about tools, and we got

Yeah, exactly. It's still a fool.

We have to learn how to how to use these tools. And they can help us, but we have to understand why we're using them and how to use them. So I'm I'm I'm happy that you mentioned that. Um this is a big thing.

We we should have a session about AI.

I think maybe we'll have a session about

I think also we'll have a session about AI. It seems to be a big thing these Not only in security.

Let's go Let's go for the summary.

Let Let's go for the summary. What's What's What's important? Um for me like most important thing is um putting a number to a security risk, so you get the resources to actually fix security, invest in security, and I not have any security breaches, hopefully at all. That's That's our number one takeaway for me.

My next takeaway is you have to understand what you what you want to keep secure and why you want to keep

Oh, very good point. Love this. like creating your inventory, having an asset inventory that tells you how to move forward. Yeah. And what else do we have?

Um tooling, use tooling, right?

You have a lot of standard tooling, but you have also a quite advanced tooling that might be useful in your case. Um AI-based tooling gets better and better each and every day. Um use it and um

Fourth area. Fourth point.

Shift security to the left. Change the mindset. Make security part of everyday software development.

Oh, important.

If we want to go into the information security, make make your employees always aware that there are threat actors, malicious threat actors, that are trying to

you and your behavior. And in in security and in application security, um it it is the the the software developers that need to learn how to build this into their into

their code, maybe through the help of Uh but training with something simple like OWASP Top 10 is I think already getting you quite far.

That that's perfect. And maybe one small thing in brackets is supply chain attacks. So,

that's that should I guess be part of the training, but the more libraries, the more external dependencies you have, the larger your um attack surface will become. And so, you have to be aware of that. You have to also upgrade the libraries regularly. But, I guess also rule fund wise, uh less libraries, less problems, I guess. Maybe that sums it up.

Different problems. Less Less libraries, different problems.

Yeah, maybe.

This means we always write our libraries on our own, right? Because we have just the AI tooling.

We can let AI No, just write it on your

Including all of the security problems that all the libraries that the AI model learned from have as well.

And all of the maintenance effort that they have to put into Yeah, yeah, that's right. All right. Cool. Thanks a lot. That was a really good exchange, I guess. Likewise. Thanks, Rafael.
