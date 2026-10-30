# `SBAssistantSession`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CSExternalBehaviorProviding`, `SBAssistantGestureManagerDelegate`
- 27 instance variables, 38 properties, 94 instance methods, 0 class methods

## Instance variables

```
@"SBFluidDismissalState" _fluidDismissalState;
@"<BSInvalidatable>" _traitsOrientationPolicySpecifier;
@"SBAssistantSessionPresentationContext" _presentationContext;
@"<BSInvalidatable>" _hostedLayoutElementAssertion;
@"SBSDisplayLayoutElement" _hostedLayoutElement;
B _visible;
B _hidingOtherWindows;
B _pendingAlerts;
B _providingCoverSheetBehavior;
B _wantsDeemphasizedBackdrop;
@"SBAssistantWindow" _assistantWindow;
@"SiriPresentationSpringBoardMainScreenViewController" _siriPresentationViewController;
@"SBAssistantAccessoryWindow" _assistantAccessoryWindow;
@"UIViewController" _siriEffectsViewController;
@"BSCompoundAssertion" _elevatedSiriEffectsViewControllerAssertion;
@"BSEventQueue" _operationQueue;
@"SBAssistantContext" _context;
@"UIApplicationSceneDeactivationAssertion" _resignActiveAssertion;
@"SBAssistantGestureConfiguration" _gestureConfiguration;
@"SBAssistantGestureManager" _gestureManager;
@"<BSInvalidatable>" _displayLayoutAssertion;
@"<BSInvalidatable>" _suspendWallpaperAnimationAssertion;
@"<BSInvalidatable>" _hideApplicationModalAlertsAssertion;
@"<BSInvalidatable>" _deferOrientationUpdatesAssertion;
@"<SBHardwareButtonLaunchZoomUpAnimationToken>" _externalDropletZoomUpToken;
@"<SBAssistantSessionDelegate>" _delegate;
@"SBWindowScene" _windowScene;
```

## Properties

```
@property (T@"SBAssistantWindow",&,N,V_assistantWindow) assistantWindow;
@property (T@"SiriPresentationSpringBoardMainScreenViewController",&,N,V_siriPresentationViewController) siriPresentationViewController;
@property (T@"SBAssistantAccessoryWindow",&,N,V_assistantAccessoryWindow) assistantAccessoryWindow;
@property (T@"UIViewController",&,N,V_siriEffectsViewController) siriEffectsViewController;
@property (T@"BSCompoundAssertion",&,N,V_elevatedSiriEffectsViewControllerAssertion) elevatedSiriEffectsViewControllerAssertion;
@property (T@"BSEventQueue",R,N,V_operationQueue) operationQueue;
@property (T@"SBAssistantContext",R,N,V_context) context;
@property (T@"UIApplicationSceneDeactivationAssertion",R,N,V_resignActiveAssertion) resignActiveAssertion;
@property (T@"SBAssistantGestureConfiguration",&,N,V_gestureConfiguration) gestureConfiguration;
@property (T@"SBAssistantGestureManager",&,N,V_gestureManager) gestureManager;
@property (TB,N,GisVisible,V_visible) visible;
@property (TB,N,GisHidingOtherWindows,V_hidingOtherWindows) hidingOtherWindows;
@property (TB,N,GisPendingAlerts,V_pendingAlerts) pendingAlerts;
@property (TB,N,GisProvidingCoverSheetBehavior,V_providingCoverSheetBehavior) providingCoverSheetBehavior;
@property (T@"<BSInvalidatable>",&,N,V_displayLayoutAssertion) displayLayoutAssertion;
@property (T@"<BSInvalidatable>",&,N,V_suspendWallpaperAnimationAssertion) suspendWallpaperAnimationAssertion;
@property (T@"<BSInvalidatable>",&,N,V_hideApplicationModalAlertsAssertion) hideApplicationModalAlertsAssertion;
@property (T@"<BSInvalidatable>",&,N,V_deferOrientationUpdatesAssertion) deferOrientationUpdatesAssertion;
@property (T@"<SBHardwareButtonLaunchZoomUpAnimationToken>",&,N,V_externalDropletZoomUpToken) externalDropletZoomUpToken;
@property (T@"SBAssistantSessionPresentationContext",&,N) presentationContext;
@property (T@"<SBAssistantSessionDelegate>",W,N,V_delegate) delegate;
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (TB,R,N) contentObscuresScreen;
@property (TB,R,N) shouldAllowBiometricAutoUnlock;
@property (TB,N,V_wantsDeemphasizedBackdrop) wantsDeemphasizedBackdrop;
@property (T@"SBWindow",R,N) window;
@property (T@"SBAssistantRootViewController",R,N) assistantRootViewController;
@property (TB,R,N,GisActive) active;
@property (Tq,R,N) scrollingStrategy;
@property (Tq,R,N) notificationBehavior;
@property (TQ,R,N) restrictedCapabilities;
@property (Tq,R,N) proximityDetectionMode;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,C,N) coverSheetIdentifier;
@property (Tq,R,N) participantState;
```

## Instance methods

