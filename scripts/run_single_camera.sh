gst-launch-1.0 v4l2src device=/dev/video0 \
                ! "image/jpeg,width=2592,height=1944,framerate=1/1" \
                ! videorate \
                ! "image/jpeg,framerate=1/1" \
                ! multifilesink location='/tmp/frames/cam0_full/cam0_%06d.jpg'