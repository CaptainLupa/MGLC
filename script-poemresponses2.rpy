label ch21_y_end:
    jump ch1_y_end

label ch22_y_end:
    stop music fadeout 2.0
    call showpoem (poem_y22, music=False, paper="images/bg/poem_y1.jpg", img="s")
    y "Ahaha..."
    y "It doesn't really matter what it's about."
    y "My mind has been a little hyperactive lately, so I had to take it out on your pen."
    y "Ah--"
    y "That is...a-a pen fell out of your backpack yesterday, so I took it home for safekeeping and..."
    y "I, um..."
    y 2y6 "I just...really like...the way...that it writes."
    y "So I wrote this...poem...with it."
    y "And now you're touching it..."
    y 2y5 "Ahaha."
    y "I-I'm okay!!"
    y "What did I just..."
    y "..."
    y "...Can we pretend this conversation never happened?"
    y "You can keep the poem, though..."
    return
label ch23_y_end:
    show darkred zorder 5:
        alpha 0
        linear 2.0 alpha 1.0
    call showpoem (poem_y23, track="bgm/5_sam2.ogg", revert_music=False, paper="images/bg/poem_y2.jpg", img="sam eyes", where=truecenter)
    y "Do you like it??"
    y "I wrote it for you!"
    $ gtext = glitchtext(80)
    show sam at i11
    y "In case you couldn't tell, the poem is about [gtext]"
    y 1y6 "More importantly, I've endowed it with my scent."
    y "See, aren't I the most thoughtful person in the club?"
    play sound "sfx/glitch2.ogg"
    show sam glitch
    $ pause(0.2)
    stop sound
    show y2
    hide darkred
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    $ renpy.music.stop(channel="music_poem")
    $ renpy.music.play(audio.t5c)
    y "..."
    y "I..."
    y "I think I'm...going to vomit."
    show sam at lhide
    hide sam
    $ pause(1.0)
    return
label ch21_n_end:
    jump ch1_n_end
label ch22_n_end:
    if n_appeal >= 2:
        jump ch22_n_end2
    else:
        call showpoem (poem_n2)
        n "Not bad, right?"
        mc "It's quite a bit longer than yesterday's."
        n "Yesterday's was way too short..."
        n "I was just warming up!"
        n "I hope you didn't think that was the best I could do."
        mc "No, of course not..."
        n "Anyway, the message is pretty straightforward in this poem."
        n "I doubt I have to explain it."
        n "Like, anyone would agree that the subject of this poem is an ignorant jerk..."
        n "Everyone has some kind of weird hobby, or a guilty pleasure."
        n "Something that you're afraid if people find out, they'd make fun of you or think less of you."
        n "...But that just makes people stupid!"
        n "Who cares what someone likes, as long as they're not hurting anyone, and it makes them happy?"
        n "I think people really need to learn to respect others for liking weird things..."
        n "...Such as two of the girls in this very club, whom I respectfully won't name."
        n "Kind of ironic that even in my one place of comfort, I can't even have people respect me..."
        n "...Jeez, now you're making me complain too much!"
        "{i}(...What did I do?){/i}"
        mc "For what it's worth, I respect you..."
        n "Well--"
        n "I guess thanks..."
        n "...But it's kind of obvious that you 'respect' Sam more, so..."
        n "Whatever... We're done sharing, so you can leave now."
    return
