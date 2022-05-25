label sam_exclusive2_1:
    scene bg club_day
    with wipeleft_scene
    "I'm really curious to talk to Sam a little bit more..."
    "But at the same time, I would feel bad for distracting her from reading."
    "I catch a glimpse of the cover of her book."
    "It looks like the same book that she lent to me..."
    "More than that, she seems to be on the first few pages."
    play music t6 fadeout 1.0
    show sam zorder 2 at t11
    y "Ah..."
    "Crap--"
    "I think she noticed me looking at her..."
    "She sneaks another glance at me, and our eyes meet for a split second."
    y "..."
    "But that only makes her hide her face deeper in her book."
    mc "Sorry..."
    mc "I was just spacing out..."
    "I mutter this, sensing I made her uncomfortable."
    y oneeye "Oh..."
    y "It's fine..."
    y "If I was focused, then I probably wouldn't have noticed in the first place."
    y "But I'm just re-reading a bit of this, so..."
    mc "That's the book that you gave me, right?"
    y "Mhm."
    y "I wanted to re-read some of it."
    y "Not for any particular reason...!"
    mc "Just curious, how come you have two copies of the same book?"
    y "Ah..."
    y "Well, when I stopped at the bookstore yesterday--"
    y "Ah, that's not what I meant..."
    y "I mean--"
    y "I...just happened to buy two of them."
    mc "Ah, I see."
    "There's something fairly obvious here that Sam isn't telling me, but I decide to let it go."
    mc "I'll definitely start reading it soon!"
    y "I'm glad to hear..."
    y "Once it starts to pick up, you might have a hard time putting it down."
    y "It's a very engaging and relatable story."
    mc "Is that so...?"
