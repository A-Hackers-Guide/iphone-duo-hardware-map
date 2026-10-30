# `BWVisionInferenceContext`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 5 instance methods, 4 class methods

## Instance variables

```
@"VNSequenceRequestHandler" _sequenceRequestHandler;
```

## Properties

```
@property (T@"VNSequenceRequestHandler",R,N,V_sequenceRequestHandler) sequenceRequestHandler;
@property (TB,R,N,GisPrepared) prepared;
```

## Class methods

```
+[BWVisionInferenceContext initialize];
+[BWVisionInferenceContext defaultTimeoutInSeconds];
+[BWVisionInferenceContext processingTimeoutInSeconds];
+[BWVisionInferenceContext usingDefaultTimeout];
```

## Instance methods

```
-[BWVisionInferenceContext isPrepared];
-[BWVisionInferenceContext dealloc];
-[BWVisionInferenceContext initWithScheduler:];
-[BWVisionInferenceContext prepareForInference];
-[BWVisionInferenceContext sequenceRequestHandler];
```
