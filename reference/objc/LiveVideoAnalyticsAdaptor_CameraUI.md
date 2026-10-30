# `LiveVideoAnalyticsAdaptor`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `AVCaptureVideoDataOutputSampleBufferDelegate`
- 16 instance variables, 10 properties, 29 instance methods, 2 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _renderersLock;
@"NSObject<OS_dispatch_queue>" _sampleBufferQueue;
[3@"<MTLTexture>"] _ciOutputRing;
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
+[LiveVideoAnalyticsAdaptor initialize];
+[LiveVideoAnalyticsAdaptor defaultCommandQueue];
```

## Instance methods

```
-[LiveVideoAnalyticsAdaptor suspended];
-[LiveVideoAnalyticsAdaptor setSuspended:];
-[LiveVideoAnalyticsAdaptor frameCount];
-[LiveVideoAnalyticsAdaptor isSuspended];
-[LiveVideoAnalyticsAdaptor suspend];
-[LiveVideoAnalyticsAdaptor init];
-[LiveVideoAnalyticsAdaptor dealloc];
-[LiveVideoAnalyticsAdaptor captureOutput:didOutputSampleBuffer:fromConnection:];
-[LiveVideoAnalyticsAdaptor setFrameCount:];
-[LiveVideoAnalyticsAdaptor resume];
-[LiveVideoAnalyticsAdaptor renderers];
-[LiveVideoAnalyticsAdaptor videoDataOutput];
-[LiveVideoAnalyticsAdaptor _convertPixelBufferViaCoreImage:commandBuffer:];
-[LiveVideoAnalyticsAdaptor _hasAttachedVideoDataOutput];
-[LiveVideoAnalyticsAdaptor _processPixelBuffer:slotReleaseHandler:];
-[LiveVideoAnalyticsAdaptor attachToRenderer:];
-[LiveVideoAnalyticsAdaptor attachToVideoDataOutput:error:];
-[LiveVideoAnalyticsAdaptor attachedVideoDataOutput];
-[LiveVideoAnalyticsAdaptor detachFromRenderer:];
-[LiveVideoAnalyticsAdaptor detachFromVideoDataOutput];
-[LiveVideoAnalyticsAdaptor flushRemovingDisplayedImage:];
-[LiveVideoAnalyticsAdaptor ingestCGImage:error:];
-[LiveVideoAnalyticsAdaptor ingestPixelBuffer:attachments:error:];
-[LiveVideoAnalyticsAdaptor ingestSampleBuffer:error:];
-[LiveVideoAnalyticsAdaptor setAttachedVideoDataOutput:];
-[LiveVideoAnalyticsAdaptor setRenderers:];
-[LiveVideoAnalyticsAdaptor setSignpostLogger:];
-[LiveVideoAnalyticsAdaptor signpostLogger];
-[LiveVideoAnalyticsAdaptor _passThroughTextureForPixelBuffer:outCVTexture:];
```
