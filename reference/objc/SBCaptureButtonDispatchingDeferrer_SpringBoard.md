# `SBCaptureButtonDispatchingDeferrer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFZStackParticipantObserver`, `SBCaptureButtonRestrictionObserver`, `FBSceneObserver`
- 8 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"BKSHIDEventDeliveryManager" _deliveryManager;
@"SBFZStackResolver" _zStackResolver;
i _currentDeferralTargetPid;
@"FBSSceneIdentityToken" _currentDeferralSceneIdentityToken;
@"FBScene" _targetScene;
@"<BSInvalidatable>" _deferringRuleAssertion;
@"<BSInvalidatable>" _inhibitionObservation;
B _inhibitedDueToRestrictionCoordinator;
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
-[SBCaptureButtonDispatchingDeferrer scene:clientDidConnect:];
-[SBCaptureButtonDispatchingDeferrer zStackParticipantWithIdentifier:settingsDidChange:];
-[SBCaptureButtonDispatchingDeferrer _processZStackParticipantSettings:];
-[SBCaptureButtonDispatchingDeferrer _stopDeferringCaptureButtonEvents];
-[SBCaptureButtonDispatchingDeferrer zStackParticipantWithIdentifier:wasAcquiredWithSettings:];
-[SBCaptureButtonDispatchingDeferrer _updateCaptureButtonDispatchingDeferringTarget];
-[SBCaptureButtonDispatchingDeferrer dealloc];
-[SBCaptureButtonDispatchingDeferrer captureButtonRestrictionChangedTo:];
-[SBCaptureButtonDispatchingDeferrer initWithZStackResolver:restrictionCoordinator:];
-[SBCaptureButtonDispatchingDeferrer _deferCaptureButtonEventsToSceneWithIdentityToken:PID:];
```
