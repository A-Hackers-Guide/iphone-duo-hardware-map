# `AVCaptureVisionDataOutputInternal`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 21 instance variables, 0 properties, 2 instance methods, 0 class methods

## Instance variables

```
@"AVCaptureDataOutputDelegateCallbackHelper" delegateCallbackHelper;
@"AVWeakReference" weakReference;
{?="value"q"timescale"i"flags"I"epoch"q} minFrameDuration;
{?="value"q"timescale"i"flags"I"epoch"q} minBurstFrameDuration;
{?="value"q"timescale"i"flags"I"epoch"q} maxBurstDuration;
Q gaussianPyramidOctavesCount;
f gaussianPyramidBaseOctaveDownscalingFactor;
Q maxKeypointsCount;
B featureBinningEnabled;
B featureOrientationAssignmentEnabled;
B dynamicThresholdingEnabled;
Q keypointDetectionFlowType;
Q subPixelThreshold;
B featureMatchingEnabled;
Q featureMatchingDescriptorSize;
f orientationDistanceThreshold;
f sigmaDistanceThreshold;
f squareDistanceDisparityFraction;
Q hammingDistanceThreshold;
@"NSData" laccConfigAndMetadata;
f keypointDetectionThreshold;
```

## Instance methods

```
-[AVCaptureVisionDataOutputInternal init];
-[AVCaptureVisionDataOutputInternal dealloc];
```
