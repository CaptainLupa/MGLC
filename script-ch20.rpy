label ch20_from_ch10:
    scene bg residential_day
    with dissolve_scene_half
    play music t2
    jump ch20_main2

label ch20_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

label ch20_main2:
    "It's an ordinary school day, like any other."
    "Mornings are usually the worst, being surrounded by couples and friend groups walking to school together."
    "Meanwhile, I've always walked to school alone."
    "I always tell myself it's about time I meet some girls or something like that..."
    "But I have no motivation to join any clubs."
    "I'm perfectly content just getting by on the average while spending my free time on games and anime."
    "There's always the anime club, but it's not like there would be any girls in it anyway..."

    scene bg class_day
    with wipeleft_scene

    "The school day is as ordinary as ever, and it's over before I know it."
    "After I pack up my things, I stare blankly at the wall, looking for an ounce of motivation."
    mc "Clubs..."
    "There really aren't any that interest me."
    "Besides, most of them would probably be way too demanding for me to want to deal with."
    "I guess I have no choice but to start with the anime club..."

    $ m_name = "???"

    m "...[player]?"
    window hide(None)
    show armstrong g2 zorder 2 at t11
    $ pause(0.75)
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    show armstrong zorder 2 at t11
    mc "...Armstrong?"
    $ m_name = "Armstrong"
    m "Oh my goodness, I totally didn't expect to see you here!"
    m 5 "It's been a while, right?"
    mc "Ah..."
    mc "Yeah, it has."
    "Armstrong smiles sweetly."
    "We do know each other - well, we rarely talked, but we were in the same class last year."
    "Armstrong was probably the most popular girl in class - smart, beautiful, athletic."
    "Basically, completely out of my league."
    "So, having her smile at me so genuinely feels a little..."
    mc "What did you come in here for, anyway?"
    m "Oh, I've just been looking for some supplies to use for my club."
    m "Do you know if there's any construction paper in here?"
    m "Or markers?"
    mc "I guess you could check the closet."
    mc "...You're in the debate club, right?"
    m 5 "Ahaha, about that..."
    m "I actually quit the debate club."
    mc "Really? You quit?"
    m "Yeah..."
    m "To be honest, I can't stand all of the politics around the major clubs."
    m "It feels like nothing but arguing about the budget and publicity and how to prepare for events..."
    m "I'd much rather take something I personally enjoy and make something special out of it."
    mc "In that case, what club did you decide to join?"
    m "Actually, I'm starting a new one!"
    m "A literature club!{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    $ pause(0.25)
    stop sound
    hide screen tear
    window show(None)
    m "A literature club!{fast}"
    window auto
    mc "Literature...?"
    "That sounds kind of...dull?"
    mc "How many members do you have so far?"
    m 5 "Um..."
    m "Ahaha..."
    m "It's kind of embarrassing, but there are only three of us so far."
    m "It's really hard to find new members for something that sounds so boring..."
    mc "Well, I can see that..."
    m "But it's really not boring at all, you know!"
    m "Literature can be anything. Reading, writing, poetry..."
    m "I mean, one of my members even keeps her manga collection in the clubroom..."
    mc "Wait...really?"
    m "Yeah, it's funny, right?"
    m "She always insists that manga is literature, too."
    m "I mean, she's not wrong, I guess..."
    m "And besides, a member's a member, right?"
    "...Did Armstrong say \"she\"?"
    "Hmm..."
    m "Hey, [player]..."
    m "By any chance...are you still looking for a club to join?"
    mc "Ah--"
    mc "I mean, I guess so, but..."
    m "In that case..."
    m 5 "Is there any chance you could do me a big favor?"
    m "I won't ask you to join, but..."
    m "If you could at the very least visit my club, it would make me really happy."
    m "Please?"
    mc "Um..."
    "Well, I guess I have no reason to refuse..."
    "Besides, how could I ever refuse someone like Armstrong?"
    mc "Sure, I guess I could check it out."
    m "Aah, awesome!"
    m "You're really sweet, [player], you know that?"
    mc "I-It's nothing, really..."
    m "Shall we go, then?"
    m "I'll look for the materials another time - you're more important."

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    "And thus, today marks the day I sold my soul to Armstrong and her irresistible smile."
    "I timidly follow Armstrong across the school and upstairs - a section of the school I rarely visit, being generally used for third-year classes and activities."
    "Armstrong, full of energy, swings open the classroom door."

    scene bg club_day2
    with wipeleft
    play music t3

    if renpy.random.randint(0, 2) == 0:
        show armstrong g1 at l31
    else:
        show armstrong at l31
    m "I'm back~!"
    m "And I brought a guest with me!"
    show sam zorder 2 at t33
    if not config.skipping:
        show screen invert(0.15, 0.3)
    y "Eh?"
    y "A...a guest?"
    show bladewolf zorder 2 at t32
    n "Seriously? You brought a boy?"
    n "Way to kill the atmosphere."
    show armstrong zorder 3 at f31
    m "Don't be mean, Bladewolf..."
    m "...But anyway, welcome to the club, [player]!"
    show armstrong zorder 2 at t31
    mc "..."
    "All words escape me in this situation."
    "This club..."
    "{i}...is full of incredibly cute girls!!{/i}"

    show bladewolf zorder 3 at f32
    n "So, let me guess..."
    n "You're Armstrong's boyfriend, right?"
    show bladewolf zorder 2 at t32
    mc "Wha--"
    mc "No, I'm not!"
    show sam zorder 3 at f33
    y "Bladewolf..."
    $ n_name = 'Bladewolf'
    "The girl with the sour attitude, whose name is apparently Bladewolf, is one I don't recognize."
    "Her small figure makes me think she's probably a first-year."

    show sam zorder 2 at t33
    show armstrong zorder 3 at f31
    m "A-Anyway, this is Bladewolf, energetic as usual..."
    m "And this is Sam, the Vice President!"
    $ y_name = 'Sam'
    show armstrong zorder 2 at t31
    show sam zorder 3 at f33
    y 4 "I-It's nice to meet you..."
    "Sam, who appears comparably more mature and timid, seems to have a hard time keeping up with someone like Bladewolf."
    show sam zorder 2 at t33
    mc "Yeah... It's nice to meet both of you."
    show armstrong zorder 3 at f31
    m "So, I ran into [player] in a classroom, and he decided to come check out the club."
    m "Isn't that great?"
    show armstrong zorder 2 at t31
    show bladewolf zorder 3 at f32
    n "Wait! Armstrong!"
    n "Didn't I tell you to let me know in advance before you brought anyone new?"
    n "I was going to...well, you know..."
    show bladewolf zorder 2 at t32
    show armstrong zorder 3 at f31
    m "Sorry, sorry!"
    m "I didn't forget that, but I just happened to run into him."
    show armstrong zorder 2 at t31
    show sam zorder 3 at f33
    y "In that case, I should at least make some tea, right?"
    show sam zorder 2 at t33
    show armstrong zorder 3 at f31
    m "Yeah, that would be great!"
    m "Why don't you come sit down, [player]?"
    hide armstrong
    hide bladewolf
    hide sam
    with wipeleft
    "The girls have a few desks arranged to form a table."
    "Sam walks to the corner of the room and opens the closet."
    "Meanwhile, Armstrong and Bladewolf sit across from each other."
    "Still feeling awkward, I take a seat next to Armstrong."
    show armstrong zorder 2 at t11
    m "So, I know you didn't really plan on coming here..."
    m "But we'll make sure you feel right at home, okay?"
    m "As president of the Literature Club, it's my duty to make the club fun and exciting for everyone!"
    mc "I'm surprised there aren't more people in the club yet."
    mc "It must be hard to start a new club."
    m "You could put it that way."
    m "Not many people are very interested in putting out all the effort to start something brand new..."
    m "Especially when it's something that doesn't grab your attention, like literature."
    m "You have to work hard to convince people that you're both fun and worthwhile."
    m "But it makes school events, like the festival, that much more important."
    m "I'm confident that we can all really grow this club before we graduate!"
    m "Right, Bladewolf?"
    show armstrong zorder 2 at t22
    show bladewolf zorder 2 at t21
    n "Well..."
    n "...I guess."
    "Bladewolf reluctantly agrees."
    "Such different girls, all interested in the same goal..."
    "Armstrong must have worked really hard just to find these two."
    "Sam returns to the table, carrying a tea set."
    "She carefully places a teacup in front of each of us before setting down the teapot in the middle."
    show bladewolf zorder 1 at thide
    show armstrong zorder 1 at thide
    hide bladewolf
    hide armstrong
    show sam zorder 2 at t21
    mc "You keep a whole tea set in this classroom?"
    y "Don't worry, the teachers gave us permission."
    y "After all, doesn't a hot cup of tea help you enjoy a good book?"
    mc "Ah... I-I guess..."
    show armstrong zorder 3 at f22
    m "Ehehe, don't let yourself get intimidated, Sam's just trying to impress you."
    show armstrong zorder 2 at t22
    show sam at hf21
    y "Eh?! T-That's not..."
    "Insulted, Sam looks away."
    y "I meant that, you know..."
    show sam zorder 2 at t21
    mc "I believe you."
    mc "Well, tea and reading might not be a pastime for me, but I at least enjoy tea."
    show sam zorder 3 at f21
    y "I'm glad..."
    show sam zorder 2 at t21
    "Sam faintly smiles to herself in relief."
    show armstrong zorder 1 at thide
    hide armstrong
    show sam zorder 2 at t32
    y "So, [player], what kinds of things do you like to read?"
    mc "Well... Ah..."
    "Considering how little I've read these past few years, I don't really have a good way of answering that."
    mc "...Manga..."
    "I mutter quietly to myself, half-joking."
    show bladewolf zorder 2 at t41
    "Bladewolf's head suddenly perks up."
    "It looks like she wants to say something, but she keeps quiet."
    show bladewolf zorder 1 at thide
    hide bladewolf
    y "N-Not much of a reader, I guess..."
    mc "...Well, that can change..."
    "What am I saying?"
    "I spoke without thinking after seeing Sam's sad smile."
    mc "Anyway, what about you, Sam?"
    y "Well, let's see..."
    "Sam traces the rim of her teacup with her finger."
    y "My favorites are usually novels that build deep and complex fantasy worlds."
    y "The level of creativity and craftsmanship behind them is amazing to me."
    y "And telling a good story in such a foreign world is equally impressive."
    "Sam goes on, clearly passionate about her reading."
    "She seemed so reserved and timid since the moment I walked in, but it's obvious by the way her eyes light up that she finds her comfort in the world of books, not people."
    y "But you know, I like a lot of things."
    y "Stories with deep psychological elements usually immerse me as well."
    y "Isn't it amazing how a writer can so deliberately take advantage of your own lack of imagination to completely throw you for a loop?"
    y "Anyway, I've been reading a lot of horror lately..."
    mc "Ah, I read a horror book once..."
    "I desperately grasp something I can relate to at the minimal level."
    "At this rate, Sam might as well be having a conversation with a rock."
    show armstrong zorder 3 at f33
    m "Ahaha. I'd expect that from you, Sam."
    m "It suits your personality."
    show armstrong zorder 2 at t33
    show sam zorder 3 at f32
    y "Oh, is that so?"
    y "Really, if a story makes me think, or takes me to another world, then I really can't put it down."
    y "Surreal horror is often very successful at changing the way you look at the world, if only for a brief moment."
    show sam zorder 2 at t32
    show bladewolf zorder 3 at f31
    n "Ugh, I hate horror..."
    show bladewolf zorder 2 at t31
    show sam zorder 3 at f32
    y "Oh? Why's that?"
    show sam zorder 2 at t32
    show bladewolf zorder 3 at f31
    n "Well, I just..."
    "Bladewolf's eyes dart over to me for a split second."
    n "Never mind."
    show bladewolf zorder 2 at t31
    show armstrong zorder 3 at f33
    m "That's right, you usually like to write about cute things, don't you, Bladewolf?"
    show armstrong zorder 2 at t33
    show bladewolf zorder 3 at f31
    n "W-What?"
    n "What gives you that idea?"
    show bladewolf zorder 2 at t31
    show armstrong zorder 3 at f33
    m "You left a piece of scrap paper behind last club meeting."
    m "It looked like you were working on a poem called--"
    show armstrong zorder 2 at t33
    show bladewolf zorder 3 at f31
    n "Don't say it out loud!!"
    n "And give that back!"
    show bladewolf zorder 2 at t31
    show armstrong zorder 3 at f33
    m "Fine, fine~"
    show armstrong zorder 2 at t33
    mc "Bladewolf, you write your own poems?"
    show bladewolf zorder 3 at f31
    n "Eh? Well, I guess sometimes."
    n "Why do you care?"
    show bladewolf zorder 2 at t31
    mc "I think that's impressive."
    mc "Why don't you share them sometime?"
    show bladewolf zorder 3 at f31
    n "N-No!"
    "Bladewolf averts her eyes."
    n "You wouldn't...like them..."
    show bladewolf zorder 2 at t31
    mc "Ah...not a very confident writer yet?"
    show sam zorder 3 at f32
    y "I understand how Bladewolf feels."
    y "Sharing that level of writing takes more than just confidence."
    y "The truest form of writing is writing to oneself."
    y "You must be willing to open up to your readers, exposing your vulnerabilities and showing even the deepest reaches of your heart."
    show sam zorder 2 at t32
    show armstrong zorder 3 at f33
    m "Do you have writing experience too, Sam?"
    m "Maybe if you share some of your work, you can set an example and help Bladewolf feel comfortable enough to share hers."
    show sam at s32
    y "..."
    mc "I guess it's the same for Sam..."
    "We all sit in silence for a moment."
    show armstrong zorder 3 at f33
    m "Hey, I just got an idea!"
    m "How about this?"
    show armstrong zorder 2 at t33
    show bladewolf zorder 3 at f31
    show sam zorder 3 at f32
    ny "...?"
    "Bladewolf and Sam look quizzically at Armstrong."
    show bladewolf zorder 2 at t31
    show sam zorder 2 at t32
    show armstrong zorder 3 at f33
    m "Let's all go home and write a poem of our own!"
    m "Then, next time we meet, we'll all share them with each other."
    m "That way, everyone is even!"
    show armstrong zorder 2 at t33
    show bladewolf zorder 3 at f31
    n "U-Um..."
    show bladewolf zorder 2 at t31
    show sam zorder 3 at f32
    y "..."
    show sam zorder 2 at t32
    show armstrong zorder 3 at f33
    m "Ah..."
    m "I mean, I thought it was a good idea..."
    show armstrong zorder 2 at t33
    show sam zorder 3 at f32
    y "Well..."
    y "...I think you're right, Armstrong."
    y "We should probably start finding activities for all of us to participate in together."
    y "I did decide to take on the responsibility of Vice President, after all..."
    y "I need to do my best to nurture the club as well as its members."
    y "Besides, now that we have a new member..."
    y "It seems like a good step for us to take."
    y "Do you agree as well, [player]?"
    show sam zorder 2 at t32
    mc "Hold on...there's still one problem."
    show armstrong zorder 3 at f33
    m "Eh? What's that?"
    "Now that we've reached the most important topic, I bluntly come forth with what's been on my mind the entire time."
    show armstrong zorder 2 at t33
    mc "I never said I would join this club!"
    mc "Armstrong may have convinced me to stop by, but I never made any decision."
    mc "I still have other clubs to look at, and...um..."
    show armstrong
    show bladewolf
    show sam
    "I lose my train of thought."
    "All three girls stare back at me with dejected eyes."
    show armstrong at s33
    m "B-But..."
    show sam at s32
    y "I'm sorry, I thought..."
    show bladewolf at s31
    n "Hmph."
    mc "Eh...?"
    "The girls exchange glances before Armstrong turns back to me."
    show armstrong zorder 3 at f33
    m "I...guess I need to tell you the truth, [player]."
    m "The thing is..."
    m "...We don't have enough members yet to form an official club."
    m "We need four..."
    m "And I've been trying really, really hard to find new members."
    m "And if we don't find one more before the festival..."
    show armstrong zorder 2 at t33
    mc "..."
    "I...I'm defenseless against these girls."
    "How am I supposed to make a clear-headed decision when it's like this?"
    "I would feel terrible for letting everyone down in this situation..."
    "And besides, the club itself seems pretty relaxed..."
    "So, if writing poems is the price I need to pay in order to spend every day with these beautiful girls..."
    mc "...Right."
    mc "Okay, I've decided, then."
    mc "I'll join the Literature Club."
    show armstrong zorder 2 at t33
    show sam zorder 2 at t32
    show bladewolf zorder 2 at t31
    "One by one, the girls' eyes light up."
    show armstrong zorder 3 at f33
    m "Oh my goodness, really?"
    m "Do you really mean that, [player]?"
    show armstrong zorder 2 at t33
    mc "Yeah..."
    mc "It could be fun, right?"
    show sam zorder 3 at f32
    y "You really did scare me for a moment..."
    show sam zorder 2 at t32
    show bladewolf zorder 3 at f31
    n "I mean, if you really just left after all this, I would be super pissed."
    show bladewolf zorder 2 at t31
    show armstrong zorder 3 at f33
    m "[player], I'm so happy..."
    m "We can become an official club now!"
    m "Thank you so much for this. You're really amazing."
    m "I'll do everything I can to give you a great time, okay?"
    show armstrong zorder 2 at t33
    mc "Ah...thanks, I guess."
    show sam zorder 1 at thide
    show bladewolf zorder 1 at thide
    show armstrong zorder 2 at t11
    hide sam
    hide bladewolf
    m "Okay, everyone!"
    m "I think with that, we can officially end today's meeting on a good note."
    m "Everyone remember tonight's assignment:"
    m "Write a poem to bring to the next meeting, so we can all share!"
    "Armstrong looks over at me once more."
    m "[player], I look forward to seeing how you express yourself."
    show armstrong at hop
    m "Ehehe~"
    mc "Y-Yeah..."
    show armstrong zorder 1 at thide
    hide armstrong
    "Can I really impress the class star Armstrong with my mediocre writing skills?"
    "I already feel the anxiety welling up inside me."
    "Meanwhile, the girls continue to chit-chat as Sam cleans up the tea set."
    mc "I guess I'll be on my way, then..."
    show armstrong zorder 2 at t11
    m "Okay!"
    m "I'll see you tomorrow, then."
    m "I can't wait!"

    scene bg residential_day
    with wipeleft_scene

    "With that, I depart the clubroom and make my way home."
    "The whole way, my mind wanders back and forth between the three girls:"
    show bladewolf zorder 2 at t31
    "Bladewolf,"
    show sam zorder 2 at t32
    "Sam,"
    show armstrong zorder 2 at t33
    "and, of course, Armstrong."
    "Will I really be happy spending every day after school in a literature club?"
    "Perhaps I'll have the chance to grow closer to one of these girls..."
    hide bladewolf
    hide sam
    hide armstrong
    with wipeleft
    "Alright!"
    "I'll just need to make the most of my circumstances, and I'm sure good fortune will find me."
    "And I guess that starts with writing a poem tonight..."

    stop music fadeout 2.0
    scene black with dissolve_scene_full
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False

    call screen confirm("You have unlocked a special poem.\nWould you like to read it?", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[0])
    else:
        pass

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
