from ultralytics import YOLO
import cv2

class Tracker:

    def __init__(self):
        self.model = YOLO("yolov8x.pt")

    def detect_objects(self, frames):

        detections = []

        for frame in frames:
            detected_objs = self.detect_frame(frame)
            detections.append(detected_objs)
        # for i in range(0, len(frames),5):
        #     frame = frames[i]
        #     detected_objs = self.detect_frame(frame)
        #     detections.append(detected_objs)

        return detections

    def detect_frame(self,frame):
        results = self.model.track(frame, persist=True)[0]
        name_dict = results.names

        dict = {}
        for box in results.boxes:
            track_id = int(box.id.tolist()[0])
            result = box.xyxy.tolist()[0]
            object_class_id = box.cls.tolist()[0]
            object_class_name = name_dict[object_class_id]
            if object_class_name in ("bicycle", "car", "motorcycle", "bus", "truck"):
                dict[track_id] = result

        return dict

    def draw_annotations(self, frames, object_detections):
        output_video_frames = []
        for frame, obj_detected in zip(frames, object_detections):
            for track_id, bbox in obj_detected.items():
                x1,y1,x2,y2 = bbox

                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0,0,255), 2)
            output_video_frames.append(frame)

        return output_video_frames

# 1: 'bicycle',
# 2: 'car',
# 3: 'motorcycle',
# 5: 'bus',
# 7: 'truck'