import cv2
import numpy as np
import time


class CaptureManager(object):
    def __init__(self,capture,previewWindowManager=None,
                 shoudMirrorrPreview=False,model_fourcc=None,val=None,size_List=None):
        self.previewWindowManager=previewWindowManager
        self.shoudMirrorPreview=shoudMirrorrPreview

        self._sizeCapture=size_List
        self.con_val=val
        self.codeck=model_fourcc

        self._capture=capture
        self._channel=0
        self._enteredFrame=False
        self._frame=None
        self._imageFilename=None
        self._VideoFileName=None
        self._videoEncoding=None
        self._videoWriter=None

        self._startTime=None
        self._framesElapsed=0
        self._fpsEstimate=None

    @property
    def channel(self):
        return  self._channel

    @channel.setter
    def channel(self,value):
        if self._channel!=value:
            self._channel=value
            self._frame=None


    @property
    def frame(self):
        if self._entereFrame and self._frame is None:
            _,self._frame=self._capture.retrieve(
                channel=self.channel
            )


    @property
    def isWritingImage(self):
        return self._imageFilename is not None

    @property
    def isWritingVideo(self):
        return self._VideoFileName is not None


    def enterFrame(self):
        """Capture the next frame,if any"""
        assert not self._enteredFrame,\
        'previous enterFrame() had no matching exitFrame()'

        if self._capture is not None:
            self._enteredFrame=self._capture.grab()


    def exitFrame(self):
        """Draw Window. WriteFile.Release the frame"""
        if self.frame is None:
            self._enteredFrame=False
            return

        #Update fps  estimate and related variables
        if self._framesElapsed==0:
            self._startTime=time.time()
        else:
            timeElapsed=time.time()-self._startTime
            self._fpsEstimate=self._framesElapsed/timeElapsed

        self._framesElapsed+=1

        #Draw to the window, if any.
        if self.previewWindowManager is not None:
            if self.shoudMirrorPreview:
                mirroredFrame=np.fliplr(self._frame).copy()
                self.previewWindowManager.show(mirroredFrame)

            else:
                self.previewWindowManager.show(self._frame)


        #Write to the image file, if any.
        if self.isWritingImage:
            out = cv2.VideoWriter(self._VideoFileName,self.codeck,self.con_val,self._sizeCapture)
            out.imwrite(self._frame)
            self._imageFilename=None

        self.writeVideoFrame()

        #release
        self._frame=None
        self._enteredFrame=False



    def writeImage(self,filename):
        """write the next exited frame to an image file"""
        self._imageFilename=filename

    def startWritingVideo(self,filename,fourcc = cv2.VideoWriter_fourcc(*'XVID')):
        """Start writing exited frames"""
        self._VideoFileName=filename
        self._videoEncoding=fourcc


    def stopWritingVideo(self):
        """Stop writing exited frames to a video file."""
        self._VideoFileName=None
        self._videoEncoding=None
        self._videoWriter=None







