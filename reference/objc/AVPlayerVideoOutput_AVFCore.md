# `AVPlayerVideoOutput`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 16 instance methods, 0 class methods

## Instance variables

```
{?="stateQueue"@"NSObject<OS_dispatch_queue>""weakPlayer"@"AVPlayer""videoTarget"^{OpaqueFigVideoTarget}"videoReceiver"^{OpaqueFigVideoReceiver}"lastSeenTaggedBufferGroup"^{OpaqueCMTaggedBufferGroup}"activeConfiguration"@"AVPlayerVideoOutputConfiguration"} _receiverState;
@"NSObject<OS_dispatch_queue>" _iVarAccessQueue;
@"AVVideoOutputSpecification" _outputSpecification;
@? _resourceLifeCycleHandler;
```

## Instance methods

```
-[AVPlayerVideoOutput dealloc];
-[AVPlayerVideoOutput initWithSpecification:];
-[AVPlayerVideoOutput _attachToPlayer:exceptionReason:];
-[AVPlayerVideoOutput _copyTaggedBufferGroupForHostTimeInternal:doNotConsume:presentationTimeStamp:activeConfiguration:lastSeenTaggedBufferGroup:];
-[AVPlayerVideoOutput _copyVideoTarget];
-[AVPlayerVideoOutput _createAndConfigureVideoReceiverIfNecessaryOnStateQueue];
-[AVPlayerVideoOutput _detachFromPlayer:];
-[AVPlayerVideoOutput _handleVideoReceiverActiveConfigurationChanged:];
-[AVPlayerVideoOutput _playerItemWithIdentifier:];
-[AVPlayerVideoOutput _setResourceLifeCycleHandler:];
-[AVPlayerVideoOutput _setUpVideoReceiverEventHandlers:];
-[AVPlayerVideoOutput _setupWithOutputSpecification:exceptionReasonOut:];
-[AVPlayerVideoOutput attachedPlayer];
-[AVPlayerVideoOutput copyTaggedBufferGroupForHostTime:presentationTimeStamp:activeConfiguration:];
-[AVPlayerVideoOutput hasNewTaggedBufferGroupForHostTime:];
-[AVPlayerVideoOutput resourceLifeCycleHandler];
```
