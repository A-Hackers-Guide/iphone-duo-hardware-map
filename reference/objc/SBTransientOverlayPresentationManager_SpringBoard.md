# `SBTransientOverlayPresentationManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBIdleTimerCoordinating`, `SBTransientOverlayScenePresenterObserver`, `SBDisplayContentModeTransitionObserver`, `SBIdleTimerProviding`, `SBWindowSceneAttachmentObserving`, `SBButtonEventsHandler`
- 11 instance variables, 17 properties, 53 instance methods, 0 class methods

## Instance variables

```
@"SBWindowSceneManager" _windowSceneManager;
@"NSMapTable" _presentersByWindowScene;
@"SBAlertItemsController" _alertItemsController;
@"SBBannerManager" _bannerManager;
@"SBInCallPresentationManager" _inCallPresentationManager;
@"SBIdleTimerCoordinatorHelper" _idleTimerCoordinatorHelper;
@"SBDisplayContentModeCoordinator" _displayContentModeCoordinator;
@"SBWindowScene" _activeWindowSceneForPresentation;
@"SBWindowScene" _transitioningFromWindowScene;
@"NSHashTable" _observers;
@"<SBTransientOverlayScenePresenterDelegate>" _presenterDelegate;
```

## Properties

```
@property (T@"<SBTransientOverlayScenePresenterDelegate>",W,N,V_presenterDelegate) presenterDelegate;
@property (T@"<SBIdleTimerCoordinating>",W,N) idleTimerCoordinator;
@property (TB,R,N) hasActivePresentation;
@property (TB,R,N) canActivePresentationBecomeLocalFirstResponder;
@property (TB,R,N) canActivePresentationBecomeFirstResponder;
@property (Tq,R,N) presentedViewControllerCount;
@property (TB,R,N) shouldUseSceneBasedKeyboardFocusForActivePresentation;
@property (TB,R,N) prefersStatusBarActivityItemVisible;
@property (TB,R,N) shouldDisableControlCenter;
@property (TB,R,N) shouldDisableCoverSheetGesture;
@property (TB,R,N) shouldDisableSiri;
@property (TB,R,N) activePresentationPreventsDragAndDrop;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) hasIdleTimerBehaviors;
```

## Instance methods

```
-[SBTransientOverlayPresentationManager isTopmostPresentedViewController:];
-[SBTransientOverlayPresentationManager isPresentingViewController:];
-[SBTransientOverlayPresentationManager hasActivePresentationFromBundleIdentifier:];
-[SBTransientOverlayPresentationManager topmostPresentedViewController];
-[SBTransientOverlayPresentationManager hasActivePresentation];
-[SBTransientOverlayPresentationManager shouldUseSceneBasedKeyboardFocusForActivePresentation];
-[SBTransientOverlayPresentationManager canActivePresentationBecomeLocalFirstResponder];
-[SBTransientOverlayPresentationManager transientOverlayPresenterForWindowScene:];
-[SBTransientOverlayPresentationManager shouldDisableCoverSheetGesture];
-[SBTransientOverlayPresentationManager idleTimerProvider:didProposeBehavior:forReason:];
-[SBTransientOverlayPresentationManager performPresentationRequest:];
-[SBTransientOverlayPresentationManager presentedViewControllerCount];
-[SBTransientOverlayPresentationManager hasActiveSpotlightPresentation];
-[SBTransientOverlayPresentationManager handleVolumeDownButtonPress];
-[SBTransientOverlayPresentationManager isTopmostPresentationFromSceneWithIdentityTokenString:];
-[SBTransientOverlayPresentationManager transientOverlayScenePresenter:didDismissViewController:wasTopmostPresentation:];
-[SBTransientOverlayPresentationManager hasActivePresentationFromProcess:];
-[SBTransientOverlayPresentationManager prefersStatusBarActivityItemVisible];
-[SBTransientOverlayPresentationManager hasPresentationAboveWindowLevel:];
-[SBTransientOverlayPresentationManager activePresentationPreventsDragAndDrop];
-[SBTransientOverlayPresentationManager transientOverlayScenePresenter:willPresentViewController:];
-[SBTransientOverlayPresentationManager handleHomeButtonLongPress];
-[SBTransientOverlayPresentationManager removeObserver:];
-[SBTransientOverlayPresentationManager windowSceneDidDisconnect:];
-[SBTransientOverlayPresentationManager displayContentModeCoordinator:handleDisplayContentModeTransition:];
-[SBTransientOverlayPresentationManager handleVoiceCommandButtonPress];
-[SBTransientOverlayPresentationManager dealloc];
-[SBTransientOverlayPresentationManager displayContentModeCoordinator:handleSwapTransitionFromPrimaryWindowScene:toPrimaryWindowScene:withContinuationLockProvider:];
-[SBTransientOverlayPresentationManager initWithWindowSceneManager:alertItemsController:bannerManager:inCallPresentationManager:displayContentModeCoordinator:];
-[SBTransientOverlayPresentationManager canActivePresentationBecomeFirstResponder];
-[SBTransientOverlayPresentationManager hasActivePresentationForWindowScene:];
-[SBTransientOverlayPresentationManager handleHeadsetButtonPress:];
-[SBTransientOverlayPresentationManager setIdleTimerCoordinator:];
-[SBTransientOverlayPresentationManager handleLockButtonPress];
-[SBTransientOverlayPresentationManager handleVolumeUpButtonPress];
-[SBTransientOverlayPresentationManager shouldDisableSiri];
-[SBTransientOverlayPresentationManager preferredDisplayConfigurationForPresentingTransientOverlayViewController:];
-[SBTransientOverlayPresentationManager handleHomeButtonDoublePress];
-[SBTransientOverlayPresentationManager addObserver:];
-[SBTransientOverlayPresentationManager shouldDisableControlCenter];
-[SBTransientOverlayPresentationManager performDismissalRequest:];
-[SBTransientOverlayPresentationManager idleTimerCoordinator];
-[SBTransientOverlayPresentationManager defaultDisplayConfigurationForTransientOverlayPresentation];
-[SBTransientOverlayPresentationManager keyboardFocusTargetForSBWindowScene:];
-[SBTransientOverlayPresentationManager _targetWindowSceneForEmbeddedDisplayTransientOverlayPresentation];
-[SBTransientOverlayPresentationManager hasIdleTimerBehaviors];
-[SBTransientOverlayPresentationManager presenterDelegate];
-[SBTransientOverlayPresentationManager windowSceneDidConnect:];
-[SBTransientOverlayPresentationManager _defaultWindowSceneForTransientOverlayPresentation];
-[SBTransientOverlayPresentationManager setPresenterDelegate:];
-[SBTransientOverlayPresentationManager handleHomeButtonPress];
-[SBTransientOverlayPresentationManager preferredWindowSceneForPresentingTransientOverlayViewController:];
-[SBTransientOverlayPresentationManager coordinatorRequestedIdleTimerBehavior:];
```