label ch22_n_end2:
    call showpoem (poem_n2b, revert_music=False)
    $ style.say_dialogue = style.edited
    n "[player]..."
    n "Why didn't you come read with me today?"
    n "I was waiting for you."
    n "I was waiting for a long time."
    n "It was the only thing I had to look forward to today."
    n "Why did you ruin it?"
    n "Do you like Sam more?"
    n "I think you're better off not associating with her."
    n "Are you listening to me?"
    show darkred zorder 5:
        alpha 0.0
        easein 4.0 alpha 1.0
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5_ghost.ogg"
    stop music_poem fadeout 2.0
    $ renpy.music.play(audio.t5c, fadein=2.0, tight=True)
    show n_rects_ghost1 zorder 4
    show n_rects_ghost2 zorder 4
    show n_rects_ghost3 zorder 4
    n ghost1 "Sam is a sick freak."
    n "That should be obvious by now."
    n "So just play with me instead."
    n "Okay?"
    n "You don't hate me, [player], do you?"
    n "Do you hate me?"
    show bladewolf_ghost_blood zorder 3
    n "Do you want to make me go home crying?"
    n "The club is the only place I feel safe."
    n "Don't ruin that for me."
    n "Don't ruin it."
    n "Please."
    n "Just stop talking to Sam."
    n "Play with me instead."
    n "It's all I have..."
    n "Play with me."
    stop music
    hide n_rects_ghost3
    n ghost2 "PLAY WITH ME!!!"
    $ style.say_dialogue = style.normal
    $ quick_menu = False
    $ pause(1)
    play sound "sfx/crack.ogg"
    hide bladewolf_ghost_blood
    hide n_rects_ghost1
    hide n_rects_ghost2
    show bladewolf ghost3
    show n_rects_ghost4 onlayer front zorder 4
    show n_rects_ghost5 onlayer front zorder 4
    $ pause(0.5)
    hide bladewolf
    play sound "sfx/run.ogg"
    show bladewolf ghost4 onlayer front at i11
    $ pause(0.25)
    window hide(None)
    hide bladewolf onlayer front
    hide n_rects_ghost4 onlayer front
    hide n_rects_ghost5 onlayer front
    scene black
    with None
    window auto
    scene black
    $ pause(0.5)
    show end:
        xzoom -1
    with dissolve_cg
    $ pause(2.0)
    scene black
    with None
    $ quick_menu = True
    return
label ch23_n_end:
    $ bladewolf_23 = True
    $ style.say_dialogue = style.normal
    call showpoem (poem_n23, revert_music=False)
    $ renpy.music.stop(channel="music_poem", fadeout=2.0)
    $ style.say_dialogue = style.edited
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    $ pause(3.0)
    stop music
    hide screen tear
    show bladewolf ghost_base
    n "I changed my mind."
    n "Ignore everything you just read."
    n "There's no point in trying to do anything."
    n "It's Sam's own fault that she's so unlikable."
    n "Can you hear me, [player]?"
    n "If you would just spend more time with Armstrong, all these problems would go away."
    n "Sam and I are too messed up for someone as wonderful as you."
    n "Just think of Armstrong from now on."
    n "Just Armstrong."
    hide bladewolf
    $ style.say_dialogue = style.edited
    "Just Armstrong."
    menu:
        "Just Armstrong."
        "Just Armstrong.":
            pass
    $ style.say_dialogue = style.normal
    $ renpy.call_screen("dialog", "Just Armstrong.", ok_action=Return())
    scene white
    play music t1
    show intro with Dissolve(0.5, alpha=True)
    $ pause(2.5)
    hide intro with Dissolve(0.5, alpha=True)
    show splash_warning "Just Armstrong." with Dissolve(0.5, alpha=True)
    $ pause(1.0)
    play music t5
    $ skip_transition = True

    return

label ch21_m_end:
    call showpoem (poem_m21)
    jump ch1_m_end2
label ch22_m_end:
    call showpoem (poem_m22, revert_music=False)
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    stop music_poem fadeout 2.0
    $ pause(2)
    show screen tear(20, 0.3, 0.3, 0, 40)
    $ pause(0.5)
    hide screen tear
    play music t5c
    m 5 "Sorry, I know it's kind of abstract."
    m "I'm just trying to...um..."
    m "Well, never mind."
    m "There's no point in explaining."
    m "Anyway..."
    m "Here's Armstrong's Writing Tip of the Day!"
    m "Sometimes you'll find yourself facing a difficult decision..."
    m "When that happens, don't forget to save your game!"
    m "You never know when...um..."
    m "...Who am I talking to?"
    m "Can you hear me?"
    m "Tell me you can hear me."
    m "Anything."
    $ renpy.call_screen("dialog", "Please help me.", ok_action=Return())
    m "...That's my advice for today!"
    m "Thanks for listening~"
    return
label ch23_m_end:
    $ quick_menu = False
    window hide
    play sound page_turn
    show paper_glitch zorder 10 with Dissolve(1)
    play music g2
    if renpy.windows and renpy.game.preferences.fullscreen:
        $ mouse_visible = False
        scene bsod
        $ pause(3.0)
    else:
        show black zorder 1
        $ pause(2.0)
    window show(None)
    show armstrong zorder 11 at i11
    $ quick_menu = True
    $ mouse_visible = True
    m "Jeez! That really startled me!{fast}"
    window auto
    m "Um..."
    m "Well, I guess I kinda messed up at, uh... 'writing' this poem."
    m "I was just trying to..."
    m "...Never mind."
    m "Let's just move on..."
    stop music
    return


