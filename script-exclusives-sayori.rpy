label sayori_exclusive_1:
    scene bg club_day
    with wipeleft_scene
    if not renpy.music.get_playing(channel='music') == audio.t2:
        play music t2 fadeout 1
    "Man..."
    "It looks like no one wants to be bothered today."
    "I slump down into the nearest desk."
    "How am I supposed to occupy myself with something literature-related by myself like this?"
    "I guess I could always read some of the book Sam gave me..."
    "...But I'm feeling a little too tired to read."
    "I could probably fall asleep right now."
    "I close my eyes and end up listening in on raiden's conversation with Armstrong."
    show raiden zorder 2 at t21
    s "We're probably gonna seem really lame compared to all the other clubs, though..."
    show armstrong zorder 3 at f22
    m "Hmm..."
    m "Well, we can't give up."
    m "The festival is our chance to show everyone what literature is all about!"
    m "The problem is that the idea of a literature club sounds too dense and intellectual..."
    m "But it's not like that at all, you know?"
    m "We just need a way of showing that to everyone..."
    m "Something that speaks to their creative minds."
    show armstrong zorder 2 at t22
    show raiden zorder 3 at f21
    s "Mmmmmmmmmmm....."
    s "That doesn't solve the problem, though!"
    show raiden zorder 2 at t21
    show armstrong zorder 3 at f22
    m "Eh? What do you mean?"
    show armstrong zorder 2 at t22
    show raiden zorder 3 at f21
    s "Even if we come up with the most fun thing ever..."
    s "Nobody will come in the first place if it's a literature event."
    s "So it's more important to figure out how to get people to show up in the first place, you know?"
    s "And after they come, we can do the thing to speak to their creative minds."
    "...What's this?"
    "raiden is taking this really seriously."
    "It's rare to hear her deliberating like this."
    show raiden zorder 2 at t21
    show armstrong zorder 3 at f22
    m "Huh, that's a good point..."
    m "In that case, do you think food will do the trick?"
    show armstrong zorder 2 at t22
    show raiden zorder 3 at f21
    s "W-What kind?!"
    show raiden zorder 2 at t21
    show armstrong zorder 3 at f22
    m "Ah... Well, I guess we could--"
    show armstrong zorder 2 at t22
    show raiden zorder 3 at f21
    s "Cupcakes!"
    show raiden zorder 2 at t21
    show armstrong zorder 3 at f22
    m "Ahaha. Good thinking."
    m "Bladewolf would love to do that."
    show armstrong zorder 2 at t22
    show raiden zorder 3 at f21
    s "Ah! You're right!"
    s "Bladewolf makes the best cupcakes!"
    s "That works out perfectly~"
    show raiden zorder 2 at t21
    show armstrong zorder 3 at f22
    m "That wasn't why you suggested it...?"
    show armstrong zorder 2 at t22
    show raiden zorder 3 at f21
    s "Cupcakes speak to my creative tummy~"
    show raiden zorder 2 at t21
    show armstrong zorder 3 at f22
    m "..."
    m "Cupcakes it is, then."
    show armstrong zorder 2 at t22
    show raiden zorder 3 at f21
    s "I'm hungry..."
    show raiden zorder 2 at t21
    show armstrong zorder 3 at f22
    m "Anyway, we still need to work out the details of the event itself..."
    scene black
    with close_eyes
    "I find myself smiling."
    "In the end, raiden is still her usual self."
    "But therein lies the unexpected reason I admire her."
    "Unlike me, who has trouble finding any motivation at all..."
    "raiden can put her mind to things and make them come to life."
    "I suppose that's why I end up letting her get on my case about things."
    "I can't help but wonder what it would be like to see the world through her eyes..."
    scene bg club_day
    show raiden at face
    with open_eyes
    mc "Uwaa--!"
    "I open my eyes to find raiden's face filling my vision."
    "I nearly fall out of my chair."
    show raiden zorder 2 at t11
    s "Ehehe, sorry~"
    s "Wait!"
    s "Actually, I'm not sorry at all!"
    s "It's your fault for sleeping like that!"
    s "This isn't the napping club!"
    mc "Does our school have a napping club...?"
    s "You're staying up late again, aren't you?"
    s "Now that you're in a club, you're gonna have less time for anime, you know!"
    s "You'll need to get used to it!"
    mc "Don't say that so loud...!"
    "I glance over my shoulder to see if Armstrong overheard."
    s "It's true, though..."
    mc "Yeah..."
    mc "I know, I know."
    mc "You're always looking out for me, raiden."
    s "Ehehe~"
    s "It's what I do best!"
    mc "...That's a problem!"
    mc "What about you?"
    mc "You look out for me better than you look out for yourself."
    mc "You're still oversleeping every day, aren't you?"
    s "Eh?"
    s "N-Not every day!"
    mc "That's not very convincing..."
    mc "How many days this past week have you gotten up on time?"
    s "That's..."
    s "...It's a secret!"
    mc "I knew it..."
    s "C'monnnn!"
    s "At least give me the benefit of the doubt..."
    mc "I can't even do that."
    mc "Look, raiden, it's written all over you."
    s "Eh...?"
    "raiden glances around at herself."
    s "How is it written all over me?"
    mc "You were clearly in a rush this morning..."
    mc "Look, your hair is sticking out all around here."
    show raiden at h11
    s "Ah--"
    "I run my fingertips down the side of raiden's hair, trying to straighten it out."
    mc "Man, you really need a brush for this..."
    s "My hair is just really hard to get right..."
    mc "I won't fall for that."
    mc "There's more than just your hair."
    mc "Look, your bow isn't straight, either."
    mc "And there's a toothpaste stain on your collar right here."
    "I try to wipe off the stain with my finger."
    show raiden at s11
    s "B-But nobody would ever notice that..."
    mc "Of course they would."
    mc "Nobody's gonna tell you about it because they don't want to embarrass you."
    mc "Fortunately, I really don't care about that."
    s "Hey, you meanie..."
    mc "And you don't even keep your blazer buttoned up."
    mc "Seriously, raiden..."
    mc "Why do you think you don't have a boyfriend yet?"
    show raiden zorder 2 at t11
    s "Eh??"
    s "That's {i}super{/i} mean!"
    mc "Sorry, but you'll thank me later..."
    "I start to button her blazer from the bottom."
    mc "Once you see how much better it looks, you'll change your mind."
    $ persistent.clear[6] = True
    $ renpy.save_persistent()
    scene s_cg1
    with dissolve_cg
    s "Ehehe~"
    s "This is so funny."
    mc "What is?"
    s "Well..."
    s "I was just thinking how weird it is to have a friend who does these kinds of things."
    mc "Eh?"
    mc "D-Don't say that!"
    mc "You'll make {i}me{/i} feel weird about it, stupid..."
    s "It's okay, though."
    s "I'm happy we're like this."
    s "Aren't you?"
    mc "Ah--"
    mc "I-I guess..."
    s "Hey, be careful..."
    s "The button might come off!"
    mc "Why is this one so hard to close...?"
    "I struggle to fully close the button near her chest."
    mc "Does this thing even fit you properly?"
    s "Ehehe~"
    s "It did when I bought it."
    mc "Sigh..."
    mc "If you ever buttoned it, you would have noticed sooner that it doesn't fit you anymore."
    mc "What are you smiling about?"
    s "It means my boobs got bigger again!"
    mc "D-Don't say that out loud!!"
    s "Ehehe~"
    mc "Anyway..."
    mc "You look much better now, so..."
    mc "Ah..."
    "...Why does it feel strange to see raiden's blazer buttoned up like that?"
    s "But it's so stuffy..."
    s "Uuu..."
    s "It's not worth it at all!"
    "raiden hastily unbuttons her blazer once more."
    scene bg club_day
    show raiden zorder 2 at i11
    with dissolve_cg
    s "Phew!"
    s "That's so much better~"
    "raiden puts her arms out and twirls around."
    s "So if I keep it unbuttoned then I won't get a boyfriend, right?"
    mc "What kind of logic is that?"
    mc "And why are you saying that like it's a good thing?"
    s "Because..."
    s "...If I had a boyfriend, then he wouldn't even let you do things like this!"
    s "And you take care of me better than anyone else would, anyway..."
    s "So that's why I'm keeping it unbuttoned!"
    mc "Stop saying all these embarrassing things!"
    s "Eh?"
    s "I didn't say anything embarrassing..."
    mc "Jeez..."
    mc "Well anyway, just focus on trying to wake up a little earlier..."
    s "Only if you focus on going to bed earlier!"
    mc "Fine, fine..."
    mc "It's a deal."
    s "Ehehe~"
    s "I guess we really are better at taking care of each other than we are at taking care of ourselves."
    mc "Yeah, I guess so, huh..."
    s "So maybe you should come wake me up in the morning!"
    mc "You're doing it again, raiden..."
    s "Aw, but I was joking that time!"
    mc "Man, it's impossible to tell with you sometimes."
    show armstrong behind raiden at l31
    m "Okay, everyone!"
    mc "Eh?"
    "Armstrong suddenly calls out."
    m "Why don't we share the poems we wrote now?"
    show raiden at h11
    s "Yay~!"
    s "[player], I can't wait to read yours!"
    mc "Yeah, same..."
    "I fail to sound enthusiastic, but raiden still trots away to retrieve her poem."
    show raiden behind armstrong at thide
    return

