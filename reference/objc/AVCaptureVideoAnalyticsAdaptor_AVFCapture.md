# `AVCaptureVideoAnalyticsAdaptor`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVCaptureVideoDataOutputSampleBufferDelegate`
- 16 instance variables, 10 properties, 28 instance methods, 2 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _renderersLock;
@"NSObject<OS_dispatch_queue>" _sampleBufferQueue;
[5@"<MTLTexture>"] _ciOutputRing;
Q _ciOutputRingIndex;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _ciOutputRingIndexLock;
@"NSObject<OS_dispatch_semaphore>" _ciOutputRingSemaphore;
@"NSObject<OS_dispatch_semaphore>" _inFlightFrameSemaphore;
[3^{__CVBuffer}] _cgImageRing;
[3Q] _cgImageRingWidths;
[3Q] _cgImageRingHeights;
[3@"NSObject<OS_dispatch_semaphore>"] _cgImageRingSemaphores;
B _suspended;
@"NSHashTable" _renderers;
@"AVCaptureVideoDataOutput" _attachedVideoDataOutput;
Q _frameCount;
@"NSObject<OS_os_log>" _signpostLogger;
```

## Properties

```
@property (T@"NSHashTable",&,N,V_renderers) renderers;
@property (TB,N,V_suspended) suspended;
@property (T@"AVCaptureVideoDataOutput",&,N,V_attachedVideoDataOutput) attachedVideoDataOutput;
@property (TQ,N,V_frameCount) frameCount;
@property (T@"NSObject<OS_os_log>",N,V_signpostLogger) signpostLogger;
@property (T@"AVCaptureVideoDataOutput",R) videoDataOutput;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[AVCaptureVideoAnalyticsAdaptor initialize];
+[AVCaptureVideoAnalyticsAdaptor defaultCommandQueue];
```

## Instance methods

```
-[AVCaptureVideoAnalyticsAdaptor suspended];
-[AVCaptureVideoAnalyticsAdaptor setSuspended:];
-[AVCaptureVideoAnalyticsAdaptor frameCount];
-[AVCaptureVideoAnalyticsAdaptor isSuspended];
-[AVCaptureVideoAnalyticsAdaptor suspend];
-[AVCaptureVideoAnalyticsAdaptor init];
-[AVCaptureVideoAnalyticsAdaptor dealloc];
-[AVCaptureVideoAnalyticsAdaptor captureOutput:didOutputSampleBuffer:fromConnection:];
-[AVCaptureVideoAnalyticsAdaptor setFrameCount:];
-[AVCaptureVideoAnalyticsAdaptor resume];
-[AVCaptureVideoAnalyticsAdaptor renderers];
-[AVCaptureVideoAnalyticsAdaptor videoDataOutput];
-[AVCaptureVideoAnalyticsAdaptor _convertPixelBufferViaCoreImage:commandBuffer:];
-[AVCaptureVideoAnalyticsAdaptor _hasAttachedVideoDataOutput];
-[AVCaptureVideoAnalyticsAdaptor _processPixelBuffer:slotReleaseHandler:];
-[AVCaptureVideoAnalyticsAdaptor attachToRenderer:];
-[AVCaptureVideoAnalyticsAdaptor attachToVideoDataOutput:error:];
-[AVCaptureVideoAnalyticsAdaptor attachedVideoDataOutput];
-[AVCaptureVideoAnalyticsAdaptor detachFromRenderer:];
-[AVCaptureVideoAnalyticsAdaptor detachFromVideoDataOutput];
-[AVCaptureVideoAnalyticsAdaptor flushRemovingDisplayedImage:];
-[AVCaptureVideoAnalyticsAdaptor ingestCGImage:error:];
-[AVCaptureVideoAnalyticsAdaptor ingestPixelBuffer:attachments:error:];
-[AVCaptureVideoAnalyticsAdaptor ingestSampleBuffer:error:];
-[AVCaptureVideoAnalyticsAdaptor setAttachedVideoDataOutput:];
-[AVCaptureVideoAnalyticsAdaptor setRenderers:];
-[AVCaptureVideoAnalyticsAdaptor setSignpostLogger:];
-[AVCaptureVideoAnalyticsAdaptor signpostLogger];
```
