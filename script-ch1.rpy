

label ch1_main:
    scene bg club_day
    with dissolve_scene_half
    play music t2
    show armstrong zorder 2 at t11

    m "Hi again, [player]!"
    m "Glad to see you didn't run away on us. Hahaha!"
    mc "Nah, don't worry."
    mc "This might be a little strange for me, but I at least keep my word."
    show armstrong zorder 1 at thide
    hide armstrong
    "Well, I'm back at the Literature Club."
    "I was the last to come in, so everyone else is already hanging out."
    show sam zorder 2 at t32
    y "Thanks for keeping your promise, [player]."
    y "I hope this isn't too overwhelming of a commitment for you."
    y "Making you dive headfirst into literature when you're not accustomed to it..."
    show bladewolf zorder 2 at t33
    n "Oh, come on! Like he deserves any slack."
    n "raiden told me you didn't even want to join any clubs this year."
    n "And last year, too!"
    n "I don't know if you plan to just come here and hang out, or what..."
    n "But if you don't take us seriously, then you won't see the end of it."
    show armstrong at l41
    m "Bladewolf, you certainly have a big mouth for someone who keeps her manga collection in the clubroom."
    n "M-M-M...!!"
    show armstrong at lhide
    hide armstrong
    "Bladewolf finds herself stuck between saying \"Armstrong\" and \"Manga\"."
    show bladewolf at h33
    n "Manga is literature!!"
    show bladewolf zorder 1 at thide
    hide bladewolf
    "Swiftly defeated, Bladewolf plops back into her seat."
    show sam zorder 2 at t22
    show raiden zorder 3 at f21
    s "Don't worry, guys~"
    s "[player] always gives it his best as long as he's having fun."
    s "He helps me with busywork without me even asking."
    s "Like cooking, cleaning my room..."
    show raiden zorder 2 at t21
    show sam zorder 3 at f22
    y "How dependable..."
    show sam zorder 2 at t22
    mc "raiden, that's because your room is so messy it's distracting."
    mc "And you almost set your house on fire once."
    show raiden at s21
    s "Is that so... Ehehe..."
    show sam zorder 3 at f22
    y "You two are really good friends, aren't you?"
    y "I might be a little jealous..."
    show sam zorder 2 at t22
    show raiden zorder 3 at f21
    s "How come? You and [player] can become good friends too!"
    show raiden zorder 2 at t21
    show sam zorder 3 at f22
    y "U-Um..."
    show sam zorder 2 at t22
    mc "S-raiden--"
    show raiden zorder 3 at f21
    s "Hmm?"
    show raiden zorder 2 at t21
    mc "..."
    "As usual, raiden seems oblivious to the weird situation she just put me into."
    show raiden zorder 3 at f21
    s "Oh, oh! Sam even brought you something today, you know~"
    show raiden zorder 2 at t21
    show sam zorder 3 at f22
    y "W-Wait! raiden..."
    show sam zorder 2 at t22
    mc "Eh? Me?"
    show sam zorder 3 at f22
    y "Um... Not really..."
    show sam zorder 2 at t22
    show raiden zorder 3 at f21
    s "Don't be shy~"
    show raiden zorder 2 at t21
    show sam zorder 3 at f22
    y "It's really nothing..."
    show sam zorder 2 at t22
    mc "What is it?"
    show sam zorder 3 at f22
    y "N-Never mind!"
    y "raiden made it sound like a big deal when it's really not..."
    y "Uuuuh, what do I do..."
    show sam zorder 2 at t22
    show raiden zorder 3 at f21
    s "Eh? I'm sorry, Sam, I wasn't thinking..."
    show raiden zorder 1 at thide
    hide raiden
    show sam zorder 2 at t11
    "I guess that means it's up to me to rescue this situation..."
    mc "Hey, don't worry about it."
    mc "First of all, I wasn't expecting anything in the first place."
    mc "So any nice gesture from you is a pleasant surprise."
    mc "It'll make me happy no matter what."
    y "I-Is that so..."
    mc "Yeah. I won't make it a big deal if you don't want it to be."
    y "Alright..."
    y "Well, here."
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


    "Now that everyone's settled in, I expected Armstrong to kick off some scheduled activities for the club."
    "But that doesn't seem to be the case."
    "raiden and Armstrong are having a cheery conversation in the corner."
    "Sam's face is already buried in a book."
    "I can't help but notice her intense expression, like she was waiting for this chance."
    "Meanwhile, Bladewolf is rummaging around in the closet."


    $ nextscene = poemwinner[0] + "_exclusive_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene


    show armstrong zorder 2 at t21
    hide raiden
    hide bladewolf
    hide sam
    m "By the way, did you remember to write a poem last night?"
    mc "Y-Yeah..."
    "My relaxation ends."
    "I can't believe I agreed to do something so embarrassing."
    "I couldn't really find much inspiration, since I've never really done this before."
    m "Well, now that everyone's ready, why don't you find someone to share with?"
    show raiden zorder 2 at t22
    s "I can't wait~!"
    show raiden zorder 1 at thide
    show armstrong zorder 1 at thide
    hide raiden
    hide armstrong
    "raiden and Armstrong enthusiastically pull out their poems."
    "raiden's is on a wrinkled sheet of loose leaf torn from a spiral notebook."
    "On the other hand, Armstrong wrote hers in a composition notebook."
    "I can already see Armstrong's pristine handwriting from where I sit."
    "Bladewolf and Sam reluctantly comply as well, reaching into their bags."
    "I do the same, myself."

    return