label ch21_n_bad:
    jump ch1_n_bad

label ch21_n_med:
    jump ch1_n_med

label ch21_n_good:
    jump ch1_n_good

label ch22_n_bad:

    if n_poemappeal[0] < 0:
        n "..."
        n "Yeah, just as I thought..."
        mc "...?"
        n "[player], come on."
        n "I'm not stupid."
        n "I know how much time you've been spending with Sam..."
        n "It's obvious that you care more about impressing her than trying to improve your writing."
        n "To put it bluntly, it's kind of pathetic."
        n "Why are you even in this club, [player]?"
        n "Honestly..."
        n "I thought getting a new member would help everyone get more involved together."
        n "Not exclude each other even more."
        n "This is such a stupid activity anyway..."
        n "...Look, I'm not in a good mood today, and I just really don't feel like talking right now."
        n "Please go away."
        $ skip_poem = True
        return
    else:


        n "...Hm."
        n "I liked your last one better."
        mc "Eh? Really?"
        n "Well yeah. I can tell you were a little more daring with this one."
        n "But you're really not good enough for that yet. It fell flat."
        mc "That may be true, but I just wanted to try something different."
        mc "I'm still figuring this all out."
        jump ch22_n_med_shared2

label ch22_n_med:

    if n_poemappeal[0] < 0:
        n "...Hm."
        n "Well, I can admit that it's better than the last one."
        n "It's nice to see that you're putting in some effort."
        mc "That's good..."
        label ch22_n_med_shared:
            n "Just make sure you find a little bit of influence from everyone."
            n "I think you're at least being influenced by Sam a little bit, aren't you?"
            n "I mean, I know you've been, like..."
            n "Spending some time with her, or whatever..."
            n "But you know, Armstrong and I are just as good as her!"
            n "A-At poems, I mean!"
            n "So you should really try to learn something, or you'll never get better!"
            n "Here's the one I wrote..."
            n "I'll make sure you learn something from it."
            return


    elif n_poemappeal[0] == 0:
        n "...Hm."
        n "Well, it's not really any worse than your last one."
        n "But I can't really say it's any better, either."
        mc "Phew..."
        n "Huh? 'Phew' what?"
        mc "Ah... Well anything that isn't a trainwreck, I'll take as a win."
        mc "And I get the feeling you're probably the most critical."
        n "H-Hey! What makes you--"
        n "{i}(Wait, maybe that was a compliment...?){/i}"
        n "A-Ahah! Glad to see someone recognizes my experience!"
        n "Well then, keep practicing and maybe you'll be as good as me someday!"
        mc "That's...uh..."
        "Something tells me Bladewolf completely missed the point."
        jump ch22_n_med_shared
    else:


        n "...Hm."
        n "Well, it's not terrible."
        n "But it's pretty disappointing after your last one."
        n "Then again, if this one was as good as your last one, I would be completely pissed."
        mc "Well, I guess I wanted to try something a little different this time."
        label ch22_n_med_shared2:
            n "Fair enough. You're still new to this, so I wouldn't expect you to find your style right away."
            n "I mean, everyone in the club writes really differently from each other..."
            n "Maybe you'll find a little influence from all of us."
            n "For instance..."
            n "I noticed that you were spending some time with Sam today..."
            n "Not that I care who you spend your time with."
            n "After all, I was taught never to expect anything from anybody."
            n "So it's not like I was waiting for you, or anything."
            n "Still, you should at least look over my poem..."
            n "You'll probably be able to learn something from it."
            return

label ch23_n_bad:
    if y_gave:
        jump ch23_n_ygave

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        n "I'm not going to read another one of your Sam suck-up poems."
        n "But I'm still going to make you read mine."
        n "There's a reason."
        n "I really wish I didn't have to do this..."
        n "But unfortunately I don't have much of a choice."
        n "Just...read it carefully, okay?"
        n "Then you can go away."
        return

    elif n_poemappeal[0] < 0 or n_poemappeal[1] < 0:
        n "..."
        n "...Meh."
        n "I guess you really haven't learned anything after all."
        n "Honestly, I don't know why I got my hopes up in the first place."
        label ch23_n_bad_shared:
            n "This is clearly Sam's influence..."
            n "I didn't realize you were so impressionable."
            n "Spending all this time with her in the club..."
            n "Now trying to write like her..."
            n "This is stupid."
            n "At least Armstrong appreciates my writing..."
            n "...Ugh."
            n "Okay...I guess I'm going to share my poem with you now."
            n "I really hate that I have to do this."
            n "But unfortunately I don't have much of a choice."
            n "Just...read it carefully, okay?"
            n "Then you can go away."
            return
    else:

        n "..."
        n "Oh, man."
        n "This is seriously a step backwards."
        mc "Eh?"
        n "I liked your last two way better than this one."
        jump ch23_n_bad_shared

