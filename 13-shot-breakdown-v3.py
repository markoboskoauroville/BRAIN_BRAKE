# THE BRAIN BRAKE, version three
# Shot breakdown, single source of truth for the camera work order and the animation brief.
# LA = live action, AN = animation only, CO = composite, live action inside animation.
# Setups: A grey backdrop mid shot walking and reacting, B seated eyeline for Coach Brain,
# C white void, still and to lens, D jump, high frame rate.

SHOTS = [
# scene 1, THE MYSTERY 0:00 - 0:14
("1.1","0:00-0:04","AN",None,"wide","Runner failing on open road, head rolling, legs collapsed, crowd thin and quiet. Road crew and barrow at far left edge. Gold key in the gutter foreground, one quarter second glint.","MANAN VO: For a hundred years we thought the answer was in the muscles.","Plant the key, the workers and the number 27. None of them may be emphasised."),
("1.2","0:04-0:07","AN",None,"wide","The same man explodes into a sprint. Speed lines, grit lifting, crowd rising.","","Diagonal, violent, energy left to right. Horizon low so he sits high."),
("1.3","0:07-0:11","CO","A","wide","Everything freezes. Manan walks into the stopped world from the right, magnifying glass raised to his eye.","","SETUP A. He walks slowly through frame looking left and right at nothing. Shoot thirty seconds of pure observing, no lines."),
("1.4","0:11-0:12","AN",None,"insert","Through the lens, a pressed footprint and a stopped watch on the tarmac.","","Crisp inside the circle, loose outside it."),
("1.5","0:12-0:14","CO","A","close up","Manan lowers the glass and turns to us. Question marks bloom. Title.","MANAN: Hold on. He had nothing left. So where did THAT come from?","SETUP A. To lens. Curious and amused, never presenting. Six takes minimum."),

# scene 2, THE OLD THEORY 0:14 - 0:30
("2.1","0:14-0:18","AN",None,"wide","Inside the leg as a working factory, gears, belts, crates, workers. Everything running.","MANAN VO: A. V. Hill, Nobel prize, 1923. Run hard, run out of oxygen, and the muscle stops.","Order and rhythm. Industrial but healthy."),
("2.2","0:18-0:21","AN",None,"medium","Crates stop arriving on the belt. One crate stencilled 27 sits alone.","","The supply failing, not the machine breaking."),
("2.3","0:21-0:24","AN",None,"medium","A worker straightens, wipes his brow, shrugs. Iron key hanging dusty on a nail behind him.","WORKER: That's it. We're done.","Resigned, not frightened. This is a shift ending."),
("2.4","0:24-0:27","AN",None,"wide","A colossal stamp descends over the whole factory. Case closed.","MANAN VO: Case closed. For a hundred years.","Weight and finality."),
("2.5","0:27-0:30","AN",None,"insert","The stamp face, and a fine crack running across it as the sprint replays inside the crack.","MANAN VO: Except it doesn't explain this.","The crack is the scene. Everything before it exists to make it land."),

# scene 3, THE FULL TANK 0:30 - 0:48
("3.1","0:30-0:33","CO","A","medium","Manan at the back of the factory, palm flat on a riveted door, head tilted, listening. Keyhole beside his hand with light behind it.","MANAN VO: When scientists tested athletes the moment they gave up...","SETUP A. Palm flat at chest height on a mark. Nothing is really there."),
("3.2","0:33-0:37","CO","A","wide","The door swings, warm light floods out over him.","","SETUP A. Silhouette from behind, then turning into the light."),
("3.3","0:37-0:43","AN",None,"wide","The hall of tanks receding, every gauge in the red, nearest tank stencilled 27.","MANAN VO: ...the muscles could still produce far more power than the athlete had just produced.","The reveal, and the first big lift. Discovery, not warning."),
("3.4","0:43-0:45","AN",None,"insert","One gauge, needle deep in the red.","","Establishes the instrument that governs the rest of the film."),
("3.5","0:45-0:48","CO","A","close up","Manan lit by the light, delighted rather than shocked.","MANAN: It was never empty. Something else closed that door.","SETUP A. To lens. The most important take of the day, shoot it many times and use the most unguarded."),

# scene 4, THE GATEKEEPER 0:48 - 1:14
("4.1","0:48-0:51","AN",None,"wide","Warm control room, monitors, a large chair beginning to turn.","","Welcoming, not clinical. Meeting somebody, not catching them."),
("4.2","0:51-0:54","AN",None,"medium","Coach Brain revealed, mug, headset, gold key glowing on the chain at his chest.","COACH BRAIN: You found me. Took you long enough.","Establish the key clearly. It is the object the whole film turns on."),
("4.3","0:54-0:58","CO","B","two shot","Manan and Coach Brain face each other, evenly matched in frame.","MANAN: You closed that door.","SETUP B. Tennis ball on a stand at seated height camera left. Shoot the line, then ten seconds of listening."),
("4.4","0:58-1:04","AN",None,"wide","The network lights, five readouts converging on one dial with a red arc and the number 27.","COACH BRAIN: Heart rate. Breath. Temperature. Water. Distance. I'm asking one question. Can we keep going safely?","One click per item as it connects, five evenly spaced."),
("4.5","1:04-1:08","AN",None,"insert","Two seconds of a phone dimming into low power mode, then back to the room.","MANAN VO: Like a phone at twenty percent. Not broken. Protecting itself.","Generic phone, no brand anywhere."),
("4.6","1:08-1:11","CO","B","two shot","Manan arrives at the idea. Coach Brain entirely unembarrassed.","MANAN: So the limit isn't my body. It's your judgement. / COACH BRAIN: My best judgement. I'm not trying to stop you. I'm trying to get you to the finish line.","SETUP B. He should sound like he is discovering it, not stating it."),
("4.7","1:11-1:14","AN",None,"insert","The dial alone, needle upright, lower third of frame clear for the subtitle.","SUBTITLE: Central Governor Theory, proposed by Prof. Tim Noakes, 1997. Scientists still debate how brain and muscle share the work.","Small, low, in and out in two seconds. This honesty is scored."),

# scene 5, THE TRICK 1:14 - 1:30
("5.1","1:14-1:18","AN",None,"wide","Laboratory, cyclist on a stationary bike facing a screen with his translucent ghost.","MANAN VO: So they let a cyclist race a recording of his own best ride.","Clean lab, not clinical."),
("5.2","1:18-1:21","AN",None,"insert","Researcher's hand turning a knurled dial, +2% on the monitor, lap counter 27, small gold key on her lanyard.","MANAN VO: Except they made the ghost two percent faster. And they didn't tell him.","Only lettering permitted anywhere, +2% and 27. One conspiratorial click."),
("5.3","1:21-1:26","AN",None,"wide","He chases, draws level, passes his own ghost, which dissolves behind him.","","Cut it like a race. The overlap as he comes through is the money frame."),
("5.4","1:26-1:28","AN",None,"close","The cyclist spent and astonished, confusion turning into a laugh.","MANAN VO: He beat his own maximum. Which means it was never his maximum.","His expression is the shot. Keep the laugh in the sound."),
("5.5","1:28-1:30","CO","B","close up","Manan to camera, thoroughly delighted, the door flashing behind him for four frames.","MANAN: Change what the brain believes, and the door opens.","SETUP B. The most cheerful line in the film. Do not let him be earnest."),

# scene 6, THE RELEASE 1:30 - 1:46
("6.1","1:30-1:33","AN",None,"close","Coach Brain runs the check, every reading green, and turns the gold key in the lock at the centre of the dial.","COACH BRAIN: All right. Everything's holding. Let's give him a little more.","The single most important gesture in the film. He chooses, he is not overpowered."),
("6.2","1:33-1:35","AN",None,"insert","The needle moves past the middle and stops well short of the red.","CAPTION: Never to one hundred.","The gap between needle and red is the moral architecture of the film. Protect it."),
("6.3","1:35-1:38","AN",None,"wide","Muscle fibres lighting in scattered clusters inside semi transparent legs, about half of them still dark.","MANAN VO: More fibres recruited. Notice, still not all of them.","Light in sequence, never all at once, and never all."),
("6.4","1:38-1:41","AN",None,"wide","The runner flies, same road and same angle as shot 1.1, transformed.","MANAN VO: The brain didn't make new energy. It gave permission.","Rhyme 1.1 exactly. Same composition, opposite feeling."),
("6.5","1:41-1:44","AN",None,"montage","Traceur rooftop to rooftop, dancer turning in the air, swimmer off the wall. Each higher in frame than the last.","","Rapid and rising. Where the audience gets goosebumps."),
("6.6","1:44-1:46","CO","D","wide","Manan himself mid air, coat flying, laughing.","","SETUP D. Jumping on the spot against grey, arms out, laughing. High frame rate if the camera allows. Let him be silly."),

# scene 7, THE VERDICT 1:46 - 1:54
("7.1","1:46-1:48","AN",None,"wide","Everything drains to white.","","The stillness before the ending. Do not rush this."),
("7.2","1:48-1:51","AN",None,"wide","The Muscle and Coach Brain face each other with the brake hanging between them, then shake hands.","MANAN VO: Hill was right about the muscle. Noakes was right about the brain.","No winner. The handshake is the answer."),
("7.3","1:51-1:54","AN",None,"medium","Held on the handshake, the gauge steady between them.","MANAN VO: Today the evidence says both. And researchers are still working out exactly how. Great ideas aren't accepted because they sound convincing. They're accepted because scientists keep testing them.","The most credible seconds in the film."),

# scene 8, THE INVITATION 1:54 - 2:00
("8.1","1:54-1:56","CO","C","medium","Manan alone in the white, eyes closed, breathing, magnifying glass on the ground at his feet.","","SETUP C. Arms at his sides, eyes closed, simply breathing. Roll a full unbroken minute and use the stillest twenty frames. No performance at all."),
("8.2","1:56-1:58","CO","C","medium","The dial beside him, his own hand on its rim.","MANAN: The wall is real. But somebody set it.","SETUP C. One sentence per take. Certain and unhurried, never triumphant."),
("8.3","1:58-1:59","CO","C","medium","Coach Brain lifts the key from his own neck and holds it out. Manan opens his eyes and takes it.","MANAN: And what your brain believes is safe can be trained.","SETUP C. Receiving at chest height then looking up. Give him a real object so the hand is right."),
("8.4","1:59-2:00","AN",None,"end card","Black.","END CARD: THE LIMIT IS A SETTING, NOT A WALL.","Clean type, no decoration, silence underneath."),
]

