import sys; sys.path.insert(0,'/home/claude/gen')
from nb import gen
B="https://raw.githubusercontent.com/markoboskoauroville/BRAIN_BRAKE/main/assets/"
M=B+"REFERENCES/MANAN_DESK.jpg"

HEAD = """Take the storyboard frame in the first reference and change one thing only.

The boy in it is currently drawn in pencil. Replace him with the real photographed boy from the second reference: real skin, real hair, real fabric, a genuine photograph of a fourteen year old Indian boy in a plain grey hooded sweatshirt and dark jeans, at exactly the same size, position and pose. """

TAIL = """

Everything else in the frame stays exactly as drawn in pencil on cream paper: the line weight, the shading, the hand drawn border, every drawn object and character.

"""

JOBS = [
 ("fix_3_2","V6/panels/S3_P2.jpg","4:3",
  "He stands with his back to camera, small in the middle of the frame, his palm flat on the riveted door at chest height.",
  "He is lit from camera left and throws a soft shadow onto the drawn door, with the pencil lines visible through it."),
 ("fix_3_3","V6/panels/S3_P3.jpg","4:3",
  "He stands with his back to camera in the open doorway, small in the frame, one hand on the edge of the door, warm light flooding out over him from the opening.",
  "The warm light from the doorway falls on him from the front so he reads almost as a silhouette, and he throws a long shadow back toward the camera across the drawn floor."),
 ("fix_3_4","V6/panels/S3_P4.jpg","4:3",
  "The back of his head and his left shoulder fill the lower left of the frame in the near foreground, cut off by the left and bottom edges, looking away down the hall.",
  "He is lit warmly from ahead of him by the light in the hall, and throws a soft shadow back toward the camera."),
 ("fix_3_6","V6/panels/S3_P6.jpg","4:3",
  "He stands in the middle of the hall between the rows of tanks, and he is turned to face the camera, seen from the front, delighted rather than shocked.",
  "He is lit by the warm light coming from the tanks around him and throws a soft shadow onto the drawn floor."),
 ("fix_4_2","V6/panels/S4_P2.jpg","4:3",
  "He stands at the left of the frame in full length, turned three quarters toward the small drawn brain character beside him, level with it.",
  "He is lit from camera left and throws a soft shadow onto the drawn floor, with the pencil lines visible through it."),
 ("fix_4_6","V6/panels/S4_P6.jpg","4:3",
  "He stands at the left of the frame in profile, hand at his chin, thinking, the small drawn brain character working the console beside him.",
  "He is lit from camera left and throws a soft shadow onto the drawn floor."),
 ("fix_8_1","V6/panels/S8_P1.jpg","4:3",
  "He stands alone in the middle of the frame facing the camera, arms at his sides, eyes closed, breathing, completely calm.",
  "Flat even light from both sides with no modelling, and only a small soft contact shadow on the white floor at his feet. The background stays plain white."),
 ("fix_8_3","V7/V7_8_3_lever_drawn.jpg","4:3",
  "Only the hand and forearm are his: replace the drawn hand resting on top of the ball with a real photographed boy's hand and forearm, entering from the right edge inside a soft grey hooded sweatshirt sleeve with a ribbed knit cuff, resting on the ball in the same position.",
  "The hand is lit from camera left and throws a soft shadow onto the drawn plate."),
 ("fix_8_5","V6/panels/S8_P5.jpg","4:3",
  "Only the receiving hand is his: replace the drawn open palm on the right with a real photographed boy's open palm and forearm, in a soft grey hooded sweatshirt sleeve, in exactly the same position receiving the key. The giving hand on the left stays drawn in pencil.",
  "The real palm is lit from camera left and throws a soft shadow onto the drawn ground. The small key stays gold, the only colour in the frame."),
 ("fix_8_6","V6/panels/S8_P6.jpg","4:3",
  "He stands in the middle of the frame facing the camera, eyes open, a small gold key hanging from his left hand and his right hand resting on top of the drawn lever beside him.",
  "Flat even light from both sides, a small soft contact shadow at his feet, the background plain white. The key stays gold, the only colour in the frame."),
]

for name, ref, ar, pose, light in JOBS:
    prompt = HEAD + pose + TAIL + light + "\n\nThe result is a photograph of a real boy inside a pencil drawing."
    print("---", name)
    gen(prompt, refs=[B+ref, M], aspect=ar, size="2K", name=name)