label ch1_end:
    stop music fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    play music t3
    mc "Phew..."
    "I guess that's everyone."
    "I glance around the room."
    "That was a little more stressful than I anticipated."
    "It's as if everyone is judging me for my mediocre writing abilities..."
    "Even if they're just being nice, there's no way my poems can stand up to theirs."
    "This is a literature club, after all."
    "I sigh."
    "I guess that's what I ended up getting myself into."
    "Across the room, raiden and Armstrong are happily chatting."
    "My eyes land on Sam and Bladewolf."
    show sam zorder 2 at t21
    show bladewolf zorder 2 at t22
    "They gingerly exchange sheets of paper, sharing their respective poems."
    show sam at t21
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
    n "raiden liked it."
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
    play music t7
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
    show raiden behind sam, bladewolf at l41
    show sam zorder 2 at t32
    show bladewolf zorder 2 at t33
    s "U-Um!!"
    s "Is everyone okay...?"
    show raiden at lhide
    hide raiden
    show bladewolf zorder 3 at f33
    n "Well, you know what?!"
    n "I wasn't the one whose boobs magically grew a size bigger as soon as [player] started showing up!!"
    show sam at h32
    show bladewolf zorder 2 at t33
    y "N-Bladewolf!!"
    show armstrong behind sam, bladewolf at l41
    m "Um, Bladewolf, that's a little--"
    show armstrong at h41
    show sam zorder 3 at f32
    show bladewolf zorder 3 at f33
    ny "This doesn't involve you!"
    show armstrong at lhide
    hide armstrong
    show sam zorder 2 at t32
    show bladewolf zorder 2 at t33
    show raiden behind sam, bladewolf at l41
    s "I-I don't like fighting, guys...!"
    show raiden at lhide
    hide raiden
    show sam zorder 2 at t21
    show bladewolf zorder 2 at t22
    "Suddenly, both girls turn towards me, as if they just noticed I was standing there."
    show sam zorder 3 at f21
    y "[player]...!"
    y "She-- She's just trying to make me look bad...!"
    show sam zorder 2 at t21
    show bladewolf zorder 3 at f22
    n "That's not true!"
    n "She started it!"
    n "If she could get over herself and learn to appreciate that {i}simple{/i} writing is more effective..."
    n "Then this wouldn't have happened in the first place!"
    n "What's the point in making your poems all convoluted for no reason?"
    n "The meaning should jump out at the reader, not force them to have to figure it out."
    n "Help me explain that to her, [player]!"
    show bladewolf zorder 2 at t22
    show sam zorder 3 at f21
    y "W-Wait!"
    y "There's a reason we have so many deep and expressive words in our language!"
    y "It's the only way to convey complex feelings and meaning the most effectively."
    y "Avoiding them is not only unnecessarily limiting yourself...it's also a waste!"
    y "You understand that, right, [player]?"
    show sam zorder 2 at t21
    mc "Um...!"
    show sam zorder 3 at f21
    show bladewolf zorder 3 at f22
    ny "Well??"
    mc "..."
    show sam zorder 2 at t21
    show bladewolf zorder 2 at t22
    "How did I get dragged into this in the first place?!"
    "It's not like I know anything about writing..."
    "But whomever I agree with, they'll probably think more highly of me!"
    menu:
        "So, of course that's going to be...!"
        "Bladewolf.":
            call ch1_end_bladewolf
        "Sam.":
            call ch1_end_sam
        "Help me, raiden!!":
            call ch1_end_raiden

    scene bg club_day
    show armstrong zorder 2 at t11
    with wipeleft_scene
    m "Okay, everyone!"
    m "It's just about time for us to leave."
    m "How did you all feel about sharing poems?"
    show armstrong
    show raiden zorder 2 at t31
    s "It was a lot of fun!"
    show raiden behind sam at thide
    show sam zorder 2 at t31
    hide raiden
    y "Well, I'd say it was worth it."
    show sam behind bladewolf at thide
    show bladewolf zorder 2 at t31
    hide sam
    n "It was alright. Well, mostly."
    show bladewolf zorder 1 at thide
    hide bladewolf
    m "[player], how about you?"
    mc "...Yeah, I'd say the same."
    mc "It was a neat thing to talk about with everyone."
    m "Awesome!"
    m "In that case, we'll do the same thing tomorrow."
    m "And maybe you learned something from your friends, too."
    m "So your poems will turn out even better!"
    mc "..."
    show armstrong zorder 1 at thide
    hide armstrong
    "I think to myself."
    "I did learn a little more about the kinds of poems everyone likes."
    "With any luck, that means I can at least do a better job impressing those I want to impress."
    "I nod to myself with newfound determination."
    show raiden zorder 2 at t11
    s "[player]!"
    s "Ready to walk home?"
    mc "Sure, let's go."
    s "Ehehe~"
    "raiden beams at me."
    "It truly has been a while since raiden and I have spent this much time together."
    "I can't really say I'm not enjoying it, either."
    scene bg residential_day
    show raiden zorder 2 at t11
    with wipeleft_scene
    mc "raiden..."
    mc "About what happened earlier..."
    s "Eh? What do you mean?"
    mc "You know, between Sam and Bladewolf."
    mc "Does that kind of thing happen often?"
    s "No, no, no!"
    s "That's really the first time I've seen them fight like that..."
    s "I promise they're both wonderful people."
    show raiden at s11
    s "You don't... You don't hate them, do you??"
    mc "No, I don't hate them!"
    mc "I just wanted your opinion, that's all."
    mc "I can see why they'd make good friends with you."
    show raiden zorder 2 at t11
    s "Phew..."
    s "You know, [player]..."
    s "It's nice that I get to spend time with you in the club."
    s "But I think seeing you get along with everyone is what makes me the happiest."
    s "And I think everyone really likes you, too!"
    mc "That's--!"
    s "Ehehe~"
    s "Every day is going to be so much fun~"
    mc "Sigh..."
    "It looks like raiden still hasn't caught onto the kind of situation I'm in."
    "Sure, being friends with everyone is nice, but..."
    "...Does it really need to stop there?"
    mc "We'll just have to see what the future holds, raiden."
    "I pat raiden on the shoulder."
    "I said that more to myself than to her, but it's easy to use raiden as an internal monologue sometimes."
    show raiden at h11
    s "Okay~!"
    "Yeah..."
    "Let's do this!"
    return