```
-[SBAssistantSession deferOrientationUpdatesAssertion];
-[SBAssistantSession setDeferOrientationUpdatesAssertion:];
-[SBAssistantSession displayLayoutAssertion];
-[SBAssistantSession _setDisplayLayoutElementActive:];
-[SBAssistantSession conformsToCSBehaviorProviding];
-[SBAssistantSession setSuspendWallpaperAnimationAssertion:];
-[SBAssistantSession observeValueForKeyPath:ofObject:change:context:];
-[SBAssistantSession setVisible:];
-[SBAssistantSession assistantRootViewController];
-[SBAssistantSession resignActiveAssertion];
-[SBAssistantSession presentationContext];
-[SBAssistantSession setPresentationContext:];
-[SBAssistantSession suspendWallpaperAnimationAssertion];
-[SBAssistantSession dealloc];
-[SBAssistantSession proximityDetectionMode];
-[SBAssistantSession isVisible];
-[SBAssistantSession window];
-[SBAssistantSession gestureManager];
-[SBAssistantSession setGestureManager:];
-[SBAssistantSession setDelegate:];
-[SBAssistantSession scrollingStrategy];
-[SBAssistantSession notificationBehavior];
-[SBAssistantSession delegate];
-[SBAssistantSession conformsToCSExternalBehaviorProviding];
-[SBAssistantSession coverSheetIdentifier];
-[SBAssistantSession isActive];
-[SBAssistantSession operationQueue];
-[SBAssistantSession commandeerCaptureDropletPreludeForVisionInvocation:];
-[SBAssistantSession windowScene];
-[SBAssistantSession setDisplayLayoutAssertion:];
-[SBAssistantSession context];
-[SBAssistantSession participantState];
-[SBAssistantSession restrictedCapabilities];
-[SBAssistantSession shouldAllowBiometricAutoUnlock];
-[SBAssistantSession requestTamaleLaunchAnimationLayerProviderWithCompletion:];
-[SBAssistantSession setSiriEffectsViewController:];
-[SBAssistantSession siriEffectsViewController];
-[SBAssistantSession assistantWindow];
-[SBAssistantSession isPendingAlerts];
-[SBAssistantSession setProvidingCoverSheetBehavior:];
-[SBAssistantSession _didChangePresentationContext];
-[SBAssistantSession _dockFrameDidChange:];
-[SBAssistantSession _newTraitsOrientationPolicySpecifier];
-[SBAssistantSession _notifyDidChangePresentationContext];
-[SBAssistantSession _notifySiriPresentationViewControllerDidAppear];
-[SBAssistantSession _notifySiriPresentationViewControllerDidDisappear];
-[SBAssistantSession _notifySiriPresentationViewControllerWillAppear];
-[SBAssistantSession _notifySiriPresentationViewControllerWillDisappear];
-[SBAssistantSession _operationQueue_dismissPresentables:withAnimationFactory:siriDismissalOptions:completion:];
-[SBAssistantSession _restoreStatusBarOrientation];
-[SBAssistantSession _setStatusBarHidden:animated:];
-[SBAssistantSession _siriPresentationViewControllerDidAppear:];
-[SBAssistantSession _siriPresentationViewControllerDidDisappear:];
-[SBAssistantSession _siriPresentationViewControllerWillAppear:];
-[SBAssistantSession _siriPresentationViewControllerWillDisappear:];
-[SBAssistantSession _supportsHomeScreenRotation];
-[SBAssistantSession _toggleModalAlertHidingAssertion:];
-[SBAssistantSession _updateAssistantAccessoryWindowWindowLevel];
-[SBAssistantSession _updateDockViewFrame:];
-[SBAssistantSession _updateOrbLocation:];
-[SBAssistantSession _updateOrientationLock];
-[SBAssistantSession acquireElevatedSiriEffectsViewControllerAssertionWithReason:];
-[SBAssistantSession assertWindowLevel:];
-[SBAssistantSession assistantAccessoryWindow];
-[SBAssistantSession assistantGestureManagerDidRecognizeDismissGesture:preferredDismissalOptions:];
-[SBAssistantSession contentObscuresScreen];
-[SBAssistantSession dismissSiriEffectsViewControllerWithCompletion:];
-[SBAssistantSession dismissSiriPresentationViewControllerWithAnimationFactory:siriDismissalOptions:completion:];
-[SBAssistantSession elevatedSiriEffectsViewControllerAssertion];
-[SBAssistantSession endWithAnimationFactory:siriDismissalOptions:completion:];
-[SBAssistantSession externalDropletZoomUpToken];
-[SBAssistantSession gestureConfiguration];
-[SBAssistantSession hideApplicationModalAlertsAssertion];
-[SBAssistantSession initWithWindowScene:operationQueue:gestureConfiguration:];
-[SBAssistantSession isHidingOtherWindows];
-[SBAssistantSession isProvidingCoverSheetBehavior];
-[SBAssistantSession noteKeyboardWillAppear];
-[SBAssistantSession noteKeyboardWillDisappear];
-[SBAssistantSession presentSiriEffectsViewController:completion:];
-[SBAssistantSession presentSiriPresentationViewController:withAnimationFactory:siriPresentationOptions:completion:];
-[SBAssistantSession setAssistantAccessoryWindow:];
-[SBAssistantSession setAssistantWindow:];
-[SBAssistantSession setElevatedSiriEffectsViewControllerAssertion:];
-[SBAssistantSession setExternalDropletZoomUpToken:];
-[SBAssistantSession setGestureConfiguration:];
-[SBAssistantSession setHideApplicationModalAlertsAssertion:];
-[SBAssistantSession setHidingOtherWindows:];
-[SBAssistantSession setPendingAlerts:];
-[SBAssistantSession setSiriPresentationViewController:];
-[SBAssistantSession setWantsDeemphasizedBackdrop:];
-[SBAssistantSession siriPresentationViewController];
-[SBAssistantSession siriStartedHostingSceneWithIdentifier:bundleIdentifier:];
-[SBAssistantSession siriStoppedHostingSceneWithIdentifier:bundleIdentifier:];
-[SBAssistantSession wantsDeemphasizedBackdrop];
```
