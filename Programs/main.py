from utils.video_utils import read_video, save_video, detect_vehicles

def main():

    frames = read_video("C:\\Users\\pardh\\PycharmProjects\\STMS\\Data\\Video\\traffic3.mp4")

    # Video processing and detection
    detection_of_vehicles = detect_vehicles(frames)




    save_video(frames, "C:\\Users\\pardh\\PycharmProjects\\STMS\\Output\\AVI\\output3.avi")

if __name__ == '__main__':
    main