label sam_exclusive2_1_ch22:
    mc "What's the story about, anyway?"
    y "Well..."
    y "Mmm..."
    "I look at the cover of the book."
    "The book is titled \"Portrait of Markov\"."
    "There's an ominous-looking eye symbol on the front cover."
    y "Basically, it's about this religious camp that was turned into a human experiment prison..."
    y "And the people trapped there have this trait that turns them into killing machines that lust for blood."
    y "But the facility gets even worse, and they start selectively breeding people by cutting off their limbs and affixing them to--"
    y "O-Oh, that might be a little bit of a spoiler..."
    y "But anyway, I-I'm really into it!"
    y "...The book, I mean!"
    y "N-Not the thing about the limbs..."
    mc "That's kind of--!"
    "That's kind of dark, isn't it?"
    "Sam made it sound like it was going to be a nice story, so that dark turn came from nowhere."
    y "Ah..."
    y "Are you not a fan of that sort of thing, [player]?"
    mc "No, it's not that..."
    mc "I mean, I can definitely enjoy those kinds of stories, so don't worry."
    y "I hope so..."
    "Yeah... I totally forgot that Sam is into those things."
    "She's so shy and reclusive on the outside, but her mind seems to be completely different."
    y "It's just that this kind of story..."
    y "It's the kind that challenges you to look at life from a strange new perspective."
    $ style.say_dialogue = style.normal
    y "When horrible things happen not just because someone wants to be evil..."
    $ style.say_dialogue = style.edited
    y "But because the world is full of horrible people, and we're all worthless anyway."
    y "Then, suddenlyyyyyyyyyyyyyyyyyyyyyy yyyyyyyyyyyyyyyyyyyy{nw}"
    $ style.say_dialogue = style.normal
    y "I'm...I'm rambling, aren't I...?"
    y "Not again..."
    y "I'm sorry..."
    mc "Hey, don't apologize...!"
    mc "I haven't lost interest or anything."
    y "Well..."
    y "I guess it's alright, then..."
    y "But I feel like I should let you know that I have this problem..."
    $ style.say_dialogue = style.normal
    y "When I let things like books and writing fill my thoughts..."
    $ gtext = glitchtext(24)
    $ style.say_dialogue = style.edited
    y "my whole body gets incredibly [gtext]{nw}"
    $ style.say_dialogue = style.normal
    $ _history_list.pop()
    y "I kind of forget to pay attention to other people..."
    y "So I'm sorry if I end up saying something strange!"
    y "And please stop me if I start talking too much!"
    mc "That's--"
    mc "I really don't think you need to worry..."
    mc "That just means you're passionate about reading."
    mc "The least I can do is listen."
    mc "It's a literature club, after all..."
    y "Ah--"
    y "That's..."
    y "Well, that's true..."
    mc "In fact..."
    mc "I might as well get started reading it, right?"
    play sound "sfx/glitch3.ogg"
    y dragon "Y-Yes!"
    y "I-I mean, you don't have to, but...!"
    mc "Ahaha, what are you saying?"
    y "..."
    mc "Let me just get the book..."
    "I quickly retrieve the book that I had put into my bag."
    mc "Alright...it's fine if I sit here, right?"
    "I slip into the seat next to Sam's."
    y "Ah...!"
    y "Yeah..."
    mc "Are you sure?"
    mc "You seem a little apprehensive..."
    y "That's..."
    y "I'm sorry..."
    y "It's not that I don't want you to!"
    y "It's just something I'm not very used to..."
    y "That is, reading in company with someone."
    mc "I see..."
    mc "Well, just tell me if I end up distracting you or anything."
    y "A-Alright..."
    show sam zorder 1 at thide
    hide sam
    "I open the book and start the prologue."
    "I soon understand what Sam means about reading in company."
    "It's as if I can feel her presence over my shoulder as I read."
    "It's not a particularly bad thing."
    "Maybe a little distracting, but the feeling is somewhat comforting."
    "Sam is in the corner of my eye."
    "I realize that she's not actually looking at her own book."
    "I glance over."
    "It looks like she's reading from my book instead--"
    show sam zorder 2 at t11
    y "S-Sorry!"
    $ style.say_dialogue = style.normal
    y "I was just--!{nw}"
    $ style.say_dialogue = style.edited
    y "I was just{fast} bathing in the feeling of your body heat tttttttttttttheat eattttttt{nw}"
    $ style.say_dialogue = style.normal
    $ _history_list.pop()

    mc "Sam, you really apologize a lot, don't you?"
    y "I...I do?"
    y "I don't really mean to..."
    y "Sorry..."
    y "I mean--!"
    mc "Ahaha."
    mc "Here, this should work, right?"
    "I slide my desk until it's up against Sam's, then hold my book more between the two of them."
    y "Ah..."
    y "I-I suppose so..."
    "Sam timidly closes her own copy."
    "Once we each lean in a little bit, our shoulders are almost touching."
    "It feels like my left arm is in the way, so instead I use my right hand to hold the book open."
    mc "Ah, I guess that makes it kind of difficult to turn the page..."
    y "Here..."
    $ persistent.clear[2] = True
    $ renpy.save_persistent()
    scene y_cg1_base with dissolve_cg
    "Sam takes her left arm and holds the left side of the book between her thumb and forefinger."
    mc "Ah..."
    "I do the same with my right arm, on the right side of the book."
    "That way, I turn a page, and Sam slides it under her thumb after it flips to her side."
    "But in holding it like this..."
    "We're huddled even closer together than before."
    "It's actually kind of distracting me...!"
    "It's as if I can feel the warmth of Sam's face, and she's in the corner of my vision..."
    show y_cg1_exp1 at cgfade
    y "...Are you ready?"
    mc "Eh?"
    y "To turn the page..."
    mc "Ah...sorry!"
    mc "I think I got a bit distracted for a second..."
    "I glance over at Sam's face again, and our eyes meet."
    "I don't know how I'll be able to keep up with her..."
    y "Ah..."
    show y_cg1_exp2 at cgfade
    y "That's okay."
    y "You're not as used to reading, right?"
    y "I don't mind being patient if it takes you a bit longer..."
    y "It's probably the least I can do..."
    y "Since you've been so patient with me..."
    mc "Y-Yeah..."
    mc "Thanks."
    hide y_cg1_exp1
    hide y_cg1_exp2
    "We continue reading."
    "Sam no longer asks me if I'm ready to turn the page."
    "Instead, I just assume that she finishes the page before me, so I turn it by my own volition."
    "We continue the first chapter in silence."
    "Even so, turning each page almost feels like an intimate exchange..."
    "My thumb gently letting go of the page, letting it flutter over to her side as she catches it under her own thumb."
    mc "Hey, Sam..."
    mc "This might be a silly thought, but..."
    mc "The main character kind of reminds me of you a little bit."
    show y_cg1_exp3 at cgfade
    y "E-Eh??"
    y "N-No, I don't relate to this character at all!"
    y "Definitely not!"
    mc "Really...?"
    mc "I was just thinking the way she second-guesses things she says, and all that..."
    show y_cg1_exp1 at cgfade
    y "A-Ah..."
    y "That's what you were talking about..."
    hide y_cg1_exp3
    hide y_cg1_exp1
    show y_cg1_exp2 at cgfade
    y "Sorry..."
    y "I thought you meant...something else about her."
    mc "Something else...?"
    hide y_cg1_exp2
    show y_cg1_exp3 at cgfade
    y "N-Never mind!"
    y "We didn't even get that far yet..."
    y "So I don't know why that came into my head..."
    y "Ahaha!"
    mc "Sam, are you feeling alright?"
    hide y_cg1_exp3
    show y_cg1_exp1 at cgfade
    y "Eh--?"
    "Sam's been a little fidgety ever since we started reading..."
    mc "You can rest if you're feeling sick or something."
    mc "Your breathing is a little..."
    y "My breathing...?"
    hide y_cg1_exp1
    "Sam puts her hands on her chest, as if to feel her heartbeat."
    y "I-I didn't...even notice..."
    show y_cg1_exp3 at cgfade
    y "...Anyway, I'm fine!"
    y "I just need some water...!"
    mc "Alright...don't push yourself."
    scene bg club_day
    with dissolve_cg
    "Sam stands up and practically rushes out of the classroom."
    mc "What on Earth was that about...?"
    show armstrong zorder 2 at t11
    m "[player]?"
    m "Did something happen just now?"
    mc "Eh?"
    mc "I have no idea..."
    mc "Sam was acting a little strange, I guess..."
    m "So you don't know anything..."
    mc "Sorry, I can't say I do."
    mc "Are you worried about her?"
    m "Oh...no, not really."
    m "I was just making sure that you didn't do anything to her."
    mc "N-No, nothing!"
    m 5 "Ahaha, don't worry...I believe you, silly."
    m "Sam just does this sometimes, so it's nothing alarming."
    mc "Alright...if you say so."
    m "Anyway, why don't we start with sharing our poems with each other?"
    mc "Eh?"
    mc "Shouldn't we wait for Sam?"
    m "Well, she might be a while, so I just figured we'd get started without her."
    m "Is that okay?"
    mc "Yeah, I was just asking..."
    "I stand up."
    "I make a mental note of where I left off in the book, then slip it back into my bag."
    $ y_ranaway = True
    return

