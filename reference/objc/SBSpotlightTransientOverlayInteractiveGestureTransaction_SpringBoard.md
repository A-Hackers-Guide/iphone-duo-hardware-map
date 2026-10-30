# `SBSpotlightTransientOverlayInteractiveGestureTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSpotlightInteractiveGestureTransaction`
- Protocols: `BSTransactionObserver`
- 5 instance variables, 8 properties, 21 instance methods, 0 class methods

## Instance variables

```
B _gestureFinishedBeforeTransactionBegan;
@"SBSpotlightSettings" _settings;
@"SBAppSwitcherSettings" _switcherSettings;
@"SBSpotlightTransientOverlayViewController" _spotlightTransientOverlayViewController;
@"SBMainWorkspaceTransaction" _presentTransientOverlayTransaction;
```

## Properties

```
@property (T@"SBSpotlightSettings",&,N,V_settings) settings;
@property (T@"SBAppSwitcherSettings",&,N,V_switcherSettings) switcherSettings;
@property (T@"SBSpotlightTransientOverlayViewController",&,N,V_spotlightTransientOverlayViewController) spotlightTransientOverlayViewController;
@property (T@"SBMainWorkspaceTransaction",&,N,V_presentTransientOverlayTransaction) presentTransientOverlayTransaction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSpotlightTransientOverlayInteractiveGestureTransaction canInterruptForTransitionRequest:];
-[SBSpotlightTransientOverlayInteractiveGestureTransaction switcherSettings];
-[SBSpotlightTransientOverlayInteractiveGestureTransaction _didComplete];
-[SBSpotlightTransientOverlayInteractiveGestureTransaction _begin];
-[SBSpotlightTransientOverlayInteractiveGestureTransaction transactionDidComplete:];
-[SBSpotlightTransientOverlayInteractiveGestureTransaction setSettings:];
-[SBSpotlightTransientOverlayInteractiveGestureTransaction settings];
-[SBSpotlightTransientOverlayInteractiveGestureTransaction _logForInterruptAttemptReason:];
-[SBSpotlightTransientOverlayInteractiveGestureTransaction _homeScreenAnimator];
-[SBSpotlightTransientOverlayInteractiveGestureTransaction setSwitcherSettings:];
-[SBSpotlightTransientOverlayInteractiveGestureTransaction endPresentation:];
-[SBSpotlightTransientOverlayInteractiveGestureTransaction updatePresentationWithProgress:translation:];
-[SBSpotlightTransientOverlayInteractiveGestureTransaction _dismissSpotlightTransientOverlayViewController];
-[SBSpotlightTransientOverlayInteractiveGestureTransaction _presentTransientOverlayViewController:];
-[SBSpotlightTransientOverlayInteractiveGestureTransaction initWithTransitionRequest:spotlightTransientOverlayViewController:];
-[SBSpotlightTransientOverlayInteractiveGestureTransaction noteGestureFinishedBeforeTransactionBegan];
-[SBSpotlightTransientOverlayInteractiveGestureTransaction presentTransientOverlayTransaction];
-[SBSpotlightTransientOverlayInteractiveGestureTransaction setLockScreenScale:withDuration:behaviorMode:completion:];
-[SBSpotlightTransientOverlayInteractiveGestureTransaction setPresentTransientOverlayTransaction:];
-[SBSpotlightTransientOverlayInteractiveGestureTransaction setSpotlightTransientOverlayViewController:];
-[SBSpotlightTransientOverlayInteractiveGestureTransaction spotlightTransientOverlayViewController];
```
