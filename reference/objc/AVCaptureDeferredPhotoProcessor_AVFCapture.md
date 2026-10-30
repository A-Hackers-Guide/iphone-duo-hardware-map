# `AVCaptureDeferredPhotoProcessor`

- Image: [`/System/Library/PrivateFrameworks/AVFCapture.framework/AVFCapture`](../userland/System__Library__PrivateFrameworks__AVFCapture.framework__AVFCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 1 properties, 28 instance methods, 3 class methods

## Instance variables

```
@"NSString" _applicationIDOverride;
@"NSObject<OS_dispatch_queue>" _processorQueue;
^{OpaqueFigCaptureDeferredPhotoProcessor=} _processor;
@"AVWeakReference" _weakReference;
^{OpaqueFigSimpleMutex=} _requestsLock;
@"NSMutableArray" _requests;
B _requestsWillBeReenqueued;
@"NSObject<OS_dispatch_queue>" _processPhotoProxyQueue;
@"NSObject<OS_dispatch_queue>" _reenqueuePhotoProxyQueue;
```

## Properties

```
@property (T@"NSArray",R,N) persistentlyStoredDeferredPhotoProxies;
```

## Class methods

```
+[AVCaptureDeferredPhotoProcessor initialize];
+[AVCaptureDeferredPhotoProcessor sharedPhotoProcessorForApplicationID:];
+[AVCaptureDeferredPhotoProcessor sharedPhotoProcessor];
```

## Instance methods

```
-[AVCaptureDeferredPhotoProcessor isPaused];
-[AVCaptureDeferredPhotoProcessor _handleNotification:payload:];
-[AVCaptureDeferredPhotoProcessor dealloc];
-[AVCaptureDeferredPhotoProcessor setPaused:];
-[AVCaptureDeferredPhotoProcessor cancelAllPrewarming];
-[AVCaptureDeferredPhotoProcessor deletePersistentStorageForPhotoProxy:];
-[AVCaptureDeferredPhotoProcessor persistentlyStoredDeferredPhotoProxies];
-[AVCaptureDeferredPhotoProcessor prewarmWithSettings:];
-[AVCaptureDeferredPhotoProcessor processPhotoProxy:queuePosition:delegate:delegateQueue:];
-[AVCaptureDeferredPhotoProcessor _dispatchFailureCallbacks:forProcessingRequest:error:];
-[AVCaptureDeferredPhotoProcessor _establishServerConnection];
-[AVCaptureDeferredPhotoProcessor _executeBlockOnProcessorQueueSync:];
-[AVCaptureDeferredPhotoProcessor _getValueForBooleanProperty:];
-[AVCaptureDeferredPhotoProcessor _handleDidFinishProcessingPhotoProxyNotificationWithPayload:forRequest:];
-[AVCaptureDeferredPhotoProcessor _handleProcessorQueueBlockError:];
-[AVCaptureDeferredPhotoProcessor _handleServerConnectionDiedAndRequestsWillBeReenqueued];
-[AVCaptureDeferredPhotoProcessor _handleServerConnectionDiedSendingClientNotification:];
-[AVCaptureDeferredPhotoProcessor _handleWillAbortProcessingDueToPriorityInversion];
-[AVCaptureDeferredPhotoProcessor _handleWillBeginProcessingPhotoProxyNotificationWithPayload:forRequest:];
-[AVCaptureDeferredPhotoProcessor _processPhotoProxy:queuePosition:delegate:delegateQueue:];
-[AVCaptureDeferredPhotoProcessor _processingRequestForCaptureRequestIdentifier:];
-[AVCaptureDeferredPhotoProcessor _reenqueueRequestsAfterPriorityInversion];
-[AVCaptureDeferredPhotoProcessor _resetFigCaptureDeferredPhotoProcessor];
-[AVCaptureDeferredPhotoProcessor _setFigCaptureDeferredPhotoProcessor:];
-[AVCaptureDeferredPhotoProcessor cancelProcessingForPhotoProxy:error:];
-[AVCaptureDeferredPhotoProcessor initWithApplicationIDOverride:];
-[AVCaptureDeferredPhotoProcessor lastJobReusedGraph];
-[AVCaptureDeferredPhotoProcessor prettyPrintDescriptionForContainer:];
```
