# `BWLandmarksInferenceConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWVisionInferenceConfiguration`
- 14 instance variables, 14 properties, 30 instance methods, 4 class methods

## Instance variables

```
B _refinesMouthLandmarks;
B _refinesLeftEyeLandmarks;
B _refinesRightEyeLandmarks;
B _detectsBlinking;
B _detectLandmarksInFullSizeInput;
@"NSNumber" _cascadeStepCount;
Q _maximumNumberOfFaces;
B _clampToLargestMaximumNumberOfFaces;
B _prioritizeISPMatchedFacesWhenClamping;
B _alwaysExecuteForRedEyeReduction;
B _considerISPRectsIfVisionFails;
i _constellationPointCount;
{?="major"S"minor"S"patch"S} _landmarksInferenceVersion;
@"NSString" _inferenceInputAttachedMediaKey;
```

## Properties

```
@property (TB,N,V_refinesMouthLandmarks) refinesMouthLandmarks;
@property (TB,N,V_refinesLeftEyeLandmarks) refinesLeftEyeLandmarks;
@property (TB,N,V_refinesRightEyeLandmarks) refinesRightEyeLandmarks;
@property (TB,N,V_detectsBlinking) detectsBlinking;
@property (T@"NSNumber",&,N,V_cascadeStepCount) cascadeStepCount;
@property (TQ,N,V_maximumNumberOfFaces) maximumNumberOfFaces;
@property (TB,N,V_clampToLargestMaximumNumberOfFaces) clampToLargestMaximumNumberOfFaces;
@property (TB,N,V_prioritizeISPMatchedFacesWhenClamping) prioritizeISPMatchedFacesWhenClamping;
@property (TB,N,V_alwaysExecuteForRedEyeReduction) alwaysExecuteForRedEyeReduction;
@property (TB,N,V_detectLandmarksInFullSizeInput) detectLandmarksInFullSizeInput;
@property (TB,N,V_considerISPRectsIfVisionFails) considerISPRectsIfVisionFails;
@property (Ti,N,V_constellationPointCount) constellationPointCount;
@property (T{?=SSS},N,V_landmarksInferenceVersion) landmarksInferenceVersion;
@property (T@"NSString",&,N,V_inferenceInputAttachedMediaKey) inferenceInputAttachedMediaKey;
```

## Class methods

```
+[BWLandmarksInferenceConfiguration initialize];
+[BWLandmarksInferenceConfiguration configuration];
+[BWLandmarksInferenceConfiguration isPortraitPrewarmingRequired];
+[BWLandmarksInferenceConfiguration portraitMaximumNumberOfFaces];
```

## Instance methods

```
-[BWLandmarksInferenceConfiguration setRefinesRightEyeLandmarks:];
-[BWLandmarksInferenceConfiguration setMaximumNumberOfFaces:];
-[BWLandmarksInferenceConfiguration clampToLargestMaximumNumberOfFaces];
-[BWLandmarksInferenceConfiguration setRefinesMouthLandmarks:];
-[BWLandmarksInferenceConfiguration constellationPointCount];
-[BWLandmarksInferenceConfiguration setClampToLargestMaximumNumberOfFaces:];
-[BWLandmarksInferenceConfiguration landmarksInferenceVersion];
-[BWLandmarksInferenceConfiguration setLandmarksInferenceVersion:];
-[BWLandmarksInferenceConfiguration setInferenceInputAttachedMediaKey:];
-[BWLandmarksInferenceConfiguration refinesLeftEyeLandmarks];
-[BWLandmarksInferenceConfiguration detectsBlinking];
-[BWLandmarksInferenceConfiguration setConsiderISPRectsIfVisionFails:];
-[BWLandmarksInferenceConfiguration alwaysExecuteForRedEyeReduction];
-[BWLandmarksInferenceConfiguration setAlwaysExecuteForRedEyeReduction:];
-[BWLandmarksInferenceConfiguration initWithInferenceType:];
-[BWLandmarksInferenceConfiguration setDetectsBlinking:];
-[BWLandmarksInferenceConfiguration setCascadeStepCount:];
-[BWLandmarksInferenceConfiguration cascadeStepCount];
-[BWLandmarksInferenceConfiguration setPrioritizeISPMatchedFacesWhenClamping:];
-[BWLandmarksInferenceConfiguration setRefinesLeftEyeLandmarks:];
-[BWLandmarksInferenceConfiguration inferenceInputAttachedMediaKey];
-[BWLandmarksInferenceConfiguration dealloc];
-[BWLandmarksInferenceConfiguration refinesRightEyeLandmarks];
-[BWLandmarksInferenceConfiguration considerISPRectsIfVisionFails];
-[BWLandmarksInferenceConfiguration setDetectLandmarksInFullSizeInput:];
-[BWLandmarksInferenceConfiguration prioritizeISPMatchedFacesWhenClamping];
-[BWLandmarksInferenceConfiguration maximumNumberOfFaces];
-[BWLandmarksInferenceConfiguration detectLandmarksInFullSizeInput];
-[BWLandmarksInferenceConfiguration refinesMouthLandmarks];
-[BWLandmarksInferenceConfiguration setConstellationPointCount:];
```