label sayori_exclusive_2:
    if not renpy.music.get_playing(channel='music') == audio.t2:
        stop music fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    if not renpy.music.get_playing(channel='music') == audio.t2:
        play music t2
    s "[player], [player]!"
    "raiden suddenly comes up to me."
    show raiden zorder 2 at t11
    s "I'm gonna go get some supplies from another classroom."
    s "Want to come with me?"
    mc "Supplies?"
    mc "What for?"
    s "Well, you know how the festival is coming up?"
    s "Me and Armstrong were gonna make some posters and stuff."
    s "So I need to go find some crayons, and markers, and glue sticks..."
    mc "Ah, I see."
    mc "Sure, I'll go with you."
    s "Yaay~"
    s "Okay Armstrong, we'll be back soon!"
    show raiden zorder 2 at t22
    show armstrong zorder 3 at f21
    m "Ah, are you going with [player] to get the supplies?"
    m "There's no need to trouble yourself."
    m "I'd be happy to go with him."
    show armstrong zorder 2 at t21
    show raiden at s22
    s "Aw, but I wanted to go!"
    s "It's so much fun exploring empty classrooms and stuff!"
    show armstrong zorder 3 at f21
    m "Hehe, okay, okay."
    m "It was just a suggestion."
    m "See if you can find poster paper too, okay?"
    show armstrong zorder 2 at t21
    show raiden zorder 3 at f22
    s "Okaay~!"
    s "Ready, [player]?"
    mc "Yep, let's go."
    scene bg corridor
    show raiden zorder 2 at t11
    with wipeleft_scene
    "raiden and I exit the clubroom."
    "I follow behind as raiden hums and skips around the hallway."
    "Honestly..."
    "It feels like I'm taking a kid to the mall or something."
    "raiden finds pleasure in the simplest things sometimes."
    mc "Hey, raiden..."
    mc "What exactly are we doing for the festival, anyway?"
    mc "I'm not sure how you would make an event out of literature..."
    s "Ehehe!"
    s "Me and Armstrong have it all planned out!"
    s "Don't you worry~"
    mc "Is that so...?"
    s "Yup!"
    s "We're gonna do a poetry performance!"
    mc "A performance...?"
    mc "Of what kind?"
    s "Well..."
    s "Everyone is gonna take turns on stage..."
    s "And recite their favorite poems!"
    mc "Ah..."
    mc "That sounds..."
    "...Kind of dull?"
    s "[player]!"
    s "You're not thinking about it the right way at all!"
    s "It's not just about reading poems..."
    s "It's about performing them!"
    s "Like, you say the lines of the poem like..."
    s "{i}Between my feet...{/i}"
    s "{i}The last remaining flower beckons to me.{/i}"
    s "{i}I twist the stem, freeing it from its clinging roots...{/i}"
    s "{i}Caressing the final joyous moment between my fingers.{/i}"
    s "{i}But to what ends have I summoned this joy?{/i}"
    s "{i}For now when I look in every direction...{/i}"
    s "{i}The once-prosperous field before me...{/i}"
    show raiden at h11
    s "{i}Is but a barren wasteland!{/i}"
    s "..."
    s "Like that!!"
    mc "raiden..."
    "How do I put this..."
    mc "I'm sure it's just me, but it's impossible for me to take you seriously when you talk like that..."
    show raiden at s11
    s "Ehhh?"
    s "You meanie!"
    s "I'm working super hard on this, you know!"
    mc "Ah, I know, I know!"
    mc "I just meant that it's a pretty unordinary contrast to your cute self."
    show raiden zorder 2 at t11
    s "Ahaha! Don't say that, it's embarrassing!"
    s "But I guess that means I'm doing a good job~"
    mc "Yeah, I guess so..."
    show raiden at h11
    s "Aaah, I'm so excited!"
    s "The festival is going to be so much fun~"
    "raiden spins herself around in the hallway again."
    s "Hey, [player], this classroom over here is empty!"
    s "Let's begin the mission!"
    show raiden zorder 1 at thide
    hide raiden
    mc "The mission, eh...?"
    "It's been a long time since I've spent time with raiden like this."
    "But in the end, she hasn't changed one bit."
    "She's nothing but a ball of sunshine, drawing happy vibes from the world around her."
    "It's a pretty nostalgic feeling for me."
    "As the years went by, I began to hole myself up in my room more and more."
    "So going adventuring with raiden brings about a special sort of feeling I forgot I had in me."
    scene bg class_day
    with wipeleft_scene
    "The two of us enter the classroom."
    "raiden heads straight to the closet, and I follow."
    show raiden zorder 2 at t11
    s "Let's see what we have in here..."
    s "...Crayons!!"
    "raiden pulls a box full of crayons off the shelf."
    s "They're the best brand, too!"
    s "They're kind of dirty, though..."
    "raiden starts pulling various crayons out of the box, reading the color names."
    mc "Alright, that's one down."
    mc "Don't get distracted, we still need to find--"
    s "Wait, I'm looking for my favorite color..."
    mc "Fine, fine..."
    mc "Then at least move aside so I can look for the poster paper."
    s "Ah, I dropped one by accident--"
    play sound "sfx/smack.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    show raiden at h11
    "{i}Smack!{/i}"
    hide white
    s "Kya--!"
    "raiden bends over and smacks her forehead right into the shelf."
    "She falls to the floor, and the crayons spill all over her lap."
    show raiden at s11
    s "Owowowowow..."
    mc "You okay?"
    s "My forehead..."
    "raiden clutches her forehead."
    mc "Jeez, raiden..."
    mc "That's just like you, isn't it?"
    mc "C'mon, let me see."
    "Since raiden is sitting on the floor, I grab her by the waist and pull her out of the closet."
    mc "You have to move your hands, raiden..."
    s "But it hurts..."
    mc "Just do it for a second."
    $ persistent.clear[7] = True
    $ renpy.save_persistent()
    scene s_cg2_base1
    show s_cg2_exp2
    with dissolve_cg
    "raiden slowly releases her hands from her forehead."
    "I gently brush her bangs to the side."
    show s_cg2_exp1 at cgfade
    show s_cg2_exp3 at cgfade
    s "Ow--!"
    mc "Sorry..."
    "There's a huge red mark on the center of her forehead."
    "A bump is starting to form, as well."
    mc "Man, that's gonna swell up."
    mc "I should find you some ice..."
    hide s_cg2_exp3
    hide s_cg2_exp1
    s "[player]..."
    mc "Where would I even find ice around this time...?"
    mc "Ah, I guess a cold drink would do..."
    s "You don't have to--!"
    show s_cg2_exp2 at cgfade
    hide s_cg2_exp2
    s "I'm fine with--looking like a unicorn--"
    "Even wincing from the pain, raiden makes a silly joke."
    mc "Ahaha, what are you saying?"
    mc "I'll be right back, okay?"
    s "O-Okay..."
    stop music fadeout 1.0
    scene bg corridor with wipeleft_scene
    "I pat raiden on the shoulder and run out into the hallway."
    "I locate the nearest vending machine."
    mc "What should I get...?"
    "It doesn't really matter, since it will be used as an ice pack, rather than to drink."
    "But I know raiden likes apple juice, so I purchase that one."
    "In just a moment, I'm already returning to the classroom where I left raiden."
    scene s_cg2_base1
    show s_cg2_exp2
    with wipeleft_scene
    play music t9
    "She has one palm on her forehead and is using the other hand to clumsily scoop crayons back into the box."
    s "At least they were already in the wrong spots before I spilled them..."
    mc "raiden, here."
    show s_cg2_base2 behind s_cg2_exp2 at cgfade
    "I hand raiden the bottle of apple juice."
    show s_cg2_exp2 at cgfade
    hide s_cg2_exp2
    s "It's nice and cold..."
    "raiden opens the cap and starts drinking from it."
    mc "raiden, what are you doing?!"
    mc "It's for your forehead, idiot!"
    show s_cg2_exp3 at cgfade
    s "Ah--"
    s "Sorry, I forgot~"
    s "Ahahaha!"
    mc "How hard did you hit your head...?"
    "raiden places the bottle against the bump on her head."
    show s_cg2_exp1 at cgfade
    s "It stings..."
    mc "Just bear with it, it'll feel better soon."
    mc "Looks like you cleaned up most of the crayons, so that's good."
    hide s_cg2_exp1
    hide s_cg2_exp3
    s "Hey, [player]..."
    s "This kind of reminds you of growing up, doesn't it...?"
    mc "Eh? What do you mean?"
    s "You know how we used to play outside all the time..."
    s "I would always try to keep up with you."
    s "You were kind of oblivious in some ways..."
    s "Like I usually fell behind or had trouble climbing on the things you did..."
    s "But sometimes when I tried to do things I couldn't, I would get myself hurt."
    s "I'd fall and scrape myself, or get a bump..."
    s "And I would start crying really hard."
    show s_cg2_exp3 at cgfade
    s "Ahaha!"
    s "And you would rush over as quick as you could."
    hide s_cg2_exp3
    s "You would try really hard to get me to stop crying."
    s "It was almost like you blamed yourself and were afraid of getting in trouble if someone found out..."
    s "Even though it really wasn't your fault at all, you know?"
    mc "Did I really do that...?"
    s "Yeah...you don't remember?"
    mc "Come to think of it, maybe I do remember a bit..."
    mc "I guess I was always so focused on my games that I didn't pay enough attention to you."
    mc "So in a way, it was my fault."
    mc "Kind of like this time, too..."
    mc "If I wasn't rushing you out of the closet, you probably wouldn't have hit your head."
    s "[player]..."
    s "I don't think you realize it, but you're always thinking about other people."
    s "Even after all these years..."
    s "You're rushing to help me, even though I'm just being clumsy."
    show s_cg2_exp3 at cgfade
    s "You're really a sweetheart..."
    mc "D-Don't call me that!"
    mc "And I don't really do this kind of thing all the time..."
    mc "I guess when it comes to you, it just feels natural."
    mc "Before I even know it, I'm treating you like that."
    mc "I guess that's what happens when you've been friends for so long."
    hide s_cg2_exp3
    s "Really...?"
    s "Maybe you're right..."
    s "[player]..."
    s "I'm so glad that nothing's changed between us."
    s "Do you think it'll be like this forever?"
    mc "Forever...?"
    "If I'm honest to myself..."
    "There's no telling where we'll each end up for college, or after that."
    "So it wouldn't be fair for me to make any promises."
    "But..."
    mc "Well, I hope so."
    mc "It's been this long already, right?"
    mc "I can't imagine you ever changing, so my hopes are up."
    s "I'm so happy..."
    "raiden has a whimsical expression in her eyes."
    "We remain silent for a moment."
    "She's so silly and clumsy on the outside that when I see her deep in thought like this..."
    "It makes me not want to disturb her."
    s "I guess we should go back..."
    s "I don't want to worry Armstrong, you know?"
    mc "Good luck with that."
    mc "She's gonna see your forehead either way."
    s "Not if I hide it under my bangs~"
    play music t8 fadeout 1.0
    scene bg class_day
    show raiden zorder 2 at i11
    with dissolve_cg
    "raiden hops to her feet."
    show raiden at s11
    s "A-Aaahh--!"
    "She clutches her forehead again."
    mc "Don't stand up so fast after hurting yourself!"
    s "Uuuu..."
    mc "Well, I guess it's too late now..."
    mc "Anyway, let's go."
    scene bg corridor
    with wipeleft_scene
    "I follow raiden out of the classroom."
    "raiden plays with her bangs to try to hide the bump, but without much success."
    "In a moment, we make it back to the clubroom."
    scene bg club_day
    show raiden zorder 2 at t21
    show armstrong zorder 2 at t22
    with wipeleft_scene
    show armstrong zorder 3 at f22
    m "Ah, you're back!"
    m "Good timing, I was just about ready to start with sharing our poems."
    m "Eh? raiden, your forehead..."
    show armstrong zorder 2 at t22
    mc "She's fine, don't worry about--"
    show raiden zorder 3 at f21
    s "I was playing with the crayons and smacked my forehead into the shelf!"
    show raiden zorder 2 at t21
    mc "..."
    show armstrong zorder 3 at f22
    m "..."
    m "...Well, anyway!"
    m "Were you able to find everything we needed?"
    show armstrong zorder 2 at t22
    show raiden zorder 3 at f21
    s "Uh-huh! I have it right--"
    s "...Eh?"
    "raiden frantically glances around herself."
    show raiden zorder 3 at hf21
    s "I...forgot all of the stuff!!"
    show raiden zorder 2 at t21
    mc "Calm down, raiden."
    mc "I have it all right here."
    mc "I found the poster paper, too."
    show raiden
    show armstrong zorder 3 at f22
    m "Ahaha!"
    m "Sounds like you ended up doing all the work, [player]."
    show armstrong zorder 2 at t22
    mc "Ah, well, raiden--"
    "I fail to come up with an excuse for raiden."
    show raiden zorder 3 at f21
    s "I made it an adventure!"
    show raiden zorder 2 at t21
    mc "...Yeah, that."
    show armstrong zorder 3 at f22
    m "Ahaha, okay, okay."
    m "In any case, good work!"
    m "I'll start working on the posters tonight."
    show armstrong zorder 2 at t22
    show raiden zorder 3 at f21
    s "Me too!"
    show armstrong zorder 2 at t11
    show raiden behind armstrong at thide
    hide raiden
    m "...Okay, everyone!"
    m "Are you ready to share your poems?"
    mc "Guess I should grab mine..."
    "After making sure the crayon box is closed tightly, I return to my seat."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
