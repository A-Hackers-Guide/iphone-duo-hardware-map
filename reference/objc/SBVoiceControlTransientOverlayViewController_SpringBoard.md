# `SBVoiceControlTransientOverlayViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBTransientOverlayViewController`
- Protocols: `SBVoiceControlViewControllerDelegate`, `CSExternalBehaviorProviding`
- 3 instance variables, 16 properties, 62 instance methods, 0 class methods

## Instance variables

```
@"_UIBackdropView" _backdropView;
@"SBVoiceControlViewController" _contentViewController;
@"<SBVoiceControlTransientOverlayViewControllerDelegate>" _voiceControlDelegate;
```

## Properties

```
@property (T@"NSArray",C,N) nextRecognitionAudioInputPaths;
@property (TB,N) shouldAllowSensitiveActions;
@property (TB,N) shouldDisableHandlerActions;
@property (TB,N) shouldDisableVoiceControlForBluetoothRequests;
@property (TB,N,GisVoiceControlLoggingEnabled) voiceControlLoggingEnabled;
@property (T@"<SBVoiceControlTransientOverlayViewControllerDelegate>",W,N,V_voiceControlDelegate) voiceControlDelegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,R,N) scrollingStrategy;
@property (Tq,R,N) notificationBehavior;
@property (TQ,R,N) restrictedCapabilities;
@property (Tq,R,N) proximityDetectionMode;
@property (T@"NSString",R,C,N) coverSheetIdentifier;
@property (Tq,R,N) participantState;
```

## Instance methods

```
-[SBVoiceControlTransientOverlayViewController preferredUnlockedGestureDismissalStyle];
-[SBVoiceControlTransientOverlayViewController initWithSource:];
-[SBVoiceControlTransientOverlayViewController conformsToCSBehaviorProviding];
-[SBVoiceControlTransientOverlayViewController handleGestureDismissal];
-[SBVoiceControlTransientOverlayViewController childViewControllerForHomeIndicatorAutoHidden];
-[SBVoiceControlTransientOverlayViewController preferredInterfaceOrientationForPresentation];
-[SBVoiceControlTransientOverlayViewController newTransientOverlayPresentationTransitionCoordinator];
-[SBVoiceControlTransientOverlayViewController setContainerOrientation:];
-[SBVoiceControlTransientOverlayViewController viewWillDisappear:];
-[SBVoiceControlTransientOverlayViewController supportedInterfaceOrientations];
-[SBVoiceControlTransientOverlayViewController endIgnoringAppearanceUpdates];
-[SBVoiceControlTransientOverlayViewController dealloc];
-[SBVoiceControlTransientOverlayViewController becomeFirstResponder];
-[SBVoiceControlTransientOverlayViewController idleTimerDuration];
-[SBVoiceControlTransientOverlayViewController newTransientOverlayDismissalTransitionCoordinator];
-[SBVoiceControlTransientOverlayViewController proximityDetectionMode];
-[SBVoiceControlTransientOverlayViewController viewDidLoad];
-[SBVoiceControlTransientOverlayViewController shouldDisableOrientationUpdates];
-[SBVoiceControlTransientOverlayViewController viewDidLayoutSubviews];
-[SBVoiceControlTransientOverlayViewController shouldAutorotate];
-[SBVoiceControlTransientOverlayViewController resignFirstResponder];
-[SBVoiceControlTransientOverlayViewController _preferredStatusBarVisibility];
-[SBVoiceControlTransientOverlayViewController preferredWhitePointAdaptivityStyle];
-[SBVoiceControlTransientOverlayViewController viewWillMoveToWindow:];
-[SBVoiceControlTransientOverlayViewController viewWillAppear:];
-[SBVoiceControlTransientOverlayViewController _canShowWhileLocked];
-[SBVoiceControlTransientOverlayViewController viewDidAppear:];
-[SBVoiceControlTransientOverlayViewController canResignFirstResponder];
-[SBVoiceControlTransientOverlayViewController preferredLockedGestureDismissalStyle];
-[SBVoiceControlTransientOverlayViewController childViewControllerForScreenEdgesDeferringSystemGestures];
-[SBVoiceControlTransientOverlayViewController scrollingStrategy];
-[SBVoiceControlTransientOverlayViewController notificationBehavior];
-[SBVoiceControlTransientOverlayViewController beginIgnoringAppearanceUpdates];
-[SBVoiceControlTransientOverlayViewController viewDidDisappear:];
-[SBVoiceControlTransientOverlayViewController conformsToCSExternalBehaviorProviding];
-[SBVoiceControlTransientOverlayViewController idleTimerMode];
-[SBVoiceControlTransientOverlayViewController coverSheetIdentifier];
-[SBVoiceControlTransientOverlayViewController preferredStatusBarStyle];
-[SBVoiceControlTransientOverlayViewController canBecomeFirstResponder];
-[SBVoiceControlTransientOverlayViewController prefersEmbeddedDisplayPresentation];
-[SBVoiceControlTransientOverlayViewController idleWarnMode];
-[SBVoiceControlTransientOverlayViewController participantState];
-[SBVoiceControlTransientOverlayViewController restrictedCapabilities];
-[SBVoiceControlTransientOverlayViewController handleHomeButtonPress];
-[SBVoiceControlTransientOverlayViewController shouldAutomaticallyForwardAppearanceMethods];
-[SBVoiceControlTransientOverlayViewController setShouldAllowSensitiveActions:];
-[SBVoiceControlTransientOverlayViewController setShouldDisableHandlerActions:];
-[SBVoiceControlTransientOverlayViewController handleHeadsetButtonUpFromButtonDownSource:];
-[SBVoiceControlTransientOverlayViewController isVoiceControlLoggingEnabled];
-[SBVoiceControlTransientOverlayViewController nextRecognitionAudioInputPaths];
-[SBVoiceControlTransientOverlayViewController prefersProximityDetectionEnabled];
-[SBVoiceControlTransientOverlayViewController resetSessionWithSource:];
-[SBVoiceControlTransientOverlayViewController setNextRecognitionAudioInputPaths:];
-[SBVoiceControlTransientOverlayViewController setShouldDisableVoiceControlForBluetoothRequests:];
-[SBVoiceControlTransientOverlayViewController setVoiceControlDelegate:];
-[SBVoiceControlTransientOverlayViewController setVoiceControlLoggingEnabled:];
-[SBVoiceControlTransientOverlayViewController shouldAllowSensitiveActions];
-[SBVoiceControlTransientOverlayViewController shouldDisableHandlerActions];
-[SBVoiceControlTransientOverlayViewController shouldDisableVoiceControlForBluetoothRequests];
-[SBVoiceControlTransientOverlayViewController voiceControlDelegate];
-[SBVoiceControlTransientOverlayViewController voiceControlViewControllerPrefersProximityDetectionEnabledDidChange:];
-[SBVoiceControlTransientOverlayViewController voiceControlViewControllerRequestsDismissal:];
```
