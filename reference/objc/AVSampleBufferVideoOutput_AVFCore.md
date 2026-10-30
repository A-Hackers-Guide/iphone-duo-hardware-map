# `AVSampleBufferVideoOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"AVSampleBufferVideoOutputInternal" _videoOutputInternal;
```

## Properties

```
@property (T@"<AVSampleBufferVideoOutputPullDelegate>",R,W,N) outputDelegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateQueue;
```

## Instance methods

```
-[AVSampleBufferVideoOutput init];
-[AVSampleBufferVideoOutput dealloc];
-[AVSampleBufferVideoOutput _weakReference];
-[AVSampleBufferVideoOutput delegateQueue];
-[AVSampleBufferVideoOutput hasNewPixelBufferForSourceTime:];
-[AVSampleBufferVideoOutput _configureWithVideoQueue:];
-[AVSampleBufferVideoOutput _copyPixelBufferForItemTimeWithOptions:itemTimeForDisplay:options:];
-[AVSampleBufferVideoOutput _dispatchOutputSequenceWasFlushed];
-[AVSampleBufferVideoOutput _resetLastImageTime];
-[AVSampleBufferVideoOutput _visualContext];
-[AVSampleBufferVideoOutput copyLastPixelBuffer:];
-[AVSampleBufferVideoOutput copyPixelBufferForSourceTime:sourceTimeForDisplay:];
-[AVSampleBufferVideoOutput outputDelegate];
-[AVSampleBufferVideoOutput setOutputDelegate:queue:];
-[AVSampleBufferVideoOutput setUpWithOutputSettings:outputSettingsArePixelBufferAttributes:withExceptionReason:];
```