label ch23_n_med:
    if y_gave:
        jump ch23_n_ygave

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        jump ch23_n_bad
    elif n_poemappeal[1] < 0:
        n "..."
        n "...This one's alright."
        mc "Alright?"
        n "Yeah, it's at least better than yesterday's."
        label ch23_n_shared:
            n "I still can't really tell how much you actually care about writing, but either way, you're doing alright."
            n "Even though you're not really spending time with anyone but Sam..."
            n "I still think it's nice to have activities that we all participate in."
            n "So you better keep working hard!"
            n "I mean..."
            n "I know I'm not President or Vice President or anything..."
            n "But that doesn't mean you can let me down, okay?"
            n "So, at least read mine too for now."
            n "But just to be clear..."
            n "This poem...means a lot to me."
            n "So read it carefully, okay?"
            return
    else:
        n "..."
        n "...This one's alright."
        mc "Alright?"
        n "Well, yeah."
        n "About as good as yesterday's, anyway."
        jump ch23_n_shared

label ch23_n_ygave:
    n "What?"
    n "You gave your poem to Sam?"
    n "Gross!"
    n "What is with you two?"
    n "Hmph..."
    n "It's not like I wanted to read it anyway."
    n "It's just pissing me off a little bit that you didn't even think to show me at all."
    n "...Ugh."
    n "Okay...I guess I'm going to share my poem with you anyway."
    n "I really hate that I have to do this."
    n "But unfortunately I don't have much of a choice."
    n "Just...read it carefully, okay?"
    n "Then you can go away."
    return

label ch23_n_good:
    jump ch23_n_med

label ch21_y_bad:
    jump ch1_y_bad

label ch21_y_med:
    jump ch1_y_med

label ch21_y_good:
    jump ch1_y_good

label ch22_y_bad:
    jump ch22_y_med

label ch22_y_med:
    y "I've been waiting for this..."
    y "Let's see what you've written for today."
    y "..."
    "Sam smiles and takes a deep breath."
    y "I like just holding it."
    mc "...?"
    y "Ah, I mean--"
    y "The poem turned out good!"
    y "It's, ah..."
    y "...Well, there are some things that you could work on..."
    y "But that doesn't really matter."
    y "It feels like anything written by you is a treasure."
    y "Ahaha..."
    y "That came out a little awkward..."
    y "L-Let's move on..."
    y "Here's the poem I wrote."
    y "You don't have to like it or anything..."
    return


label ch22_y_good:

    if y_poemappeal[0] < 1:
        y "I've been waiting for this..."
        y "Let's see what you've written for today."
        y "..."
        y "......"
        "Sam stares at the poem with a surprised expression on her face."
        mc "Do you...like it?"
        y "[player]..."
        y "...How did you pick up on this so quickly?"
        label ch22_y_good_shared:
            y "Just yesterday, I was telling you the kind of techniques worth practicing..."
            mc "Maybe that's why..."
            mc "You did a good job explaining."
            mc "I really wanted to try giving it more imagery."
            show sam zorder 2 at t11
            "Sam visibly swallows."
            "Even her hands appear sweaty."
            y "A-Ah..."
            y "That makes me so happy..."
            y 3y5 "It's so amazing to feel like I'm valued, [player]!"
            y "Everything that you write is a treasure to me."
            y "My heart pounds just holding it..."
            y "Ahaha..."
            y "I want to write a poem about this feeling..."
            y 3y6 "Is that bad, [player]?"
            y "I'm not being weird, right?"
            y "I-I'm having a harder time than usual at concealing my emotions..."
            y "I'm kind of embarrassed."
            y 3y6 "But right now, I just want you to read my poem, too."
            y 3y5 "Okay?"
            return
    else:

        y "I've been waiting for this..."
        y "Let's see what you've written for today."
        y "..."
        y "......"
        "Sam stares at the poem with a surprised expression on her face."
        mc "Do you...like it?"
        y "[player]..."
        y "This one might even be better than yesterday's..."
        y "...How did you even pick up on this so quickly?"
        jump ch22_y_good_shared

