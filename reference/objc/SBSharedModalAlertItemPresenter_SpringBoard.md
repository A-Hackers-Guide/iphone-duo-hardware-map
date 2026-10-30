# `SBSharedModalAlertItemPresenter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_SBAlertControllerDelegate`, `SBModalViewControllerStackDelegate`, `UIAlertControllerCoordinatedActionPerforming`, `SBBarSwipeAffordanceObserver`, `SBBarSwipeAffordanceDelegate`, `SBFZStackParticipantDelegate`, `SBHomeGrabberPointerClickDelegate`, `SBReachabilityObserver`, `BSInvalidatable`
- 10 instance variables, 7 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"<SBFLockOutStatusProvider>" _lockOutProvider;
@"SBSystemGestureManager" _systemGestureManager;
@"SBFZStackParticipant" _zStackParticipant;
@"SBFZStackResolver" _zStackResolver;
@"SBReachabilityController" _reachabilityController;
@"SBAlertLayoutPresentationVerifier" _alertLayoutPresentationVerifier;
@"SBBarSwipeAffordanceView" _barSwipeView;
@"SBModalViewControllerStack" _modalViewControllerStack;
@"SBWindow" _window;
@"<BSInvalidatable>" _windowConstraint;
```

## Properties

```
@property (T@"SBModalViewControllerStack",&,N,G_modalViewControllerStack,S_setModalViewControllerStack:,V_modalViewControllerStack) modalViewControllerStack;
@property (T@"SBWindowScene",R,W,N) windowScene;
@property (T@"SBAlertItem",R,N) currentlyPresentedAlertItem;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSharedModalAlertItemPresenter homeGrabberViewDidReceiveClick:];
-[SBSharedModalAlertItemPresenter zStackParticipant:updatePreferences:];
-[SBSharedModalAlertItemPresenter barSwipeAffordanceView:systemGestureTypeForType:];
-[SBSharedModalAlertItemPresenter dealloc];
-[SBSharedModalAlertItemPresenter zStackParticipantDidChange:];
-[SBSharedModalAlertItemPresenter zStackParticipant:updateZOrderPreferences:];
-[SBSharedModalAlertItemPresenter homeGesturePerformedForBarSwipeAffordanceView:];
-[SBSharedModalAlertItemPresenter invalidate];
-[SBSharedModalAlertItemPresenter handleReachabilityYOffsetDidChange];
-[SBSharedModalAlertItemPresenter windowScene];
-[SBSharedModalAlertItemPresenter _performActionForAlertController:invokeActionBlock:dismissControllerBlock:];
-[SBSharedModalAlertItemPresenter alertControllerDidDisappear:];
-[SBSharedModalAlertItemPresenter initWithLockOutProvider:systemGestureManager:reachabilityController:alertLayoutPresentationVerifier:windowScene:enableGestures:];
-[SBSharedModalAlertItemPresenter _modalViewControllerStack];
-[SBSharedModalAlertItemPresenter _setModalViewControllerStack:];
-[SBSharedModalAlertItemPresenter _updateBarSwipeViewWithAlertController:];
-[SBSharedModalAlertItemPresenter _updateHomeGestureParticipant];
-[SBSharedModalAlertItemPresenter currentlyPresentedAlertItem];
-[SBSharedModalAlertItemPresenter dismissAlertItem:animated:completion:];
-[SBSharedModalAlertItemPresenter initWithLockOutProvider:systemGestureManager:reachabilityController:alertLayoutPresentationVerifier:windowScene:];
-[SBSharedModalAlertItemPresenter modalViewControllerStack:didDismissViewController:];
-[SBSharedModalAlertItemPresenter modalViewControllerStack:didPresentViewController:];
-[SBSharedModalAlertItemPresenter modalViewControllerStack:willDismissViewController:animated:];
-[SBSharedModalAlertItemPresenter modalViewControllerStack:willPresentViewController:];
-[SBSharedModalAlertItemPresenter presentAlertItem:isLocked:animated:completion:];
```
