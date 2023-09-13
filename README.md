# Plant Based Ireland


![Image](readme_images/mockup_2.JPG)


Link to website on Heroku

Link to project GitHub Repository

## About 
Plant Based Ireland is a website built to provide a community space for people in Ireland who are interested in exploring vegetarian and vegan foods. It provides a place where members can make blog posts, share articles from around the web, arrange meetups and post photos. It is intended to be a chill space welcoming to all comers, from hardcore vegans to omnivores who are curious about plant based subjects. It uses a simple design aesthetic to appear non-overwhelming and welcoming. It has a few simple data structures to enable users to create, read , update and delete data of their choosing. There are some aspects that are only available to admin / superusers, but the main content of the site should be provided by user upload so it can be self sustaining to a degree.


## Content
- Introduction
- About 
- Contents 
- Preparation : Research
- Preparation : Intent
- Preparation: User Stories / Agile methodologies
- Features
- Visual Design - colour aesthetic & wireframes
- Validation and testing 
- Creation and deployment
- Technologies used
- Known bugs and issues
- Future updates / places to improve 
- Sources 
- acknowledgements


## Preparation : Research, Intent , Agile / User Stories

### - Prep : Research 

In preparation for this project, I wanted to consider what would be a site that can utilise CRUD functionality for users but also caters to a gap in the web space / market. I wanted a website that meets the assessment criteria for the Full Stack project but I also didn't want it to be a repeat of a typical website that already exists in the real world.

 Although there are plenty of blogsites and community websites with some user interaction / social media elements, I thought it would make sense to focus on more niche demographic. There are lots of sites for general info sharing and community friendship, but not too many in the mainstream which are based on vegetarian / vegan topics. This would mean an admittedly smaller user base, but by targeting a smaller group with a more focused product, I believe it is more likely to be  utilised by that group. Its more likely to stand out in smaller space where there is less representation for plant based communities, rather than target everyone and compete with larger more established social media  / blog sites.


I decided to research existing irish vegan websites, to see how the more established sites in this category are designed. I looked at 

https://irishvegan.ie/

https://thehappypear.ie/

https://dicedandspiced.com/

https://holly.ie

https://veganeire.com/

I found that while they have a varied design aesthetic and goals, they offer a lot of content / pages, more than what would be in the scope of my project. However, I did notice that most do not feature much in the way of social media / community interaction, so it would appear there is some merit to my goal of a more user-curated site about irish plantbased topics.  I also found that some of these websites were surprisingly vast, with loads of pages, sub sections and options for some level of user interactivity. This differs from what I had in mind for my site as I want to offer something that is relatively simple that anyone could feel comfortable navigating and contributing to. The difference here is another reason my site can hopefully stand out from the more mainstream irish plant based sites.


I also looked at more popular global websites, not just based on or in Ireland.

https://www.vegansociety.com/

https://plantbasednews.org/

https://tryveg.com/

https://simple-veganista.com/

https://www.nomeatathlete.com/

I was surprised again, to find that most of the larger websites based around plant based nutrition, don't really focus on user provided content, user interaction or similar social media elements. Primarily they are hosted, contributed to and curated by the owners and operators of the site. At most , users can typically sign up to receive newsletters, comment on posts shared by the site itself, but they rarely have full CRUD functionality when it comes to content on the site.
You would find examples of the type of community I'm referring to in smaller subsections of existing larger websites. For example vegan subreddits, vegan facebook pages, vegan instagram groups etc. These are all larger websites with a broad user base, including smaller sub communities with a more narrow focus. They are essentially similar to the intent of my website , but I believe I can offer something more original or unique by providing a website that is purely dedicated to the irish plant based community. It can't compete with the broader social media sites, it can't compete with the larger vegan information websites, but by carving out a unique space somewhere in between, there is a real opportunity to stand out and serve the irish plant based community.


### - Prep : Intent

Based on the above research of existing websites with a focus on plant based nutrition, I decided to focus on providing a welcoming , simple to grasp website that allows users to post their own content and interact with one another. Although there will be some admin curation , moderation and contribution of special content, I want to allow the majority of site content to be user generated. 

