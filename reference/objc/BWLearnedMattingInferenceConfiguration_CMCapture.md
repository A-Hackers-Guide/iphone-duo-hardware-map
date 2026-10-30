# `BWLearnedMattingInferenceConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWTiledEspressoInferenceConfiguration`
- 7 instance variables, 7 properties, 17 instance methods, 0 class methods

## Instance variables

```
f _mainImageDownscalingFactor;
f _targetAspectRatio;
B _appliesFinalCropRect;
B _produceLowResPersonMaskClone;
B _inputSegmentationPortraitOrientationSupportEnabled;
@"NSString" _networkConfiguration;
@"NSString" _inferenceInputAttachedMediaKey;
```

## Properties

```
@property (TB,N,V_inputSegmentationPortraitOrientationSupportEnabled) inputSegmentationPortraitOrientationSupportEnabled;
@property (Tf,N,V_mainImageDownscalingFactor) mainImageDownscalingFactor;
@property (Tf,N,V_targetAspectRatio) targetAspectRatio;
@property (TB,N,V_appliesFinalCropRect) appliesFinalCropRect;
@property (TB,N,V_produceLowResPersonMaskClone) produceLowResPersonMaskClone;
@property (T@"NSString",&,N,V_networkConfiguration) networkConfiguration;
@property (T@"NSString",&,N,V_inferenceInputAttachedMediaKey) inferenceInputAttachedMediaKey;
```

## Instance methods

```
-[BWLearnedMattingInferenceConfiguration setInferenceInputAttachedMediaKey:];
-[BWLearnedMattingInferenceConfiguration initWithInferenceType:];
-[BWLearnedMattingInferenceConfiguration produceLowResPersonMaskClone];
-[BWLearnedMattingInferenceConfiguration inferenceInputAttachedMediaKey];
-[BWLearnedMattingInferenceConfiguration targetAspectRatio];
-[BWLearnedMattingInferenceConfiguration appliesFinalCropRect];
-[BWLearnedMattingInferenceConfiguration setMainImageDownscalingFactor:];
-[BWLearnedMattingInferenceConfiguration setProduceLowResPersonMaskClone:];
-[BWLearnedMattingInferenceConfiguration mainImageDownscalingFactor];
-[BWLearnedMattingInferenceConfiguration dealloc];
-[BWLearnedMattingInferenceConfiguration setTargetAspectRatio:];
-[BWLearnedMattingInferenceConfiguration setInputSegmentationPortraitOrientationSupportEnabled:];
-[BWLearnedMattingInferenceConfiguration setAppliesFinalCropRect:];
-[BWLearnedMattingInferenceConfiguration description];
-[BWLearnedMattingInferenceConfiguration networkConfiguration];
-[BWLearnedMattingInferenceConfiguration inputSegmentationPortraitOrientationSupportEnabled];
-[BWLearnedMattingInferenceConfiguration setNetworkConfiguration:];
```
