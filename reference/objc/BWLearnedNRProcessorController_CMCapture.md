# `BWLearnedNRProcessorController`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorController`
- Protocols: `BWLearnedNRInputDelegate`, `BWInferenceFormatProvider`
- 7 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"BWLearnedNRProcessorControllerConfiguration" _configuration;
@"FigStateMachine" _stateMachine;
@"NSMutableArray" _requestQueue;
@"BWLearnedNRRequest" _currentRequest;
B _inferenceEnginePrepared;
@"BWInferenceEngine" _inferenceEngine;
@"NSMutableDictionary" _inferenceConfigurationByInferenceType;
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
+[BWLearnedNRProcessorController initialize];
```

## Instance methods

```
-[BWLearnedNRProcessorController outputFormatForAttachedMediaKey:];
-[BWLearnedNRProcessorController intermediateResourceTrackingAllowedForAttachedMediaKey:];
-[BWLearnedNRProcessorController inputVideoFormatForAttachedMediaKey:];
-[BWLearnedNRProcessorController dealloc];
-[BWLearnedNRProcessorController initWithConfiguration:];
-[BWLearnedNRProcessorController inputInferenceVideoFormatForAttachedMediaKey:];
-[BWLearnedNRProcessorController outputVideoFormatForAttachedMediaKey:];
-[BWLearnedNRProcessorController inputFormatForAttachedMediaKey:];
-[BWLearnedNRProcessorController prepareWithPixelBufferPoolProvider:];
-[BWLearnedNRProcessorController type];
-[BWLearnedNRProcessorController cancelProcessing];
-[BWLearnedNRProcessorController enqueueInputForProcessing:delegate:];
-[BWLearnedNRProcessorController input:setInputFrame:];
```
