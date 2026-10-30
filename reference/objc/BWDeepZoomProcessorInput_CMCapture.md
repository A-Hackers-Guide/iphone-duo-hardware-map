# `BWDeepZoomProcessorInput`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageProcessorControllerInput`
- 5 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _sampleBufferSet;
^{opaqueCMSampleBuffer=} _sampleBuffer;
Q _bufferType;
@"<BWDeepZoomProcessorInputDelegate>" _delegate;
B _enqueued;
```

## Properties

```
@property (TB,N,V_sampleBufferSet) sampleBufferSet;
@property (T@"<BWDeepZoomProcessorInputDelegate>",&,N,V_delegate) delegate;
@property (T^{opaqueCMSampleBuffer=},R,N) sampleBuffer;
@property (TQ,R,N) bufferType;
@property (TB,N,GisEnqueued,V_enqueued) enqueued;
```

## Instance methods

```
-[BWDeepZoomProcessorInput dealloc];
-[BWDeepZoomProcessorInput setDelegate:];
-[BWDeepZoomProcessorInput delegate];
-[BWDeepZoomProcessorInput description];
-[BWDeepZoomProcessorInput sampleBuffer];
-[BWDeepZoomProcessorInput sampleBufferSet];
-[BWDeepZoomProcessorInput addSampleBuffer:bufferType:];
-[BWDeepZoomProcessorInput bufferType];
-[BWDeepZoomProcessorInput isEnqueued];
-[BWDeepZoomProcessorInput setEnqueued:];
-[BWDeepZoomProcessorInput setSampleBufferSet:];
```
