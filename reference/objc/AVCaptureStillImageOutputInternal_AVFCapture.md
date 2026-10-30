# `AVCaptureStillImageOutputInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 24 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"AVWeakReference" weakReference;
@"NSMutableArray" stillImageRequests;
{CGSize="width"d"height"d} previewImageSize;
I imageDataFormatType;
f jpegQuality;
B jpegQualitySpecified;
B noiseReductionEnabled;
@"NSDictionary" outputSettings;
B isCapturingPhoto;
B SISSupported;
B SISEnabled;
B SISActive;
B highResStillEnabled;
I shutterSoundID;
{?="imageCount"I"outputFormat"i"outputWidth"I"outputHeight"I} preparedBracket;
@"NSMutableArray" prepareRequests;
Q maxBracketedCaptureCount;
B lensStabilizationDuringBracketedCaptureSupported;
B lensStabilizationDuringBracketedCaptureEnabled;
B bravoImageFusionSupported;
B cameraSensorOrientationCompensationSupported;
B cameraSensorOrientationCompensationEnabled;
B cameraSensorOrientationCompensationAutomaticallyEnabled;
^{ct_green_tea_logger_s=} greenTeaLogger;
```

## Instance methods

```
-[AVCaptureStillImageOutputInternal init];
-[AVCaptureStillImageOutputInternal dealloc];
```