label sam_exclusive2_2:
    $ y_exclusivewatched = True
    play music t6 fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    mc "Hey, Sam."
    show sam zorder 2 at t11
    y "Eh?"
    mc "Ah..."
    "I suddenly notice that Sam is reading a different book from the one we've been reading together."
    mc "Sorry! I didn't mean to interrupt..."
    y "Ah, no..."
    y "I was kind of just waiting for you..."
    show sam     mc "Ah, if that's the case..."
    mc "Why don't we go ahead and get started?"
    y "Yes, let's!"
label sam_exclusive2_2_ch22:
    y "Actually, I have a request..."
    y "...Do you mind if I make some tea first?"
    mc "Not at all."
    y "Thanks very much."
    y "If there's one thing that can make my reading time here any better, it's a nice cup of tea."
    y "Not to mention for yourself, as well."
    show sam zorder 1 at thide
    hide sam
    "Sam stands up and makes her way to the closet."
    "I follow and watch as she retrieves a small water pitcher from the shelf - the kind with a filter inside."
    show sam zorder 2 at t11
    y "Can you hold this for a second?"
    mc "Sure..."
    "Sam hands me the water pitcher and also fetches an electric kettle."
    y "I'm going to plug this in at the teacher's desk, and then I'll go get some water."
    show sam zorder 1 at thide
    hide sam
    "She walks past me and sets the kettle down on the teacher's desk."
    "I simply watch her movements."
    "To my surprise, the way she moves really contrasts her speaking mannerisms."
    "Especially because of her long legs, Sam appears elegant and methodical."
    show sam zorder 2 at t11
    y "Okay, may I have the water pitcher?"
    y "Thanks. I'll be right back."
    mc "Ah, I might as well walk with you..."
    y "T-That's okay!"
    y "You stay here..."
    y "It won't take long."
    show sam zorder 1 at thide
    hide sam
    "Pitcher in hand, Sam hurries out of the classroom."
    show armstrong zorder 2 at t11
    m "Ah..."
    m "Did Sam leave you again?"
    mc "No, it's not like that this time."
    mc "She's just filling up the water pitcher to make tea."
    m 5 "Oh, okay!"
    m "Sorry for misunderstanding~"

    scene bg club_day
    with wipeleft_scene

    "..."
    "Ten minutes pass."
    "Sam said it wouldn't take long..."
    "Is something holding her up?"
    "I'm bored just waiting here, so I decide to go look for her."
    scene bg corridor
    with wipeleft_scene
    $ currentpos = get_pos()
    play music "<from " + str(currentpos) + " loop 10.893>bgm/6o.ogg"
    mc "Let's see..."
    "The most logical place for Sam to be would be the nearest water fountain..."
    $ y_name = "Sam"
    "I start heading down the hallway."
    $ y_name = "???"
    y "Haah.....haah...."
    y "....Haah.....haah...."
    "...What's that noise?"
    "It's coming from around the corner..."
    "It sounds like breathing."
    y "Khhhhh--"
    "A sharp inhale, like someone is sucking the air through their teeth."
    "Are they in pain...?"
    "I reach the corner and peer around it."
    mc "Sam...?"
    $ y_name = "Sam"
    show sam cuts zorder 2 at t11
    y "Kya--!"

    $ currentpos = 45.264 - (get_pos() / 2.0)
    $ audio.t6r = "<from " + str(currentpos) + " to 39.817 loop 0>bgm/6r.ogg"
    $ quick_menu = False
    play music t6r
    show sam zorder 1 at thide
    hide sam
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    $ y_name = "???"
    mc "{cps=150}Sam...?{/cps}{nw}"
    "{cps=150}I reach the corner and peer around it.{/cps}{nw}"
    "{cps=150}Are they in pain...?{/cps}{nw}"
    "{cps=150}A sharp inhale, like someone is sucking the air through their teeth.{/cps}{nw}"
    y "{cps=150}Khhhhh--{/cps}{nw}"
    "{cps=150}It sounds like breathing.{/cps}{nw}"
    "{cps=150}It's coming from around the corner...{/cps}{nw}"
    "{cps=150}...What's that noise?{/cps}{nw}"
    y "{cps=150}....Haah.....haah....{/cps}{nw}"
    y "{cps=150}Haah.....haah....{/cps}{nw}"
    $ y_name = "Sam"
    "{cps=150}I start heading down the hallway.{/cps}{nw}"
    "{cps=150}The most logical place for Sam to be would be the nearest water fountain...{/cps}{nw}"
    mc "{cps=150}Let's see...{/cps}{nw}"
    window hide(None)
    window auto
    scene bg club_day
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    "{cps=150}I'm bored just waiting here, so I decide to go look for her.{/cps}{nw}"
    "{cps=150}Is something holding her up?{/cps}{nw}"
    "{cps=150}Sam said it wouldn't take long...{/cps}{nw}"
    "{cps=150}Ten minutes pass.{/cps}{nw}"
    "{cps=150}...{/cps}{nw}"

    $ del _history_list[-37:]
    if poemwinner[0] == "sam" and chapter == 3:
        jump sam_exclusive2_2_ch23
    $ currentpos = 90.528 - (get_pos() * 2.0)
    $ audio.t6r = "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
    $ quick_menu = True
    play music t6r
    hide noise
    hide vignette
    show layer master
    show sam zorder 2 at t11
    y "I'm back."
    y "Thanks for waiting patiently."
    y "[player], do you like oolong tea?"
    mc "Ah, yeah."
    mc "Anything is fine."
    y "Very well."
    "Sam sets the temperature on the kettle to 200 degrees."
    y "Now it's time to get the teapot."
    mc "You really do this properly, don't you?"
    y "Of course..."
    y "I shouldn't do any less when I'm making tea for others."
    mc "Even if I'm not an expert on tea or anything...?"
    y "Huhu."
    y "In that case, you'll only be even more impressed."
    mc "Ah...perhaps I will!"
    show sam zorder 1 at thide
    hide sam
    "Sam fetches the teapot and begins measuring the tea leaves."
    "To my surprise, she even starts humming a little to herself."
    show sam zorder 2 at t11
    mc "You must be in a good mood now..."
    y "Is that so?"
    y "I was letting it show..."
    y "And you noticed."
    y "I was doing a bit of thinking..."
    y "And I decided that I would try expressing myself a little bit more."
    y "It turns out it's not very hard for me to do..."
    y "When it's you who's around, anyway."
    show sam     mc "Ah..."
    mc "That's great, Sam!"
    mc "Just don't push yourself too much."
    y "You're always worrying about me, [player]..."
    y "It's very endearing."
    mc "That's..."
    "Sam wasn't kidding..."
    "I don't even know if I can keep up with this...!"
    "I watch Sam pour a cup of tea for each of us."
    y "[player], I have another request."
    y "Do you mind if we sit on the floor today?"
    mc "Eh? Why's that?"
    y "It's a little bit easier on my back..."
    y "I can read with my back against the wall rather than bending over at my desk."
    mc "Ah, sorry, I didn't realize."
    y "No worries."
    y "I just have back pain fairly regularly, so I do my best to manage it."
    mc "Is that so?"
    mc "I wonder why that is..."
    y "It's most likely because my--"
    y "Ah--"
    y "M-My..."
    mc "Your posture, right?"
    mc "Always hunched over like that while reading..."
    y "Yes!"
    y "I have terrible reading posture!"
    y "So that's why we should sit on the floor."
    mc "Fair enough."
    mc "I'll go ahead and get the book."
    show sam zorder 1 at thide
    hide sam
    "I retrieve the book from my bag."
    mc "Ah, I have some chocolate as well..."
    "It's a bag of small chocolate candies."
    "I take it, since it'll go well with the tea."
    "Sam and I then sit against the wall, teacups at our sides."
    "As if in sync, we assume the same reading position as last time, each holding one half of the book."
    "Except this time..."
    "Our bodies are even closer to each other."
    show sam zorder 2 at t11
    y "I can't see too well..."
    mc "--!"
    show sam at d11
    "Sam slides closer until our shoulders are touching."
    "How am I supposed to focus on reading like this...?!"
    "Sam was always kind of cute, but..."
    "When she's being less apprehensive, it's almost more than I can handle!"
    y "Your teacup..."
    "Sam hands me my teacup."
    "Holding it with my hand that's not holding the book, I end up in a position that makes it even harder to focus."
    "Because now I need to worry about making sure I don't accidentally touch her chest...!"
    "Meanwhile, Sam hasn't noticed a single thing."
    "She wears her intense reading expression, and I can only presume the world around her has faded away."
    "I use all of my willpower to focus on reading."
    "..."
    "After a few minutes, I finally manage to relax a little."
    "I put the teacup between my legs and fumble with the chocolate wrapper."
    mc "Ah, sorry..."
    "I briefly let go of the book to finish opening the wrapper."
    mc "You can have as much as you want."
    y "Ah, that's..."
    y "That's okay, I won't take any..."
    mc "Eh? Are you sure?"
    y "Well..."
    y "If I touch it, then it might get smudges on the pages..."
    mc "Ah, you're right..."
    mc "I didn't even think about that."
    mc "My bad..."
    y "No need to apologize."
    y "I'll hold the book, okay?"
    mc "Are you sure...?"
    y "Of course."
    $ persistent.clear[3] = True
    $ renpy.save_persistent()
    scene y_cg2_bg
    show y_cg2_base
    show y_cg2_details
    show y_cg2_nochoc
    show y_cg2_dust1
    show y_cg2_dust2
    show y_cg2_dust3
    show y_cg2_dust4
    with dissolve_cg
    "Sam opens the book with both hands."
    "She holds it so that I don't have any harder of a time reading from it."
    "But as a result, her left arm is practically resting on top of my leg."
    mc "Well, in that case..."
    "Sam is already totally focused on reading again."
    "I take a chocolate candy and pop it into my mouth."
    "Then, I take another chocolate..."
    "And I hold it up to Sam."
    "She doesn't even look away from the book."
    "She simply parts her lips, as if this situation was completely natural."
    "But that means I can't stop here!"
    hide y_cg2_nochoc
    "I apprehensively place the chocolate in her mouth."
    "Just like that, Sam closes her lips over it."
    y "Eh...?"
    show y_cg2_exp2
    "Sam's expression suddenly breaks."
    y "Did..."
    y "Did I just..."
    "Sam looks at me like she needs to confirm what just happened."
    show y_cg2_exp3
    show y_cg2_nochoc:
        alpha 0
        linear 0.5 alpha 1
    hide y_cg2_exp2
    y "U-Um..."
    y "[player]..."
    mc "S-Sorry!"
    mc "I guess I shouldn't have done that..."
    stop music
    y "A-Ah..."
    "Sam starts to breathe heavily."
    y "I..."
    y "I can't..."
    y "[player]..."
    "Suddenly, Sam forcefully grabs my arm and jerks me to my feet."
    "My teacup gets knocked over."
    scene bg closet
    show sam zorder 2 at t11
    with wipeleft
    y "[player]..."
    play sound closet_close
    show dark zorder 100
    with wipeleft
    y "My heart..."
    y 2y6 "My heart won't stop pounding, [player]..."
    y "I can't calm down."
    y "I can't focus on anything anymore...!"
    y "Can you feel it, [player]?"
    "Sam suddenly presses my hand against her chest."
    play music hb
    show layer master at heartbeat
    y "Why is this happening to me?"
    y "I feel like I'm losing my mind..."
    y 3y4 "I can't make it stop."
    y 3y6 "It even makes me not want to read..."
    y "I just want..."
    y "...to look..."
    y "...at you."
    hide sam
    show sam eyes
    $ pause(3.0)
    y "...Haah..."
    $ pause(3.0)
    y "...Haah..."
    $ pause(3.0)
    y "...Haah..."
    $ pause(3.0)
    play sound closet_open
    stop music
    show layer master
    hide sampupils
    show sam at face
    with None
    show sam at t32 with None
    hide dark
    show armstrong zorder 3 at f31
    with wipeleft
    m "U-Um..."
    m "It's...time to share poems..."




    return

