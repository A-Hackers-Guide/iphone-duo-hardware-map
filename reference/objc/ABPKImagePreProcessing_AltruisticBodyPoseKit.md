# `ABPKImagePreProcessing`

- Image: [`/System/Library/PrivateFrameworks/AltruisticBodyPoseKit.framework/AltruisticBodyPoseKit`](../userland/System__Library__PrivateFrameworks__AltruisticBodyPoseKit.framework__AltruisticBodyPoseKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 0 properties, 18 instance methods, 0 class methods

## Instance variables

```
@"ABPKPaddingParams" _paddingParameters;
d _startScale;
d _timeScale;
d _startPadding;
d _timePadding;
d _startConvertYCbCrToBGRA;
d _timeConvertYCbCrToBGRA;
d _startConvertARGBToBGRA;
d _timeConvertARGBToBGRA;
d _startConvertGrayScaleToBGRA;
d _timeConvertGrayScaleToBGRA;
^{OpaqueVTPixelTransferSession=} _vtPixelTransferSession;
```

## Instance methods

```
-[ABPKImagePreProcessing dealloc];
-[ABPKImagePreProcessing _endARGBToBGRASignpost];
-[ABPKImagePreProcessing _endARGBToRGBASignpost];
-[ABPKImagePreProcessing _endGrayToBGRASignpost];
-[ABPKImagePreProcessing _endPaddingSignpost];
-[ABPKImagePreProcessing _endScaleSignpost];
-[ABPKImagePreProcessing _endYCbCrToARGBSignpost];
-[ABPKImagePreProcessing _startARGBToBGRASignpost];
-[ABPKImagePreProcessing _startARGBToRGBASignpost];
-[ABPKImagePreProcessing _startGrayToBGRASignpost];
-[ABPKImagePreProcessing _startPaddingSignpost];
-[ABPKImagePreProcessing _startScaleSignpost];
-[ABPKImagePreProcessing _startYCbCrToARGBSignpost];
-[ABPKImagePreProcessing initWithPreProcessingParams:];
-[ABPKImagePreProcessing logProfilingDetails];
-[ABPKImagePreProcessing preprocessColorImage:outputBuffer:];
-[ABPKImagePreProcessing preprocessData:outputBuffer:];
-[ABPKImagePreProcessing preprocessGrayscaleImage:outputBuffer:];
```
