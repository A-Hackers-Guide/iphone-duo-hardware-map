# `BWStereoDisparityProcessorController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorController`
- Protocols: `BWStereoDisparityProcessorInputDelegate`, `DisparityProcessorInferenceDelegate`, `BWInferenceFormatProvider`
- 7 instance variables, 4 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"FigDisparityGenerator" _disparityProcessor;
@"BWInferenceEngine" _inferenceEngine;
@"NSSet" _currentInferenceEnginePortTypes;
^{opaqueCMFormatDescription=} _refFormatDescription;
^{opaqueCMFormatDescription=} _auxFormatDescription;
^{opaqueCMFormatDescription=} _disparityFormatDescription;
@"NSDictionary" _videoFormatByAttachedMediaKey;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWStereoDisparityProcessorController usesCustomProcessingFlow];
```

## Instance methods

```
-[BWStereoDisparityProcessorController outputFormatForAttachedMediaKey:];
-[BWStereoDisparityProcessorController intermediateResourceTrackingAllowedForAttachedMediaKey:];
-[BWStereoDisparityProcessorController inputVideoFormatForAttachedMediaKey:];
-[BWStereoDisparityProcessorController process];
-[BWStereoDisparityProcessorController dealloc];
-[BWStereoDisparityProcessorController reset];
-[BWStereoDisparityProcessorController initWithConfiguration:];
-[BWStereoDisparityProcessorController inputInferenceVideoFormatForAttachedMediaKey:];
-[BWStereoDisparityProcessorController outputVideoFormatForAttachedMediaKey:];
-[BWStereoDisparityProcessorController inputFormatForAttachedMediaKey:];
-[BWStereoDisparityProcessorController type];
-[BWStereoDisparityProcessorController prepare];
-[BWStereoDisparityProcessorController requestForInput:delegate:errOut:];
-[BWStereoDisparityProcessorController inputReceivedNewInputData:];
-[BWStereoDisparityProcessorController processDisparityInferenceWithReferenceBuffer:auxBuffer:outputDisparityBuffer:];
```