label ch1_end_bladewolf:
    $ ch1_choice = "natsuki"
    stop music fadeout 1.0
    mc "Um..."
    mc "Sam!"
    mc "You're really talented."
    show samat s21
    y "Eh? W-Well..."
    play music t8
    mc "But Bladewolf has a point!"
    mc "I think that..."
    show sam zorder 2 at t21
    "I wrack my brain in an attempt to back myself up."
    mc "I think that conveying feelings with few words..."
    mc "Can be just as impressive as well!"
    mc "It lets the reader's imagination take over."
    mc "And Bladewolf's poem did a really good job at that!"
    show bladewolf zorder 3 at f22
    n "...Yeah!!"
    n "It did, didn't it?!"
    n "Ahah!"
    n "Shows how much {i}you{/i} know!"
    show bladewolf zorder 2 at t22
    show sam zorder 3 at f21
    y "T-That's not..."
    show sam zorder 2 at t21
    mc "Bladewolf..."
    mc "I think that's enough."
    show bladewolf zorder 3 at f22
    n "Huh?"
    n "Me?"
    n "But she was so mean to me...!"
    "Bladewolf's voice whines."
    show bladewolf zorder 2 at t22
    mc "Look..."
    mc "What we talked about yesterday was right."
    mc "Writing is a really personal thing."
    mc "And sharing it can definitely be hard."
    mc "It looks like we learned that today."
    mc "Even small criticism can lead to something pretty heated."
    "I glance over my shoulder."
    "raiden is nodding vigorously."
    mc "Yeah, so..."
    mc "You don't need to feel threatened."
    mc "You're a great writer, Bladewolf."
    show bladewolf zorder 3 at f22
    n "Ah--"
    "Bladewolf's voice gets caught in surprise."
    n"...Thanks for noticing."
    "She finally mutters that, barely audible."
    show bladewolf zorder 2 at t22
    mc "Sam..."
    show sam zorder 3 at f21
    y "...?"
    "Sam looks at me dejectedly."
    "With a face like that, I can't help but feel bad for her as well."
    show sam zorder 2 at t21
    mc "I'm sure that Bladewolf didn't mean everything she said."
    mc "So you don't need to feel threatened, either."
    show sam zorder 3 at f21
    y "Well..."
    y "If you say so..."
    show sam zorder 2 at t21
    show bladewolf zorder 3 at f22
    n "Hey...!"
    n "It's not like you need to apologize {i}for{/i} me, [player]."
    n "Sheesh."
    "Bladewolf takes a breath."
    n "I..."
    n "The thing about..."
    n "Uu..."
    "Bladewolf glances around the room."
    show bladewolf zorder 3 at hf22
    n"{i}Would everyone stop staring at me??{/i}"
    "Unsurprisingly, Bladewolf has a harder time with it than she boasted."
    "raiden and Armstrong look away."
    show bladewolf zorder 3 at f22
    n "Hmph."
    n "Anyway...!"
    n "The thing about your boobs. I didn't mean it, okay?"
    n "That's all."
    "Bladewolf looks away, avoiding eye contact with anyone."
    show bladewolf zorder 2 at t22
    show raiden behind sam at l41
    s "Yeah! You're naturally beautiful, Sam!!"
    mc "raiden?!"
    show sam zorder 3 at f21
    y "..."
    y "I-I'll go make some tea..."
    show sam at lhide
    hide sam
    show raiden zorder 3 at f41
    s "Ehh?"
    s "I was just trying to help!"
    show raiden zorder 2 at t41
    mc "I'm sure she appreciated it, raiden."
    "I pat raiden on the shoulder."
    show raiden zorder 1 at thide
    show bladewolf zorder 1 at thide
    show armstrongzorder 2 at t11
    hide raiden
    hide bladewolf
    m "Well, now that we're past that..."
    m "Everyone's read each other's poems, right?"
    m "I hope that it was worthwhile for everyone!"
    m "Especially you, [player]!"
    m "And to be honest..."
    m "It's a nice change of pace from the lazing around we got a little too used to."
    m "Ahahaha!"
    mc "Ah, so my joining the club was responsible for ruining the atmosphere..."
    m "No, not at all, not at all!"
    m "There's still time before we go home."
    m "So we'll all relax for a bit."
    m "Of course, besides chatting, we do literature-related things in the clubroom..."
    m "So maybe you can take the chance to pick up a book, or do some writing."
    m "After all, that's what the club is for!"
    show raidenzorder 3 at f31
    s "I disagree, Armstrong!"
    show raiden zorder 2 at t31
    show armstrong zorder 3 at f32
    m "Eh? About what?"
    show armstrong zorder 2 at t32
    show raiden zorder 3 at f31
    s "That's not the most important thing about the literature club!"
    s "The most important thing..."
    show raidenzorder 3 at hf31
    s "Is having fun!"
    show raiden zorder 2 at t31
    show armstrong zorder 3 at f32
    m "Ahaha, of course..."
    m "Well, I guess that's why you're the Vice President, raiden."
    show armstrong zorder 2 at t32
    show raiden zorder 3 at f31
    s "Ehehe..."
    hide raiden
    hide armstrong
    with wipeleft
    "In the end, though, Armstrong's right."
    "Being in the Literature Club probably means I can't spend all my time doing nothing."
    "But in the end..."
    "...I guess it's been worth it so far."
    return

