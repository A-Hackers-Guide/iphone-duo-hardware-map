# `FigCaptureVisionDataSinkConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FigCaptureSinkConfiguration`
- 19 instance variables, 20 properties, 47 instance methods, 0 class methods

## Instance variables

```
f _maxFrameRate;
f _maxBurstFrameRate;
{?="value"q"timescale"i"flags"I"epoch"q} _maxBurstDuration;
I _gaussianPyramidOctavesCount;
f _gaussianPyramidBaseOctaveDownscalingFactor;
I _maxKeypointsCount;
f _keypointDetectionThreshold;
B _featureBinningEnabled;
B _featureOrientationAssignmentEnabled;
B _dynamicThresholdingEnabled;
I _keypointDetectionFlowType;
Q _subPixelThreshold;
B _featureMatchingEnabled;
i _featureMatchingDescriptorSize;
f _orientationDistanceThreshold;
f _sigmaDistanceThreshold;
f _squareDistanceDisparityFraction;
Q _hammingDistanceThreshold;
@"NSData" _laccConfigAndMetadata;
```

## Properties

```
@property (Tf,N,V_maxFrameRate) maxFrameRate;
@property (Tf,N,V_maxBurstFrameRate) maxBurstFrameRate;
@property (T{?=qiIq},N,V_maxBurstDuration) maxBurstDuration;
@property (TI,N,V_gaussianPyramidOctavesCount) gaussianPyramidOctavesCount;
@property (Tf,N,V_gaussianPyramidBaseOctaveDownscalingFactor) gaussianPyramidBaseOctaveDownscalingFactor;
@property (TI,N,V_maxKeypointsCount) maxKeypointsCount;
@property (Tf,N,V_keypointDetectionThreshold) keypointDetectionThreshold;
@property (TB,N,V_featureBinningEnabled) featureBinningEnabled;
@property (TB,N,V_featureOrientationAssignmentEnabled) featureOrientationAssignmentEnabled;
@property (TB,N,GisDynamicThresholdingEnabled,V_dynamicThresholdingEnabled) dynamicThresholdingEnabled;
@property (TI,N,V_keypointDetectionFlowType) keypointDetectionFlowType;
@property (TQ,N,V_subPixelThreshold) subPixelThreshold;
@property (TB,N,GisFeatureMatchingEnabled,V_featureMatchingEnabled) featureMatchingEnabled;
@property (Ti,N,V_featureMatchingDescriptorSize) featureMatchingDescriptorSize;
@property (Tf,N,V_orientationDistanceThreshold) orientationDistanceThreshold;
@property (Tf,N,V_sigmaDistanceThreshold) sigmaDistanceThreshold;
@property (Tf,N,V_squareDistanceDisparityFraction) squareDistanceDisparityFraction;
@property (TQ,N,V_hammingDistanceThreshold) hammingDistanceThreshold;
@property (T@"NSData",&,N,V_laccConfigAndMetadata) laccConfigAndMetadata;
@property (T@"NSDictionary",R,N) embeddedCaptureDeviceConfiguration;
```

## Instance methods

```
-[FigCaptureVisionDataSinkConfiguration maxFrameRate];
-[FigCaptureVisionDataSinkConfiguration isDynamicThresholdingEnabled];
-[FigCaptureVisionDataSinkConfiguration sinkType];
-[FigCaptureVisionDataSinkConfiguration reasonForNotEqualingConfiguration:];
-[FigCaptureVisionDataSinkConfiguration setOrientationDistanceThreshold:];
-[FigCaptureVisionDataSinkConfiguration laccConfigAndMetadata];
-[FigCaptureVisionDataSinkConfiguration setMaxFrameRate:];
-[FigCaptureVisionDataSinkConfiguration gaussianPyramidBaseOctaveDownscalingFactor];
-[FigCaptureVisionDataSinkConfiguration dealloc];
-[FigCaptureVisionDataSinkConfiguration maxKeypointsCount];
-[FigCaptureVisionDataSinkConfiguration orientationDistanceThreshold];
-[FigCaptureVisionDataSinkConfiguration setFeatureMatchingEnabled:];
-[FigCaptureVisionDataSinkConfiguration maxBurstDuration];
-[FigCaptureVisionDataSinkConfiguration setMaxKeypointsCount:];
-[FigCaptureVisionDataSinkConfiguration setLaccConfigAndMetadata:];
-[FigCaptureVisionDataSinkConfiguration keypointDetectionThreshold];
-[FigCaptureVisionDataSinkConfiguration maxBurstFrameRate];
-[FigCaptureVisionDataSinkConfiguration featureOrientationAssignmentEnabled];
-[FigCaptureVisionDataSinkConfiguration isFeatureMatchingEnabled];
-[FigCaptureVisionDataSinkConfiguration setKeypointDetectionFlowType:];
-[FigCaptureVisionDataSinkConfiguration embeddedCaptureDeviceConfiguration];
-[FigCaptureVisionDataSinkConfiguration setMaxBurstDuration:];
-[FigCaptureVisionDataSinkConfiguration setFeatureMatchingDescriptorSize:];
-[FigCaptureVisionDataSinkConfiguration squareDistanceDisparityFraction];
-[FigCaptureVisionDataSinkConfiguration featureMatchingDescriptorSize];
-[FigCaptureVisionDataSinkConfiguration gaussianPyramidOctavesCount];
-[FigCaptureVisionDataSinkConfiguration setSubPixelThreshold:];
-[FigCaptureVisionDataSinkConfiguration setGaussianPyramidBaseOctaveDownscalingFactor:];
-[FigCaptureVisionDataSinkConfiguration copyXPCEncoding];
-[FigCaptureVisionDataSinkConfiguration description];
-[FigCaptureVisionDataSinkConfiguration setHammingDistanceThreshold:];
-[FigCaptureVisionDataSinkConfiguration setKeypointDetectionThreshold:];
-[FigCaptureVisionDataSinkConfiguration initWithXPCEncoding:];
-[FigCaptureVisionDataSinkConfiguration sigmaDistanceThreshold];
-[FigCaptureVisionDataSinkConfiguration copyWithZone:];
-[FigCaptureVisionDataSinkConfiguration setFeatureOrientationAssignmentEnabled:];
-[FigCaptureVisionDataSinkConfiguration subPixelThreshold];
-[FigCaptureVisionDataSinkConfiguration isEqual:];
-[FigCaptureVisionDataSinkConfiguration setMaxBurstFrameRate:];
-[FigCaptureVisionDataSinkConfiguration keypointDetectionFlowType];
-[FigCaptureVisionDataSinkConfiguration setFeatureBinningEnabled:];
-[FigCaptureVisionDataSinkConfiguration setSigmaDistanceThreshold:];
-[FigCaptureVisionDataSinkConfiguration setDynamicThresholdingEnabled:];
-[FigCaptureVisionDataSinkConfiguration setGaussianPyramidOctavesCount:];
-[FigCaptureVisionDataSinkConfiguration hammingDistanceThreshold];
-[FigCaptureVisionDataSinkConfiguration featureBinningEnabled];
-[FigCaptureVisionDataSinkConfiguration setSquareDistanceDisparityFraction:];
```
