label ch21_main:
    scene bg club_day2
    with dissolve_scene_half
    play music t2g3
    show armstrong zorder 2 at t11
    show layer master:
        subpixel True
        truecenter
        linear 240 rotate 8 zoom 1.30
    m "Hi again, [player]!"
    m "Glad to see you didn't run away on us. Hahaha!"
    mc "Nah, don't worry."
    mc "This might be a little strange for me, but I at least keep my word."
    show armstrong zorder 1 at thide
    hide armstrong
    "Well, I'm back at the Literature Club."
    "I was the last to come in, so everyone else is already hanging out."
    show sam glitch2 zorder 2 at t32
    y "Thanks for keeping your promise, [player]."
    y "I hope this isn't too overwhelming of a commitment for you."
    y "Making you dive headfirst into literature when you're not accustomed to it..."
    show bladewolf glitch1 zorder 2 at i33
    n "Oh, come on! Like he deserves any slack."
    n "You already had to be dragged here by Armstrong."
    n "I don't know if you plan to just come here and hang out, or what..."
    n "But if you don't take us seriously, then you won't see the end of it."
    show armstrong onlayer front at l41
    m "Bladewolf, you certainly have a big mouth for someone who keeps her manga collection in the clubroom."
    n "M-M-M...!!"
    show armstrong onlayer front at lhide
    hide armstrong onlayer front
    "Bladewolf finds herself stuck between saying \"Armstrong\" and \"Manga\"."
    show bladewolf at h33
    n "Manga is literature!!"
    show bladewolf zorder 1 at thide
    hide bladewolf
    "Swiftly defeated, Bladewolf plops back into her seat."
    show sam zorder 2 at t11
    y "I'm sorry, [player]..."
    y "We'll make sure to put your comfort first, okay?"
    show sam     "Sam shoots Bladewolf with a disappointed glance."
    y "Um, anyway..."
    y "Now that you're in the club and all..."
    y "...Perhaps you might have interest in picking up a book to read?"
    mc "Well..."
    mc "I can't really say no either way."
    mc "Like you said, I'm in this club now."
    mc "So it only feels right for me to do something like that, if you ask."
    y "W-Wait..."
    y "I didn't mean it like that!"
    y "Uu..."
    y "If you don't really want to, then forget I said anything, I guess..."
    mc "Ah--No, it's not that, Sam."
    mc "I want to try to be a part of this club."
    mc "So even if I don't read often, I'd be happy to pick up a book if you wanted me to."
    y "A-Are you sure...?"
    y "I just felt like..."
    y "...Well, as Vice President and all..."
    y "...That I should help you get started on something you might like."
    "Sam reaches into her bag and pulls out a book."
    y "I didn't want you to feel left out..."
    y "So I picked out a book that I thought you might enjoy."
    y "It's a short read, so it should keep your attention, even if you don't usually read."
    y "And we could, you know..."
    show sam at sink
    y "Discuss it...if you wanted..."
    "Th-This is..."
    "How is this girl accidentally being so cute?"
    "She even picked out a book she thinks I'll like, despite me not reading much..."
    mc "Sam, thank you! I'll definitely read this!"
    "I enthusiastically take the book."
    show sam zorder 2 at t11
    y "Phew..."
    y "Well, you can read it at your own pace."
    y "I look forward to hearing what you think."
    show sam zorder 1 at thide
    hide sam
    show layer master


    "Now that everyone's settled in, I expected Armstrong to kick off some scheduled activities for the club."
    "But that doesn't seem to be the case."
    "Sam's face is already buried in a book."
    "I can't help but notice her intense expression, like she was waiting for this chance."
    "Meanwhile, Bladewolf is rummaging around in the closet."


    $ nextscene = poemwinner[0] + "_exclusive2_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene

    return

