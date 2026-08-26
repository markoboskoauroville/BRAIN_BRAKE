# PROMPTS, image to image, one frame at a time

Every frame becomes **two pictures**: a plate with nobody in it, and the character alone on flat cream.
Frames marked LIVE need only a plate, because the character is Manan and he is real footage.

## The two prompts

**PLATE.** Reference the frame itself.

```
A clean empty background plate in the same graphite pencil drawing on aged cream paper, same line
weight and same shading as the reference, wide 16:9.

The picture contains only: [WHAT REMAINS].

The floor and the walls continue unbroken across the whole frame. Even light from the right.
The paper texture reaches all four edges.
```

`[WHAT REMAINS]` is the room, the furniture, the machinery, the sky. **Never name the person you
want gone.** Saying no summons it. Never write *redraw* or *same image but*, both anchor the model
to the whole reference, figure included.

**CHARACTER.** Reference the character file, never the frame.

```
A single full body character drawing on a plain flat cream background, nothing else in the picture,
in graphite pencil in the same style and line weight as the reference.

[COSTUME], [POSE].

The whole figure is inside the frame with clear empty space above the head and below the feet.
Flat even background, no border, no panel, no frame line, no shadow behind the figure.
```

## Check before cutting

Nothing touching the top edge. No panel border around the figure. Right costume.

---

## 1.1   DRAWN
> For a hundred years we blamed the muscles.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_1_1_face.jpg

**Plate**, then **character: RUNNER**

Costume line, verbatim: *a gaunt marathon runner of about forty five, long face, heavy brow, deep set eyes, hair swept back, in a plain running singlet with the number 27 and shorts*

## 1.2   DRAWN

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_1_2_going_down.jpg

**Plate**, then **character: RUNNER**

Costume line, verbatim: *a gaunt marathon runner of about forty five, long face, heavy brow, deep set eyes, hair swept back, in a plain running singlet with the number 27 and shorts*

## 1.3   DRAWN

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_1_3_sprint.jpg

**Plate**, then **character: RUNNER**

Costume line, verbatim: *a gaunt marathon runner of about forty five, long face, heavy brow, deep set eyes, hair swept back, in a plain running singlet with the number 27 and shorts*

## 1.5   LIVE

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_1_5_walks_in.jpg

**Plate only.** The character is Manan, real footage.

## 1.6   LIVE
> Hold on. He had nothing left. So where did THAT come from?

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_1_6_turns_to_us.jpg

**Plate only.** The character is Manan, real footage.

## 2.1   LIVE
> A. V. Hill. Nineteen twenty three.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_2_1_blackboard.jpg

**Plate only.** The character is Manan, real footage.

## 2.2   DRAWN

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_2_2_board_close.jpg

**Plate only.** No character in this frame.

## 2.3   LIVE

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_2_3_lens.jpg

**Plate only.** The character is Manan, real footage.

## 2.4   DRAWN
> That's it. We're done.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_2_4_case_worker.jpg

**Plate**, then **character: WORKERS**

Costume line, verbatim: *a factory worker in dungaree overalls and a soft cap, ordinary and tired*

## 2.6   LIVE
> Except it doesn't explain this.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_2_6_case_closed.jpg

**Plate only.** The character is Manan, real footage.

## 3.1   DRAWN

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_3_1_factory_empty.jpg

**Plate only.** No character in this frame.

## 3.2   LIVE
> At the back, a door nobody opens.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_3_2_door.jpg

**Plate only.** The character is Manan, real footage.

## 3.3   LIVE

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_3_3_swings.jpg

**Plate only.** The character is Manan, real footage.

## 3.4   LIVE
> Tested the moment they gave up, the muscles could still do far more.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_3_4_tanks.jpg

**Plate only.** The character is Manan, real footage.

## 3.6   LIVE
> It was never empty. Somebody closed that door.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_3_6_turns.jpg

**Plate only.** The character is Manan, real footage.

## 4.1   STRIP
> You found me. Took you long enough.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_4_1_found_me.jpg

**Plate**, then **character: COACH**

Costume line, verbatim: *a friendly cartoon brain for a head, a thin headset microphone at his cheek, a zip up tracksuit jacket with a stripe down each sleeve, matching tracksuit trousers, a lanyard round his neck, and white trainers*

Character reference file: `assets/BRAND/COACH_BRAIN_ON_SET.png`, single figure. **Never the four view sheet.**

## 4.2   LIVE
> You closed that door.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_4_2_level.jpg

**Plate only.** The character is Manan, real footage.

## 4.3   STRIP
> Heart rate. Breath. Temperature. Water. Distance.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_4_3_sensors.jpg

**Plate**, then **character: COACH**

Costume line, verbatim: *a friendly cartoon brain for a head, a thin headset microphone at his cheek, a zip up tracksuit jacket with a stripe down each sleeve, matching tracksuit trousers, a lanyard round his neck, and white trainers*

Character reference file: `assets/BRAND/COACH_BRAIN_ON_SET.png`, single figure. **Never the four view sheet.**

## 4.4   STRIP
> I'm asking one question. Can we keep going safely?

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_4_4_one_question.jpg

**Plate**, then **character: COACH**

Costume line, verbatim: *a friendly cartoon brain for a head, a thin headset microphone at his cheek, a zip up tracksuit jacket with a stripe down each sleeve, matching tracksuit trousers, a lanyard round his neck, and white trainers*

Character reference file: `assets/BRAND/COACH_BRAIN_ON_SET.png`, single figure. **Never the four view sheet.**

