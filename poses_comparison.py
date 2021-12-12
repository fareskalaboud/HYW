import json 
from joblib import Parallel, delayed
import statistics

def bb_intersection_over_union(boxA, boxB):
    # 39, 63, 203, 112], [54, 66, 198, 114]

	# determine the (x, y)-coordinates of the intersection rectangle
	xA = max(boxA[0], boxB[0])
	yA = max(boxA[1], boxB[1])
	xB = min(boxA[2], boxB[2])
	yB = min(boxA[3], boxB[3])
	# compute the area of intersection rectangle
	interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
	# compute the area of both the prediction and ground-truth
	# rectangles
	boxAArea = (boxA[2] - boxA[0] + 1) * (boxA[3] - boxA[1] + 1)
	boxBArea = (boxB[2] - boxB[0] + 1) * (boxB[3] - boxB[1] + 1)
	# compute the intersection over union by taking the intersection
	# area and dividing it by the sum of prediction + ground-truth
	# areas - the interesection area
	iou = interArea / float(boxAArea + boxBArea - interArea)
	# return the intersection over union value
	return iou


def read_keypoints_from_json_file(json_files, c):

    # print(json_files)

    file = json_files[c]

    # JSON file
    f = open (file, "r")
    
    # # Reading from file
    data = json.loads(f.read())

    return data['people'][0]['pose_keypoints_2d']
    


def sci_notation_to_int(joint):
    return int(float(("%.3f" % joint).rstrip('0').rstrip('.')))



def create_box_around_point_from_stream(joint):

    x = sci_notation_to_int(joint[0])
    y = sci_notation_to_int(joint[1])

    if x-25 > 0:
        x1 = x-25
    else:
        x1 = 0
    if y-25 > 0:
        y1 = y-25
    else:
        y1 = 0
    if x+25 < 1080:
        x2 = x+25
    else:
        x2 = 1080
    if y+25 < 1080:
        y2 = y+25
    else:
        y2 = 1080

    return [x1,y1,x2,y2]


def create_box_around_point_from_json_file(song_keypoints):
    bboxes = []
    c=0
    for i in range(len(song_keypoints)):

        if c == 2:
            c = 0

            x_index = i-2
            y_index = i-1

            x = int(song_keypoints[x_index])
            y = int(song_keypoints[y_index])

            if x-25 > 0:
                x1 = x-25
            else:
                x1 = 0
            if y-25 > 0:
                y1 = y-25
            else:
                y1 = 0
            if x+25 < 1000:
                x2 = x+25
            else:
                x2 = 1080
            if y+25 < 1000:
                y2 = y+25
            else:
                y2 = 1080

            bbox = (x1,y1,x2,y2)
            bboxes.append(bbox)
        c += 1
    return bboxes


def compare_poses(stream_keypoints,json_files, c):
    
    song_keypoints = read_keypoints_from_json_file(json_files, c)

    stream_bboxes = Parallel(n_jobs=3)(delayed(create_box_around_point_from_stream)(joint) for joint in stream_keypoints)

    json_bboxes = create_box_around_point_from_json_file(song_keypoints)

    # print(song_keypoints)
    # print(json_bboxes)

    iou_list = Parallel(n_jobs=3)(delayed(bb_intersection_over_union)(stream_bboxes[i], json_bboxes[i]) for i in range(len(stream_bboxes)))

    return statistics.mean(iou_list), song_keypoints
