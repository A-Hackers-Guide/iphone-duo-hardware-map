# `GVSOverscanPredictor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 14 instance variables, 0 properties, 9 instance methods, 0 class methods

## Instance variables

```
_margin;
_imageSize;
_imageCenter;
{?="vector"} _cameraAlignment;
d _detectionTimeoutSeconds;
d _resetTimeoutSeconds;
d _overscanFitsTimestamp;
d _latestSampleTimestamp;
@"NSString" _previousPort;
@"VISRotationCorrectionEstimator" _visEstimator;
@"NSDictionary" _pixelSizeByPortType;
[36{?="doingBiasEstimation"B"timestamp"d"quaternion"{?="w"d"x"d"y"d"z"d}}] _rawQuaternionArray;
_estimatedCorrection;
_estimatedOverscan;
```

## Instance methods

```
-[GVSOverscanPredictor resetPrediction];
-[GVSOverscanPredictor computeFocalLength:fromMetadata:];
-[GVSOverscanPredictor estimateOverscanUseFromMetadata:finalCropRect:];
-[GVSOverscanPredictor estimateOverscanUseFromRotation:focalLength:cornerCoords:];
-[GVSOverscanPredictor initWithConfig:cameraInfoByPortType:visInputPixelBufferAttributes:];
-[GVSOverscanPredictor parseCameraInfoByPortType:];
-[GVSOverscanPredictor predictOverscanFitsFromMetadata:finalCropRect:boundingRect:];
-[GVSOverscanPredictor resetAndClear];
-[GVSOverscanPredictor setCameraAlignmentForPortType:];
```
