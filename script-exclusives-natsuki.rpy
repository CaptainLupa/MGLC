label bladewolf_exclusive_1:
    scene bg club_day
    with wipeleft_scene
    n "Ugh...!"
    "I hear Bladewolf utter an exasperated sigh from within the closet."
    "She seems to be annoyed by something."
    "I approach her, in case she needs a hand."
    play music t6 fadeout 1
    scene bg closet
    show bladewolf zorder 2 at t11
    with wipeleft_scene
    mc "You looking for something in there?"
    n "Freaking Armstrong..."
    n "She never puts my stuff back in the right spot!"
    n "What's the point in keeping your collection organized if someone else is just gonna mess it up?"
    "Bladewolf slides a bunch of stacked books and boxes across the shelf."
    mc "Manga..."
    n "You read manga, right?"
    mc "Ah--"
    mc "...Sometimes..."
    "Manga is one of those things where you can't admit you're really into it until you figure out where the other person stands."
    mc "...How did you know, anyway?"
    n "I heard you bring it up at some point."
    n "Besides, it's kind of written on your face."
    "What's that supposed to mean...?"
    mc "I-I see..."
    "There's a lone volume of manga amidst a stack of various books on the side of one of the shelves."
    "Curious, I pull it out of the stack."
    n "{i}There{/i} it is!"
    "Bladewolf snatches it out of my hand."
    "She then turns to a box of manga and slips the volume right into the middle of the rest."
    n "Aah, much better!"
    n "Seeing a box set with one book missing is probably the most irritating sight in the world."
    mc "I know that feel..."
    "I get a closer look at the box set she's admiring."
    mc "Parfait Girls...?"
    "It's a series I've never heard of in my life."
    "That probably means it's either way out of my demographic, or it's simply terrible."
    n "If you're gonna judge, you can go do it through the glass on that door."
    "She points to the classroom door."
    mc "H-Hey, I wasn't judging anything...!"
    mc "I didn't even say anything."
    n "It was the tone of your voice."
    n "But I'll tell you one thing, [player]."
    n "Consider this a lesson straight from the Literature Club: Don't judge a book by its cover!"
    n "In fact--"
    "Bladewolf pulls out the first volume of Parfait Girls from the box."
    n "I'm gonna show you exactly why!"
    "She shoves the book right into my hands."
    mc "Ah..."
    "I stare at the cover."
    "It features four girls in colorful attire striking animated feminine poses."
    "It's...exceedingly \"moe\"."
    n "Don't just stand there!"
    mc "Uwa--"
    show bladewolf zorder 1 at thide
    hide bladewolf
    "Bladewolf grabs my arm and pulls me out of the closet."
    "She then takes a seat against the wall, beneath the windowsills."
    "She pats on the ground next to her, signaling me to sit there."
    show bg club_day
    show bladewolf zorder 2 at t11
    with wipeleft
    mc "Wouldn't chairs be more comfortable...?"
    "I take my seat."
    n "Chairs wouldn't work."
    n "We can't read at the same time like that."
    mc "Eh? Why's that?"
    mc "Ah...I guess it's easier to be close together like this..."
    n "--!"
    n "D-Don't just say that!"
    n "You'll make me feel weird about it!"
    "Bladewolf crosses her arms and scootches an inch away from me."
    mc "Sorry..."
    show bladewolf     "I didn't exactly expect to be sitting this close to her, either..."
    "Not that I can say it's a particularly bad thing."
    "I open the book."
    "It's only a few seconds before Bladewolf once again inches closer, reclaiming the additional space while she hopes I won't notice."
    "I can feel her peering over my shoulder, much more eager to begin reading than I am."
    n "Wow, how long has it been since I read the beginning...?"
    mc "Hm?"
    mc "You don't go back and flip through the older volumes every now and then?"
    n "Not really."
    n "Maybe sometimes after I've already finished the series."
    n "Hey, are you paying attention?"
    mc "Uh..."
    "I am, but nothing's really happened yet, so I can talk at the same time."
    "It looks like it's about a bunch of friends in high school."
    "Typical slice-of-life affair."
    "I kind of grew out of these, since it's rare for the writing to be entertaining enough to make up for the lack of plot."
    mc "So..."
    mc "What should I expect from this?"
    mc "Is there going to be plot?"
    n "Well, obviously!"
    n "You think I would enjoy something that didn't have a plot?"
    n "I mean..."
    n "Well, I guess I know what you're saying..."
    n "A lot of the beginning is about simple things..."
    n "Like there's a really funny chapter where they're obsessed with a guy at the ice cream shop..."
    n "But that just helps you get to know the characters!"
    n "And besides, it's still entertaining."
    n "But later on, there's all kinds of drama..."
    n "Like when they get into all their backstories, and when some of the romance starts to happen..."
    n "That's really what makes it so good."
    n "There are so many touching parts."
    mc "Ah, is that so?"
    mc "It sounds like you really know what you're talking about."
    mc "Maybe I underestimated you."
    n "Ehehe."
    n "...Hey, wait!"
    n "What's {i}that{/i} supposed to mean?!"
    mc "Uwa--"
    "Bladewolf gives me a little shove."
    mc "I just meant that I haven't yet seen you at your full power..."
    n "Hmph. Good save."
    mc "Ah... This chapter seems like it's about baking."
    mc "This is just a guess, but is there a lot of baking in this manga?"
    n "Well--"
    "Bladewolf pauses for a moment, as if she doesn't want to admit something."
    n "...Yeah."
    n "Why does that matter?"
    mc "It doesn't, I was just curious..."
    mc "Since you enjoy baking too, right?"
    n "That's--"
    n "Just a coincidence!"
    n "I just happened to get into baking around the same time I got this manga."
    n "Like I would ever get into anything because it's in a manga."
    n "I feel bad for anyone that impressionable."
    n "Ahaha!"
    "Definitely not a coincidence..."
    "I guess that explains Bladewolf's interest in baking."
    "Still, of all the hobbies to pick up from a manga, that's definitely one of the better ones."
    "Not to mention she's really good at it, so who am I to judge?"
    $ persistent.clear[0] = True
    $ renpy.save_persistent()
    scene n_cg1_bg
    show n_cg1_base
    with dissolve_cg
    "..."
    "We read on for a few more minutes."
    "I've finished a couple chapters at this point."
    mc "..."
    mc "...Are you sure this isn't boring for you?"
    n "It's not!"
    mc "Even though you're just watching me read?"
    n "Well...!"
    n "I'm...fine with that."
    mc "If you say so..."
    mc "...I guess it's fun sharing something you like with someone else."
    mc "I always get excited when I convince any of my friends to pick up a series I enjoy."
    mc "You know what I mean?"
    n "...?"
    mc "Hm?"
    mc "You don't?"
    show n_cg1_exp2 at cgfade
    n "Um..."
    n "That's not..."
    n "Well, I wouldn't really know."
    mc "...What do you mean?"
    mc "Don't you share your manga with your friends?"
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "Could you not rub it in?"
    n "Jeez..."
    mc "Ah... Sorry..."
    n "Hmph."
    n "Like I could ever get my friends to read this..."
    n "They just think manga is for kids."
    n "I can't even bring it up without them being all like..."
    n "'Eh? You still haven't grown out of that yet?'"
    n "Makes me want to punch them in the face..."
    mc "Urgh, I know those kinds of people..."
    mc "Honestly, it takes a lot of effort to find friends who don't judge, much less friends who are also into it..."
    mc "I'm already kind of a loser, so I guess I gravitated toward the other losers over time."
    mc "But it's probably harder for someone like you..."
    hide n_cg1_exp3
    n "Hm."
    n "Yeah, that's pretty accurate."
    "{i}...Wait, which part??{/i}"
    n "I mean, I feel like I can't even keep it in my own room..."
    n "I don't even know what my dad would do if he found this."
    n "At least it's safe here in the clubroom."
    show n_cg1_exp3 at cgfade
    n "'Cept Armstrong was kind of a jerk about it..."
    n "Ugh! I just can't win, can I?"
    mc "Well, it paid off in the end, didn't it?"
    mc "I mean, here I am, reading it."
    n "Well, it's not like that solves any of my problems."
    mc "Maybe..."
    mc "But at least you're enjoying yourself, right?"
    hide n_cg1_exp3
    show n_cg1_exp2 at cgfade
    n "--"
    n "..."
    n "...So?"
    mc "Ahaha."
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "Jeez, that's enough!"
    n "Are you gonna keep reading, or what?"
    mc "Yeah, yeah..."
    "I flip the page."
    "Suddenly, Bladewolf starts laughing."
    hide n_cg1_exp3
    show n_cg1_exp1 at cgfade
    n "Ahahaha!"
    n "I totally forgot that happens!"
    "Bladewolf puts her finger on one of the panels."
    n "Minori is my favorite character."
    n "You always feel a little bad for her, since she's so unlucky."
    n "But it gets especially bad when--"
    hide n_cg1_exp1
    n "Uu..."
    n "I shouldn't be talking about that yet!"
    n "Just finish this chapter!"
    scene bg club_day
    with dissolve_cg
    "Bladewolf's voice sparkles with excitement."
    "It's a stark contrast to her usual bossy tone."
    "But if she's not used to sharing her favorite manga with her friends, I can understand why."
    "It's hard to express in words the feeling you get when connecting with someone like that."
    "And being able to provide that to Bladewolf, for whom it's a rare experience..."
    "The thought makes me smile a little to myself."
    show armstrong zorder 3 at f21
    m "Okay, everyone!"
    mc "Eh?"
    m "Are you all ready with today's poems?"
    mc "..."
    show armstrong zorder 2 at t21
    show bladewolf zorder 3 at f22
    n "Oh, come on!"
    n "Could your timing be any worse?"
    show bladewolf zorder 2 at t22
    show armstrong zorder 3 at f21
    m 5 "Sorry~!"
    m "I just need to make sure we have enough time."
    m "Though you do look pretty cozy over there. Ahaha!"
    show armstrong zorder 2 at t21
    show bladewolf zorder 3 at f22
    n "Eh...?"
    n "A-Ah!"
    "Bladewolf suddenly notices how close she's gotten to me."
    "She hastily slides herself a good twelve inches away from me."
    show armstrong zorder 1 at thide
    show bladewolf zorder 2 at t11
    hide armstrong
    mc "Alright..."
    mc "Guess I'll stop here for now."
    "I close the book and hand it towards Bladewolf."
    n "You're just giving it back...?"
    n "Don't you want to know what happens?"
    mc "Ah... Yeah, but..."
    mc "Armstrong just said--"
    n "Don't be dumb."
    n "Just take it home with you."
    mc "Eh?"
    mc "...Is that really alright?"
    "I say that mostly because I really didn't plan on using my spare time to read this..."
    n "Well, of course."
    n "It would take forever to finish if you didn't take it home."
    n "Just finish that one before tomorrow, so we can start the next one."
    n "And if it gets bent, I'll kill you."
    mc "By tomorrow...?"
    show bladewolf zorder 1 at thide
    hide bladewolf
    "I only got partway through the volume so far."
    "I might fall behind on some shows if I try to get through this..."
    "But I suppose that's a necessary sacrifice in exchange for seeing Bladewolf's enthusiastic face."
    "Or am I more scared of what will happen if I {i}don't{/i} finish it...?"
    mc "Alright, then!"
    "I stand up."
    "I return to where I put my stuff and carefully slip the book into my bag."
    return