label ch1_end_sam:
    $ ch1_choice = "yuri"
    stop music fadeout 1.0
    mc "Bladewolf."
    mc "You're right that I liked your poem."
    show bladewolf zorder 3 at f22
    n "See??"
    show bladewolfzorder 2 at t22
    play music t8
    mc "Wait!"
    mc "That's not an excuse for you to be so mean!"
    mc "You shouldn't pick a fight just because someone's opinion is different."
    show bladewolf zorder 3 at f22
    n "That's not what happened at all!"
    n "Sam wouldn't even take my poem seriously!"
    show bladewolf zorder 2 at t22
    mc "Mm..."
    mc "I understand."
    mc "Sam."
    show sam zorder 3 at f21
    y "Eh?"
    show sam zorder 2 at t21
    mc "You're a seriously talented writer."
    mc "It's no secret that I was impressed."
    show sam zorder 3 at f21
    y "W-Well, that's..."
    show sam zorder 2 at t21
    mc "But here's the thing."
    mc "No matter how simple or refined someone's writing style is..."
    mc "They're still putting feelings into it, and it becomes something really personal."
    mc "That's why Bladewolf felt threatened when you said her poem was cute."
    show sam zorder 3 at f21
    y "I...see..."
    y "I didn't notice that I..."
    show sam zorder 2 at t21
    y "I-I'm sorry..."
    show sam at s21
    y "Uuu..."
    show bladewolf zorder 2 at t11
    show sam zorder 1 at thide
    hide sam
    mc "But Bladewolf, you took it way too far!"
    mc "Sam means well, and if you just told her how you felt..."
    mc "Then this wouldn't have happened in the first place."
    n "Are you kidding?"
    n "That's exactly what I did!"
    n "It was {i}her{/i} that--"
    show bladewolf zorder 2 at t22
    show armstrongzorder 3 at f21
    m "Bladewolf, I think that's enough."
    m "You both said some things that you didn't mean."
    m "Sam apologized. Don't you think you should, too?"
    show armstrong zorder 2 at t21
    show bladewolf zorder 3 at f22
    n "Nnn...!"
    show bladewolf zorder 2 at t22
    "Bladewolf clenches her fists."
    "In the end, nobody has taken her side."
    "She's trapped, at this point being defiant only because she can't handle the pressure."
    "I end up even feeling bad for her."
    show armstrong zorder 2 at t32
    show bladewolf zorder 2 at t33
    show raidenat l41
    s "U-Um!"
    s "Sometimes when I'm hurt..."
    s "It helps to take a walk and clear my head!"
    show raiden zorder 2 at t41
    mc "raiden, she doesn't need to--"
    show bladewolf zorder 3 at f33
    n "You know what?"
    n "I'm going to do that."
    n "It'll spare me from having to look at all your faces right now."
    show bladewolf zorder 1 at thide
    hide bladewolf
    "Without warning, Bladewolf snatches her own poem up from the desk and storms out."
    "On her way out, she crumples up the poem with her hands and throws it in the trash."
    show raiden zorder 3 at f41
    s "Bladewolf..."
    show raiden zorder 2 at t41
    show armstrong zorder 3 at f32
    m "She really didn't need to do that..."
    show raiden zorder 1 at thide
    show armstrong zorder 1 at thide
    hide raiden
    hide armstrong
    "I look across the room."
    "Sam has her chin buried in her hands while she stares down at her desk."
    "I gingerly approach her and sit in an adjacent chair."
    show samzorder 2 at t11
    y "Sigh..."
    mc "Everything alright?"
    y "I'm so embarrassed..."
    y "I can't believe I acted like that."
    y "You probably hate me now..."
    mc "No--Sam!"
    mc "How could anyone not have gotten frustrated after being treated like that?"
    mc "You handled it as well as anyone could."
    mc "I don't think any less of you."
    y "Well..."
    y "...Alright, I believe you."
    y "Thanks, [player]. You're too kind."
    y "I'm thankful to have you a part of this club now."
    mc "Er-- It's nothing."
    y "One more thing..."
    y "Um, that one thing that Bladewolf said..."
    y "About...you know..."
    y "I would never do anything...so shameful..."
    y "So..."
    mc "...Eh?"
    mc "What thing did Bladewolf say?"
    y "--!"
    y "U-Um!"
    y "Well, never mind that..."
    y "I-I'm going to go make some tea..."
    mc "Ah, good idea."
    mc "Make enough for more than one person, okay?"
    y "Y-Yeah."
    return