label ch23_y_bad:
    jump ch23_y_good

label ch23_y_med:
    jump ch23_y_good

label ch23_y_good:
    y "Finally..."
    y 3y5 "Ahaha..."
    show sam     "Sam holds my poem to her face and takes a deep breath."
    y 3y6 "I love it."
    y "I love everything about it."
    y 3y5 "[player], I want to take this home."
    y "Will you let me keep it?"
    y "Please?"
    mc "Sure, I don't care..."
    y 2y5 "Ahaha."
    y "You're too nice to me, [player]..."
    y "I've never met anyone as nice as you."
    y 2y6 "I could die..."
    y 3y5 "N-Not really, but--!"
    y "I just don't know how to describe it."
    y "It's okay to be feeling this way, right?"
    show sam:
        "y4"
        0.4
        "y6"
    y "It's not bad, right?"
    "Sam holds my poem to her chest."
    y "I'm going to take this home with me and keep it in my room."
    y "I hope that it makes you feel good when you think about me having it."
    $ style.say_dialogue = style.normal
    y 3y5 "I'll take good care of it!"
    $ style.say_dialogue = style.edited
    y 3y6 "I'll even touch myself while reading it over and over."
    $ _history_list.pop()
    y "I'll give myself paper cuts so your skin oil enters my bloodstream."
    $ _history_list.pop()
    y 3y1 "Ahahahahaha."
    $ _history_list.pop()
    $ style.say_dialogue = style.normal
    y "You can have my poem too."
    y "Besides, after you read it, I know you're really going to want to keep it."
    y 2y6 "Here, take it. I can't wait any longer."
    y 2y5 "Hurry! Read it!"
    $ y_gave = True
    return


label ch21_m_start:
    m "Hi, [player]!"
    m "Having a good time so far?"
    mc "Ah...yeah."
    m "Good! Glad to hear it!"
    m "By the way, since you're new and everything..."
    m "If you ever have any suggestions for the club, like new activities, or things we can do better..."
    m "I'm always listening!"
    m "Don't be afraid to bring things up, okay?"
    show armstrong     mc "Alright...I'll keep that in mind."
    "Of course I'll be afraid to bring things up."
    "I'm much better off just going with the flow until I'm more settled in."
    m "Anyway..."
    m "Want to share your poem with me?"
    mc "It's kind of embarrassing, but I guess I have to."
    m "Ahahaha!"
    m "Don't worry, [player]!"
    m "We're all a little embarrassed today, you know?"
    m "But it's that sort of barrier that we'll all learn to get past soon."
    mc "Yeah, that's true."
    "I hand Armstrong my poem."
    m "...Mhm!"
    $ nextscene = "m2_" + poemwinner[0] + "_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene

    m "Anyway, do you want to read my poem now?"
    m "Don't worry, I'm not very good..."
    mc "You sound pretty confident for someone who claims to not be very good."
    m "Well...that's 'cause I have to sound confident."
    m "That doesn't mean I always feel that way, you know?"
    mc "I see..."
    mc "Well, let's read it, then."
    return

label ch22_m_start:
    if y_appeal < 2:
        m "Hi again, [player]!"
        m "How's the writing going?"
        mc "Alright, I guess..."
        m "I'll take that."
        m "As long as it's not going bad!"
        m "I'm happy that you're applying yourself."
        m "Maybe soon you'll come up with a masterpiece!"
        mc "Ahaha, I wouldn't count on that..."
        m "You never know!"
        m "Want to share what you wrote for today?"
        mc "Sure... Here you go."
        "I give my poem to Armstrong."
        m "..."
        m "...Alright!"
    $ nextscene = "m2_sam_" + str(eval("y_appeal"))
    call expression nextscene

    m "But anyway..."
    m "You want to read my poem now?"
    m "I like the way this one turned out, so I hope you do too~"
    return

label ch23_m_start:
    $ nextscene = "m2_sam_" + str(eval("y_appeal"))
    call expression nextscene
    if y_appeal < 3:
        m "Anyway..."
        if y_gave:
            m "I guess we won't worry about your poem..."
            m "Sam should have at least had the courtesy of letting you finish sharing it before taking it."
            m "...Well, whatever."
            m "If it makes her happy, I won't stop her."
            m "As for mine..."
        m "I worked really...really hard on this poem, so..."
        m "I hope that it's, uh, effective."
        m "Here goes..."
        $ persistent.seen_colors_poem = True
    return



