# `AVCaptureMovieFileOutputAssetWriterInputHelper`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_semaphore>" _readyForMoreSemaphore;
@"AVAssetWriterInput" _assetWriterInput;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _signalRequestLock;
B _signalRequested;
```

## Instance methods

```
-[AVCaptureMovieFileOutputAssetWriterInputHelper observeValueForKeyPath:ofObject:change:context:];
-[AVCaptureMovieFileOutputAssetWriterInputHelper dealloc];
-[AVCaptureMovieFileOutputAssetWriterInputHelper ensureWriterInputIsReadyForMoreMediaData];
-[AVCaptureMovieFileOutputAssetWriterInputHelper initWithAsssetWriterInput:];
```