# Camera department summary, derived
SETUPS = {
 "A": ("Grey backdrop, mid shot, walking and reacting",
       ["1.3","1.5","3.1","3.2","3.5"],
       "Camera at eye level on sticks, locked off. Soft key from camera left at 45 degrees, "
       "large source, no hard shadow on the backdrop. Fill from the right at half strength. "
       "Manan is lit slightly warm because every scene in this setup ends with warm light arriving."),
 "B": ("Seated eyeline, reacting to Coach Brain",
       ["4.3","4.6","5.5"],
       "Same lighting as A, unchanged. Tennis ball on a stand at seated height, camera left, "
       "for eyeline. Do not relight between A and B, only move the eyeline mark."),
 "C": ("White void, still, to lens",
       ["8.1","8.2","8.3"],
       "Flat even light from both sides, no modelling, no shadow on the backdrop. This is the "
       "brightest setup of the day and the calmest."),
 "D": ("Jump, high frame rate",
       ["6.6"],
       "Same as C, wider, room above his head for the jump. Shoot last, when he is loose."),
}

RUNNING_ORDER = ["A","B","D","C"]
# reasoning: A and B share one lighting state, so they run back to back. D is loud and loosening.
# C is last because the stillest material needs him tired of performing but not physically tired,
# and because relighting to flat can happen while he rests.
