image sam half = "images/sam/1l.png"
image sam_half2:
    "images/sam/1r.png"
    block:
        xoffset -360
        linear 0.2 xoffset -280
        repeat

label ch22_main:
    scene bg club_day2
    with dissolve_scene_half
    play music t6
    "Another day passes, and it's time for the club meeting already."
    "I've gotten a little more comfortable here over the past couple days."
    "Entering the clubroom, the usual scene greets me."
    if renpy.random.randint(0,2) == 0:
        show sam half zorder 2 at i11
        show sam_half2 zorder 1 at i11
    else:
        show sam zorder 2 at t11
    y "Welcome back, [player]..."
    hide sam_half2
    mc "Ah, hi Sam..."
    "I'm not sure if it's me, or if it's Sam's expression..."
    "But the weight of yesterday's quarrel still hangs in the air a little."
    y "U-Um..."
    "Sam glances over her shoulder, looking around the room."
    "Bladewolf is reading manga at a desk."
    "And surprisingly, Armstrong isn't here yet."
    "Suddenly, Sam takes my arm and pulls me to the corner of the room."
    show bg closet
    show sam zorder 2 at t11
    with wipeleft
    y "About yesterday..."
    y "I..."
    y "I really need to apologize."
    y "Nothing like that has ever happened before..."
    y "And...something just came over me, I guess..."
    y "I wasn't acting mentally sound."
    y "Please don't think we're usually like this!"
    y "Not just me, but Bladewolf as well..."
    show sam     mc "Sam..."
    mc "I'm happy that you were considerate and apologized."
    mc "You don't have to worry too much."
    mc "Even though I've only been here a couple days, I could tell something was off yesterday..."
    mc "Maybe we were just a little extra sensitive because it was our first time sharing poems."
    mc "But whatever it was..."
    mc "It didn't make me think any less of you."
    mc "I had already decided that there's no way you can be a bad person."
    mc "And now that you're apologizing, I know you really didn't mean it."
    y "A-Ah..."
    y "[player]..."
    y "Don't say those kinds of things so frankly..."
    y "They make me a little too happy."
    y "I'm really glad that you're such an understanding person..."
    y "And I'm really glad that you joined this club."
    y "Everything is a little bit brighter with you around, and--"
    y "Ah--"
    y "Sorry, what am I saying right now...?"
    y "I just--"
    show bladewolf zorder 3 at f33
    n "Hey, have you guys seen Armstrong?"
    show bladewolf zorder 2 at t33
    show sam at h32
    y "Ah--!"
    mc "No, I haven't..."
    mc "I was also kind of wondering where she was."
    show bladewolf zorder 3 at f33
    n "Man..."
    n "Sam, I'm guessing you haven't, either?"
    show bladewolf zorder 2 at t33
    show sam zorder 3 at f32
    y "..."
    "Sam is clearly taken aback by how calmly Bladewolf is addressing her."
    y "N-No, I haven't..."
    show sam zorder 2 at t32
    show bladewolf zorder 3 at f33
    n "Jeez, this isn't like her at all."
    n "I know it's stupid, but I can't help but worry a little bit..."
    show bladewolf zorder 2 at t33
    show sam zorder 3 at f32
    y "..."
    show sam zorder 2 at t32
    show bladewolf zorder 3 at f33
    n "What?"
    n "Why're you looking at me like that?"
    show bladewolf zorder 2 at t33
    show sam zorder 3 at f32
    y "U-Um..."
    y "Bladewolf, about yesterday..."
    y "I-I just wanted to apologize!"
    y "I promise I didn't mean any of the things I said!"
    y "And I'll do my best to stay under control from now on..."
    y "So--"
    show sam zorder 2 at t32
    show bladewolf zorder 3 at f33
    n "Sam, what the heck are you talking about?"
    n "Did you do something yesterday?"
    show bladewolf zorder 2 at t33
    show sam zorder 3 at f32
    y "...Eh?"
    show sam zorder 2 at t32
    show bladewolf zorder 3 at f33
    $ style.say_dialogue = style.normal
    n "Jeez..."
    $ style.say_dialogue = style.edited
    n "Whatever's on your mind, I'm sure it was nothing."
    n "I don't even remember anything bad happening."
    n "You're the kind of person who worries too much about the little things, aren't you?"
    $ style.say_dialogue = style.normal
    show bladewolf zorder 2 at t33
    show sam zorder 3 at f32
    y "..."
    y "B-But..."
    show sam zorder 2 at t32
    if renpy.random.randint(0, 3) == 0:
        $ style.say_dialogue = style.edited
        show bladewolf mouth as nm zorder 3 at i33
        show n_moving_mouth zorder 3:
            xoffset 400
        n "mibulls sailcloth blindsight lifeline anan rectipetality faultlessly offered scleromalacia neighed catholicate"
        hide nm
        hide n_moving_mouth
        $ style.say_dialogue = style.normal
    show bladewolf zorder 3 at f33
    n "I'll accept your apology anyway, if it helps you feel better about it."
    n "Besides, it's kinda nice to hear, since I was always afraid you secretly hated me or something like that."
    n "Ehehe."
    show bladewolf zorder 2 at t33
    show sam zorder 3 at f32
    y "N-No, not at all...!"
    y "I don't hate you..."
    show sam zorder 2 at t32
    show bladewolf zorder 3 at f33
    n "Ahaha."
    n "Well, you're kind of weird, but I don't hate you either."
    show bladewolf zorder 2 at t33
    show sam zorder 3 at f32
    y "..."
    "Bladewolf turns to me."
    show sam zorder 2 at t32
    show bladewolf zorder 3 at f33
    n "You're still on trial, though."
    show bladewolf zorder 2 at t33
    mc "Hey...!"
    "Suddenly, the door swings open."
    show armstrong at l41
    m "Sorry! I'm super sorry!"
    mc "Ah, there you are..."
    show armstrong zorder 3 at f41
    m "I didn't mean to be late..."
    m "I hope you guys weren't worried or anything!"
    show armstrong zorder 2 at t41
    mc "Nah..."
    mc "Well, Bladewolf was."
    show bladewolf zorder 3 at f33
    n "I-I was not!!"
    show bladewolf zorder 2 at t33
    show armstrong zorder 3 at f41
    m "Ahaha."
    show armstrong zorder 2 at t41
    show bladewolf zorder 3 at f33
    n "...What took you so long, anyway?"
    show bladewolf zorder 2 at t33
    show armstrong zorder 3 at f41
    m "Ah..."
    m "Well, my last period today was study hall."
    m "To be honest, I kind of just lost track of time..."
    m "Ahaha..."
    show armstrong zorder 2 at t41
    show bladewolf zorder 3 at f33
    n "That makes no sense, though."
    n "You would have heard the bell ring, at least."
    show bladewolf zorder 2 at t33
    show armstrong zorder 3 at f41
    m "I must not have heard it, since I was practicing piano..."
    show armstrong zorder 2 at t41
    show sam zorder 3 at f32
    y "Piano...?"
    y "I wasn't aware you played music as well, Armstrong."
    show sam zorder 2 at t32
    show armstrong zorder 3 at f41
    m "Ah, don't give me more credit than I deserve."
    m "I guess I've been practicing for a while, but I'm still not really good yet."
    show armstrong zorder 2 at t41
    show sam zorder 3 at f32
    y "Still..."
    y "That must require a lot of dedication."
    y "So, I'm still impressed."
    show sam zorder 2 at t32
    show armstrong zorder 3 at f41
    m 5 "Aw, well thanks, Sam~"
    show armstrong zorder 2 at t41
    show bladewolf zorder 3 at f33
    n "You should play something for us sometime!"
    show bladewolf zorder 2 at t33
    show armstrong zorder 3 at f41
    m "Ahaha, that's..."
    "Armstrong looks at me."
    m "Well, I am working on writing a song, but it's not quite done yet..."
    m "Maybe once I get a little bit better, I will."
    show armstrong zorder 2 at t41
    mc "That sounds cool."
    mc "I look forward to it."
    show armstrong zorder 3 at f41
    m "Is that so?"
    m "In that case..."
    m "I won't let you down, [player]."
    show sam zorder 1 at thide
    show bladewolf zorder 1 at thide
    hide sam
    hide bladewolf
    show armstrong zorder 2 at t11
    "Armstrong smiles sweetly."
    mc "Ah..."
    mc "I didn't mean any pressure or anything like that!"
    m "Ahaha, don't worry."
    m "I was hoping that I could share it with you, anyway."
    m "I guess that's why I've been practicing so much recently."
    mc "I see..."
    "I'm not sure if Armstrong was referring to the whole club, or just me..."
    mc "In that case, best of luck."
    m "Thanks~!"
    m "So, I didn't miss anything, did I?"
    mc "Not...not really."
    show armstrong zorder 1 at thide
    hide armstrong
    "I choose not to bring up anything that the three of us talked about."
    "Besides, Bladewolf has already run off into the closet."
    show sam zorder 2 at t11
    y "[player]..."
    y "Um..."
    y "Since your compliments put me in a good mood..."
    y "I was wondering if you would like to spend some time together today."
    y "I mean--in the club!"
    if poemwinner[0] == "bladewolf":
        $ y_appeal = 1
        mc "Ah, I suppose so."
        mc "I don't think I could say no to you, after you gave that book to me."
        mc "Well, I guess I need to make sure Bladewolf isn't waiting for me."
        mc "After we finished reading yesterday, she--"
        if n_appeal >= 2:
            y "She's fine!"
            $ style.say_dialogue = style.normal
            y "She's reading over there. See?"
            $ style.say_dialogue = style.edited
            y "Don't think about her so much."
            y "She's used to being ignored."
            y "Come on, we're going over there."
            $ style.say_dialogue = style.normal
            window hide(None)
            $ currentpos = get_pos()
            stop music
            scene black
            window auto
            $ pause(2.0)
            play music "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
            jump ch22_main2
        else:
            y "S-She's fine!"
            y "She's reading over there."
            y 3y6 "So it's okay, right?"
            mc "Ah--"
            mc "In that case, I don't see any problem..."
    else:
        $ y_appeal = 2
        mc "Yeah, definitely."
        mc "I planned on it anyway."
    show sam zorder 2 at h11
    y 3y5 "Okay!"
    y "Can we start now?"
    y "Let's find a place to sit--"
    y "A-Ah--"
    y "I'm being a little forceful, aren't I...?"
    y "I'm sorry!"
    y "My heart...just won't stop pounding, for some reason..."
    mc "Don't worry about it."
    mc "If anything, it's nice to see you have so much energy."
    y "Y-Yeah!"
    y "But..."
    y "I need to try to calm down."
    y "I won't be able to focus on reading like this..."
    mc "Take your time."
    "Sam takes a deep breath, then pulls a copy of the book out of her bag."
