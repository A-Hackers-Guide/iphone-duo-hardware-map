# `SBAlertLayoutPresentationVerifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBUIActiveOrientationObserver`, `SBReachabilityObserver`
- 10 instance variables, 4 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _pendingLayoutVerification;
B _pendingScheduledLayoutVerification;
@"NSMutableArray" _updateReasons;
@"UIWindow" _alertWindow;
@"SBSharedModalAlertItemPresenter" _alertPresenter;
@"SBWindowScene" _windowScene;
@"SBReachabilityController" _reachabilityController;
@"NSTimer" _bugCaptureTimer;
d _lastAutoBugCaptureEventTime;
d _firstLogEventTime;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBAlertLayoutPresentationVerifier activeInterfaceOrientationDidChangeToOrientation:willAnimateWithDuration:fromOrientation:];
-[SBAlertLayoutPresentationVerifier dealloc];
-[SBAlertLayoutPresentationVerifier activeInterfaceOrientationWillChangeToOrientation:];
-[SBAlertLayoutPresentationVerifier initWithWindowScene:];
-[SBAlertLayoutPresentationVerifier handleReachabilityYOffsetDidChange];
-[SBAlertLayoutPresentationVerifier scheduleAlertLayoutVerificationForReason:];
-[SBAlertLayoutPresentationVerifier scheduleDelayedAlertLayoutVerificationForReason:];
-[SBAlertLayoutPresentationVerifier setAlertItemWindow:];
-[SBAlertLayoutPresentationVerifier setAlertPresenter:];
```
