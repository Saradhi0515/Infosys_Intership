from Programs.utils.video_utils import read_video, save_video, detect_vehicles
from Programs.object_tracker.tracker import Tracker

def main():

    frames = read_video("C:\\Users\\pardh\\PycharmProjects\\STMS\\Programs\\data\\traffic_video.mp4")


    obj_tracker = Tracker()
    result = obj_tracker.detect_objects(frames)

    output_frames = obj_tracker.draw_annotations(frames, result)

    save_video(output_frames, "C:\\Users\\pardh\\PycharmProjects\\STMS\\output\\output.avi")


if __name__ == '__main__':
    main()