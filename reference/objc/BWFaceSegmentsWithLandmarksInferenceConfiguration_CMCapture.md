# `BWFaceSegmentsWithLandmarksInferenceConfiguration`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWLandmarksInferenceConfiguration`
- 5 instance variables, 5 properties, 12 instance methods, 1 class methods

## Instance variables

```
I _requestTypes;
B _detectFacesInFullSizeInput;
B _includesInvalidContent;
f _faceSegmentsFaceBoundingBoxExpansionRatio;
B _faceSegmentsAsFullFrameMasks;
```

## Properties

```
@property (TI,N,V_requestTypes) requestTypes;
@property (TB,N,V_detectFacesInFullSizeInput) detectFacesInFullSizeInput;
@property (TB,N,V_includesInvalidContent) includesInvalidContent;
@property (Tf,N,V_faceSegmentsFaceBoundingBoxExpansionRatio) faceSegmentsFaceBoundingBoxExpansionRatio;
@property (TB,N,V_faceSegmentsAsFullFrameMasks) faceSegmentsAsFullFrameMasks;
```

## Class methods

```
+[BWFaceSegmentsWithLandmarksInferenceConfiguration configuration];
```

## Instance methods

```
-[BWFaceSegmentsWithLandmarksInferenceConfiguration includesInvalidContent];
-[BWFaceSegmentsWithLandmarksInferenceConfiguration initWithInferenceType:];
-[BWFaceSegmentsWithLandmarksInferenceConfiguration setIncludesInvalidContent:];
-[BWFaceSegmentsWithLandmarksInferenceConfiguration detectFacesInFullSizeInput];
-[BWFaceSegmentsWithLandmarksInferenceConfiguration faceSegmentsFaceBoundingBoxExpansionRatio];
-[BWFaceSegmentsWithLandmarksInferenceConfiguration setRequestTypes:];
-[BWFaceSegmentsWithLandmarksInferenceConfiguration setDetectFacesInFullSizeInput:];
-[BWFaceSegmentsWithLandmarksInferenceConfiguration description];
-[BWFaceSegmentsWithLandmarksInferenceConfiguration requestTypes];
-[BWFaceSegmentsWithLandmarksInferenceConfiguration faceSegmentsAsFullFrameMasks];
-[BWFaceSegmentsWithLandmarksInferenceConfiguration setFaceSegmentsAsFullFrameMasks:];
-[BWFaceSegmentsWithLandmarksInferenceConfiguration setFaceSegmentsFaceBoundingBoxExpansionRatio:];
```