label bladewolf_exclusive_2:
    $ n_exclusivewatched = True
    play music t6 fadeout 1
    scene bg club_day
    show bladewolf zorder 2 at t11
    with wipeleft_scene
    n "..."
    "It's not long before Bladewolf comes up to me expectantly."
    mc "Yeah, yeah."
    mc "Don't worry, I kept my promise."
label bladewolf_exclusive_2_ch3:
    "I pull the first volume of Parfait Girls out from my bag."
    "Bladewolf takes it from my hands, then quickly turns it over, presumably to check for wrinkles."
    mc "Hey, I'm not that careless..."
    mc "I handle manga all the time, you know."
    n "I just wanted to make sure!"
    n "Can you blame me for being paranoid?"
    n "I don't give people my manga every day, you know."
    mc "That's true..."
    mc "I don't blame you."
    n "Well anyway, let me put this one back."
    n "I'm gonna get the next one, okay?"
    show bladewolf zorder 1 at thide
    hide bladewolf
    "Bladewolf makes her way to the closet."
    "I follow."
    show bg closet
    show bladewolf zorder 2 at t11
    with wipeleft
    n "So you're gonna tell me everything you thought, right??"
    n "Where did this volume leave off again? I forget."
    mc "Ah, the chapter ended when Minori and Alice found--"
    show bladewolf at h11
    n "{i}Armstrong!!{/i}"
    "Bladewolf's voice resonates out from inside the closet."
    mc "Eh...?"
    "I peer inside."
    "All of Bladewolf's books are lined up on the top shelf."
    n "Did you move my manga again?!"
    show armstrong at l31
    m "Ah, sorry, sorry!"
    m "The teacher got mad at me for taking up so much space in her closet..."
    m "So I had to move some stuff around and clean up a little bit."
    m "It's all still there, I just had to organize it a bit!"
    show armstrong zorder 1 at thide
    hide armstrong
    n "Ugh..."
    "The top shelf is far above Bladewolf's head."
    show bladewolf at h11
    "She makes a futile hop, trying to figure out how to reach her manga."
    n "Jeez...!"
    n "This is so inconvenient!"
    n "I'm moving these all back down."
    n "There's plenty of room on these shelves."
    n "And besides..."
    n "They're really pretty to look at when they're all lined up!"
    n "Why would you waste that on the top shelf?"
    mc "Ah, Bladewolf..."
    mc "There's a stool on the wall there."
    "In the closet, there's a collapsible stool that's hanging on the wall."
    mc "If you want, I can reach up there and hand them to you..."
    n "I can get them myself!"
    "Bladewolf grabs the stool from the wall and unfolds it."
    n "You think I'm too short or something?"
    mc "I mean--"
    n "I {i}knew{/i} it!"
    n "Well, you know what?"
    n "Just watch me!"
    "Bladewolf hops onto the stool, which ends up being a little wobbly because of its collapsible design."
    n "A-Ah..."
    mc "Careful..."
    n "I know what I'm doing!!"
    "Standing on the stool, Bladewolf's fingertips reach the top shelf."
    "The stool would be enough for me to easily grab the books, but Bladewolf is being stubborn as usual."
    n "U-Uuuh..."
    "Bladewolf uses her fingers to scoot one of the smaller boxes to the edge of the shelf."
    n "See...?"
    n "Kyah--!"
    "The box suddenly tips."
    "Bladewolf barely catches it before it falls to the floor."
    "The stool wobbles."
    show bladewolf at h11
    n "Wawaa--"
    "Losing balance, Bladewolf hops off the stool."
    "Thankfully, she was able to stay on her feet."
    "She holds the box triumphantly."
    n "T-There!"
    "Having almost fell, Bladewolf is a bit shaken up."
    mc "Jeez..."
    mc "No need to prove yourself to me."
    mc "There's no way you'll be able to get the bigger boxes like that."
    mc "I can reach them, so just--"
    n "I said I can do it!"
    n "I don't want your help, okay?"
    mc "Sigh..."
    n "I'm gonna get a chair, so just hang on."
    show bladewolf zorder 1 at thide
    hide bladewolf
    "Bladewolf forces her way past me out of the closet."
    n "Let's see..."
    "The classroom chairs have the desks attached, so they're too inconvenient to fit into the closet."
    n "Aha!"
    "Bladewolf trots over to the teacher's desk, which has a computer chair behind it."
    "She rolls it on its wheels back over to the closet."
    show bladewolf zorder 2 at t11
    mc "Ah--"
    "It's a little dangerous, since the chair swivels and rolls."
    "But I've already learned my lesson, so I keep my mouth shut."
    n 1 "Ush--"
    "Bladewolf climbs onto the chair, then slowly balances onto her feet."
    "Since she refuses my help, I take a seat with my back against the side of the doorway and simply watch."
    $ persistent.clear[1] = True
    $ renpy.save_persistent()
    scene n_cg2_bg
    show n_cg2_base
    with dissolve_cg
    n "Aha! There we go!"
    n "See? I can easily do it now."
    "Bladewolf grabs a stack of manga and bends down to put it on the shelf below."
    show n_cg2_base at n_cg2_wiggle
    n "W-Wahh--"
    "The chair swivels."
    "Bladewolf catches herself on the shelf."
    show n_cg2_exp1 at cgfade
    n "What are you doing??"
    n "Can you at least hold the chair steady instead of sitting and doing nothing?"
    "{i}(Who was it who told me not to help...?){/i}"
    mc "Yeah, yeah...I got you."
    hide n_cg2_exp1
    "I hold the chair while Bladewolf reaches back up."
    mc "--!"
    "I can..."
    "{i}I can almost see up her skirt?!{/i}"
    mc "Guh--"
    "I force myself to turn away."
    "Bladewolf seriously didn't think this through...!"
    "Once she realizes, I'll be dead!"
    show n_cg2_base at n_cg2_wiggle
    n "Hup--"
    "Bladewolf wraps her arms around the Parfait Girls box set, easily the largest one on the shelf."
    n "Uu...heavy..."
    show n_cg2_exp1 at cgfade
    n "Hey, [player]..."
    n "I-I don't think I can bend down without falling...!"
    n "Hurry and take this one..."
    mc "Eh?"
    mc "But then I have to let go of the chair..."
    n "That's fine...!"
    n "Just for a second!"
    n "Hurry up..."
    mc "Alright...!"
    mc "Let me just stand up."
    "I slowly release my grip from the chair."
    n "What do you mean 'stand up'?"
    "Bladewolf looks down at me."
    n "Why are you all the way back--"
    stop music fadeout 1
    n "E-Eh...?"
    "Bladewolf looks like she just realized something, but she'll lose her balance if she moves."
    mc "Bladewolf, the box--"
    play music t7
    show n_cg2_exp2 at cgfade
    n "{i}W-What are you looking at?!{/i}"
    mc "--!"
    show n_cg2_base at n_cg2_wiggle_loop
    show n_cg2_exp1 at n_cg2_wiggle_loop
    show n_cg2_exp2 at n_cg2_wiggle_loop
    n "You're trying to look at my...m-my..."
    "Bladewolf's legs shake."
    mc "I-I'm not! I was just--"
    mc "--Bladewolf, don't try to move!"
    mc "Just give me the box!"
    n "You...you perv!"
    n "You set me up!!"
    n "Go away!"
    n "Get out!"
    mc "But--"
    n "I'll do it myself!!"
    hide n_cg2_exp2
    n "A-Ah--"
    "The chair suddenly swivels beneath Bladewolf's feet."
    mc "Bladewolf--!"
    show n_cg2_base at n_cg2_wiggle_loop
    show n_cg2_exp1 at n_cg2_wiggle_loop
    show n_cg2_exp2 at n_cg2_wiggle_loop
    n "{i}Kyaaaaa!{/i}"
    "The scene turns to chaos in a split second."
    "The chair flies from under Bladewolf's feet."
    "Frantically, I try to catch her."
    "The box topples out of her hands, and the books go flying."
    mc "I got you--"
    show n_cg2_base at n_cg2_zoom
    show n_cg2_exp1 at n_cg2_zoom
    show n_cg2_exp2 at n_cg2_zoom
    show black:
        alpha 0
        0.10
        linear 0.10 alpha 1
    $ pause(0.20)
    stop music
    play sound "sfx/fall2.ogg"
    "{i}Crash!{/i}"
    "The full force of Bladewolf's body against me throws me to the ground."
    "A whole bunch of books pelt me in the face."
    "Bladewolf tries to shield herself with her own arms as her face lands straight on my chest."
    mc "Ungh..."
    "My right arm and my back seriously felt the impact."
    play music t8 fadeout 1.0
    scene bg closet
    show bladewolf at face
    with dissolve_cg
    n "U-Uu..."
    "Slowly, Bladewolf comes to her senses."
    mc "Ghk--!"
    "She presses her arms straight into me to prop herself up."
    n "Eh...?"
    "Bladewolf seems to realize that it's not the floor that's beneath her."
    n "G-Guuuuu...!!"
    n "Gross! Gross!"
    mc "Ghak--!"
    "A fist pounds into my chest."
    "Bladewolf then hoists herself to her feet."
    show bladewolf zorder 2 at t11
    n "What were you thinking?!"
    n "You sicko!"
    show armstrong zorder 3 at f31
    m "Everything okay over there...?"
    m "I heard a loud noise..."
    "Armstrong suddenly peers in."
    show armstrong zorder 2 at t31
    show bladewolf zorder 3 at f11
    n "Armstrong!"
    n "See what happens when you put the manga on the top shelf?!"
    n "Are you trying to kill your club members or something?"
    n "Jeez!"
    show bladewolf zorder 2 at t11
    show armstrong zorder 3 at f31
    m 5 "S-Sorry, sorry!"
    m "Ahaha..."
    show armstrong zorder 2 at t31
    show bladewolf zorder 3 at f11
    n "Oh, and one more thing."
    n "It seems like your most recent club member is a total pervert."
    n "So I hope you're happy."
    show bladewolf zorder 2 at t11
    mc "I didn't--!"
    "Somehow, it's impossible for me to explain this whole bizarre situation to Armstrong."
    mc "I didn't do anything, I swear...!"
    show armstrong zorder 3 at f31
    m "I know, I know, don't worry~"
    show armstrong zorder 1 at thide
    hide armstrong
    "Armstrong says that quietly to me."
    "Looks like I'm off the hook..."
    stop music fadeout 1
    n "Oh no...!"
    n "My...my..."
    show bladewolf     mc "Eh?"
    "I look down."
    "Bladewolf is kneeling on the floor, holding one of the books that are scattered all over."
    "There's a large diagonal crease along the page that she's desperately trying to smooth out."
    mc "Ah, it must have landed on the page..."
    stop music fadeout 1
    "Bladewolf tries a bit more to fix the crease, but she can't get it out."
    show bladewolf     "Suddenly, she gives up and slams the book shut, then throws it to the floor."
    "Instead of continuing to yell, she just lowers her head."
    play music t9
    show bladewolf at s11
    n "{i}*Sob*{/i}"
    mc "...Bladewolf, are you--"
    show bladewolf zorder 2 at t11
    n "No!"
    "Bladewolf's voice squeaks."
    "I see tears on her face."
    mc "Ah..."
    mc "I'll help get the crease out, okay?"
    mc "It's partially my fault, so..."
    "Bladewolf shakes her head, still looking down."
    n "No..."
    n "I don't even care that much..."
    n "I'm just..."
    n "Having a really bad day today..."
    "Bladewolf sobs again."
    n "I didn't mean to take it out on you..."
    n "I really didn't mean to!"
    mc "It's...it's fine."
    mc "...Is there anything you want to talk about?"
    show bladewolf     "Bladewolf shakes her head."
    n "Just..."
    n "Every day..."
    n "...is...so hard."
    n "I just want to..."
    n "...come to the club and..."
    n "..."
    "Bladewolf falls silent again."
    "I can't press her, so I can only do what I know how to do."
    mc "Alright..."
    mc "Well, I'll help clean this up."
    mc "And I'll move the rest of your manga for you."
    mc "Ah."
    "I pick up volume 2 of Parfait Girls."
    mc "We'll set this one aside."
    mc "This'll help cheer you up a bit, right?"
    mc "We can get started on it once I'm done here."
    show bladewolf     "Bladewolf looks up with her glossy eyes."
    "Her lip quivers."
    n "You're..."
    n "You're really nice to me..."
    mc "Eh?"
    "That sounds really strange, coming from Bladewolf."
    "I didn't expect it at all."
    mc "Well..."
    mc "I'm just treating you like a friend, you know?"
    n "Nn..."
    show bladewolf at thide
    hide bladewolf
    "Bladewolf lowers her head and stifles another sob."
    "I'm not sure what happened to her today, but being nice is the least I could do."
    "The next couple minutes are silent between us as I begin gathering the scattered books."
    "I make sure to slip them into the box in their correct order."
    "After a little bit, Bladewolf starts helping."
    "It isn't long before we're done, and I hoist the box onto the shelf where Bladewolf wanted to put it."
    "Then, I get on the stool and quickly finish moving the rest of her books from the top shelf."
    mc "Alright--!"
    mc "That should do it."
    "I hop off the stool."
    "Bladewolf averts her gaze."
    show bladewolf at t11
    n "T-Thanks..."
    mc "Ahaha..."
    mc "It's nothing."
    "Bladewolf is holding the volume I set aside in her hands."
    mc "Alright, I'm ready."
    n "Good."
    n "Even if you weren't, I'd make you anyway."
    n "You're taking responsibility for what you said."
    n "The thing about cheering me up."
    mc "If you insist!"
    play music t8 fadeout 1
    scene bg club_day
    with wipeleft_scene
    "We sit in the same spot as last time, and I open the second volume."
    "Bladewolf's mood quickly improves, laughing and pointing things out to me."
    "She's surprisingly sharp, making note of a lot of subtle repeated jokes and background elements."
    "In the end, I'm pretty impressed by how everything ties together in this manga."
    "I guess Bladewolf has good taste after all."
    "After some time, Armstrong gets our attention as usual, and it's time to share poems again."
    show bladewolf zorder 2 at t11
    mc "Guess I'll be holding onto this for now."
    n "Yep!"
    n "Even you sound more enthusiastic this time."
    mc "Well, I'm starting to get into it, you know."
    n "Ehehe."
    n "Told you."
    mc "Yeah, yeah..."
    show bladewolf zorder 1 at thide
    hide bladewolf
    "I return to my seat and slip the book into my bag."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