label sam_exclusive2_2_ch23:
    $ config.skipping = False
    scene black
    with None
    $ audio.t6g = "<loop 10.893>bgm/6g.ogg"
    play music t6g
    $ pause(4.62)
    scene bg corridor
    show sam eyes_base
    $ pause(1.0)
    show bg glitch:
        yoffset 480 ytile 2
        linear 0.25 yoffset 0
        repeat
    show sam glitch at i11
    $ gtext = glitchtext(80)
    $ currentpos = get_pos()
    play music g1
    y "{cps=70}[gtext]{nw}"
    stop music
    scene bg corridor
    show sam at i11
    $ quick_menu = True
    y "Um..."
    y "Wait..."
    y "How did I..."
    y 2y6 "...Sorry, I just had a really weird déjà vu..."
    y "This hasn't happened before or anything...right?"
    y "My head has been a little fuzzy lately..."
    y "I hope it hasn't really been showing or anything!"
    y "I would hate for you to think I'm weird just after we started spending time together..."
    y "I mean..."
    show bg corridor:
        xoffset 0
        parallel:
            0.36
            xoffset 1
            repeat
        parallel:
            0.49
            xoffset 0
            repeat
    show black zorder 5:
        alpha 0.5
        parallel:
            0.36
            alpha 0.5
            repeat
        parallel:
            0.49
            alpha 0.475
            repeat

    play music t9
    y "Everyone has a few unusual things about them."
    y "But expressing those things so soon after meeting someone is usually seen as inappropriate...or unlikable."
    y "At least, that's what I've discovered."
    y "When I was a bit younger, I think I would come on really strongly and get a little too intense..."
    y "It made people not want to be around me."
    y "So...I started hating those things about myself."
    y "My obsession with certain hobbies."
    y "And the way I can't control myself when I get too excited about something."
    y "So..."
    y "I eventually stopped trying to talk to people."
    y "If nobody could ever like me for the things that matter most to me..."
    y "...Then it's just easier if I close myself off."
    y "But recently, something's been wrong."
    y "I don't know what it is."
    y 2y6 "But every time we come to the club, my heart starts to go crazy."
    y "Like it's going to rip out of my chest."
    y "It overwhelms me with energy and emotions that I can't let out."
    y "It's been making me do weird things."
    y "I don't know why it's happening!"
    stop music
    y "[player]..."
    y "Is it just me, or has Armstrong been acting a little off lately?"
    y "She's always been a sweetheart ever since I joined the club..."
    y "But recently, I've been feeling something sharp whenever she's around."
    y 2y4 "I'm not crazy, right?"
    y 2y1 "Please tell me I'm not!"
    y "I couldn't say anything before, because she's always listening!"
    y 2y3 "But finally, we're alone..."
    y "Can we just stay here for a while?"
    y "Yeah..."
    y "..."
    play music hb
    show layer master at heartbeat
    show sam as yuri_eyes zorder 4:
        "sam/eyesfull.png"
        i11
        alpha 0.0
        block:
            2.012 * 4 - 1.49
            alpha 1.0
            0.52
            alpha 0.0
            1.49
            repeat
    $ pause(2.0)
    $ ad = 40.0
    $ ac = 1.0
    show sam onlayer front at malpha(ac / ad)
    y "I just want to stay here."
    $ ac += 0
    show sam onlayer front at malpha(ac / ad)
    y "Just the two of us."
    $ ac += 0
    show sam onlayer front at malpha(ac / ad)
    y "We can stay here until the club ends."
    $ ac += 0
    show sam onlayer front at malpha(ac / ad)
    y "And then we'll have the clubroom all to ourselves."
    $ ac += 0.5
    show sam onlayer front at malpha(ac / ad)
    y "Nobody to interfere with our reading time."
    $ ac += 0.5
    show sam onlayer front at malpha(ac / ad)
    y 1y4 "Nobody to make me feel like stabbing myself in the throat."
    $ ac += 0.5
    show sam onlayer front at malpha(ac / ad)
    y "Ahaha..."
    $ ac += 0.5
    show sam onlayer front at malpha(ac / ad)
    y "That was a joke!"
    $ ac += 0.5
    show sam onlayer front at malpha(ac / ad)
    y "Just a joke."
    $ ac += 0.5
    show sam onlayer front at malpha(ac / ad)
    y "I do like knives, though..."
    $ ac += 0.5
    show sam onlayer front at malpha(ac / ad)
    y "It sounds strange, but you wouldn't understand if you've never seen how beautiful they can be."
    $ ac += 0.5
    show sam onlayer front at malpha(ac / ad)
    y "I have an idea."
    $ ac += 1
    show sam onlayer front at malpha(ac / ad)
    y "Why don't you come to my house sometime?"
    $ ac += 1
    show sam onlayer front at malpha(ac / ad)
    y 1y6 "I can show you my collection."
    $ ac += 1
    show sam onlayer front at malpha(ac / ad)
    y "I've gotten them all from various artisans."
    $ ac += 1
    show sam onlayer front at malpha(ac / ad)
    y "I make sure to give them all their fair share of use."
    $ ac += 1
    show sam onlayer front at malpha(ac / ad)
    y "I don't want them to get lonely or anything..."
    $ ac += 1
    show sam onlayer front at malpha(ac / ad)
    y 1y6 "Nobody deserves to be lonely."
    $ ac += 1
    show sam onlayer front at malpha(ac / ad)
    y 1y4 "Nobody."
    $ ac += 1
    show sam onlayer front at malpha(ac / ad)
    y "And that's why I'm so happy you joined the Literature Club, [player]."
    $ ac += 1
    show sam onlayer front at malpha(ac / ad)
    y "Now we don't need to be lonely anymore."
    $ ac += 1
    show sam onlayer front at malpha(ac / ad)
    y "Because we have each other."
    $ ac += 1
    show sam onlayer front at malpha(ac / ad)
    y "Every day."
    $ ac += 1
    show sam onlayer front at malpha(ac / ad)
    y "That's all we need."
    $ ac += 1
    show sam onlayer front at malpha(ac / ad)
    y 1y6 "You know what?"
    $ ac += 1
    show sam onlayer front at malpha(ac / ad)
    y "Let's quit the Literature Club."
    $ ac += 1
    show sam onlayer front at malpha(ac / ad)
    y "There's no need for us to be around Armstrong's slimy tongue anymore."
    $ ac += 1
    show sam onlayer front at malpha(ac / ad)
    y 1y4 "Not to mention that other pathetic child."
    $ ac += 1
    show sam onlayer front at malpha(ac / ad)
    y "We can walk home together every day after school."
    $ ac += 1
    show sam onlayer front at malpha(ac / ad)
    y "And read together."
    $ ac += 1
    show sam onlayer front at malpha(ac / ad)
    y "Eat together."
    $ ac += 1
    show sam onlayer front at malpha(ac / ad)
    y "Sleep together."
    $ ac += 1
    show sam onlayer front at malpha(ac / ad)
    y "Doesn't that sound perfect?"
    $ ac += 2
    show sam onlayer front at malpha(ac / ad)
    y "It's everything we could ever want."
    $ ac += 2
    show sam onlayer front at malpha(ac / ad)
    y "Isn't that why you joined the club in the first place?"
    $ ac += 2
    show sam onlayer front at malpha(ac / ad)
    y "It's almost like it was fate."
    $ ac += 2
    show sam onlayer front at malpha(ac / ad)
    y "Fate that we would meet each other."
    $ ac += 2
    show sam onlayer front at malpha(ac / ad)
    y "And now we get the happy ending that I've patiently waited years for."
    $ ac += 2
    show sam onlayer front at malpha(ac / ad)
    y "Will you do that with me, [player]?"
    $ ac += 2
    show sam onlayer front at malpha(ac / ad)
    $ gtext = glitchtext(200)
    y "Will{space=60}[gtext]{nw}"
    hide armstrong onlayer front
    window hide(None)
    $ poemsread = 0
    $ y_gave = False
    play music t5
    scene bg club_day
    window show(None)
    window auto

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
