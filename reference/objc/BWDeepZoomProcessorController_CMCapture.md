# `BWDeepZoomProcessorController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorController`
- Protocols: `BWDeepZoomProcessorInputDelegate`, `BWInferenceFormatProvider`
- 7 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"BWDeepZoomProcessorControllerConfiguration" _configuration;
@"FigStateMachine" _stateMachine;
@"NSMutableArray" _requestQueue;
@"BWDeepZoomProcessorRequest" _currentRequest;
@"BWInferenceEngine" _inferenceEngine;
@"NSMutableDictionary" _inferenceConfigurationByInferenceType;
@"NSMutableDictionary" _videoFormatByAttachedMediaKey;
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
+[BWDeepZoomProcessorController initialize];
```

## Instance methods

```
-[BWDeepZoomProcessorController outputFormatForAttachedMediaKey:];
-[BWDeepZoomProcessorController intermediateResourceTrackingAllowedForAttachedMediaKey:];
-[BWDeepZoomProcessorController inputVideoFormatForAttachedMediaKey:];
-[BWDeepZoomProcessorController dealloc];
-[BWDeepZoomProcessorController initWithConfiguration:];
-[BWDeepZoomProcessorController inputInferenceVideoFormatForAttachedMediaKey:];
-[BWDeepZoomProcessorController outputVideoFormatForAttachedMediaKey:];
-[BWDeepZoomProcessorController inputFormatForAttachedMediaKey:];
-[BWDeepZoomProcessorController prepareWithPixelBufferPoolProvider:];
-[BWDeepZoomProcessorController type];
-[BWDeepZoomProcessorController cancelProcessing];
-[BWDeepZoomProcessorController enqueueInputForProcessing:delegate:];
-[BWDeepZoomProcessorController inputSampleBufferReceived:];
```
