import sys

# Def:
# shots - the count of times the interval finished
# brackets - number of images capture in each shot
# total images taken is equal to shots*brackets

# Note: 
#
# This program outputs 2 calculation - interval and storage. Note that:
#
# interval_s is:
#   a function of:  total_time_h, video_time_s, fps 
#   independent of: brackets_count, estimated_image_size_M
#
# estimated_memory_GB is: 
#   a function of:  video_time_s, fps, brackets_count, estimated_image_size_M
#   independent of: total_time_h (!!!!)

total_time_h = 18.0 # time of timelapse in hours
video_time_s = 60.0 # time of output video seconds
fps = 60 # frames/sec of output video
brackets_count = 2 # number of brackets to take for HDR
estimated_image_size_M = 30.0 # estimated size of each image in MB

def main() -> int:
    total_time_s = total_time_h * 60 * 60  # time of timelapse in secs
    total_number_of_shots = video_time_s * fps 
    total_number_of_images = total_number_of_shots * brackets_count
    
    interval_s = float(total_time_s) / float(total_number_of_shots) # interval time in secs
    estimated_memory_GB = total_number_of_images * estimated_image_size_M / 2**10 # estimated total memory to be used in GB
    
    print()
    print("******************** INPUT ********************")
    print(f"Total time of photoshoot in hours: {total_time_h:.2f}[h]")
    print(f"Total length of video in seconds: {video_time_s:.2f}[s]")
    print(f"Number of brackets after each interval: {brackets_count}")
    print(f"Estimated size of each image in MB: {estimated_image_size_M}")
    print("***********************************************")
    # print()
    # print("------------ DENUG ------------")
    # print(f"total_time_s: {total_time_s}")
    # print(f"total_number_of_shots: {total_number_of_shots}")
    # print("-------------------------------")
    print()
    print("◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄► RESULTS ◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►")
    print(f"Calculated interval in seconds: {interval_s:.2f}[s]")
    print(f"Estimated total memory to be used in GB: {estimated_memory_GB:.2f}[GB]")
    print("◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄►◄")
    print()

    return 0

if __name__ == '__main__':
    sys.exit(main())  # next section explains the use of sys.exit