label ch21_end:
    stop music fadeout 1.0
    scene bg club_day2
    with wipeleft_scene
    play music t3g
    queue music t3g2
    mc "Phew..."
    "I guess that's everyone."
    "I glance around the room."
    "That was a little more stressful than I anticipated."
    "It's as if everyone is judging me for my mediocre writing abilities..."
    "Even if they're just being nice, there's no way my poems can stand up to theirs."
    "This is a literature club, after all."
    "I sigh."
    "I guess that's what I ended up getting myself into."
    "Across the room, Armstrong is writing something in her notebook."
    "My eyes land on Sam and Bladewolf."
    show sam zorder 2 at t21
    show bladewolf zorder 2 at t22
    "They gingerly exchange sheets of paper, sharing their respective poems."
    show sam zorder 2 at t21
    "As they read in tandem, I watch each of their expressions change."
    "Bladewolf's eyebrows furrow in frustration."
    "Meanwhile, Sam smiles sadly."
    show bladewolf zorder 3 at f22
    n "{i}(What's with this language...?){/i}"
    show bladewolf zorder 2 at t22
    show sam zorder 3 at f21
    y "Eh?"
    y "Um...did you say something?"
    show sam zorder 2 at t21
    show bladewolf zorder 3 at f22
    n "Oh, it's nothing."
    "Bladewolf dismissively returns the poem to the desk with one hand."
    n "I guess you could say it's fancy."
    show bladewolf zorder 2 at t22
    show sam zorder 3 at f21
    y "Ah-- Thanks..."
    y "Yours is...cute..."
    show sam zorder 2 at t21
    show bladewolf zorder 3 at f22
    n "Cute?"
    n "Did you completely miss the symbolism or something?"
    n "It's clearly about the feeling of giving up."
    n "How can that be cute?"
    show bladewolf zorder 2 at t22
    show sam zorder 3 at f21
    y "I-I know that!"
    y "I just meant..."
    y "The language, I guess..."
    y "I was trying to say something nice..."
    show sam zorder 2 at t21
    show bladewolf zorder 3 at f22
    n "Eh?"
    n "You mean you have to try that hard to come up with something nice to say?"
    n "Thanks, but it really didn't come out nice at all!"
    show bladewolf zorder 2 at t22
    show sam zorder 3 at f21
    y "Um..."
    y "Well, I do have a couple suggestions..."
    show sam zorder 2 at t21
    show bladewolf zorder 3 at f22
    n "Hmph."
    n "If I was looking for suggestions, I would have asked someone who actually liked it."
    n "Which people {i}did{/i}, by the way."
    n "Armstrong liked it."
    n "And [player] did, too!"
    n "So based on that, I'll gladly give you some suggestions of my own."
    n "First of all--"
    show bladewolf zorder 2 at t22
    show sam zorder 3 at f21
    y "Excuse me..."
    y "I appreciate the offer, but I've spent a long time establishing my writing style."
    y "I don't expect it to change anytime soon, unless of course I come across something particularly inspiring."
    y "Which I haven't yet."
    show sam zorder 2 at t21
    show bladewolf zorder 3 at f22
    n "Nn...!"
    show bladewolf zorder 2 at t22
    show sam zorder 3 at f21
    y "And [player] liked my poem too, you know."
    y "He even told me he was impressed by it."
    stop music fadeout 1.0
    "Bladewolf suddenly stands up."
    show sam zorder 2 at t21
    show bladewolf zorder 3 at f22
    n "Oh?"
    n "I didn't realize you were so invested in trying to impress our new member, Sam."
    play music t7a
    show bladewolf zorder 2 at t22
    show sam zorder 3 at f21
    y "E-Eh?!"
    y "That's not what I...!"
    y "Uu..."
    y "You...You're just..."
    "Sam stands up as well."
    y "Maybe you're just jealous that [player] appreciates my advice more than he appreciated yours!"
    show sam zorder 2 at t21
    show bladewolf zorder 3 at f22
    n "Huh! And how do you know he didn't appreciate {i}my{/i} advice more?"
    n "Are you that full of yourself?"
    show bladewolf zorder 2 at t22
    show sam zorder 3 at f21
    y "I...!"
    y "No..."
    y "If I was full of myself..."
    y "...I would deliberately go out of my way to make everything I do overly cutesy!"
    show sam zorder 2 at t21
    show bladewolf zorder 3 at f22
    n "Uuuuuu...!"
    n "Well, you know what?!"
    n "I wasn't the one whose boobs magically grew a size bigger as soon as [player] started showing up!!"
    show sam at h21
    show bladewolf zorder 2 at t22
    y "N-Bladewolf!!"
    show sam zorder 2 at t32
    show bladewolf zorder 2 at t33
    show armstrong behind sam, bladewolf at l41
    m "Um, Bladewolf, that's a little--"
    show armstrong at h41
    show sam zorder 3 at f32
    show bladewolf zorder 3 at f33
    ny "This doesn't involve you!"
    show armstrong at lhide
    hide armstrong
    show sam zorder 2 at f21
    show bladewolf zorder 2 at t22
    queue music t7g
    $ timeleft = 12.453 - get_pos()
    show noise zorder 3 at noisefade(25 + timeleft)
    show vignette as flicker zorder 4 at vignetteflicker(timeleft)
    show vignette zorder 4 at vignettefade(timeleft)
    show layer master at layerflicker(timeleft)
    y "Taking out your own insecurities on others like that..."
    y "You really act as young as you look, Bladewolf."
    show sam zorder 2 at t21
    show bladewolf zorder 3 at f22
    n "{i}Me?{/i} Look who's talking, you wannabe edgy bitch!"
    show bladewolf zorder 2 at t22
    show sam zorder 3 at f21
    y "Edgy...?"
    y "Sorry that my lifestyle is too much for someone of your mental age to comprehend!"
    show sam zorder 2 at t21
    show bladewolf zorder 3 at f22
    n "See??"
    n "Just saying that proves my point!"
    n "Most people learn to get over themselves after they graduate middle school, you know."
    show bladewolf zorder 2 at t22
    show sam zorder 3 at f21
    y "If you want to prove anything, then stop harassing others with your sickening attitude!"
    y "You think you can counterbalance your toxic personality just by dressing and acting cute?"
    y "The only cute thing about you is how hard you try."
    show sam zorder 2 at t21
    show bladewolf zorder 3 at f22
    n "Whoa, be careful or you might cut yourself on that edge, Sam."
    n "Oh, my bad... You already do, don't you?"
    show bladewolf zorder 2 at t22
    show sam zorder 3 at f21
    y "D-Did you just accuse me of cutting myself??"
    y "What the fuck is wrong with your head?!"
    show sam zorder 2 at t21
    show bladewolf zorder 3 at f22
    n "Yeah, go on!"
    n "Let [player] hear everything you really think!"
    n "I'm sure he'll be head over heels for you after this!"
    show bladewolf zorder 2 at t22
    show sam zorder 3 at f21
    y "A-Ah--!"
    show sam zorder 2 at t21
    "Suddenly, Sam turns toward me, as if she just noticed I was standing here."
    show sam zorder 3 at f21
    y "[player]...!"
    y "She-- She's just trying to make me look bad...!"
    show sam zorder 2 at t21
    show bladewolf zorder 3 at f22
    n "That's not true!"
    n "She started it!"
    show sam zorder 2 at t21
    show bladewolf zorder 2 at t22
    $ style.say_dialogue = style.normal
    mc "..."
    $ style.say_dialogue = style.edited
    "{cps=*2}How did I get dragged into this in the first place?!{/cps}{nw}"
    "{cps=*2}It's not like I know anything about writing...{/cps}{nw}"
    "{cps=*2}But whomever I agree with, they'll probably think more highly of me!{/cps}{nw}"
    "{cps=*2}So, of course that's going to be...!{/cps}{nw}"
    $ style.say_dialogue = style.normal
    $ menu_clicked = 0
    window hide(None)
    label ch21_end_menu:
        menu:
            "Bladewolf.":
                jump menu_click
            "Sam.":
                jump menu_click

    label menu_click:
        $ srf = screenshot_srf()
        show layer screens:
            truecenter
            zoom 1.00
        show screen tear(20, 0.1, 0.1, 0, 40, srf)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        hide screen tear
        stop sound
        $ menu_clicked += 1
        if menu_clicked < 9:
            show layer master:
                truecenter
                zoom 1.00 + menu_clicked * menu_clicked * 0.06
                yalign 0.25
            show layer screens:
                truecenter
                zoom 1.00 + menu_clicked * menu_clicked * 0.06
                yalign 0.25
            jump ch21_end_menu


    window show(None)
    stop music
    $ menu_clicked = 8
    $ quick_menu = False
    show layer master:
        truecenter
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    show layer screens:
        truecenter
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    show raiden onlayer front at i11:
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    $ renpy.display_menu(items=[('Bladewolf.', True), ('Sam.', True)], interact=False, screen='choice')
    m "..."
    show layer master
    show layer screens
    show armstrong onlayer front at i11
    window auto
    $ renpy.display_menu(items=[('Bladewolf.', True), ('Sam.', True)], interact=False, screen='choice')
    m "..."
    $ renpy.display_menu(items=[('Bladewolf.', True), ('Sam.', True)], interact=False, screen='choice')
    m "..."
    show armstrong onlayer front at i11
    $ renpy.display_menu(items=[('Bladewolf.', True), ('Sam.', True)], interact=False, screen='choice')
    m "Um..."
    $ renpy.display_menu(items=[('Bladewolf.', True), ('Sam.', True)], interact=False, screen='choice')
    m "Hey, [player]..."
    show armstrong onlayer front at i11
    $ renpy.display_menu(items=[('Bladewolf.', True), ('Sam.', True)], interact=False, screen='choice')
    m "Why don't we\nstep outside for\na little bit?"
    $ renpy.display_menu(items=[('Bladewolf.', True), ('Sam.', True)], interact=False, screen='choice')
    m "Okay?"
    scene bg corridor
    hide armstrong onlayer front
    show armstrong onlayer master at t11
    with wipeleft_scene
    $ quick_menu = True
    m "Sorry about that..."
    m "They really shouldn't have tried to get you involved."
    m "It's probably better for us to stay out of this..."
    m "We'll go back inside once they're done yelling."
    m 5 "Ahaha..."
    m "Some president I am, right?"
    m "I can't even confront my own club members properly..."
    m "I just wish I was able to be a little more assertive sometimes."
    m "But I never have it in me to put my foot down against others..."
    m "You understand, right?"
    m "Anyway..."
    m "If this makes you want to spend less time with the others, then that's fine."
    m "I'd be happy to spend time with you instead..."
    show armstrong zorder 1 at thide
    hide armstrong
    "Suddenly, Bladewolf runs out of the classroom."
    show bladewolf zorder 2 at t11
    n "..."
    show bladewolf at lhide
    $ pause(0.75)
    hide bladewolf
    "She quickly runs away."
    show armstrong zorder 2 at t11
    m "Oh dear..."
    m "...Well, it looks like they're done..."
    scene bg club_day2
    with wipeleft_scene
    y "I didn't mean it..."
    y "I didn't mean it..."
    y "I didn't mean it..."
    "Sam is rocking back and forth in her desk with her palms on her forehead."
    mc "Sam...?"
    show sam zorder 2 at t11
    y "I didn't mean it!!"
    mc "I-I believe you..."
    "I have no idea what Sam might have said to Bladewolf."
    "Or did."
    y "[player]."
    y "Please don't hate me."
    y "Please!"
    y "I'm not like this!"
    y "There's something wrong with me today..."
    show armstrong zorder 3 at f31
    m "It's fine, Sam."
    m "We know you didn't mean it."
    m "Besides, I'm sure Bladewolf will forget all about it by tomorrow."
    m "Completely."
    show armstrong zorder 2 at t31
    show sam zorder 3 at f32
    y "..."
    show sam zorder 3 at t32
    show armstrong zorder 2 at f31
    m "Anyway, the meeting is over, so you can go home now if you want."
    show armstrong zorder 2 at t31
    show sam zorder 3 at f32
    y "..."
    show sam zorder 2 at t32
    "Sam looks at me like she wants to say something."
    "But she keeps glancing at Armstrong."
    show sam zorder 3 at f32
    y "Y-You can go first, Armstrong..."
    y "I'd like to stay a little bit longer."
    show sam zorder 2 at t32
    show armstrong zorder 3 at f31
    m "I'm the President, so I should be the last one out."
    m "I'll wait for you to be done."
    show armstrong zorder 2 at t31
    show sam zorder 3 at f32
    y "..."
    y "..."
    y "Well-- I'm Vice President, so..."
    y "Please let me take that responsibility today."
    show sam zorder 2 at t32
    show armstrong zorder 3 at f31
    m "It kind of sounds like you don't want me around for something, Sam."
    show armstrong zorder 2 at t31
    show sam zorder 3 at f32
    y "I-It's not that!"
    y "It's not that..."
    y "I just..."
    y "I didn't get much of a chance to discuss my book with [player]..."
    y "It would just be...embarrassing with you listening..."
    show sam zorder 2 at t32
    show armstrong zorder 3 at f31
    m "{i}*Sigh*{/i}"
    m "I guess I don't really have a choice, do I?"
    show armstrong zorder 2 at t31
    show sam zorder 3 at f32
    y "I-I'm sorry for causing trouble..."
    $ gtext = glitchtext(20)
    y "But I really appreciate you understan{nw}"
    play music g1
    show sam onlayer front at i31
    y glitch "But I really appreciate you understan{fast}[gtext] [gtext][gtext]{nw}"
    $ _history_list.pop()
    hide armstrong onlayer front
    window hide(None)
    window auto

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
