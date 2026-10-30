# `BWFaceAndInstanceSegmentationConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWInferenceConfiguration`
- 4 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _portraitOrientationSupportEnabled;
B _inputAspectRatioIsLandscape;
B _appliesFinalCropRect;
{?="major"S"minor"S"patch"S} _version;
```

## Properties

```
@property (TB,N,V_portraitOrientationSupportEnabled) portraitOrientationSupportEnabled;
@property (TB,N,V_inputAspectRatioIsLandscape) inputAspectRatioIsLandscape;
@property (TB,N,V_appliesFinalCropRect) appliesFinalCropRect;
@property (T{?=SSS},R,N,V_version) version;
```

## Instance methods

```
-[BWFaceAndInstanceSegmentationConfiguration initWithInferenceType:];
-[BWFaceAndInstanceSegmentationConfiguration appliesFinalCropRect];
-[BWFaceAndInstanceSegmentationConfiguration portraitOrientationSupportEnabled];
-[BWFaceAndInstanceSegmentationConfiguration version];
-[BWFaceAndInstanceSegmentationConfiguration setAppliesFinalCropRect:];
-[BWFaceAndInstanceSegmentationConfiguration description];
-[BWFaceAndInstanceSegmentationConfiguration setPortraitOrientationSupportEnabled:];
-[BWFaceAndInstanceSegmentationConfiguration setInputAspectRatioIsLandscape:];
-[BWFaceAndInstanceSegmentationConfiguration inputAspectRatioIsLandscape];
```