label ch1_end_raiden:
    $ ch1_choice = "sayori"
    mc "N-Bladewolf..."
    show bladewolf
    "Bladewolf glares at me, drying up any words I had in my mouth."
    "So instead, I turn to Sam."
    mc "Sam..."
    y "..."
    "But Sam's expression is so defenseless that I can't bring myself to say anything to her."
    stop music fadeout 1.0
    mc "..."
    mc "...raiden!"
    show raiden behind sam at l31
    show sam zorder 2 at t32
    show bladewolf zorder 2 at t33
    s "Eh?!"
    mc "...Yeah!"
    mc "Everyone's fighting is making raiden uncomfortable."
    mc "How can the two of you keep fighting when you know you're making your friend feel like this?"
    show raiden zorder 3 at f31
    s"[player]..."
    show raiden zorder 2 at t31
    show bladewolf zorder 3 at f33
    n "Well... That's her problem! This isn't about her."
    show bladewolf zorder 2 at t33
    show sam zorder 3 at f32
    y "I-I agree..."
    y "It's unfair for others to interject their own feelings into our conflict."
    show sam zorder 2 at t32
    show bladewolf zorder 3 at f33
    n"Yeah, unless raiden wants to tell Sam what a stuck-up jerk she's being."
    show bladewolf zorder 2 at t33
    show sam zorder 3 at f32
    play music t7
    y "She would never...!"
    y "It's your immaturity that's made her upset in the first place!"
    show sam zorder 2 at t32
    show bladewolf zorder 3 at f33
    n "{i}Excuse{/i} me?"
    n "Are you listening to yourself?"
    n "This is exactly why..."
    n "Exactly why nobody likes--"
    show bladewolf zorder 2 at t33
    show raiden at h31
    stop music
    s "{i}Stop!!{/i}"
    show sam zorder 3 at f32
    show bladewolf zorder 3 at f33
    ny "--"
    show sam zorder 2 at t32
    show bladewolf zorder 2 at t33
    show raiden zorder 3 at f31
    play music t8
    s "Bladewolf! Sam!"
    s "You guys are my friends!"
    s "I-I just want everyone to get along and be happy!"
    s "My friends are wonderful people..."
    s "And I love them because of their differences!"
    s "Bladewolf's poems..."
    s "They're amazing because they give you so many feelings with just a few words!"
    s "And Sam's poems are amazing because they paint beautiful pictures in your head!"
    s "Everyone's so talented..."
    s "...So why are we fighting...?"
    show raiden zorder 2 at t31
    show bladewolf zorder 3 at f33
    n "Be-Because..."
    show bladewolf zorder 2 at t33
    show sam zorder 3 at f32
    y "Well..."
    show sam zorder 2 at t32
    show raiden zorder 3 at f31
    s "Also!"
    s "Bladewolf's cute and there's nothing wrong with that!"
    s "And Sam's boobs are the same as they always were!"
    show raiden at hf31
    s "Big and beautiful!!"
    show raiden zorder 2 at t31
    show bladewolf zorder 3 at f33
    n "..."
    show bladewolf zorder 2 at t33
    show sam zorder 3 at f32
    y "..."
    show sam zorder 2 at t32
    mc "raiden..."
    "raiden stands triumphantly."
    "Armstrong stands behind her with a bewildered expression."
    show sam at s32
    y "I'll...make some tea..."
    show sam behind raiden at lhide
    hide sam
    "Sam rushes off."
    show bladewolf zorder 1 at thide
    hide bladewolf
    "Bladewolf sits down with a blank expression on her face, staring at nothing."
    show raiden zorder 1 at thide
    show armstrong zorder 2 at t11
    hide raiden
    mc "So, this is why raiden is Vice President..."
    "I whisper to Armstrong."
    "She nods in return."
    m "To be honest..."
    m "I might come off as a good leader, and I can organize things..."
    m"But I'm not very good with people..."
    m "I couldn't even bring myself to interject."
    m "As President, that's kind of embarrassing of me."
    m "Ahaha..."
    mc "Nah..."
    mc "It's not like I can blame you."
    mc "I wasn't able to say anything, either."
    m "Well..."
    m "I guess that just means raiden is amazing in her own ways, isn't she?"
    mc "You could say that."
    mc "She might be an airhead, but sometimes it's weirdly suspicious that she knows exactly what she's doing."
    m "I see~"
    m "Take good care of her, okay?"
    m "I would hate to see her get herself hurt."
    mc "That makes two of us..."
    mc "You can count on me."
    "Armstrong smiles sweetly at me, causing my stomach to knot."
    "Such a genuine person really does make a good President, regardless of what she says."
    "If only I could get the chance to talk to her a little more..."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
