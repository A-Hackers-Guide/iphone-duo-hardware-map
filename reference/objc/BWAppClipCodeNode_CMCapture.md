# `BWAppClipCodeNode`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWNode`
- 10 instance variables, 1 properties, 9 instance methods, 1 class methods

## Instance variables

```
^{AppC3DSession=} _appClipCodeSession;
B _appC3DAvailable;
@"NSObject<OS_dispatch_queue>" _processingQueue;
@"FigWeakReference" _weakSelf;
B _haveInputTransform;
i _rotationDegrees;
B _mirroringHorizontal;
B _mirroringVertical;
@"<BWMetadataDetectedResultsObserver>" _detectedResultsObserver;
q _lastAppClipCodeCount;
```

## Properties

```
@property (T@"<BWMetadataDetectedResultsObserver>",N,V_detectedResultsObserver) detectedResultsObserver;
```

## Class methods

```
+[BWAppClipCodeNode initialize];
```

## Instance methods

```
-[BWAppClipCodeNode prepareForCurrentConfigurationToBecomeLive];
-[BWAppClipCodeNode renderSampleBuffer:forInput:];
-[BWAppClipCodeNode dealloc];
-[BWAppClipCodeNode setDetectedResultsObserver:];
-[BWAppClipCodeNode didReachEndOfDataForConfigurationID:input:];
-[BWAppClipCodeNode nodeSubType];
-[BWAppClipCodeNode detectedResultsObserver];
-[BWAppClipCodeNode initWithProcessingQueuePriority:];
-[BWAppClipCodeNode nodeType];
```
