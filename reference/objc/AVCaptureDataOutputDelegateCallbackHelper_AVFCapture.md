# `AVCaptureDataOutputDelegateCallbackHelper`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 6 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"NSString" _defaultCallbackQueueName;
@"NSObject<OS_dispatch_queue>" _defaultCallbackQueue;
^{OpaqueFigSimpleMutex=} _stateMutex;
@"AVWeakReferencingDelegateStorage" _delegateStorage;
@"AVWeakReferencingDelegateStorage" _delegateOverrideStorage;
^{remoteQueueReceiverOpaque=} _remoteQueueReceiver;
@? _remoteQueueHandler;
^{localQueueOpaque=} _localQueue;
@? _localQueueHandler;
```

## Properties

```
@property (T@,R) activeDelegate;
@property (T@"NSObject<OS_dispatch_queue>",R) activeCallbackQueue;
@property (T@,R) clientDelegate;
@property (T@"NSObject<OS_dispatch_queue>",R) clientCallbackQueue;
@property (T@,R) delegateOverride;
@property (T@"NSObject<OS_dispatch_queue>",R) delegateOverrideCallbackQueue;
```

## Class methods

```
+[AVCaptureDataOutputDelegateCallbackHelper initialize];
```

## Instance methods

```
-[AVCaptureDataOutputDelegateCallbackHelper clientCallbackQueue];
-[AVCaptureDataOutputDelegateCallbackHelper activeDelegate];
-[AVCaptureDataOutputDelegateCallbackHelper initWithQueueName:];
-[AVCaptureDataOutputDelegateCallbackHelper setClientDelegate:clientCallbackQueue:exceptionReason:];
-[AVCaptureDataOutputDelegateCallbackHelper dealloc];
-[AVCaptureDataOutputDelegateCallbackHelper _validateCallbackQueue:exceptionReason:];
-[AVCaptureDataOutputDelegateCallbackHelper activeCallbackQueue];
-[AVCaptureDataOutputDelegateCallbackHelper _activeCallbackQueue];
-[AVCaptureDataOutputDelegateCallbackHelper setDelegateOverride:delegateOverrideCallbackQueue:exceptionReason:];
-[AVCaptureDataOutputDelegateCallbackHelper _activeDelegate];
-[AVCaptureDataOutputDelegateCallbackHelper clientDelegate];
-[AVCaptureDataOutputDelegateCallbackHelper releaseRemoteQueueReceiver];
-[AVCaptureDataOutputDelegateCallbackHelper updateRemoteQueueReceiver:handler:];
-[AVCaptureDataOutputDelegateCallbackHelper updateLocalQueue:handler:];
-[AVCaptureDataOutputDelegateCallbackHelper delegateOverrideCallbackQueue];
-[AVCaptureDataOutputDelegateCallbackHelper delegateOverride];
```
