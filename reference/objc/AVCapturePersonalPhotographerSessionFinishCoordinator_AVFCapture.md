# `AVCapturePersonalPhotographerSessionFinishCoordinator`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 0 properties, 10 instance methods, 2 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
@"NSMutableSet" _expectedSettingsIDs;
@"NSMutableSet" _completedSettingsIDs;
B _expectedSetOfSettingsIDsCommitted;
B _completed;
@"AVCaptureInactivityWatchdog" _watchdog;
@"AVCapturePhotoRequest" _pendingRequest;
@"NSError" _pendingError;
@? _completionHandler;
```

## Class methods

```
+[AVCapturePersonalPhotographerSessionFinishCoordinator initialize];
+[AVCapturePersonalPhotographerSessionFinishCoordinator inactivityTimeoutForSystemPressureState:];
```

## Instance methods

```
-[AVCapturePersonalPhotographerSessionFinishCoordinator dealloc];
-[AVCapturePersonalPhotographerSessionFinishCoordinator reset];
-[AVCapturePersonalPhotographerSessionFinishCoordinator description];
-[AVCapturePersonalPhotographerSessionFinishCoordinator _handleWatchdogTimeout];
-[AVCapturePersonalPhotographerSessionFinishCoordinator _invokeCompletionWithRequest:error:];
-[AVCapturePersonalPhotographerSessionFinishCoordinator _shouldInvokeCompletionCopyOutRequest:copyOutError:];
-[AVCapturePersonalPhotographerSessionFinishCoordinator finishWithRequest:expectedSettingsIDs:error:];
-[AVCapturePersonalPhotographerSessionFinishCoordinator initWithInactivityTimeout:completionHandler:];
-[AVCapturePersonalPhotographerSessionFinishCoordinator recordCaptureCompleteForSettingsID:];
-[AVCapturePersonalPhotographerSessionFinishCoordinator recordStillComplete];
```
