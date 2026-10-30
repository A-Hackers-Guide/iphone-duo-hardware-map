# `AVCaptureSynchronizedSampleBufferData`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureSynchronizedData`
- 1 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"AVCaptureSynchronizedSampleBufferDataInternal" _internal;
```

## Properties

```
@property (T^{opaqueCMSampleBuffer=},R) sampleBuffer;
@property (TB,R) sampleBufferWasDropped;
@property (Tq,R) droppedReason;
```

## Class methods

```
+[AVCaptureSynchronizedSampleBufferData initialize];
```

## Instance methods

```
-[AVCaptureSynchronizedSampleBufferData dealloc];
-[AVCaptureSynchronizedSampleBufferData sampleBuffer];
-[AVCaptureSynchronizedSampleBufferData _initWithSampleBuffer:sampleBufferWasDropped:];
-[AVCaptureSynchronizedSampleBufferData constituentDeviceCaptureID];
-[AVCaptureSynchronizedSampleBufferData droppedReason];
-[AVCaptureSynchronizedSampleBufferData hasCorrespondingDepthData];
-[AVCaptureSynchronizedSampleBufferData hasCorrespondingVisionData];
-[AVCaptureSynchronizedSampleBufferData sampleBufferWasDropped];
```
