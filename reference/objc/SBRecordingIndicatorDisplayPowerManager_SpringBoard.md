# `SBRecordingIndicatorDisplayPowerManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDisplayContentModeTransitionObserver`, `SBRecordingIndicatorDisplayPowerManaging`
- 7 instance variables, 10 properties, 18 instance methods, 0 class methods

## Instance variables

```
B _hasReportedDisplayPowerRequired;
B _lastReportedDisplayPowerRequired;
B _windowSceneActive;
B _secureStateWantsWindowSceneActive;
@"BSCompoundAssertion" _displayPowerAssertion;
@"<SBRecordingIndicatorDisplayPowerManagerDelegate>" _delegate;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"BSCompoundAssertion",R,N,V_displayPowerAssertion) displayPowerAssertion;
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (TB,R,N) displayPowerRequired;
@property (T@"<SBRecordingIndicatorDisplayPowerManagerDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisWindowSceneActive,V_windowSceneActive) windowSceneActive;
@property (TB,N,V_secureStateWantsWindowSceneActive) secureStateWantsWindowSceneActive;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBRecordingIndicatorDisplayPowerManager setWindowScene:];
-[SBRecordingIndicatorDisplayPowerManager init];
-[SBRecordingIndicatorDisplayPowerManager windowSceneDidDisconnect:];
-[SBRecordingIndicatorDisplayPowerManager displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBRecordingIndicatorDisplayPowerManager displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBRecordingIndicatorDisplayPowerManager setDelegate:];
-[SBRecordingIndicatorDisplayPowerManager displayPowerAssertion];
-[SBRecordingIndicatorDisplayPowerManager delegate];
-[SBRecordingIndicatorDisplayPowerManager windowSceneDidConnect:];
-[SBRecordingIndicatorDisplayPowerManager acquireDisplayPowerAssertionForReason:];
-[SBRecordingIndicatorDisplayPowerManager windowScene];
-[SBRecordingIndicatorDisplayPowerManager _displayPowerAssertionDidUpdate];
-[SBRecordingIndicatorDisplayPowerManager _leaveBothOnAlways];
-[SBRecordingIndicatorDisplayPowerManager displayPowerRequired];
-[SBRecordingIndicatorDisplayPowerManager isWindowSceneActive];
-[SBRecordingIndicatorDisplayPowerManager secureStateWantsWindowSceneActive];
-[SBRecordingIndicatorDisplayPowerManager setSecureStateWantsWindowSceneActive:];
-[SBRecordingIndicatorDisplayPowerManager setWindowSceneActive:];
```
