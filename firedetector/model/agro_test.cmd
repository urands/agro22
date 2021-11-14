rem darknet_no_gpu.exe detector train data/obj.data cfg/yolov4-obj.cfg yolov4.conv.137

REM darknet.exe detector train data/obj.data cfg/yolov4-obj.cfg yolov4.conv.137

rem darknet_no_gpu.exe detector test data/obj.data cfg/yolov4-tiny-obj-test.cfg backup/yolov4-tiny-obj_last.weights data/test_big/000951.jpg 
darknet_no_gpu.exe detector test data/obj.data cfg/yolov4-tiny-obj-test.cfg weight/yolov4-tiny-obj_400000.weights data/img/000744.jpg
rem -save_labels -i 0 -out result.json
rem -dont_show -save_labels