My favourite websites are all primarily user generated , compared to more curated websites that host content specifically created, chosen , shared by the people who run the site. Although the latter can provide more professional and insightful contributions on topics that require expertise, such as journalism, science, politics  - the content I typically most enjoy is generated in a free form environment where users interact with one another. The kind of post made by  journalist reviewing a videogame a week after release, will be different from the kind of post made by a person who has played it for a thousand hours and has a unique perspective on it. Whether its a detailed diatribe on a specific aspect, a comprehensive overview on the topic as a whole, or a simple meme on a niche feature, the unrestrained user content will often be more interesting to me personally. So with this in mind, I am happy to push user content to the forefront with admin/superuser content existing as secondary content.

The subject of meat-free diets can be hot button issue today. Plant based topics, vegetarianism and most of all veganism can generate heated debates at the mere mention of the word. Biases and misinformation abound, it is difficult to change one's mind when presented with evidence to the contrary - whether you are for or against plant based diets. Some people find the topic offensive in general, so safe to say it should be approached mindfully and delicately. With this in mind, my approach would be to provide a friendly welcoming space for any all looking for content related to plantbased nutrition. I don't want to exclude anyone, I would hope that all types of people would visit the site if they are curious. So I was careful to include language that doesn't forbid anyone from any belief system or dietary choices. But because of the aforementioned controversial nature of plant-based nutrition, I must also safeguard against the possibility that users on the site could be subject to bullying or harassment. If an omnivore posts a question, I don't want them to be bullied off the site by those who are plant based. Similarly, I don't want online trolls harassing well-meaning users on the site due to veggie / vegan choices.  I think this can be best implemented by providing a clear statement in the about section, stating that such conduct will not be tolerated. The admin and superusers will have the ability to delete content of any kind and delete users if they engage in harassment. To some degree, the user generated nature of the site should also protect against bullying and harassment for the most part. If the site fosters a community of like-minded individuals with values that align with the welcoming / non-bullying goals of the site, they are less likely to interact favourably with such users / content. If an online troll makes an offensive post, they would be unlikely to 'like' the post or post comments on it. There could also be a means of reporting offensive content to the admin , either by a specific report function or just by emailing the site email with the info.

In line with the goal of user generated content, I also do not wish to overwhelm the user - not just in terms of the available databases/range of user content, but also just in terms of the website design itself. This means not having loads of forms / databases for the users to interact with. I would be happy if the user can register, login, make posts, like and comment on posts, delete or edit their posts, submit links to online articles from other sites, upload images to a gallery. Although this might sound like a lot in text, it is actually relatively simple in terms of scope for users - especially compared to more complex websites.  To add on to this , the functional and visual design of the website should be relatively simple and non-complex. In my research I found that a lot of websites about plant based nutrition are quite vast with loads of content, pages, sub sections etc. Unless you are quite familiar with the navigation it could be a little bit overwhelming. This overload of content and visual noise might just be the thing that drives away someone who was curious enough to visit the site. So it is important to me that the website is visually pleasing with a simple aesthetic with only a few options for users to navigate to. It should always be clear what part of the site they are currently on, how they can get back to the home page, whether they are currently logged in or not. There should be a visual search bar at all times so that no matter what page they are on they can try a search if they can't find a specific post. This simple design will hopefully provide a more comfortable environment for new users , which means they are more likely to stay and engage with the site, instead of getting overwhelmed and leaving the site.


