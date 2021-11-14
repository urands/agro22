rem darknet_no_gpu.exe detector train data/obj.data cfg/yolov4-obj.cfg yolov4.conv.137

REM darknet.exe detector train data/obj.data cfg/yolov4-obj.cfg yolov4.conv.137

rem darknet_no_gpu.exe detector test data/obj.data cfg/yolov4-tiny-obj-test.cfg backup/yolov4-tiny-obj_last.weights data/test_big/000951.jpg 
rem darknet.exe detector demo data/obj.data cfg/yolov4-tiny-obj-test.cfg weight/yolov4-tiny-obj_400000.weights data/video/result_h264.avi --ext_output video.mp4 -out_filename video_results.mp4


darknet.exe detector demo data/obj.data cfg/yolov4-tiny-obj-test.cfg weight/yolov4-tiny-obj_400000.weights d:/work/uran/ready1.avi --ext_output video.mp4 -out_filename video2_results.mp4

rem -save_labels -i 0 -out result.json
rem -dont_show -save_labels