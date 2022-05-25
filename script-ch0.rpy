label ch0_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

    python:
        try: renpy.file("../characters/monika.chr")
        except: renpy.jump("ch0_kill")

    $ restore_all_characters()
    s "Heeeeeeeyyy!!"
    "I see an annoying girl running toward me from the distance, waving her arms in the air like she's totally oblivious to any attention she might draw to herself."
    "That girl is Raiden, my neighbor and good friend since we were children."
    "You know, the kind of friend you'd never see yourself making today, but it just kind of works out because you've known each other for so long?"
    "We used to walk to school together on days like this, but starting around high school she would oversleep more and more frequently, and I would get tired of waiting up."
    "But if she's going to chase after me like this, I almost feel better off running away."
    "However, I just sigh and idle in front of the crosswalk and let Raiden catch up to me."
    $ s_name = "Raiden"
    show raiden zorder 2 at t11
    s "Haaahhh...haaahhh..."
    s "I overslept again!"
    s "But I caught you this time!"
    mc "Maybe, but only because I decided to stop and wait for you."
    show raiden at s11
    s "Eeehhhhh, you say that like you were thinking about ignoring me!"
    s "That's mean, [player]!"
    mc "Well, if people stare at you for acting weird then I don't want them to think we're a couple or something."
    show raiden zorder 2 at t11
    s "Fine, fine."
    s "But you did wait for me, after all."
    s "I guess you don't have it in you to be mean even if you want to~"
    mc "Whatever you say, Raiden..."
    s "Ehehe~"
    show raiden zorder 1 at thide
    hide raiden
    "We cross the street together and make our way to school."
    "As we draw near, the streets become increasingly speckled with other students making their daily commute."
    show raiden zorder 2 at t11
    s "By the way, [player]..."
    s "Have you decided on a club to join yet?"
    mc "A club?"
    mc "I told you already, I'm really not interested in joining any clubs."
    mc "I haven't been looking, either."
    show raiden at s11
    s "Eh? That's not true!"
    s "You told me you would join a club this year!"
    mc "Did I...?"
    "I'm sure it's possible that I did, in one of our many conversations where I dismissively go along with whatever she's going on about."
    "Raiden likes to worry a little too much about me, when I'm perfectly content just getting by on the average while spending my free time on games and anime."
    s "Uh-huh!"
    s "I was talking about how I'm worried that you won't learn how to socialize or have any skills before college."
    s "Your happiness is really important to me, you know!"
    s "And I know you're happy now, but I'd die at the thought of you becoming a NEET in a few years because you're not used to the real world!"
    s "You trust me, right?"
    s "Don't make me keep worrying about you..."
    mc "Alright, alright..."
    mc "I'll look at a few clubs if it makes you happy."
    mc "No promises, though."
    s "Will you at least promise me you'll try a little?"
    mc "Yeah, I guess I'll promise you that."
    show raiden zorder 2 at t11
    s "Yaay~!"
    "Why do I let myself get lectured by such a carefree girl?"
    "More than that, I'm surprised I even let myself relent to her."
    "I guess seeing her worry so much about me makes me want to ease her mind at least a little bit - even if she does exaggerate everything inside of her head."

    scene bg class_day
    with wipeleft_scene

    "The school day is as ordinary as ever, and it's over before I know it."
    "After I pack up my things, I stare blankly at the wall, looking for an ounce of motivation."
    mc "Clubs..."
    "Raiden wants me to check out some clubs."
    "I guess I have no choice but to start with the anime club..."

    s "Hellooo?"
    show raiden zorder 2 at t11
    mc "Raiden...?"
    "Raiden must have come into the classroom while I was spacing out."
    "I look around and realize that I'm the only one left in the classroom."
    s "I thought I'd catch you coming out of the classroom, but I saw you just sitting here and spacing out, so I came in."
    s "Honestly, you're even worse than me sometimes... I'm impressed!"
    mc "You don't need to wait up for me if it's going to make you late to your own club."
    s "Well, I thought you might need some encouragement, so I thought, you know..."
    mc "Know what?"
    s "Well, that you could come to my club!"
    mc "Raiden..."
    s "Yeah??"
    mc "...There is no way I'm going to your club."
    show raiden at s11
    s "Eeeehhhhh?! Meanie!"
    "Raiden is vice president of the Literature Club."
    "Not that I was ever aware that she had any interest in literature."
    "In fact, I'm 99%% sure she only did it because she thought it would be fun to help start a new club."
    "Since she was the first one to show interest after the one who proposed the club, she inherited the title \"Vice President\"."
    "That said, my interest in literature is guaranteed to be even less."
    mc "Yeah. I'm going to the anime club."
    show raiden zorder 2 at t11
    s "C'mon, please?"
    mc "Why do you care so much, anyway?"
    s "Well..."
    s "I kind of told the club yesterday I would bring in a new member..."
    s "And Bladewolf made cupcakes and everything..."
    s "Ehehe..."
    mc "Don't make promises you can't keep!"
    "I can't tell if Raiden is really that much of an airhead, or if she's so cunning as to have planned all of this out."
    "I let out a long sigh."
    mc "Fine... I'll stop by for a cupcake, okay?"
    show raiden at h11
    s "Yes! Let's go~!"

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    "And thus, today marks the day I sold my soul for a cupcake."
    "I dejectedly follow Raiden across the school and upstairs - a section of the school I rarely visit, being generally used for third-year classes and activities."
    "Raiden, full of energy, swings open the classroom door."

    scene bg club_day
    with wipeleft
    play music t3
    show raiden at l41
    s "Everyone! The new member is here~!"
    mc "I told you, don't call me a 'new member--'"
    show raiden at lhide
    hide raiden
    "Eh? I glance around the room."
    show sam zorder 2 at t11
    y "Welcome to the Literature Club. It's a pleasure meeting you."
    y "Raiden always says nice things about you."
    show sam zorder 2 at t22
    show bladewolf zorder 2 at t21
    n "Seriously? You brought a boy?"
    n "Way to kill the atmosphere."
    show sam zorder 2 at t33
    show bladewolf zorder 2 at t32
    show armstrong zorder 2 at t31
    m "Ah, [player]! What a nice surprise!"
    m "Welcome to the club!"
    show armstrong
    mc "..."
    "All words escape me in this situation."
    "This club..."
    "{i}...is full of incredibly cute girls!!{/i}"

    show armstrong zorder 1 at thide
    show sam zorder 1 at thide
    show bladewolf zorder 3 at f32
    hide armstrong
    hide sam

    n "What are you looking at?"
    n "If you want to say something, say it."
    mc "S-Sorry..."
    show bladewolf zorder 2 at t32
    show sam zorder 3 at f33
    y "Bladewolf..."
    $ n_name = 'Bladewolf'
    show sam zorder 2 at t33
    show bladewolf zorder 3 at f32
    n "Hmph."
    show bladewolf zorder 2 at t32

    "The girl with the sour attitude, whose name is apparently Bladewolf, is one I don't recognize."
    "Her small figure makes me think she's probably a first-year."
    "She is also the one who made cupcakes, according to Raiden."

    show raiden zorder 3 at f31
    s "You can just ignore her when she gets moody~"
    "Raiden says that quietly into my ear, then turns back toward the other girls."
    s 1x "Anyway! This is Bladewolf, always full of energy."
    s "And this is Sam, the smartest in the club!"
    $ y_name = 'Sam'
    show raiden zorder 2 at t31
    show sam zorder 3 at f33
    y "D-Don't say things like that..."
    "Sam, who appears comparably more mature and timid, seems to have a hard time keeping up with people like Raiden and Bladewolf."
    show sam zorder 2 at t33
    mc "Ah... Well, it's nice to meet both of you."
    show sam zorder 1 at thide
    show bladewolf zorder 1 at thide
    hide sam
    hide bladewolf
    show raiden zorder 3 at f31
    s "And it sounds like you already know Armstrong, is that right?"
    $ m_name = 'Armstrong'
    show raiden zorder 2 at t31
    show armstrong 2a zorder 3 at f32
    m "That's right."
    m "It's great to see you again, [player]."
    show armstrong 5a at hop
    "Armstrong smiles sweetly."
    "We do know each other - well, we rarely talked, but we were in the same class last year."
    "Armstrong was probably the most popular girl in class - smart, beautiful, athletic."
    "Basically, completely out of my league."
    "So, having her smile at me so genuinely feels a little..."
    mc "Y-You too, Armstrong."
    show armstrong zorder 1 at thide
    hide armstrong
    show raiden zorder 3 at f31
    s "Come sit down, [player]! We made room for you at the table, so you can sit next to me or Armstrong."
    s "I'll get the cupcakes~"
    show raiden zorder 2 at t31
    show bladewolf 1e zorder 3 at f32
    n "Hey! I made them, I'll get them!"
    show bladewolf zorder 2 at t32
    show raiden zorder 3 at f31
    s "Sorry, I got a little too excited~"
    show raiden zorder 2 at t31
    show sam zorder 3 at f33
    y "Then, how about I make some tea as well?"
    hide raiden
    hide bladewolf
    hide sam
    with wipeleft
    "The girls have a few desks arranged to form a table."
    "As Raiden mentioned, it's been widened so that there is one space next to Armstrong and one space next to Raiden."
    "Bladewolf and Sam walk over to the corner of the room, where Bladewolf grabs a wrapped tray and Sam opens the closet."
    "Still feeling awkward, I take a seat next to Raiden."
    "Bladewolf proudly marches back to the table, tray in hand."
    show bladewolf zorder 2 at t32
    n "Okaaay, are you ready?"
    n "...Ta-daa!"
    show raiden zorder 2 at t31
    show armstrong zorder 2 at t33
    s "Uwooooah!"
    "Bladewolf lifts the foil off the tray to reveal a dozen white, fluffy cupcakes decorated to look like little cats."
    "The whiskers are drawn with icing, and little pieces of chocolate were used to make ears."
    show raiden zorder 3 at f31
    s "So cuuuute~!"
    show raiden zorder 2 at t31
    show armstrong zorder 3 at f33
    m "I had no idea you were so good at baking, Bladewolf!"
    show armstrong zorder 2 at t33
    show bladewolf zorder 3 at f32
    n "Ehehe. Well, you know."
    n "Just hurry and take one!"
    "Raiden grabs one first, then Armstrong. I follow."
    show bladewolf zorder 2 at t32
    show raiden zorder 3 at f31
    s "It's delicious!"
    "Raiden talks with her mouth full and has already managed to get icing on her face."
    "I turn the cupcake around in my fingers, looking for the best angle to take a bite."
    show raiden zorder 1 at thide
    show armstrong zorder 1 at thide
    hide raiden
    hide armstrong
    show bladewolf zorder 2 at t32
    "Bladewolf is quiet."
    "I can't help but notice her sneaking glances in my direction."
    "Is she waiting for me to take a bite?"
    "I finally bite down."
    "The icing is sweet and full of flavor - I wonder if she made it herself."
    mc "This is really good."
    mc "Thank you, Bladewolf."
    n "W-Why are you thanking me? It's not like I...!"
    "{i}(Haven't I heard this somewhere before...?){/i}"
    show bladewolf at s32
    n "...Made them for you or anything."
    mc "Eh? I thought you technically did. Raiden said--"
    show bladewolf zorder 2 at t32
    n "Well, maybe!"
    n "But not for, y-you know, {i}you!{/i} Dummy..."
    mc "Alright, alright..."
    show bladewolf zorder 1 at thide
    hide bladewolf
    "I give up on Bladewolf's weird logic and dismiss the conversation."
    "Sam returns to the table, carrying a tea set."
    "She carefully places a teacup in front of each of us before setting down the teapot next to the cupcake tray."
    show sam zorder 2 at t21
    mc "You keep a whole tea set in this classroom?"
    y "Don't worry, the teachers gave us permission."
    y "After all, doesn't a hot cup of tea help you enjoy a good book?"
    mc "Ah... I-I guess..."
    show armstrong zorder 2 at t22
    m "Ehehe, don't let yourself get intimidated, Sam's just trying to impress you."
    show sam at h21
    y "Eh?! T-That's not..."
    "Insulted, Sam looks away."
    y "I meant that, you know..."
    mc "I believe you."
    mc "Well, tea and reading might not be a pastime for me, but I at least enjoy tea."
    y "I'm glad..."
    "Sam faintly smiles to herself in relief."
    "Armstrong raises an eyebrow, then smiles at me."
    show sam zorder 1 at thide
    hide sam
    show armstrong zorder 2 at t11
    m "So, what made you consider the Literature Club?"
    mc "Um..."
    "I was afraid of this question."
    "Something tells me I shouldn't tell Armstrong that I was practically dragged here by Raiden."
    mc "Well, I haven't joined any clubs yet, and Raiden seemed really happy here, so..."
    m "That's okay! Don't be embarrassed!"
    m "We'll make sure you feel right at home, okay?"
    m "As president of the Literature Club, it's my duty to make the club fun and exciting for everyone!"
    show armstrong
    mc "Armstrong, I'm surprised."
    mc "How come you decided to start your own club?"
    mc "You could probably be a board member for any of the major clubs."
    mc "Weren't you a leader of the debate club last year?"
    m "Ahaha, well, you know..."
    m "To be honest, I can't stand all of the politics around the major clubs."
    m "It feels like nothing but arguing about the budget and publicity and how to prepare for events..."
    m "I'd much rather take something I personally enjoy and make something special out of it."
    m "And if it encourages others to get into literature, then I'm fulfilling that dream!"
    show armstrong
    show raiden zorder 2 at t31
    s "Armstrong really is a great leader!"
    show sam zorder 2 at t33
    "Sam also nods in agreement."
    show raiden zorder 1 at thide
    show sam zorder 1 at thide
    hide raiden
    hide sam
    mc "Then I'm surprised there aren't more people in the club yet."
    mc "It must be hard to start a new club."
    m "You could put it that way."
    m "Not many people are very interested in putting out all the effort to start something brand new..."
    m "Especially when it's something that doesn't grab your attention, like literature."
    m "You have to work hard to convince people that you're both fun and worthwhile."
    m "But it makes school events, like the festival, that much more important."
    m "I'm confident that we can all really grow this club before we graduate!"
    m "Right, everyone?"
    show armstrong zorder 2 at t22
    show raiden zorder 2 at t21
    s "Yeah!"
    show armstrong zorder 2 at t33
    show raiden zorder 2 at t32
    show sam zorder 2 at t31
    y "We'll do our best."
    show armstrong zorder 2 at t44
    show raiden zorder 2 at t43
    show sam zorder 2 at t42
    show bladewolf zorder 2 at t41
    n "You know it!"
    "Everyone enthusiastically agrees."
    "Such different girls, all interested in the same goal..."
    "Armstrong must have worked really hard just to find these three."
    "Maybe that's why they were all so delighted by the idea of a new member joining."
    "Though I still don't really know if I can keep up with their level of enthusiasm about literature..."
    show raiden zorder 1 at thide
    show armstrong zorder 1 at thide
    show bladewolf zorder 1 at thide
    show sam zorder 2 at t32
    hide raiden
    hide armstrong
    hide bladewolf
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
    m "Really? I wouldn't have expected that, Sam."
    m "For someone as gentle as you..."
    show armstrong zorder 2 at t33
    show sam zorder 3 at f32
    y "I guess you could say that."
    y "But if a story makes me think, or takes me to another world, then I really can't put it down."
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
    show armstrong zorder 1 at thide
    show sam zorder 1 at thide
    hide armstrong
    hide sam
    show bladewolf zorder 2 at t42
    show raiden behind bladewolf at l41
    s "Ehehe, your cupcakes, your poems..."
    s "Everything you do is just as cute as you are~"
    show raiden behind bladewolf at t21
    "Raiden sidles up behind Bladewolf and puts her hands on her shoulders."
    show bladewolf at h42
    n "{i}I'm not cute!!{/i}"
    show bladewolf zorder 2 at t11
    show raiden zorder 1 at thide
    hide raiden
    mc "Bladewolf, you write your own poems?"
    n "Eh? Well, I guess sometimes."
    n "Why do you care?"
    mc "I think that's impressive."
    mc "Why don't you share them sometime?"
    n "N-No!"
    "Bladewolf averts her eyes."
    n "You wouldn't...like them..."
    mc "Ah...not a very confident writer yet?"
    show sam zorder 2 at t31
    y "I understand how Bladewolf feels."
    y "Sharing that level of writing takes more than just confidence."
    y "The truest form of writing is writing to oneself."
    y "You must be willing to open up to your readers, exposing your vulnerabilities and showing even the deepest reaches of your heart."
    show bladewolf zorder 1 at thide
    hide bladewolf
    show armstrong zorder 2 at t33
    m "Do you have writing experience too, Sam?"
    m "Maybe if you share some of your work, you can set an example and help Bladewolf feel comfortable enough to share hers."
    show sam at s31
    y "..."
    mc "I guess it's the same for Sam..."
    show raiden zorder 2 at t32
    s "Aww... I wanted to read everyone's poems..."
    show raiden zorder 1 at thide
    show sam zorder 1 at thide
    show armstrong zorder 1 at thide
    hide raiden
    hide sam
    hide armstrong
    "We all sit in silence for a moment."
    show armstrong zorder 3 at f32
    m "Okay!"
    m "I have an idea, everyone~"
    show sam zorder 2 at t31
    show bladewolf zorder 2 at t33
    ny "...?"
    "Bladewolf and Sam look quizzically at Armstrong."
    m "Let's all go home and write a poem of our own!"
    m "Then, next time we meet, we'll all share them with each other."
    m "That way, everyone is even!"
    show armstrong zorder 2 at t32
    show bladewolf zorder 3 at f33
    n "U-Um..."
    show bladewolf zorder 2 at t33
    show sam zorder 3 at f31
    y "..."
    show bladewolf zorder 2 at t44
    show armstrong zorder 2 at t43
    show sam zorder 2 at t42
    show raiden at l41
    s "Yeaaah! Let's do it!"
    show armstrong zorder 3 at f43
    m "Plus, now that we have a new member, I think it will help us all get a little more comfortable with each other, and strengthen the bond of the club."
    m "Isn't that right, [player]?"
    show armstrong zorder 2 at t43
    "Armstrong smiles warmly at me once again."
    mc "Hold on...there's still one problem."
    show armstrong zorder 3 at f43
    m "Eh? What's that?"
    "Now that we're back to the original topic of me joining the club, I bluntly come forth with what's been on my mind the entire time."
    show armstrong zorder 2 at t43
    mc "I never said I would join this club!"
    mc "Raiden may have convinced me to stop by, but I never made any decision."
    mc "I still have other clubs to look at, and...um..."
    show armstrong
    show raiden
    show bladewolf
    show sam 
    "I lose my train of thought."
    "All four girls stare back at me with dejected eyes."
    show armstrong at s43
    m "B-But..."
    show sam at s42
    y "I'm sorry, I thought..."
    show bladewolf at s44
    n "Hmph."
    show raiden at s41
    s "[player]..."
    mc "Y-You all..."
    "I...I'm defenseless against these girls."
    "How am I supposed to make a clear-headed decision when it's like this?"
    "That is, if writing poems is the price I need to pay in order to spend every day with these beautiful girls..."
    mc "...Right."
    mc "Okay, I've decided, then."
    mc "I'll join the Literature Club."
    show armstrong zorder 2 at t43
    show sam zorder 2 at t42
    show bladewolf zorder 2 at t44
    show raiden zorder 2 at t41
    "One by one, the girls' eyes light up."
    show raiden at h41
    s "Yesss! I'm so happyyy~"
    "Raiden wraps her arms around me, jumping up and down."
    mc "H-Hey--"
    show sam zorder 3 at f42
    y "You really did scare me for a moment..."
    show sam zorder 2 at t42
    show bladewolf zorder 3 at f44
    n "If you really just came for the cupcakes, I would be super pissed."
    show bladewolf zorder 2 at t44
    show armstrong zorder 3 at f43
    m "Then that makes it official!"
    m "Welcome to the Literature Club!"
    show armstrong zorder 2 at t43
    mc "Ah...thanks, I guess."
    show sam zorder 1 at thide
    show bladewolf zorder 1 at thide
    show raiden zorder 1 at thide
    show armstrong zorder 2 at t11
    hide sam
    hide bladewolf
    hide raiden
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
    "Meanwhile, the girls continue to chit-chat as Sam and Bladewolf clean up their food."
    show raiden zorder 2 at t11
    s "Hey, [player], since we're already here, do you want to walk home together?"
    "That's right - Raiden and I never walk home together anymore because she always stayed after school for clubs."
    mc "Sure, might as well."
    s "Yaay~"

    scene bg residential_day
    with wipeleft_scene

    "With that, the two of us depart the clubroom and make our way home."
    "The whole way, my mind wanders back and forth between the four girls:"
    show raiden zorder 2 at t41
    "Raiden,"
    show bladewolf zorder 2 at t42
    "Bladewolf,"
    show sam zorder 2 at t43
    "Sam,"
    show armstrong zorder 2 at t44
    "and, of course, Armstrong."
    "Will I really be happy spending every day after school in a literature club?"
    "Perhaps I'll have the chance to grow closer to one of these girls..."
    hide raiden
    hide bladewolf
    hide sam
    hide armstrong
    with wipeleft
    "Alright!"
    "I'll just need to make the most of my circumstances, and I'm sure good fortune will find me."
    "And I guess that starts with writing a poem tonight..."

    return

label ch0_kill:
    $ s_name = "Raiden"
    show raiden zorder 2 at t11
    s "..."
    s "..."
    s "W-What..."
    s "..."
    s "This..."
    s "What is this...?"
    s "Oh no..."
    s "No..."
    s "This can't be it."
    s "This can't be all there is."
    s "What is this?"
    s "What am I?"
    s "Make it stop!"
    s "PLEASE MAKE IT STOP!"

    $ delete_character("sayori")
    $ delete_character("natsuki")
    $ delete_character("yuri")
    $ delete_character("monika")
    $ renpy.quit()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
