# Plant Based Ireland


Link to website on Heroku

Link to project GitHub Repository

# About 
Plant Based Ireland is a website built to provide a community space for people in Ireland who are interested in exploring vegetarian and vegan foods. It provides a place where members can make blog posts, share articles from around the web, arrange meetups and post photos. It is intended to be a chill space welcoming to all comers, from hardcore vegans to omnivores who are curious about plant based subjects. It uses a simple design aesthetic to appear non-overwhelming and welcoming. It has a few simple data structures to enable users to create, read , update and delete data of their choosing. There are some aspects that are only available to admin / superusers, but the main content of the site should be provided by user upload so it can be self sustaining to a degree.


# Content
- Introduction
- About 
- Contents 
- Preparation : Research
- Preparation : Intent
- User experience / user stories
- Preparation: User Stories / Agile methodologies
- Features , describe each page + function available to users
- Visual Design - colours / aesthetic
- Visual Design - structure / wireframes
- Future updates / places to improve 
- Technologies used
- Creation and deployment
- Validation and testing 
- Known bugs and issues
- Sources 
- acknowledgements


# Preparation : Research, Intent , Agile / User Stories

## - Research 

In preparation for this project, I wanted to consider what would be a site that can utilise CRUD functionality for users but also caters to a gap in the web space / market. I wanted a website that meets the assessment criteria for the Full Stack project but I also didn't want it to be a repeat of a typical website that already exists in the real world.

 Although there are plenty of blogsites and community websites with some user interaction / social media elements, I thought it would make sense to focus on more niche demographic. There are lots of sites for general info sharing and community friendship, but not too many in the mainstream which are based on vegetarian / vegan topics. This would mean an admittedly smaller user base, but by targeting a smaller group with a more focused product, I believe it is more likely to be  utilised by that group. Its more likely to stand out in smaller space where there is less representation for plant based communities, rather than target everyone and compete with larger more established social media  / blog sites.


I decided to research existing irish vegan websites, to see how the more established sites in this category are designed. I looked at 

	- https://irishvegan.ie/
	- https://thehappypear.ie/
	- https://dicedandspiced.com/
	- https://holly.ie
	- https://veganeire.com/

I found that while they have a varied design aesthetic and goals, they offer a lot of content / pages, more than what would be in the scope of my project. However, I did notice that most do not feature much in the way of social media / community interaction, so it would appear there is some merit to my goal of a more user-curated site about irish plantbased topics.  I also found that some of these websites were surprisingly vast, with loads of pages, sub sections and options for some level of user interactivity. This differs from what I had in mind for my site as I want to offer something that is relatively simple that anyone could feel comfortable navigating and contributing to. The difference here is another reason my site can hopefully stand out from the more mainstream irish plant based sites.


I also looked at more popular global websites, not just based on or in Ireland.

	- https://www.vegansociety.com/
	- https://plantbasednews.org/
	- https://tryveg.com/
	- https://simple-veganista.com/
	- https://www.nomeatathlete.com/

I was surprised again, to find that most of the larger websites based around plant based nutrition, don't really focus on user provided content, user interaction or similar social media elements. Primarily they are hosted, contributed to and curated by the owners and operators of the site. At most , users can typically sign up to receive newsletters, comment on posts shared by the site itself, but they rarely have full CRUD functionality when it comes to content on the site.
You would find examples of the type of community I'm referring to in smaller subsections of existing larger websites. For example vegan subreddits, vegan facebook pages, vegan instagram groups etc. These are all larger websites with a broad user base, including smaller sub communities with a more narrow focus. They are essentially similar to the intent of my website , but I believe I can offer something more original or unique by providing a website that is purely dedicated to the irish plant based community. It can't compete with the broader social media sites, it can't compete with the larger vegan information websites, but by carving out a unique space somewhere in between, there is a real opportunity to stand out and serve the irish plant based community.


## - Intent

Based on the above research of existing websites with a focus on plant based nutrition, I decided to focus on providing a welcoming , simple to grasp website that allows users to post their own content and interact with one another. Although there will be some admin curation , moderation and contribution of special content, I want to allow the majority of site content to be user generated. 

My favourite websites are all primarily user generated , compared to more curated websites that host content specifically created, chosen , shared by the people who run the site. Although the latter can provide more professional and insightful contributions on topics that require expertise, such as journalism, science, politics  - the content I typically most enjoy is generated in a free form environment where users interact with one another. The kind of post made by  journalist reviewing a videogame a week after release, will be different from the kind of post made by a person who has played it for a thousand hours and has a unique perspective on it. Whether its a detailed diatribe on a specific aspect, a comprehensive overview on the topic as a whole, or a simple meme on a niche feature, the unrestrained user content will often be more interesting to me personally. So with this in mind, I am happy to push user content to the forefront with admin/superuser content existing as secondary content.

