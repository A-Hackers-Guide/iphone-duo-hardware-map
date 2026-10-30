# `BWInferenceTextureStylesPostProcessor`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferencePostProcessor`
- 4 instance variables, 10 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSSet" _requiredInferenceTypes;
B _finalCropRectAppliedToPersonSemanticMasks;
B _finalCropRectAppliedToFaceAndInstanceSegmentationMasks;
B _validBufferRectAppliedToVisionFaceLandmarks;
```

## Properties

```
@property (TB,N,V_finalCropRectAppliedToPersonSemanticMasks) finalCropRectAppliedToPersonSemanticMasks;
@property (TB,N,V_finalCropRectAppliedToFaceAndInstanceSegmentationMasks) finalCropRectAppliedToFaceAndInstanceSegmentationMasks;
@property (TB,N,V_validBufferRectAppliedToVisionFaceLandmarks) validBufferRectAppliedToVisionFaceLandmarks;
@property (T@"NSSet",R,C,N) requiredInferenceTypes;
@property (TI,R,N) postProcessorType;
@property (TB,R,N) needsReprepareForLiveReconfiguration;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWInferenceTextureStylesPostProcessor initialize];
```

## Instance methods

```
-[BWInferenceTextureStylesPostProcessor dealloc];
-[BWInferenceTextureStylesPostProcessor description];
-[BWInferenceTextureStylesPostProcessor initWithRequiredInferenceTypes:];
-[BWInferenceTextureStylesPostProcessor finalCropRectAppliedToFaceAndInstanceSegmentationMasks];
-[BWInferenceTextureStylesPostProcessor finalCropRectAppliedToPersonSemanticMasks];
-[BWInferenceTextureStylesPostProcessor needsReprepareForLiveReconfiguration];
-[BWInferenceTextureStylesPostProcessor postProcessInferenceResults:attachingSampleBuffer:];
-[BWInferenceTextureStylesPostProcessor postProcessorType];
-[BWInferenceTextureStylesPostProcessor preparePostProcessor];
-[BWInferenceTextureStylesPostProcessor requiredInferenceTypes];
-[BWInferenceTextureStylesPostProcessor setFinalCropRectAppliedToFaceAndInstanceSegmentationMasks:];
-[BWInferenceTextureStylesPostProcessor setFinalCropRectAppliedToPersonSemanticMasks:];
-[BWInferenceTextureStylesPostProcessor setValidBufferRectAppliedToVisionFaceLandmarks:];
-[BWInferenceTextureStylesPostProcessor validBufferRectAppliedToVisionFaceLandmarks];
```