label ch22_main2:
    if n_poemappeal[1] == 1:
        $ n_poemappeal[1] = 0
    $ poemwinner[1] = "sam"


    scene bg club_day2
    show sam at i11
    with wipeleft
    $ nextscene = "sam_exclusive2_" + str(eval("y_appeal")) + "_ch22"
    call expression nextscene

    return

label ch22_end:
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    call screen confirm("You have unlocked a special poem.\nWould you like to read it?", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[1])
        scene black with Dissolve(1.0)
    else:
        pass
    if not faint_effect and renpy.random.randint(0,2) == 0:
        $ faint_effect = True
    else:
        $ faint_effect = None
    scene bg club_day2
    show armstrong zorder 2 at t32
    if faint_effect:
        show layer master at dizzy(0.5, 1.0)
        show layer screens at dizzy(0.5, 1.0)
        show expression Solid("ff0000") as i1 onlayer front:
            additive 1.0
        show expression Solid("#440000") as i2 onlayer front:
            additive 0.4
        show veins onlayer front:
            additive 0.5
    with wipeleft_scene
    if faint_effect:
        play music t3g3
    else:
        play music t3
    if renpy.random.randint(0,2) == 0:
        $ config.mouse = {"default": [
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ]}



    m "Okay, everyone!"
    m "We're all done reading each other's poems, right?"
    $ config.mouse = None
    m "We have something we need to go over today, so if everyone could come sit at the front of the room..."
    show bladewolf zorder 3 at f31
    n "Is this about the festival?"
    show bladewolf zorder 2 at t31
    show armstrong zorder 3 at f32
    m "Well, sort of~"
    show armstrong zorder 2 at t32
    show bladewolf zorder 3 at f31
    n "Ugh. Do we really have to do something for the festival?"
    n "It's not like we can put together anything good in just a few days."
    n "We'll just end up embarrassing ourselves instead of getting any new members."
    if faint_effect:
        $ currentpos = get_pos() + 2.0
        stop music fadeout 2.0
        show black onlayer front:
            alpha 0.0
            linear 2.0 alpha 1.0
    show bladewolf zorder 2 at t31
    show sam zorder 3 at f33
    y "That's a concern of mine as well."
    if faint_effect:
        hide black onlayer front
        hide veins onlayer front
        hide i1 onlayer front
        hide i2 onlayer front
        show layer master
        show layer screens
        play music "<from " + str(currentpos) + " loop 4.618>bgm/3.ogg"
    y "I don't really do well with last-minute preparations..."
    show sam zorder 2 at t33
    show armstrong zorder 3 at f32
    m "Don't worry so much!"
    m "We're going to keep it simple, okay?"
    m "Look..."
    m "I know everyone's been a little more...lively...ever since [player] joined and we've started with some club activities."
    m "But this isn't the time for us to become complacent."
    m "We still only have four members..."
    m "And the festival is our only real chance to find more, you know?"
    show armstrong zorder 2 at t32
    show bladewolf zorder 3 at f31
    n "What's so great about getting new members, anyway?"
    n "We already have enough to be considered an official club."
    n "More members will just mean everything gets noisier and more difficult to manage."
    show bladewolf zorder 2 at t31
    show armstrong zorder 3 at f32
    m "Bladewolf..."
    m "I don't think you're looking at it the right way at all."
    m "Don't you want to share your passion with as many people as you can?"
    m "To inspire them to find the same feelings that brought you here in the first place?"
    m "The Literature Club should be a place where people can express themselves like they can't do anywhere else."
    m "It should be a place so intimate that you never want to leave."
    m "I know you feel that way, too."
    m "I know we all do!"
    m "So that's why we should work hard and put something together for the festival...even if it's something small!"
    m "Right, [player]?"
    show armstrong zorder 2 at t32
    mc "Ah..."
    show bladewolf zorder 3 at f31
    n "Oh, come on!"
    n "You can't take advantage of [player] to agree with you just because he doesn't know how to say no to anything."
    stop music fadeout 1
    n "Look, Armstrong."
    n "Do you really think any of us here joined the club with other people in mind?"
    n "Sam never even talked until [player] joined."
    n "As for me, I just like it better here than I do at home."
    n "And [player] isn't even passionate about literature in the first place."
    n "And that's everyone."
    n "Sorry, but you're really the only one who's so interested in finding new members."
    n "The rest of us are fine like this."
    n "I know you're President and all, but you should really consider our opinions for once."
    show bladewolf zorder 2 at t31
    show armstrong zorder 3 at f32
    m "..."
    "Armstrong is clearly taken aback by Bladewolf's words."
    play music t9
    m "That's...not true at all."
    m "I'm sure Sam and [player] want to get more members too..."
    m "...Right?"
    show armstrong zorder 2 at t32
    show sam zorder 3 at f33
    y "..."
    show sam zorder 2 at t33
    mc "..."
    "I don't know about Sam, but I'm kind of indifferent."
    "If I showed as much enthusiasm as Armstrong wanted, then I would probably be lying."
    "Still, if it's up to me to rescue this situation..."
    mc "Um--"
    show armstrong zorder 3 at f32
    m "No."
    m "Bladewolf's right, isn't she?"
    m "This club..."
    m "It's nothing more than a place for a few people to hang out."
    m "Why did I think that everyone here saw it the same way as I did?"
    show armstrong zorder 2 at t32
    mc "But that doesn't mean that we're against getting new members or anything..."
    show armstrong zorder 3 at f32
    m "[player], why did you even join this club?"
    m "What were you hoping to get out of it?"
    show armstrong zorder 2 at t32
    mc "Well--"
    "That's not really something I can be honest about, is it?"
    show armstrong zorder 3 at f32
    m "In fact..."
    m "If I remember, you weren't even given a choice not to join."
    show armstrong zorder 1 at thide
    hide armstrong
    "Armstrong sits down and stares at her desk."
    m "What's the point of all this, anyway?"
    m "What if starting this club was a mistake?"
    mc "..."
    show sam zorder 3 at f33
    y "Now you've done it, Bladewolf..."
    show sam zorder 2 at t33
    show bladewolf zorder 3 at f31
    n "What, me?"
    n "I just spoke my mind..."
    n "Is it a crime to be honest?"
    show bladewolf zorder 2 at t31
    show sam zorder 3 at f33
    y "It's not about being honest."
    y "It's about word choice."
    y "Besides, you have no right to speak for everyone else in the club like that..."
    show sam zorder 2 at t33
    show bladewolf zorder 3 at f31
    n "You don't understand at all!"
    n "I just..."
    n "I just want a place that feels nice to hang out with a few friends."
    n "Is there a problem with the club being that for me?"
    n "There aren't...there aren't many other places like that for me..."
    n "And now Armstrong wants to take it away from me!"
    show bladewolf zorder 2 at t31
    mc "She's not taking anything away--"
    show bladewolf zorder 3 at f31
    n "No, [player]."
    n "It's not the same."
    n "It won't be the same with the direction she wants to take it."
    n "If I wanted that, then I could have just joined any other stupid club."
    n "But this one..."
    n "I mean..."
    n "At least for a little bit of time..."
    n "Things were nice."
    "Bladewolf starts packing up her things."
    n "I'm going home."
    n "I feel like...I don't belong here right now."
    show bladewolf zorder 2 at t31
    show sam zorder 3 at f33
    y "Bladewolf..."
    show bladewolf zorder 1 at thide
    hide bladewolf
    "Bladewolf ignores Sam and walks right out of the classroom."
    show sam zorder 2 at t11
    y "..."
    y "This is bad..."
    y "I don't know what to do..."
    mc "Well..."
    mc "Do you have an opinion on the festival?"
    y "I-I don't know..."
    $ style.say_dialogue = style.normal
    y "I'm kind of indifferent, I guess..."
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 630 ypos -50 zoom 2.0
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 1.532>bgm/9g.ogg"
    y "Who cares about that obnoxious brat?"
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos() * 2.07
    play music "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    hide black
    hide y_glitch_head
    y "I mean, I like how nice and quiet the club is right now..."
    y "And I'm just...happy with you here..."
    y "But still!"
    y "I'm the Vice President..."
    y "It's not right for me to ignore my responsibilities like that..."
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 430 ypos -450 zoom 4.5
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 1.532>bgm/9g.ogg"
    y "Nobody would cry if she killed herself."
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos() * 2.07
    stop music
    $ pause(0.5)
    play sound "sfx/stab.ogg"
    show blood_eye zorder 3:
        pos (710,380) zoom 2.5
    $ pause(0.75)
    stop sound
    play music "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    hide black
    hide y_glitch_head
    hide blood_eye
    y "I should do my best to consider everyone's perspective and make the decision that's right for the club."
    y "But what about you, [player]?"
    y "What do you want to get out of this club?"
    "Sam repeats the same question as Armstrong."
    "I decide giving an indirect answer is better than nothing."
    mc "...I think the most important thing is for everyone to get along..."
    mc "...And for the club to provide something that you can't get anywhere else."
    mc "I don't think it's about how many members, but rather the quality of each member."
    mc "That's what will end up making the Literature Club a special place."
    y "I see..."
    y "I really agree with you."
    show blood_eye2 zorder 3:
        pos (568, 165)
    y "Each member contributes their own qualities in a special way."
    y "With each change in members, the identity of the club as a whole will change, too."
    y "I don't think that's necessarily a bad thing."
    y "Stepping out of your comfort zone once in a while..."
    y "So if you would like to help Armstrong with the festival, then I'm on your side as well."
    hide blood_eye2
    mc "Alright."
    mc "Well, maybe we can all talk to Bladewolf tomorrow..."
    "Sam nods."
    show armstrong zorder 3 at f21
    show sam zorder 2 at t22
    m "Hey, Sam..."
    show armstrong zorder 2 at t21
    show sam zorder 3 at f22
    y "Eh?"
    show sam zorder 2 at t22
    show armstrong zorder 3 at f21
    m "Um, I know things were a little awkward yesterday..."
    m "But I feel like you deserve to know that I still think you're a wonderful vice president."
    m "And also, a wonderful friend."
    show armstrong zorder 2 at t21
    show sam zorder 3 at f22
    y "M-Armstrong..."
    show sam zorder 2 at t22
    show armstrong zorder 3 at f21
    m "I want to do everything I can to make this the best club ever."
    m "Okay?"
    show armstrong zorder 2 at t21
    show sam zorder 3 at f22
    y "...Me too."
    show sam zorder 2 at t22
    show armstrong zorder 3 at f21
    m "Yeah..."
    m "Let's all go home for today."
    m "We'll talk about the festival tomorrow."
    show armstrong zorder 2 at t21
    show sam zorder 3 at f22
    y "Okay."
    y "I look forward to it."
    y "Shall we go, [player]?"
    show sam zorder 2 at t22
    show armstrong zorder 3 at f21
    m "Um--"
    m "Please don't take this the wrong way, but..."
    m "I'm going to chat a little bit with [player] before we leave."
    m "Just to see what he thinks of his time here and all that..."
    m "It's important to me, as President."
    show armstrong zorder 2 at t21
    show sam zorder 3 at f22
    y "..."
    "Sam looks a little troubled, but she doesn't protest."
    y "Okay."
    y "I trust your judgment, Armstrong."
    y "In that case, I'll see the two of you tomorrow."
    show sam zorder 2 at t22
    show armstrong zorder 3 at f21
    m "See you tomorrow~"
    show sam zorder 1 at thide
    hide sam
    "Armstrong waves as Sam exits the classroom."

    show armstrong zorder 2 at t11
    m "Phew..."
    m "Things have been a bit hectic lately, haven't they?"
    show darkred:
        additive 0.2
        alpha 0
        linear 20 alpha 1.0
    show noise:
        alpha 0
        linear 20 alpha 0.1
    m "[player], I just wanted to make sure you're enjoying your time at this club."
    m "I would really hate to see you unhappy."
    m "I feel kind of like I'm responsible for that, as President..."
    stop music
    m "And I really do care about you...you know?"
    m "I don't like seeing the other girls give you a hard time."
    m "With how mean Bladewolf is and everything..."
    m "And Sam being a little bit...you know."
    m "Ahaha..."
    m "Sometimes it feels like you and I are the only real people here."
    m "You know what I mean?"
    m "But it's weird, because in all the time you've been here, we've hardly gotten to spend any time together."
    m "Ah...I mean..."
    m "I guess it's technically only been a couple days..."
    m "Sorry, I didn't mean to say something weird!"
    m "There are just some things I've been hoping to talk about with you..."
    m "Things I know only you could understand."
    stop music fadeout 3.0
    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00
    m "So that's why--\"{space=5000}{w=0.75}{nw}"
    m "Wait, not yet!\"{space=5000}{w=0.5}{nw}"
    m "No!\"{space=5000}{w=0.5}{nw}"
    m "Stop it!\"{space=5000}{w=1.0}{nw}"
    window hide(None)
    window auto
    hide black onlayer front





    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
