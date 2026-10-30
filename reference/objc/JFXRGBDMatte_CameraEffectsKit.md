# `JFXRGBDMatte`

- Image: [`/System/Library/PrivateFrameworks/CameraEffectsKit.framework/CameraEffectsKit`](../userland/System__Library__PrivateFrameworks__CameraEffectsKit.framework__CameraEffectsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `JFXMatting`
- 42 instance variables, 0 properties, 27 instance methods, 2 class methods

## Instance variables

```
[2@"PVComputeGrabCut"] _grabCutModules;
I _grabCutCounter;
{CGSize="width"d"height"d} _depthSize;
{CGSize="width"d"height"d} _depthSizeRotated;
^{__CVPixelBufferPool=} _fixedPointDepthPool;
@"NSObject<OS_dispatch_queue>" _submissionQ;
@"NSObject<OS_dispatch_queue>" _processQ;
@"NSObject<OS_dispatch_semaphore>" _processThrottle;
i _numberOfGaussiansBackgroundGMM;
i _numberOfGaussiansForegroundGMM;
i _numberOfIterationsGrabcut;
i _topOfHeadHalf;
i _heightOfMattingWin;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _largestFaceRect;
q _interfaceOrientation;
B _isRepeatingFrame;
[100i] _depthHist;
[4*] _depthBufferHalf;
* _depthBufferFull;
* _vImageTempBuffer;
Q _numFramesWithVeryClosePixels;
Q _previousMattingStatus;
Q _currentMattingStatus;
i _minObjectDistance;
^{__CVPixelBufferPool=} _scaledSourcePool;
^{__CVPixelBufferPool=} _scaledDestinationPool;
^{__CVPixelBufferPool=} _processedMattePool;
^{__CVPixelBufferPool=} _rotatedMattePool;
^{__CVBuffer=} _alphaMatteHistory;
@"JFXImageScaler" _imageScaler;
@"JFXPixelRotationSession" _matteRotator;
@"JFXPixelRotationSession" _colorRotator;
B _disableMattingMultithreading;
B _usingFaceRect;
B _usingforegroundSegBooster;
B _usingLargerRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastLargestFaceRect;
i _faceRectDepth;
B _motionDetected;
B _visualizeFaceRect;
^{DepthProcessingDataRGBD=^i^i^iQQ^{__CVBuffer}*@QQ***iii} _depthProcessingData;
^{ContourMemoryPool=**^i^i} _contourMemoryPool;
```

## Class methods

```
+[JFXRGBDMatte _defaultMatteGeneratorPrefersDepth];
+[JFXRGBDMatte mattingDepthInputSize];
```

## Instance methods

```
-[JFXRGBDMatte dealloc];
-[JFXRGBDMatte alphaMatteForFrameSet:mattingPerfState:completionHandler:];
-[JFXRGBDMatte createInvertedMatte:];
-[JFXRGBDMatte createTemporalFilteredMatte:];
-[JFXRGBDMatte depthToAlphaMap:];
-[JFXRGBDMatte erodeAndDilateMatte:];
-[JFXRGBDMatte expansionOfKnownRegionsRGBD:processingData:regionWin:centerOfRow:];
-[JFXRGBDMatte featherMatte:];
-[JFXRGBDMatte findDepthForFace:];
-[JFXRGBDMatte findLocalMattingRect:processingData:mattingRect:];
-[JFXRGBDMatte findRectOrientationRightLeft:numContourPixels:winHeight:halfHeight:originY:sizeHeight:isRight:];
-[JFXRGBDMatte getDepthData:processData:];
-[JFXRGBDMatte grabCutWithTrimap:color:processWin:];
-[JFXRGBDMatte initForFrameSet:];
-[JFXRGBDMatte innerOuterFusion:processWin:];
-[JFXRGBDMatte isValidForCameraFrameSet:];
-[JFXRGBDMatte localDepthBuffer];
-[JFXRGBDMatte localDepthBufferBig];
-[JFXRGBDMatte localDepthBufferSmall];
-[JFXRGBDMatte localDepthBufferTemp];
-[JFXRGBDMatte localMattingHalfRGBD:colorBuffer:];
-[JFXRGBDMatte makeTrimap:];
-[JFXRGBDMatte mattingGrabCut:depthMap:colorBuffer:processWin:];
-[JFXRGBDMatte moveLocalDepthBufferToDepthOuter:];
-[JFXRGBDMatte postProcessing:depthDataSmall:depthData:RGBDMatte:halfHeight:halfWidth:];
-[JFXRGBDMatte processAlphaMapUsingDepthAndColor:colorBuffer:];
-[JFXRGBDMatte requestMattingStatus];
```
