from flask.scaffold import F
import json

data = [
    544.8982543945312,
    199.16781616210938,
    1.0,
    537.4922485351562,
    259.3768310546875,
    1.0,
    463.91455078125,
    254.35853576660156,
    1.0,
    452.2116394042969,
    353.3133544921875,
    1.0,
    477.58660888671875,
    418.23321533203125,
    1.0,
    582.439208984375,
    258.08355712890625,
    1.0,
    617.9515380859375,
    362.7923583984375,
    1.0,
    593.5240478515625,
    412.3018798828125,
    1.0,
    518.2569580078125,
    458.3076477050781,
    1.0,
    493.85162353515625,
    458.1862487792969,
    1.0,
    442.07470703125,
    605.3922729492188,
    1.0,
    387.778564453125,
    768.66552734375,
    1.0,
    569.614501953125,
    460.5773620605469,
    1.0,
    582.43798828125,
    614.0833740234375,
    1.0,
    607.382568359375,
    773.2880859375,
    1.0,
    533.593994140625,
    194.31942749023438,
    1.0,
    549.6932983398438,
    194.843017578125,
    1.0,
    508.0466613769531,
    189.06124877929688,
    1.0,
    579.1771850585938,
    195.93643188476562,
    1.0,
    632.7014770507812,
    806.2693481445312,
    1.0,
    640.7095336914062,
    804.5030517578125,
    1.0,
    593.134033203125,
    790.950927734375,
    1.0,
    383.62890625,
    807.4512939453125,
    1.0,
    374.3594055175781,
    798.2952270507812,
    1.0,
    402.6040344238281,
    779.5150756835938,
    1.0
]

# chunks = [data[x:x+3] for x in range(0, len(data), 3)]
# print(chunks)

# print("L_hip", str(chunks[12][0]), str(chunks[12][1]))
# print("R_hip", str(chunks[13][0]), str(chunks[13][1]))
# print("L_elbow", str(chunks[6][0]), str(chunks[6][1]))
# print("R_elbow", str(chunks[3][0]), str(chunks[3][1]))
# print("L_shoulder", str(chunks[5][0]), str(chunks[5][1]))
# print("R_shoulder", str(chunks[2][0]), str(chunks[2][1]))

file_n_list = []
filenames = []
second = 0

for i in range(0,450):
    if (i % 15 == 0):
        file_n_list.append(i)

for n in file_n_list:
    if (len(str(n)) == 1):
        filenames.append(f'00000000000{n}_keypoints.json')
    elif (len(str(n)) == 2):
        filenames.append(f'0000000000{n}_keypoints.json')
    else:
        filenames.append(f'000000000{n}_keypoints.json')

for f in filenames:
    jd = json.load(open(f'Learning2Dance\output\michael\\vid2vid\\test_openpose\\{f}'))
    pose_keypoints_2d = jd['people'][0]['pose_keypoints_2d']
    chunks = [pose_keypoints_2d[x:x+3] for x in range(0, len(pose_keypoints_2d), 3)]
    print("FRAME NUMBER: ", second)
    print("L_hip", str(float(chunks[12][0]/1000)), str(float(chunks[12][1]/1000)))
    print("R_hip", str(float(chunks[13][0]/1000)), str(float(chunks[13][1]/1000)))
    print("L_elbow", str(float(chunks[6][0]/1000)), str(float(chunks[6][1]/1000)))
    print("R_elbow", str(float(chunks[3][0]/1000)), str(float(chunks[3][1]/1000)))
    print("L_shoulder", str(float(chunks[5][0]/1000)), str(float(chunks[5][1]/1000)))
    print("R_shoulder", str(float(chunks[2][0]/1000)), str(float(chunks[2][1]/1000)), '\n\n')
    second += 1

print(second)