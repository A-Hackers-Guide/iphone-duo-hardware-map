# `FigCaptureSourceCompanionFormat`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 12 properties, 15 instance methods, 0 class methods

## Instance variables

```
i _formatIndex;
{?="width"i"height"i} _fesDimensions;
{?="width"i"height"i} _fesInputCropDimensions;
{?="width"i"height"i} _outputCropDimensionsWhenFesIsEnabled;
{?="width"i"height"i} _sensorCropDimensions;
{CGPoint="x"d"y"d} _sensorCenterOffset;
{?="width"i"height"i} _highQualitySensorDimensions;
{?="width"i"height"i} _postGDCCropDimensions;
{?="width"i"height"i} _geometricDistortionCorrectedNativeDimensions;
B _sifrEnabled;
f _stereoVideoAEMaxGain;
{?="width"i"height"i} _sensorDimensions;
```

## Properties

```
@property (Ti,R,V_formatIndex) formatIndex;
@property (T{?=ii},R,V_fesDimensions) fesDimensions;
@property (T{?=ii},R,V_fesInputCropDimensions) fesInputCropDimensions;
@property (T{?=ii},R,V_outputCropDimensionsWhenFesIsEnabled) outputCropDimensionsWhenFesIsEnabled;
@property (T{?=ii},R,V_sensorDimensions) sensorDimensions;
@property (T{?=ii},R,V_sensorCropDimensions) sensorCropDimensions;
@property (T{CGPoint=dd},R,V_sensorCenterOffset) sensorCenterOffset;
@property (T{?=ii},R,V_postGDCCropDimensions) postGDCCropDimensions;
@property (T{?=ii},R,V_highQualitySensorDimensions) highQualitySensorDimensions;
@property (T{?=ii},R,V_geometricDistortionCorrectedNativeDimensions) geometricDistortionCorrectedNativeDimensions;
@property (TB,R,V_sifrEnabled) sifrEnabled;
@property (Tf,R,V_stereoVideoAEMaxGain) stereoVideoAEMaxGain;
```

## Instance methods

```
-[FigCaptureSourceCompanionFormat sensorDimensions];
-[FigCaptureSourceCompanionFormat sensorCenterOffset];
-[FigCaptureSourceCompanionFormat sensorCropDimensions];
-[FigCaptureSourceCompanionFormat dealloc];
-[FigCaptureSourceCompanionFormat stereoVideoAEMaxGain];
-[FigCaptureSourceCompanionFormat geometricDistortionCorrectedNativeDimensions];
-[FigCaptureSourceCompanionFormat fesInputCropDimensions];
-[FigCaptureSourceCompanionFormat description];
-[FigCaptureSourceCompanionFormat postGDCCropDimensions];
-[FigCaptureSourceCompanionFormat formatIndex];
-[FigCaptureSourceCompanionFormat fesDimensions];
-[FigCaptureSourceCompanionFormat highQualitySensorDimensions];
-[FigCaptureSourceCompanionFormat initWithCompanionFormatDictionary:];
-[FigCaptureSourceCompanionFormat outputCropDimensionsWhenFesIsEnabled];
-[FigCaptureSourceCompanionFormat sifrEnabled];
```