Regarding the simple visual design , but more specifically about the artistic choices , my intent is to convey the site design with simple contrasting colours and imagery that relates to plants / food. I would like it to have a main color palette of green ( for association with vegetables ) and white ( for clarity of reading text / content ). I would like this to either have supporting images in the different sections, or one large background image that is a staple on all of the pages of the site. I believe having one main background image would provide a uniform look no matter where you are on the site, and because the image is repeated, it is less likely to distract the user too much ( since , after the first time they see the image, it is likely to they won't focus on the background when they navigate to a new page )


In terms of my intent regarding what functionality is available on the site, I will base this off user stories / agile thinking. I will conduct some thought into what a hypothetical user will want out of the site, I will consider as many versions of this idea as possible , within a context of agile methodologies. This means that while I might have some intentions after completing the user stories, I am not locked into them either. If they do not seem to fit within the site ethos or the project timeframe after some iterations / sprints, they may be re-evaluated, replaced or removed entirely.



### - Prep : User Stories / Agile 

As I said in the prior sections on research and intent, it is the ultimate goal to provide a welcoming / uncomplicated website for members of the Irish plant based community, where the content is mostly provided by users. With this broad goal in mind, I conducted preparation with an agile mindset. I looked at the potential of the website in terms of user stories : what would a user want to do on the site, why would they want to do it, what do they gain from doing it.
I looked at the user stories from the MOSCOW perspective, assigning them labels of must-have, should-have, could-have and omitting any ideas which I concluded it won't have. In terms of the actual work on the project, I would create a milestone called the 'product backlog' to track the userstories. I would them a few at a time, into a new milestone called Iteration (n). Each iteration would typically contain around 3 user stories, which I would hope could be completed in a couple of days (depending on how much free time I have to work on the project). Within each of these iterations I would create a project with a 'board' view. This would allow me to track the stories from 'todo' , 'in progress' and finally 'done'. On completion I would close the project, close the related user stories and iteration. I would then return the product backlog milestone to reassess the remaining user stories. Continuing with agile methodologies, I would try to predict the required timeframe of future iterations by thinking of them in terms of timeboxing . This is based on previous iterations , where if it took me X amount of time to complete an iteration with Y amount of userstories, it would logically take me a similar amount of time to complete a similarly structured iteration ( provided that the userstories are also related in terms of scope) And again, upon completion of every iteration, I would re-asses the remaining user stories , to decide if any of the requirements had changed, if some should be prioritized or if I have to conclude that I don't have the time or ability to implement everything. This will keep me focused on the big picture and not get distracted by smaller parts of the site. With agile thinking, I am not beheld to an unflinching list of tasks. I can re-asses and decide if I would be better off changing the approach and goals of the site, based on new developments.


* Example of user story
![Image](readme_images/user-story.png)


* Iterations 
![Image](readme_images/image-53.png)

* Projects

![Image](readme_images/image-54.png)


* pp4 Plant Based Ireland issues
https://github.com/gazamcnulty/pp4-plant-based-ireland/issues

* pp4 Plant Based Ireland projects
https://github.com/gazamcnulty/pp4-plant-based-ireland/projects?query=is%3Aclosed

* 

## Stucture / Features

* Home page large monitor
![Image](readme_images/image-58.png)

* Home page mobile
![Image](readme_images/image-59.png)



For overall structure, the website features a fairly standard build. As I have integrated bootstrap features into the styling, the focus was on mobile first and larger screens second. This makes it easier for responsiveness and makes it more likely that more users of any device will be able to view the site properly.
 
On first visiting the site, the user can see a strong navbar horizontal across the page, it is styled so that it is always on top of the visual window, no matter where the user is in the site. It uses bootstrap navbar features which provide easy uniform styling

Below the nav is a horizontal banner welcoming the user to the site, with an immediate call to action. It entices the user to sign up / register with the site, displays a large green button to sign up and lists some additional benefits to users of the site if they sign up. This is deliberate so that as soon as a user goes to the site , they have been made aware that they can sign up to gain access to additional features of the site. Even if they don't sign up immediately on the first go , it is in the back of their minds while they navigate the site. In other places this is re-enforced , for example in the post_detail section , when a user clicks in to read the post without having logged in, it tells the user they will need to log in , in order to like or post a comment.

The sign up button in the welcome call to action banner activates a modal sub window, displaying a small form for the client to register. This is beneficial so that the client does not lose their place on the site, they are not taken to a different page all together, it is quick and seamless to register. Since we want as many people as possible signing up and interacting with the site, we want the process to be as quick and painless as possible

Below the call to action / welcome banner, is the main content of the site, the front page of Plant Based Ireland. It features an fractional bootstrap grid / column view structure, with the user posts being the main focus on the left with a small section on the right showing latest articles from around the web. The first focus is on user generated content, which is why user posts take up the most real estate on the frontpage. We want to encourage users to engage in conversations, we want user posts to generate threads, comments, likes. Not quite as versatile as a true forum but an effective framework to foster users socialising with one another, interacting with the site.

The articles sub section on the left is also user generated, in that the links are submitted by users. But the content itself is external, linking to other websites separate to Plant Based Ireland. I was initially hesitant to include this feature as I would want users to stay on the site, instead of going elsewhere. But I thought we can better serve a niche of providing a hub of user interaction with a host of links to other plant based content, rather than trying to have everything on our site alone. Even if another site has more content , the purpose Plant Based Ireland serves is to act as a nexus for these other sites and the users who would browse them. For this reason, a user may be more likely to go to Plant Based Ireland for a summary of the latest most interesting links from other sites, rather than going direct to the site first. 

As I said above , the user posts and external articles are presented horizontally on a 2/3 ratio of the page. Using bootstrap grid / cols layout, this changes on smaller screens for better visuals. On smaller screen like mobiles, the user posts take up the full width of the small screen. The additional news/articles are removed entirely on smaller screens. I had initially had them render below the user posts on small screen, but I think it is better on mobile to have a cleaner more focused design. And the news/articles are still readily available on the News section, they just don't render on the home page anymore. On a larger monitor screen its ok to render both sets of posts, as there is much more room for content.

If the user clicks into one of the posts submitted, they are brought to the post_detail page. This renders the same post title that served as the link on the home page, it also renders the post content, user submitted image with the post, comments from users and the number of likes the post has received. All of these features are related to the Post database, rendered with django template language in the post_detail template. On this page, the rendered info changes based on whether or not the user is currently logged in. If they are logged in, it shows the input field to post a comment and a like button , which likes or dislikes the current post when clicked . This is one of the listed features from the home page call to action : users who log in gain access to post comments and like content.

* Post detail - logged out

![Image](readme_images/image-60.png)


* Post detail - logged in

![Image](readme_images/image-61.png)


If the user is not logged in, they can still see the amount of likes and user comments, however they cannot see the like button or an input field for comments . Instead there is a text field telling user to login if they want to post comments or likes. This feeds back in to the loop of the site, where all content either suggests logged in users should contribute content, or non-logged in users should log in so they don't miss out on more content.
As well as these features, the user can see an edit button and delete button only if they are the one who created this post. If you go into the post detail of a post created by another user , you cannot edit or delete it. 
Similarly, a comment on a post will also show a delete button , if the user is the one who made the comment. You cannot delete other users comments.
Even in the post detail page, the navbar and footer still shows, so navigation is still as user friendly on this page as it is on the homepage.


The news section has a similar visual structure to the home page, except the welcome banner is replaced by a summary of types of news articles that should be submitted and button for clients to submit. Below this the same bootstrap grid / column structure is in place but now the focus is on the articles / news , with posts being on the side. In addition there are a few buttons that allow the user to filter these articles,  from all , news, blogs, reviews and recipes. This is another layer of optimisation for the user , so they can get straight to the articles they are interested in. As was the case with the home page, if the screen size changes to a small screen the listed news/articles take up the full width of the screen but the user posts small section is removed entirely. The user can still access it from the homepage if they want
The listed news articles differ slightly from the user posts in that they also list the 'category' of the news article. It will either show Blog, News, Recipe, Review. This is shown just above the title for quick info at a glance. The title serves as a link to the external website, it opens in a new tab and brings the user to the other site. It is important to do this , as we don't want the user to lose their place on our site, this would not be good user experience. For the purposes of site engagement, we also want the users to be on our site as much as possible.

![Image](readme_images/image-57.png)

The blog, news, recipe and review sections are functionally identical to the main news/articles sections . The only distinguishing features are the buttons which lead to each respective section , as well as the currently filtered articles on the page. If the use is on the 'blog' page, the button for the blog section is greyed out so it cant be selected. This also communicates to the user what page they are currently on , which also improves the user experience and reduces likelihood of them being lost on site.


The about section is a straight forward page with text info. It is static paragraphs of text without any dynamic elements. The sections are laid out via bootstrap grid / col layout, this allows for a 1/2 layout horizontally on a larger screen but changes to full width layout on smaller screens. These bootstrap layouts ensures the content is clear and has a pleasant appearance on any device. The about section has font awesome icons flanking the sub headers of each section , this is for additional flavour and communicates the vibes of the site to prospective users. This is especially important in the about section, since this is where the site introduces itself and its beliefs / goals to users learning about the site. If the site effectively communicates its ethos with a user here , and if it resonates with the user , it may be enough to convince them to register on the site and log in to interact with the content.

* About section

![Image](readme_images/image-62.png)

The events section is similar to the about section in that it is static without dynamic features or user interaction. It features paragraphs of content, informing the user of upcoming events being organised by the website . The events section is different in that it requires the user to be logged in to access. If you are not logged in you cant see the events and are instead referred back to the login page. This is one of the advertised features in the call to action on the home page, the exclusivity of the events can encourage a user to sign up to the website. This is easily achieved by locking the content off for non-authenticated users.

* Events section

![Image](readme_images/image-63.png)


The gallery section is similarly straight forward in terms of design, it is just a place for users to upload images without lots of text if they wish. It could be optimised in future to act as a true 'feed' like one might see in a social media page, or it could be combined with the  news articles and posts into one dense feed of content. For now it operates with a basic bootstrap grid column structure, allowing users to upload photos / pictures of their choosing. While it may not be as involved as a user post or link to external site, it is an attractive feature to have a quick user submission option that contrasts more dense user posts. In theory,  a user may want to contribute to the site but not on the level of complexity as a full user post. The quick context - free image gallery allows a user to throw up a quick pic or meme, if they want to contribute content quickly.

* Gallery

![Image](readme_images/image-64.png)

The login page is accessible from the navbar, you can also be referred there from other pages if you are not logged in. The page is a simple form asking the user to provide username and password to log in , it also has a separate button allowing non-registered users to sign up now.
The login link only shows in the navbar, if the user is currently not logged in. If the user is logged in , it instead shows Account. This is simple static page that shows the user's username, email address and date they joined the site. It has a button for change password which brings the user to the change password page. They can change password here , or go back.
As well as the navigation links in the navbar, there is a search bar on the top right. If the user searches here, it brings them to the search results page and shows and counts how many results have been found, based on the terms searched.
The navbar was implemented using Bootstrap boilerplate code for navbar design, it includes an expand / toggle button feature. This means that on larger screens, the navbar renders as normal with all of the navigation items listed, but when the screen gets smaller, the nav items are replaced by a simple toggle button. Clicking the toggle button shows a list of the nav items, which can then be toggled closed again. This is better for responsive design as a navbar with lots of words across the top does not look good on mobile, for the most part.

* Account info with navbar

![Image](readme_images/image-66.png)

In the footer , there are navigation links again in a vertical arrangement. This is just additional optimisation for user experience, so even if they are at the bottom of any page, they can quickly see what page they are currently on and see what other sites are available to click. It also shows static text describing contact details. Finally there are social media links , styled with font awesome icons. These open on the social media sites in a new tab if clicked. The footer uses bootstrap grid responsiveness, so that on a smaller screen it will only list the social media links

* Footer 

![Image](readme_images/image-65.png)


## Visual Design



### Visuals - colours / aesthetic

Per the research sections above, I decided to opt for a simple visual design to the site. I wanted it to look welcoming and uncomplicated, the simpler and quicker it is for a prospective user to navigate the site, the more likely they are to stick around and contribute.

I have used a fairly standard design set up , with strong green coloured navbar and footer , slightly translucent white body containing text and content, all on top of a high def image of a food counter surrounded by vegetables. The main colours being used are green , white and black. I am aware this isn't the most original design choice but I felt it was fitting for the ethos of the website and the simpler design aesthetic would allow greater time and effort towards more complex aspects of this assessment which I am less familiar with , such as django / database model management, and bootstrap utilisation . 

I like the idea of strong coloured navbar and matching footer, especially when the navbar is stuck to the top of the screen at all times while scrolling. This is an additional layer of user info and support, no matter where they are on the site or how far down the page they scroll, they can always see the logo of the site and navigation bar, which also informs what page they are currently on. So the user is always reminded of the site name and they are less likely to get lost of frustrated. The strong green was chosen as it contrasts directly with the slightly translucent white body elements, so it has striking visuals that aid legibility.
Also in the navigation and footer, when mouse icon hovers over a link , the background changes to a darker green and the text changes colour to white. This immediately communicates to the user that they are hovering over a link to a new location so they are fully informed as to whether they want to click the link and leave the page.

The main body of content on the site is white and 0.9 opaque. This means it is mostly a complete solid white background but just slightly shows the visuals that lie underneath it. This is most effective when used with a white color so the image can be seen clearly and the white easily contrasts with black text font for easy legibility.  The opacity allows for the background image to be beheld while scrolling anywhere on the website. I was concerned that this may be slightly distracting and turn the user's attention away from the main content. However I ultimately decided it was a very minor risk , vs the overall design aesthetic being pleasing to the eye. The image itself, while high definition, is a simple image of a food counter surrounded by vegetables, with the words EAT VEG spelled out with green beans. Even if the user does momentarily get distracted by the background image, its a short 2 word message that is immediately understood so it won't serve to distract too much. It contributes to the philosophy of the site both in terms of the message to eat vegetables , and shows colourful delicious vegetables surrounding the main body of content. So it furthers not only the agenda of the website , but the agenda of the plant based movement as well .

As well as the footer and navbar green colour, I have also given the main buttons  a slightly darker green color. This gives the site a uniform look , where the colour reminds the user of the navbar, which shows the logo of Plant Based Ireland. So when the user sees the big green button , attractive and friendly, inviting the user to sign up or post content, it makes them think of Plant Based Ireland. Even something as innocuous as the colour of a button can contribute to the overall communication of the website.
Some other buttons I gave a more muted color , so that they are clearly secondary to the main green buttons, while also clearly displaying a clickable button to the user.

For fonts I chose 'Quicksand', 'NunitoSans', Verdana, Geneva, Tahoma, sans-serif
For font colour I chose simple black colour, so it is easily distinguishable against the white body. 
With some of the section headers , I also put in a small font awesome icon for some visual flourish. This serves as an unwritten means of communicating with the user and adds a little bit of fun and personality to the website too.

I have included a favicon to render a logo on the browser tab, for additional flavour and site design. So even if a user has multiple tabs open , they can quickly see the tab related to Plant Based Ireland



### Visual - Wireframes

* Homepage
![Image](readme_images/Wireframe_home.JPG)

* News
![Image](readme_images/News_wireframe.JPG)

* Gallery 
![Image](readme_images/Wireframe_gallery.JPG)

* Post Detail 
![Image](readme_images/Wireframe_post_detail.JPG)


## Testing 

### Test - Intro 

All tests performed with deployed site on Heroku.

- Tested:
- User stories
- Site navigation / page links validation
- Responsiveness
- Browsers
- Devices
- Performance Lighthouse
- W3 HTML Validation
- Bugs


For PP4 Plant Based Ireland I have used manual testing to assess functionality,
usability, responsiveness and data management within the entire web application. 

### Test - User stories

For testing I will review the user stories / milestones linked with PP4 Plant Based Ireland and assess whether they have been completed or not. If it passes the description and if the Acceptance Criteria has been met it will be given a pass. If it has not been completed it will be given a fail.


![Image](readme_images/image-3.png)


![Image](readme_images/image-5.png)


![Image](readme_images/image-6.png)

![Image](readme_images/image-7.png)

![Image](readme_images/image-8.png)

![Image](readme_images/image-9.png)

![Image](readme_images/image-10.png)


![Image](readme_images/image-11.png)


![Image](readme_images/image-12.png)


![Image](readme_images/image-13.png)


![Image](readme_images/image-14.png)


![Image](readme_images/image-15.png)


![Image](readme_images/image-16.png)


![Image](readme_images/image-17.png)


![Image](readme_images/image-18.png)


![Image](readme_images/image-19.png)


![Image](readme_images/image-20.png)


![Image](readme_images/image-21.png)


![Image](readme_images/image-22.png)


![Image](readme_images/image-23.png)


![Image](readme_images/image-24.png)


![Image](readme_images/image-25.png)


![Image](readme_images/image-26.png)


![Image](readme_images/image-27.png)


![Image](readme_images/image-28.png)


![Image](readme_images/image-29.png)


![Image](readme_images/image-30.png)


![Image](readme_images/image-31.png)


![Image](readme_images/image-32.png)


![Image](readme_images/image-33.png)


![Image](readme_images/image-34.png)


Conclusion : I completed almost all of the goals and tasks set out in the user stories, with some being removed either due to time constraints or change in intention, upon agile reassessment.  Other features I ended up implementing while working on the main user stories, could have been user stories themselves like delete comment, pagination. Most of all , it has served to show me how different features should be split up into smaller issues or collected as epics. I am satisfied that most of the user stories have been completed and allowed the website to be completed as intended.



### Tests - Links, website validation

This is to test that all the links/pages in the site are working properly. I performed the test on chrome and changed screensize with dev tools to observe any responsiveness issues. There was no major bugs found, the issues presented were expected from urls which are not supposed to run on their own, like base.html / navbar.html. There were a couple of failures discovered regarding layout / css . 

Layout in 404 page is not correct, the main div is overlapped by navbar and the footer is too high up, it is not fixed at the bottom of the page
- Added subscreen_container class to 404 page so it inherits the margin pushing the footer down

the url add/ is different from name of template add_post, I found this was because I had named it add/ in url pathway instead of add_post/. Nothing wrong but for ease of use I would rather the nomenclature match
- Changed name in url path to add_post/

Beyond these small issues which have been corrected, everything else works as expected and I am satisfied with the testing of the page validation






![Image](readme_images/image-47.png)








### Tests - Responsiveness 

The responsiveness test involves me viewing all of the web pages across multiple devices. They had been tested throughout the development so they all Pass and appear fine with the final product. The only one which could be imporved is Surface Pro 7 - 912 x 1368 as it causes the content to stretch with a large gap betweeen navbar , content and footer. This was especially apparent in smaller content screens, like 0 search results, loginpage and 404 error. It still looks ok and is functional howver.

 All devices pass


- 4K monitor 2560 x 1897 
- Laptop 1440 x 1004
- Laptop 1024 x 854
- Tablet 768 x 854
- Mobile 425 x 854
- iPhone SE - 320 x 854
- iPhone XR - 414 x 896
- iPhone 12 Pro - 390 x 844
- Pixel 5 - 393 x 851
- Samsung Galaxy S8+ - 360 x 740
- Samsung Galaxy S20 Ultra - 412 x 915
- iPad Air - 820 x 1180
- iPad Mini - 768 x 1024
- Surface Pro 7 - 912 x 1368
- Surface Duo - 540 x 720
- Galaxy Fold - 280 x 653
- Samsung Galaxy A51/71 - 412 x 914
- Nest Hub - 1024 x 600
- Nest Hub Max - 1280 x 800
- Pixel 6 - 412 x 892


![Image](readme_images/image-51.png)



### Tests - Browser 

The purpose of browser cross testing is to check the site looks and runs ok on all browsers, not just chrome in which it was developed. This was tested with chrome, edge, firefox on windows 10 laptop and safari on Mac. All pages rendered fine and worked properly as intended.

- CHROME - PASS
- EDGE - PASS
- FIREFOX - PASS
- SAFARI - PASS



### Tests - Devices 


The purpose of device testing was to check the website is functional across different devices, this is seperate from window / viewport responsiveness alone, which can be tested in devtools. I tested the website on windows 10 laptop, Mac, iphone 10 and Samsung Galaxy s8+. 
The website runs absolutely fine on all devices, though there is one issue I noticed about the background image in the Samsung Chrome app. On chrome on android, there is a menu bar at the top of the screen showing the current url . Unfortunately it is not fixed, it disappears if you scroll down which increases the size of the viewport. This changes how the background image is rendered and it jumps, so that the zoomed in part is moved ever so slightly. If you scroll back up the menu pops back in , reverting the toobar and changing it again. Both versions look good, the problem is it is a little distracting between both. In future I would look at changing the background CSS to avoid this, but in terms of visuals and website functionality it is absolutely fine. Pass on all tested devices.


- Windows 10 Laptop - PASS
- Macbook Pro Laptop - PASS
- iPhone 10 - PASS
- Samsung Galaxy s8+ - PASS




### Tests - Lighthouse Performance

Chrome devtools Lighthouse was used to test for performance, accessibility , best practices and search engine optimisation.  It was tested across all pages, screenshots with scores listed below.
 The loss in performance score refer to delay in the cache, related to the cloudinary storage and font aweseome, bootstrap, google fonts and heroku content. Accessiblity fell down because the given aria label does not match the attribute role. I am unsure what has causd this . It also states heading elements are not in sequential order , but I can't find a specific ecample.

The most significant loss was a low performance score on the gallery section, this is due to various image sizes and large images being submittable by users. This could be changed by making the image size uniform , but I am happy leaving it as it is for now , for user experience.

registration page
![Image](readme_images/Lighthouse_register-1.JPG.png)

post_detail page
![Image](readme_images/Lighthouse_post_detail.JPG)

news page
![Image](readme_images/image-35.png)

login page
![Image](readme_images/image-36.png)

index.html
![Image](readme_images/image-37.png)

gallery
![Image](readme_images/image-38.png)

events page
![Image](readme_images/image-39.png)

delete 
![Image](readme_images/image-40.png)

change password page
![Image](readme_images/image-41.png)

add_post page
![Image](readme_images/image-42.png)

add_news
![Image](readme_images/image-43.png)

account page
![Image](readme_images/image-44.png)

about page
![Image](readme_images/image-45.png)

edit
![Image](readme_images/image-46.png)




### Tests - W3 HTML Validator


W3 Markup Validator checks the markup validity of Web documents in HTML. As these html pages containing django pythonic / jinja template language, the validator returned MANY errors , which were all related to the django template language {{}} {%%} . See below example of html error referring to django template python code

![Image](readme_images/image-49.png)

 In some instances it would return a seemingly legitimate html error, which could only be considered incorrect becuase its not considering the logic of a django python command within the same element. I ignored all of the errors relating to the template language and focused on strict html errors.

All pages passed , with minor corrections of closing tags on void elements and stray closing tags. These have all been corrected. 


### Tests - W3 Validator 

W3C CSS Validator was used to check validity of stlye code laid out in style.css , per correct practices and check for errors. For my stylesheet it found one error for display:flexbox; which should have been display:flex; . This has now been corrected.

![Image](readme_images/W3C_CSS_Validator_ss.JPG)


### Tests - Code Institute Python Linter

The code institute Python Linter was used to test Python validation with Pep8 style guide . It returned a good few errors which were almost all corrected, trailing spaces, #comment without space, no new line at end of file, line too long etc. I only tested the .py files I amended as part of the project, I didn't test the python files installed in the django set up as I did not change or add to these. 

Most only had a few errors to correct but views.py had many errors - lines too long, white spaces, no space after : or before = , blank lines with white space, # with no space for comment. most all were corrected, except for a few line too long errors , specifically in the news filters sections , to filter by category. Unfortunately these were discovered close to the project submission so I have opted to leave them in as attempting to amend them is causing errors. In future I will come back to these to correct the syntax without line being too long


![Image](readme_images/image-52.png)


## Creation and deployment 





## Technologies used 




## Bugs

There aren't any significant bugs that I am aware of with the site. There is nothing that can cause an error through ordinary navigation and user inputs. I am aware of some issues with the site which I would like to improve but they don't significantly impact user experience.

1. Glitchy image on chrome in android on Samsung Galaxy. As I mentioned in the testing section,  On chrome on android, there is a menu bar at the top of the screen showing the current url . Unfortunately it is not fixed, it disappears if you scroll down which increases the size of the viewport. This changes how the background image is rendered and it jumps, so that the zoomed in part is moved ever so slightly. If you scroll back up the menu pops back in , reverting the toobar and changing it again. Both versions look good, the problem is it is a little distracting between both. In future I would look at changing the background CSS to avoid this, but in terms of visuals and website functionality it is absolutely fine.  

2. Python code in views.py could be improved to correct for better syntactical and stylistic code. Currently there are a couple of lines that give the 'line too long' error when run through a Python Linter. As I am about to submit the project , I am hesitant to change it too much in case it causes errors . But I will look at improving this in the future.


## Future improvements

There are a lot of ways my site could be improved. At the moment, it serves as a basic way for users to submit , read, edit and delete content but only very specific aspects. It would be better if the full CRUD framework applied equally to all user generated content, it shouldn't vary per item.

For example, users can create a user post on homepage. They can edit their own post and delete their own post, edit and delete is restricted to only the user who created the post. Other users can read this post they can 'like' it , 'dislike' it and they can comment on it. These features are good and users should have this level of control. However , this does not extend to other user created content like news articles, gallery images. For these , there isn't an option to delete or edit , it would need to be done in the admin page by admin / superuser. I don't mind this too much as for a lot of sites, once you submit content to the public, it is not always immediately available to delete the content. For example, an image submitted anonymously on an image board can't be deleted a normal way. For some sites you would need to message the admins to request it . This doesn't mean its ok either, it is a significant issue I would want to improve in the future. As far as the project is concerned I am satisfied that there is full CRUD functionality available to users for posts but I will endeavour to extend this to the other content at some point going forward.

Similarly the search function currently returns items from the Post model and News model where the searched term is listed in the title of the item. But it can only find user submitted posts or user submitted news/articles. It can't find gallery images , comments or post content via the search. The search function could be extended to include these parameters as well  in future , for better user experience

I would like have some kind of dynamic features on the home page, where some content is changed or cycled in / out. For example maybe instead of the separate section of news / articles on the home page, it could be a more general section showing recent user content ; comments, gallery images, user posts etc. Maybe it could loop through these visually.

In the site it is advertised that registered users will receive monthly email newsletters. This is accomplished by the email address being required on user registration, so the emails are listed and available to admin team / super users. They can take the listed emails from the admin page and use them when sending the monthly email news letter. It would be great if the email input could be expanded on, either for user to receive an automatic email on registration confirming the sign up. Or it could be used for more secure password resets. As it is now, the site can allow for users to change their account password, but there isn't a way if the user cannot remember their password. An email password reset link would be a way to use the existing framework to add additional features for the user.


## Sources





## Acknowledgements