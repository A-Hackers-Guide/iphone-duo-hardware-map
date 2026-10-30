# `BWSubjectRelightingCalculator`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BWInferenceEngineControllerDelegate`, `BWInferencePixelBufferPoolProvider`
- 11 instance variables, 5 properties, 9 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _prepareQueue;
@"NSObject<OS_dispatch_queue>" _calculationQueue;
B _startedPrepare;
B _waitedForPrepare;
@"BWPhotoDecompressor" _jpegDecompressor;
@"BWInferenceScheduler" _inferenceScheduler;
@"BWInferenceEngineController" _inferenceController;
@"NSDictionary" _inferenceOutputPoolsByAttachedMediaKey;
@"SubjectRelightingStage" _subjectRelightingStage;
@"FigMetalContext" _metalContext;
@"BWVideoFormat" _preparedVideoFormat;
```

## Properties

```
@property (T@"BWVideoFormat",R,N) preparedVideoFormat;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BWSubjectRelightingCalculator initialize];
```

## Instance methods

```
-[BWSubjectRelightingCalculator preparedOutputPixelBufferPoolForAttachedMediaKey:format:];
-[BWSubjectRelightingCalculator processorController:didFinishProcessingInput:err:];
-[BWSubjectRelightingCalculator processorController:didFinishProcessingSampleBuffer:type:processorInput:err:];
-[BWSubjectRelightingCalculator processorController:newOutputPixelBufferForProcessorInput:type:];
-[BWSubjectRelightingCalculator dealloc];
-[BWSubjectRelightingCalculator initWithInferenceScheduler:];
-[BWSubjectRelightingCalculator prepareForVideoFormatAsync:];
-[BWSubjectRelightingCalculator preparedVideoFormat];
-[BWSubjectRelightingCalculator startCalculationWithJPEGSampleBuffer:stillImageRequestSettings:stillImageCaptureSettings:];
```
