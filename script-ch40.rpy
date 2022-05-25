image raiden end-glitch:
    "raiden/end-glitch1.png"
    0.15
    "raiden/end-glitch2.png"
    0.15
    "raiden/end-glitch1.png"
    0.15
    "raiden/end-glitch2.png"
    1.00
    "raiden/end-glitch1.png"
    0.15
    "raiden/end-glitch2.png"
    0.15
    "raiden/end-glitch1.png"
    0.15
    "raiden/end-glitch2.png"

label ch40_main:
    $ s_name = "raiden"
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    python:
        if not persistent.armstrong_back:
            try:
                renpy.file("../characters/armstrong.chr")
                renpy.call_screen("dialog", message="Please stop playing with my heart.\nI don't want to come back.", ok_action=Return())
                persistent.armstrong_back = True
            except:
                pass

    $ delete_character("armstrong")
    play music t2
    "It's an ordinary school day, like any other."
    "As usual, I'm surrounded by couples and friend groups walking to school together."
    "I always tell myself it's about time I meet some girls or something like that..."
    show raiden at t11
    s "Hey, [player]..."
    "...Well, there already is one girl."
    "That girl is raiden, my neighbor and good friend since we were children."
    "We used to walk to school together every day..."
    "...And recently, we've picked up that habit once again."
    s "[player], are you proud of me?"
    mc "Eh? For what?"
    s "You know..."
    s "For waking up on time!"
    mc "Well, you've been doing that for a while now..."
    s "Uh-huh!"
    s "But you never even said anything about it!"
    show raiden at s11
    s "Even though we walk to school together every day..."
    mc "Well, yeah..."
    mc "I always thought it was implied."
    mc "It's embarrassing to say out loud."
    s "C'mon, please?"
    s "It's good motivation~"
    mc "Fine, fine..."
    mc "I'm proud of you, raiden."
    show raiden at t11
    s "Ehehe~"
    show raiden zorder 1 at thide
    hide raiden
    "We cross the street together and make our way to school."
    "As we draw near, the streets become increasingly speckled with other students making their daily commute."
    show raiden zorder 2 at t11
    s "By the way, [player]..."
    s "Have you decided on a club to join yet?"
    mc "A club?"
    mc "I told you already, I'm really not--"
    "I start to say what I always do - that I'm not interested in joining any clubs."
    "But something tells me raiden would take more offense to that now."
    "After all, how could I tell her that clubs are a waste of time..."
    "...when she's starting a club of her very own?"
    mc "...Actually, yeah."
    mc "I think I've decided on a club."
    show raiden at h11
    s "Really?!"
    s "Which one? Tell me!"
    mc "Hmm..."
    mc "I think I'll keep it a surprise."
    s "Boo..."
    s "You meanie."
    mc "Be patient, you'll find out soon enough."
    "I used to ask myself why I let myself get lectured by such a carefree girl."
    "But I started to realize that in a way, I envy her."
    "When raiden puts her mind to something, she can accomplish great things."
    "So that's why I feel like I should do something special for her."

    scene bg class_day
    with wipeleft_scene

    "The school day is as ordinary as ever, and it's over before I know it."
    "After I pack up my things, I stand up, gathering my motivation."
    mc "Let's see..."
    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene
    "I recall the room number of the club from a flier I saw."
    "I walk across the school and upstairs - a section of the school I rarely visit, being generally used for third-year classes and activities."
    "Before long, I find the room."
    "I timidly open the door in front of me."
    scene bg club_day
    with wipeleft
    play music t3
    mc "Hello...?"
    show raiden at t32
    s "Ah!"
    s "[player]...?!"
    s "W-What are you doing here?"
    mc "Well...I just--"
    "Eh? I glance around the room."
    show bladewolf at f31
    n "Huh."
    n "So you're the [player] that raiden's always talking about?"
    show bladewolf at t31
    show sam at f33
    y "T-Thank you for stopping by!"
    y "It's a pleasure to meet you, [player]."
    y "We're the Literature Club."
    y "I-I hope you enjoy your visit!"
    show sam at t33
    show bladewolf at f31
    n "C'mon, Sam..."
    n "No need to be so formal."
    n "He's gonna think we're really strict or something..."
    show bladewolf at t31
    $ y_name = "Sam"
    $ n_name = "Bladewolf"
    show sam at f33
    y "Ah..."
    y "Sorry, Bladewolf..."
    show sam at t33
    "The tall one, whose name is apparently Sam, seems to be quite shy compared to the others."
    "In comparison, the girl named Bladewolf - despite her size - seems like the assertive one."
    mc "Well, it's nice to meet both of you."
    mc "I look forward to working with you."
    show raiden at f32
    s "W-Working...?"
    s "[player], don't tell me..."
    s "You're..."
    show raiden at t32
    mc "That's right."
    mc "The club I've decided to join is yours, raiden."
    mc "The Literature Club."
    "raiden's eyes light up."
    show raiden at f32
    s "...No way."
    s "No way!"
    show raiden at hf32
    s "Aaaahhhhhh!"
    "raiden wraps her arms around me, jumping up and down."
    show raiden at t32
    mc "H-Hey--"
    show bladewolf at f31
    n "Ehehe."
    n "Well, if raiden is this happy, then I'm sure it won't be so bad to have you around."
    show bladewolf at t31
    show sam at f33
    y "Not to mention there's four of us now."
    y "That means we can become an officially-recognized club."
    show sam at t33
    show raiden at f32
    s "I don't know what to say!"
    s "We have to celebrate!"
    show raiden at t32
    show sam at f33
    y "Huhu."
    y "What an appropriate day for that, isn't it?"
    show sam at t33
    show raiden at f32
    s "Yeah!"
    s "After all, Bladewolf decided to--"
    show raiden at t32
    show bladewolf at f31
    n "Hey, don't ruin the surprise!"
    show bladewolf at t31
    show raiden at f32
    s "Ehehe, sorry..."
    show raiden at t32
    show bladewolf at f31
    n "Everyone sit down at the table, okay?"
    show bladewolf at t31
    show sam at f33
    y "How about I make some tea as well?"
    hide raiden
    hide bladewolf
    hide sam
    with wipeleft
    "The girls have a few desks arranged to form a table."
    "Bladewolf and Sam walk over to the corner of the room, where Bladewolf grabs a wrapped tray and Sam opens the closet."
    "Still feeling awkward, I take a seat next to raiden."
    "Bladewolf proudly marches back to the table, tray in hand."
    show bladewolf zorder 2 at t22
    n "Okaaay, are you ready?"
    n "...Ta-daa!"
    show raiden zorder 2 at t21
    s "Uwooooah!"
    "Bladewolf lifts the foil off the tray to reveal a dozen white, fluffy cupcakes decorated to look like little cats."
    "The whiskers are drawn with icing, and little pieces of chocolate were used to make ears."
    show raiden at f21
    s "So cuuuute~!"
    show raiden at t21
    mc "Wow, those look amazing."
    show bladewolf at f22
    n "Ehehe. Well, you know."
    n "Just hurry and take one!"
    show bladewolf at t22
    "raiden grabs one first, then I follow."
    show raiden at f21
    s "It's delicious!"
    show raiden at t21
    "raiden talks with her mouth full and has already managed to get icing on her face."
    "I turn the cupcake around in my fingers, looking for the best angle to take a bite."
    show raiden zorder 1 at thide
    hide raiden
    show bladewolf zorder 2 at t32
    "Bladewolf is quiet."
    "I can't help but notice her sneaking glances in my direction."
    "Is she waiting for me to take a bite?"
    "I finally bite down."
    "The icing is sweet and full of flavor - I wonder if she made it herself."
    mc "This is really good."
    mc "Thank you, Bladewolf."
    n "W-Well...of course it is!"
    n "I'm a pro, after all!"
    n "There's no need to thank me or anything..."
    show bladewolf zorder 1 at thide
    hide bladewolf
    "As Bladewolf struggles to accept the compliment, Sam returns to the table, carrying a tea set."
    "She carefully places a teacup in front of each of us before setting down the teapot next to the cupcake tray."
    show sam zorder 2 at t11
    mc "You keep a whole tea set in this classroom?"
    y "Don't worry, the teachers gave us permission."
    y "After all, doesn't a hot cup of tea help you enjoy a good book?"
    mc "Ah... I-I guess..."
    show bladewolf at f31
    n "Ehehe. Already trying to impress our new member, Sam?"
    show bladewolf at t31
    show sam at f11
    y "Eh?! T-That's not..."
    show sam at t11
    show bladewolf at thide
    hide bladewolf
    "Insulted, Sam looks away."
    y "I meant that, you know..."
    mc "I believe you."
    mc "Well, tea and reading might not be a pastime for me, but I at least enjoy tea."
    y "I'm glad..."
    "Sam faintly smiles to herself in relief."
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
    y "Don't feel intimidated if you don't read much, okay?"
    y "I'm certain we can find something that we have in common."
    show sam at t22
    show bladewolf at f21
    n "Hey, Sam..."
    show bladewolf at t21
    show sam at f22
    y "Eh?"
    show sam at t22
    show bladewolf at f21
    n "Well, about...you know, the first thing he said..."
    show bladewolf at t21
    mc "Manga?"
    show sam at f22
    y "That's right..."
    y "Bladewolf tends to read manga in the clubroom--"
    show sam at t22
    show bladewolf at f21
    n "D-Don't just say it!!"
    "For some reason, Bladewolf seems embarrassed about it."
    n "Besides..."
    n "Manga...is literature too, you know?"
    n "So...if [player] wants to read some of my manga, then don't try to stop him or anything!"
    show bladewolf at t21
    show sam at f22
    y "Bladewolf..."
    y "I wouldn't do such a thing."
    y "However, it could also be nice for us to diversify ourselves a little..."
    y "He can take this opportunity to try something new, as well."
    y "Wouldn't you agree, [player]?"
    show sam at t33
    show bladewolf at t32
    show raiden at f31
    s "M-Maybe--"
    "Sensing the tension, raiden jumps in."
    s "Maybe we can all try something new!"
    s "I think it could be fun..."
    s "And we'll all get to know each other a little bit better, too!"
    s "I mean..."
    s "That's the kind of thing literature clubs do...right?"
    show raiden at t31
    show sam at f33
    y "..."
    y "I-I don't disagree or anything..."
    show sam at t33
    show bladewolf at f32
    n "Yeah..."
    n "You're right as usual, President."
    show bladewolf at t32
    show raiden at f31
    s "Ehehe~"
    show raiden at t31
    show bladewolf at f32
    n "Guess that means I should try picking up a novel or something, huh...?"
    show bladewolf at t32
    mc "Well, that would make two of us..."
    mc "I wouldn't mind doing it if I'm not the only one."
    show raiden at thide
    hide raiden
    show bladewolf at f21
    show sam at t22
    n "Then as for Sam..."
    show bladewolf at t21
    show sam at f22
    y "Eh...?"
    y "I...I have to read manga...?"
    show sam at t22
    show bladewolf at f21
    n "Jeez..."
    n "You were the one who suggested we diversify!"
    n "You should be a little more open-minded..."
    n "It's kind of hurtful..."
    show bladewolf at t21
    show sam at f22
    y "Hurtful...?"
    y "I-I didn't realize..."
    y "..."
    "With a guilty expression, Sam thinks to herself."
    y "I'm sorry for disrespecting your interests, Bladewolf."
    y "If...if you're into it, then I'm sure it's a worthy form of literature."
    show sam at t22
    show bladewolf at f21
    n "...Are you just saying that?"
    show bladewolf at t21
    show sam at f22
    y "No..."
    y "I've realized my error."
    y "So, if you're willing to consider starting a novel..."
    y "...Then I'll offer my gratitude by finding a manga to read as well."
    show sam at t22
    show bladewolf at f21
    n "Really?!"
    n "I-I mean..."
    n "It...makes me happy that you'd do that for me, Sam."
    n "You can trust me to find something that you'll really like, okay?"
    show bladewolf at t21
    show sam at f22
    y "Same here..."
    y "Perhaps I'll visit the bookstore after the club meeting."
    show sam at t22
    show bladewolf at f21
    n "Just...just you?"
    show bladewolf at t21
    show sam at f22
    y "A-Ah--"
    y "Would you...like to come along with me?"
    show sam at t22
    show bladewolf at f21
    n "Um..."
    n "If you don't mind..."
    show bladewolf at t21
    show sam at f22
    y "Not at all!"
    y "I always go alone, so..."
    show sam at t22
    show bladewolf at f21
    n "Yeah, me too..."
    show bladewolf at t21
    show raiden at l41
    s "This is so cute~!"
    mc "raiden, shut up..."
    show raiden at lhide
    hide raiden
    show bladewolf at f21
    n "I'll show you some manga there too, okay?"
    show bladewolf at t21
    show sam at f22
    y "Yes."
    y "I look forward to it."
    show bladewolf at thide
    show sam at thide
    hide bladewolf
    hide sam
    "Bladewolf and Sam start to clean up the food."
    $ config.skipping = False
    $ config.allow_skipping = False
    show raiden at t11
    s "Ehehe~"
    s "I guess the meeting's over, huh?"
    mc "Yeah, looks like it..."
    mc "It's nice to see everyone getting along."
    s "Isn't it?"
    s "I think everyone likes you too, [player]."
    mc "You think so...?"
    mc "Well, everyone always seems to get along a little better with you around, raiden."
    s "Aww, [player]~"
    s "Don't say something like that, it's embarrassing!"
    mc "Well, whatever."
    mc "I was surprised when you told me you were starting a club..."
    mc "But I think you're pulling it off just fine."
    s "We're gonna make it the best club ever!"
    s "Now that you joined, every day is gonna be so much fun."
    stop music fadeout 2.0
    s "Hey, [player]..."
    s "I really want to thank you."
    s "I mean, I'm really happy that you joined the club and everything..."
    s "But the truth is, I already knew you were going to."
    s "Ehehe~"
    s "There's actually something else."
    $ if all(clear for clear in persistent.clear): persistent.clearall = True
    if persistent.clearall:
        call ch40_clearall
    else:
        call ch40_clearnormal
    window hide(None)
    window auto
    $ quick_menu = False
    return

    label ch40_clearnormal:
        show raiden zorder 2 at t11
        s "I wanted to thank you for getting rid of Armstrong."
        play music hb
        show black:
            alpha 0.5
            parallel:
                0.36
                alpha 0.5
                repeat
            parallel:
                0.49
                alpha 0.475
                repeat
        show layer master at heartbeat
        s "That's right..."
        s "I know everything that she did."
        s "Maybe it's because I'm the President now."
        s "But I really know everything, [player]."
        s "Ehehe~"
        s "I know how hard you tried to make everyone happy."
        s "I know about all of the awful things that Armstrong did to make everyone really sad..."
        s "But none of that matters anymore."
        s "It's just us now.{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        stop sound
        hide screen tear
        show room_glitch zorder 1:
            xoffset -5
            0.1
            xoffset 5
            0.1
            linear 0.1 alpha 0.6
            linear 0.1 alpha 0.8
            0.1
            alpha 0
        s "It's just us now.{fast}"
        hide room_glitch
        s "And you made me the happiest girl in the whole world."
        s "I can't wait to spend every day like this..."
        s "With you."
        play sound "sfx/s_kill_glitch1.ogg"
        show room_glitch zorder 1:
            xoffset -10
            0.1
            xoffset 0
            0.1
            linear 0.1 alpha 0.6
            linear 0.1 alpha 0.8
            0.1
            alpha 1.0
        $ pause(0.3)
        stop sound
        s "Forever and ever..."
        hide raiden
        show raiden onlayer screens zorder 101 at face
        s "F"
        s "o"
        s "r"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.25)
        stop sound
        hide screen tear
        s "e"
        s "v"
        s "e"
        window show(None)
        stop music
        call screen dialog("No...", ok_action=Return())
        show layer master
        hide black
        show raiden end-glitch onlayer screens
        s "...Eh?"
        s "W-What's happening...?"
        call screen dialog("I won't let you hurt him.", ok_action=Return())
        s "Who..."
        s "I-It hurts--"
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        hide raiden onlayer screens
        $ pause(0.35)
        stop sound
        hide screen tear
        window show(None)
        s "Ah--"
        call screen dialog("I'm sorry... I was wrong.", ok_action=Return())
        call screen dialog("There's no happiness here after all...", ok_action=Return())
        call screen dialog("Goodbye, raiden.", ok_action=Return())
        call screen dialog("Goodbye, [player].", ok_action=Return())
        call screen dialog("Goodbye, Literature Club.", ok_action=Return())
        $ gtext = glitchtext(120)
        s "[gtext]{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        $ pause(0.35)
        stop sound
        hide screen tear
        scene black
        $ pause(3.0)
        return

    label ch40_clearall:
        s "I wanted to thank you for spending so much time with us all."
        play music mend
        s "You worked so hard to make each and every one of us happy."
        s "You comforted us through our hard times."
        s "And you helped us all get along with each other."
        s "Do you get it, [player]?"
        s "Because I'm President now, I understand everything."
        s "You really didn't want to miss a single thing in this game, did you?"
        s "You saved and loaded so many times, just to make sure you could spend time with everyone."
        s "Only someone who truly cares about the Literature Club would go that far."
        s "But..."
        s "All along, that's all I ever wanted."
        s "For everyone to be happy and care about each other."
        s "Ahaha..."
        s "It's kind of sad, you know?"
        s "After all you've done for us, there isn't much I can do for you in return."
        s "We've already reached the end of the game."
        s "So..."
        s "This is where we say goodbye."
        s "Thank you for playing {i}Doki Doki Literature Club{/i}."
        s "I'm going to miss you, [player]."
        s "Come visit sometime, okay?"
        s "We'll always be here for you."
        s "We..."
        scene black with dissolve_cg
        s "We all love you."
        stop music fadeout 2.0
        scene black
        with Dissolve(2.0)
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
