# `SBDeviceApplicationSceneOverlayViewProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 7 instance variables, 15 properties, 35 instance methods, 0 class methods

## Instance variables

```
@"SBIsolatedSceneOrientationFollowingWrapperViewController" _orientationWrapperViewController;
@"SBDeviceApplicationSceneOverlayBasicWrapperViewController" _basicWrapperViewController;
Q _reportedSupportedInterfaceOrientations;
B _prefersStatusBarHidden;
B _contentWantsSimplifiedOrientationBehavior;
@"<SBDeviceApplicationSceneOverlayViewProviderDelegate>" _delegate;
@"SBDeviceApplicationSceneHandle" _sceneHandle;
```

## Properties

```
@property (T@"SBDeviceApplicationSceneHandle",&,N,V_sceneHandle) sceneHandle;
@property (T@"<SBDeviceApplicationSceneOverlayViewProviderDelegate>",R,W,N,V_delegate) delegate;
@property (T@"UIViewController<SBDeviceApplicationSceneOverlayViewController>",R,N) overlayViewController;
@property (TB,R,N) constrainsContainingSceneOrientation;
@property (TB,R,N) affectsStatusBarPresentation;
@property (TB,R,N,V_prefersStatusBarHidden) prefersStatusBarHidden;
@property (Tq,R,N) preferredStatusBarStyle;
@property (TB,R,N) shouldSuppressKeyboard;
@property (TB,R,N) wantsResignActiveAssertion;
@property (TB,R,N,V_contentWantsSimplifiedOrientationBehavior) contentWantsSimplifiedOrientationBehavior;
@property (Tq,R,N) priority;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDeviceApplicationSceneOverlayViewProvider priority];
-[SBDeviceApplicationSceneOverlayViewProvider _realOverlayViewController];
-[SBDeviceApplicationSceneOverlayViewProvider sceneHandle];
-[SBDeviceApplicationSceneOverlayViewProvider preferredInterfaceOrientationForPresentation];
-[SBDeviceApplicationSceneOverlayViewProvider noteLiveContentDisableReasonsChanged];
-[SBDeviceApplicationSceneOverlayViewProvider supportedInterfaceOrientations];
-[SBDeviceApplicationSceneOverlayViewProvider hideContentWithAnimation:completionHandler:];
-[SBDeviceApplicationSceneOverlayViewProvider contentWantsSimplifiedOrientationBehavior];
-[SBDeviceApplicationSceneOverlayViewProvider dealloc];
-[SBDeviceApplicationSceneOverlayViewProvider handledStatusBarTap:type:];
-[SBDeviceApplicationSceneOverlayViewProvider initWithSceneHandle:delegate:];
-[SBDeviceApplicationSceneOverlayViewProvider _activateIfPossible];
-[SBDeviceApplicationSceneOverlayViewProvider invalidate];
-[SBDeviceApplicationSceneOverlayViewProvider showContentWithAnimation:completionHandler:];
-[SBDeviceApplicationSceneOverlayViewProvider noteDisplayModeChange:];
-[SBDeviceApplicationSceneOverlayViewProvider _deactivateIfPossible];
-[SBDeviceApplicationSceneOverlayViewProvider prepareForContainingSceneMovingToWindowScene:];
-[SBDeviceApplicationSceneOverlayViewProvider delegate];
-[SBDeviceApplicationSceneOverlayViewProvider wantsResignActiveAssertion];
-[SBDeviceApplicationSceneOverlayViewProvider shouldSuppressKeyboard];
-[SBDeviceApplicationSceneOverlayViewProvider containerDidUpdateTraitsParticipant:];
-[SBDeviceApplicationSceneOverlayViewProvider preferredStatusBarStyle];
-[SBDeviceApplicationSceneOverlayViewProvider prefersStatusBarHidden];
-[SBDeviceApplicationSceneOverlayViewProvider setSceneHandle:];
-[SBDeviceApplicationSceneOverlayViewProvider shouldFollowSceneOrientation];
-[SBDeviceApplicationSceneOverlayViewProvider overlayViewController];
-[SBDeviceApplicationSceneOverlayViewProvider _contentSupportedInterfaceOrientationsRequireContainerCounterRotation];
-[SBDeviceApplicationSceneOverlayViewProvider _mightNeedCounterRotationForBasicContentWrapper];
-[SBDeviceApplicationSceneOverlayViewProvider _noteSupportedInterfaceOrientationsChanged];
-[SBDeviceApplicationSceneOverlayViewProvider affectsStatusBarPresentation];
-[SBDeviceApplicationSceneOverlayViewProvider bestHomeAffordanceOrientationForOrientation:];
-[SBDeviceApplicationSceneOverlayViewProvider configureForSecureDisplay:];
-[SBDeviceApplicationSceneOverlayViewProvider constrainsContainingSceneOrientation];
-[SBDeviceApplicationSceneOverlayViewProvider initialTraitsParticipantForOverlayContainer];
-[SBDeviceApplicationSceneOverlayViewProvider willDoBoundsPreservingRotationFromInterfaceOrientation:toInterfaceOrientation:];
```
