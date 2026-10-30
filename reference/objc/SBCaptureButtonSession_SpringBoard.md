# `SBCaptureButtonSession`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSDisplayLayoutPublisherObserving`, `SBAppInteractionEventSourceObserving`, `BSInvalidatable`
- 9 instance variables, 5 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _interactions;
@"BSAbsoluteMachTimer" _timer;
B _sealed;
@"NSString" _captureAppBundleID;
B _inCaptureApp;
@"BSAbsoluteMachTimer" _captureAppInteractionTimer;
@"SBDisplayAppInteractionEventSource" _displayAppInteractionEventSource;
@"<FBSDisplayLayoutPublishing>" _displayLayoutPublisher;
@"<SBCaptureButtonSessionDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBCaptureButtonSessionDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBCaptureButtonSession eventSource:userTouchedApplication:];
-[SBCaptureButtonSession dealloc];
-[SBCaptureButtonSession publisher:didUpdateLayout:withTransition:];
-[SBCaptureButtonSession invalidate];
-[SBCaptureButtonSession setDelegate:];
-[SBCaptureButtonSession _handleNotification:];
-[SBCaptureButtonSession delegate];
-[SBCaptureButtonSession isActive];
-[SBCaptureButtonSession logToCoreAnalytics];
-[SBCaptureButtonSession _startCountdown];
-[SBCaptureButtonSession _sealIntentionalLaunch];
-[SBCaptureButtonSession _sealIntentionalMitigation];
-[SBCaptureButtonSession _sealLowConfidenceIntentionalLaunch];
-[SBCaptureButtonSession _sealUnintentionalLaunch];
-[SBCaptureButtonSession _sealWithReason:block:];
-[SBCaptureButtonSession _startCaptureInteractionTimer];
-[SBCaptureButtonSession coalesceInteraction:];
-[SBCaptureButtonSession initWithInteraction:delegate:];
-[SBCaptureButtonSession logInteractionIntentions];
-[SBCaptureButtonSession sealAsUnintentionalDueToDisplaySwap];
```