## 4.4b   LIVE
> So you're secretly pacing me?

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_4_4b_pacing.jpg

**Plate only.** The character is Manan, real footage.

## 4.5   LIVE
> Like a phone at twenty percent. Not broken. Protecting itself.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_4_4_phone.jpg

**Plate only.** The character is Manan, real footage.

## 4.6   STRIP
> Fatigue isn't your body failing. It's me slowing you down before real danger.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_4_6b_not_sorry.jpg

**Plate**, then **character: COACH**

Costume line, verbatim: *a friendly cartoon brain for a head, a thin headset microphone at his cheek, a zip up tracksuit jacket with a stripe down each sleeve, matching tracksuit trousers, a lanyard round his neck, and white trainers*

Character reference file: `assets/BRAND/COACH_BRAIN_ON_SET.png`, single figure. **Never the four view sheet.**

## 4.7   LIVE
> So the limit isn't my body. It's your judgement. They call it the Central Governor Theory.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_4_6_arrives.jpg

**Plate only.** The character is Manan, real footage.

## 4.8   LIVE
> It sets your limit in advance, and keeps something in reserve.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_4_8_definition.jpg

**Plate only.** The character is Manan, real footage.

## 5.1   DRAWN
> They let him race his own best ride.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_5_1_lab_cyclist.jpg

**Plate**, then **character: CYCLIST**

Costume line, verbatim: *a racing cyclist in a plain jersey and shorts, sensors taped to his chest, on a road bicycle*

## 5.3   DRAWN
> He beat it. So it was never his maximum.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_5_3_beat_it.jpg

**Plate**, then **character: CYCLIST**

Costume line, verbatim: *a racing cyclist in a plain jersey and shorts, sensors taped to his chest, on a road bicycle*

## 5.4   LIVE

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_5_4_idea_lands.jpg

**Plate only.** The character is Manan, real footage.

## 5.5   LIVE
> So I tried it.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_5_5_road.jpg

**Plate only.** The character is Manan, real footage.

## 5.6   LIVE

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_5_6_racing.jpg

**Plate only.** The character is Manan, real footage.

## 5.7   LIVE

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_5_7_the_wall.jpg

**Plate only.** The character is Manan, real footage.

## 5.8   LIVE
> Nothing about my legs changed.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_5_8_eyes_closed.jpg

**Plate only.** The character is Manan, real footage.

## 5.9   LIVE
> Only what I believed they had left.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_5_9_eyes_open.jpg

**Plate only.** The character is Manan, real footage.

## 6.1   STRIP
> All right. Everything's holding. Let's give him a little more.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_6_1_check_green.jpg

**Plate**, then **character: COACH**

Costume line, verbatim: *a friendly cartoon brain for a head, a thin headset microphone at his cheek, a zip up tracksuit jacket with a stripe down each sleeve, matching tracksuit trousers, a lanyard round his neck, and white trainers*

Character reference file: `assets/BRAND/COACH_BRAIN_ON_SET.png`, single figure. **Never the four view sheet.**

## 6.2   DRAWN

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_6_2_lever_hand.jpg

**Plate**, then **character: HAND**

Costume line, verbatim: *a hand and forearm in a ribbed sleeve, gripping a slider lever*

## 6.4   DRAWN

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_6_4_one_fibre.jpg

**Plate**, then **character: FIBRES**

Costume line, verbatim: *glowing muscle fibres*

## 6.5   DRAWN

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_6_5_cluster.jpg

**Plate**, then **character: FIBRES**

Costume line, verbatim: *glowing muscle fibres*

## 6.6   DRAWN

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_6_6_whole_leg.jpg

**Plate**, then **character: FIGURE**

Costume line, verbatim: *a bare human figure, anatomical, seen whole*

## 6.7   DRAWN

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_6_7_whole_body.jpg

**Plate**, then **character: FIGURE**

Costume line, verbatim: *a bare human figure, anatomical, seen whole*

## 6.8   DRAWN

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_6_8_pushing_off.jpg

**Plate**, then **character: FIGURE**

Costume line, verbatim: *a bare human figure, anatomical, seen whole*

## 6.9   DRAWN
> It didn't make new energy. It gave permission.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_6_9_the_leap.jpg

**Plate**, then **character: FIGURE**

Costume line, verbatim: *a bare human figure, anatomical, seen whole*

## 7.1   DRAWN

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_7_1_apart.jpg

**Plate only.** No character in this frame.

## 7.3   LIVE

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_7_3_white.jpg

**Plate only.** The character is Manan, real footage.

## 7.5   DRAWN

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_7_5_two_cards.jpg

**Plate only.** No character in this frame.

## 8.1   LIVE

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_8_1_breathing.jpg

**Plate only.** The character is Manan, real footage.

## 8.3   LIVE

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_8_3_hand_lever.jpg

**Plate only.** The character is Manan, real footage.

## 8.6   LIVE
> Next time somebody finds one last burst of speed,

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_8_5_key.jpg

**Plate only.** The character is Manan, real footage.

## 8.7   LIVE
> don't just wonder how strong their muscles are.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_8_7_closing.jpg

**Plate only.** The character is Manan, real footage.

## 8.8   LIVE
> Wonder what their brain believed was safe.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_8_6_eyes_open.jpg

**Plate only.** The character is Manan, real footage.

## 8.9   BOOTH
> The limit is a setting, not a wall.

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_ENDCARD.jpg

**Plate only.** No character in this frame.

## 8.10   DRAWN

Reference: https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/V7/V7_BLANK_PAPER.jpg

**Plate only.** No character in this frame.