The subject of meat-free diets can be hot button issue today. Plant based topics, vegetarianism and most of all veganism can generate heated debates at the mere mention of the word. Biases and misinformation abound, it is difficult to change one's mind when presented with evidence to the contrary - whether you are for or against plant based diets. Some people find the topic offensive in general, so safe to say it should be approached mindfully and delicately. With this in mind, my approach would be to provide a friendly welcoming space for any all looking for content related to plantbased nutrition. I don't want to exclude anyone, I would hope that all types of people would visit the site if they are curious. So I was careful to include language that doesn't forbid anyone from any belief system or dietary choices. But because of the aforementioned controversial nature of plant-based nutrition, I must also safeguard against the possibility that users on the site could be subject to bullying or harassment. If an omnivore posts a question, I don't want them to be bullied off the site by those who are plant based. Similarly, I don't want online trolls harassing well-meaning users on the site due to veggie / vegan choices.  I think this can be best implemented by providing a clear statement in the about section, stating that such conduct will not be tolerated. The admin and superusers will have the ability to delete content of any kind and delete users if they engage in harassment. To some degree, the user generated nature of the site should also protect against bullying and harassment for the most part. If the site fosters a community of like-minded individuals with values that align with the welcoming / non-bullying goals of the site, they are less likely to interact favourably with such users / content. If an online troll makes an offensive post, they would be unlikely to 'like' the post or post comments on it. There could also be a means of reporting offensive content to the admin , either by a specific report function or just by emailing the site email with the info.

In line with the goal of user generated content, I also do not wish to overwhelm the user - not just in terms of the available databases/range of user content, but also just in terms of the website design itself. This means not having loads of forms / databases for the users to interact with. I would be happy if the user can register, login, make posts, like and comment on posts, delete or edit their posts, submit links to online articles from other sites, upload images to a gallery. Although this might sound like a lot in text, it is actually relatively simple in terms of scope for users - especially compared to more complex websites.  To add on to this , the functional and visual design of the website should be relatively simple and non-complex. In my research I found that a lot of websites about plant based nutrition are quite vast with loads of content, pages, sub sections etc. Unless you are quite familiar with the navigation it could be a little bit overwhelming. This overload of content and visual noise might just be the thing that drives away someone who was curious enough to visit the site. So it is important to me that the website is visually pleasing with a simple aesthetic with only a few options for users to navigate to. It should always be clear what part of the site they are currently on, how they can get back to the home page, whether they are currently logged in or not. There should be a visual search bar at all times so that no matter what page they are on they can try a search if they can't find a specific post. This simple design will hopefully provide a more comfortable environment for new users , which means they are more likely to stay and engage with the site, instead of getting overwhelmed and leaving the site.


Regarding the simple visual design , but more specifically about the artistic choices , my intent is to convey the site design with simple contrasting colours and imagery that relates to plants / food. I would like it to have a main color palette of green ( for association with vegetables ) and white ( for clarity of reading text / content ). I would like this to either have supporting images in the different sections, or one large background image that is a staple on all of the pages of the site. I believe having one main background image would provide a uniform look no matter where you are on the site, and because the image is repeated, it is less likely to distract the user too much ( since , after the first time they see the image, it is likely to they won't focus on the background when they navigate to a new page )


In terms of my intent regarding what functionality is available on the site, I will base this off user stories / agile thinking. I will conduct some thought into what a hypothetical user will want out of the site, I will consider as many versions of this idea as possible , within a context of agile methodologies. This means that while I might have some intentions after completing the user stories, I am not locked into them either. If they do not seem to fit within the site ethos or the project timeframe after some iterations / sprints, they may be re-evaluated, replaced or removed entirely.



## - User Stories / Agile 

As I said in the prior sections on research and intent, it is the ultimate goal to provide a welcoming / uncomplicated website for members of the Irish plant based community, where the content is mostly provided by users. With this broad goal in mind, I conducted preparation with an agile mindset. I looked at the potential of the website in terms of user stories : what would a user want to do on the site, why would they want to do it, what do they gain from doing it.
I looked at the user stories from the MOSCOW perspective, assigning them labels of must-have, should-have, could-have and omitting any ideas which I concluded it won't have. In terms of the actual work on the project, I would create a milestone called the 'product backlog' to track the userstories. I would them a few at a time, into a new milestone called Iteration (n). Each iteration would typically contain around 3 user stories, which I would hope could be completed in a couple of days (depending on how much free time I have to work on the project). Within each of these iterations I would create a project with a 'board' view. This would allow me to track the stories from 'todo' , 'in progress' and finally 'done'. On completion I would close the project, close the related user stories and iteration. I would then return the product backlog milestone to reassess the remaining user stories. Continuing with agile methodologies, I would try to predict the required timeframe of future iterations by thinking of them in terms of timeboxing . This is based on previous iterations , where if it took me X amount of time to complete an iteration with Y amount of userstories, it would logically take me a similar amount of time to complete a similarly structured iteration ( provided that the userstories are also related in terms of scope) And again, upon completion of every iteration, I would re-asses the remaining user stories , to decide if any of the requirements had changed, if some should be prioritized or if I have to conclude that I don't have the time or ability to implement everything. This will keep me focused on the big picture and not get distracted by smaller parts of the site. With agile thinking, I am not beheld to an unflinching list of tasks. I can re-asses and decide if I would be better off changing the approach and goals of the site, based on new developments.