label m2_bladewolf_1:
    m "I like it, [player]!"
    mc "Really...?"
    m "It's a lot cuter than I expected."
    m "Ahahaha!"
    mc "Oh jeez..."
    m "No, no!"
    m "It kind of makes me think of something Bladewolf would write."
    m "And she's a good writer, too."
    m "So take that as a compliment!"
    mc "Ahaha..."
    mc "If you say so."
    m "Yep!"
    m "If you're interested in Bladewolf, then always keep a snack on you."
    m "She'll cling to you like a puppy."
    m "Ahaha!"
    m "Bladewolf's dad doesn't give her lunch money or leave her any food in the house, so she's in a fussy mood pretty often..."
    m "But sometimes she just loses all of her strength and shuts down."
    m "Like earlier."
    m "This is just a guess, but I think she's so small because her malnutrition is interfering with her adolescent growth..."
    m "...But hey, some guys are into petite girls too, you know?"
    m "Sorry...just trying to look at the bright side!"

    return

label m2_sam_1:
    m "Great job, [player]!"
    m "I was going 'Ooh' in my head while reading it."
    m "It's really metaphorical!"
    m "I'm not sure why, but I didn't expect you to go for something so deep."
    m "I guess I underestimated you!"
    mc "It's easiest for me to keep everyone's expectations low."
    mc "That way, it always counts when I put in some effort."
    m "Ahaha! That's not very fair!"
    m "Well, I guess it worked, anyway."
    m "You know that Sam likes this kind of writing, right?"
    m "Writing that's full of imagery and symbolism."
    m "Sometimes I feel like Sam's mind is just totally detached from reality."
    m "I don't mean that like it's a bad thing, though."
    m "But sometimes I get the impression that she's just totally given up on people."
    m "She spends so much time in her own head that it's probably a much more interesting place for her..."
    m "But that's why she gets so happy when you treat her with a lot of kindness."
    m "I don't think she's used to being indulged like that."
    m "She must be really starved for social interaction, so don't blame her for coming on a little strongly."
    m "Like earlier..."
    m "I think if she gets too stimulated, she ends up withdrawing and looking for alone time."
    "Suddenly, the door opens."
    m "Sam!"
    show armstrong
    show sam zorder 3 at f31
    y "I'm back..."
    y "Did I miss anything?"
    show sam zorder 2 at t31
    show armstrong zorder 3 at f32
    m "Not really..."
    m "Well, we all started sharing our poems with each other."
    show armstrong zorder 2 at t32
    show sam zorder 3 at f31
    y "Eh?"
    y "Already?"
    y "I-I'm sorry for being late..."
    show sam zorder 2 at t31
    show armstrong zorder 3 at f32
    m "No need to apologize!"
    m "We still have plenty of time, so I'm more glad that you took all the time you needed."
    show armstrong zorder 2 at t32
    show sam zorder 3 at f31
    y "Alright..."
    y "Thanks, Armstrong."
    y "I suppose I should go get my poem now."
    show sam zorder 1 at thide
    hide sam
    $ y_ranaway = False
    return

label m2_sam_2:
    m "[player], I think you saw something earlier that you weren't supposed to see."
    m "I didn't want to have to tell you this, but I don't think I have a choice."
    m "It's getting kind of dangerous for you to spend so much time with Sam."
    m "I don't know why, but she seems pretty easily excitable when she's around you..."
    m "Which shouldn't be a problem in itself."
    m "But when Sam gets too excited, she finds a place to hide and starts cutting herself with a pocket knife."
    m "Isn't that kind of messed up?"
    m "She even brings a different one to school every day, like she has a collection or something..."
    m "I mean, it's definitely not because she's depressed or anything like that!"
    m "I think she just gets some kind of high from it."
    m "It might even be, like, a sexual thing..."
    m "But the point is, you've kind of been enabling her."
    m "I'm not saying it's your fault, though!"
    m "But I guess that's why I had to explain it all to you..."
    m "So I think if you keep your distance, that would probably be best for her."
    m 5 "While you're at it, don't be shy to spend a little more time with me..."
    m "To put it lightly, I at least have it together in the head...and I know how to treat my club members."
    return

label m2_sam_3:
    stop music
    m "Don't say I didn't warn you, [player]."
    $ skip_poem = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
