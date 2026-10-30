# `SBRemoteTransientOverlayHostViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIRemoteViewController`
- Protocols: `SBUIRemoteAlertHostInterface_Internal`, `BSDescriptionProviding`
- 28 instance variables, 29 properties, 90 instance methods, 2 class methods

## Instance variables

```
i _preferredStatusBarVisibility;
@"NSNumber" _preferredStatusBarStyleValue;
@"NSNumber" _hasTranslucentContentValue;
@"NSMutableArray" _pendedDelegateCalloutBlocks;
B _allowsStackingOverlayContentAbove;
B _prefersWallpaperTunnelActive;
B _shouldEnableFadeInAnimation;
B _shouldEnableFadeOutAnimation;
B _allowsHomeButtonDismissal;
B _shouldDisableOrientationUpdates;
B _allowsCustomPresentationDismissalAnimations;
B _shouldIgnoreContentOverlayInsetUpdates;
B _movesAutomaticallyToPrimaryDisplay;
B _shouldDisableBanners;
B _shouldDisableControlCenter;
B _shouldDisableReachability;
B _shouldDisableInteractiveScreenshotGesture;
B _shouldDisableSiri;
B _shouldPendAlertItems;
B _attachedToWindowedAccessory;
@"<SBRemoteTransientOverlayHostViewControllerDelegate>" _delegate;
q _requestedBackgroundStyle;
Q _preferredHardwareButtonEvents;
q _dismissalAnimationStyle;
q _swipeDismissalStyle;
@"NSNumber" _preferredSceneDeactivationReasonValue;
@"NSSet" _preferredBackgroundActivitiesToSuppress;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _windowedAccessoryCutoutFrameInScreen;
```

## Properties

```
@property (T@"<SBRemoteTransientOverlayHostViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N,V_allowsStackingOverlayContentAbove) allowsStackingOverlayContentAbove;
@property (TB,R,N,GisContentOpaque) contentOpaque;
@property (Tq,R,N,V_requestedBackgroundStyle) requestedBackgroundStyle;
@property (TB,R,N,V_prefersWallpaperTunnelActive) prefersWallpaperTunnelActive;
@property (TB,N,V_shouldEnableFadeInAnimation) shouldEnableFadeInAnimation;
@property (TB,N,V_shouldEnableFadeOutAnimation) shouldEnableFadeOutAnimation;
@property (TB,R,N,V_allowsHomeButtonDismissal) allowsHomeButtonDismissal;
@property (TQ,R,N,V_preferredHardwareButtonEvents) preferredHardwareButtonEvents;
@property (Tq,R,N,V_dismissalAnimationStyle) dismissalAnimationStyle;
@property (Tq,R,N,V_swipeDismissalStyle) swipeDismissalStyle;
@property (T@"NSNumber",R,C,N,V_preferredSceneDeactivationReasonValue) preferredSceneDeactivationReasonValue;
@property (T@"NSSet",R,C,N,V_preferredBackgroundActivitiesToSuppress) preferredBackgroundActivitiesToSuppress;
@property (TB,R,N,V_shouldDisableOrientationUpdates) shouldDisableOrientationUpdates;
@property (TB,N,V_allowsCustomPresentationDismissalAnimations) allowsCustomPresentationDismissalAnimations;
@property (TB,N,V_shouldIgnoreContentOverlayInsetUpdates) shouldIgnoreContentOverlayInsetUpdates;
@property (TB,N,V_movesAutomaticallyToPrimaryDisplay) movesAutomaticallyToPrimaryDisplay;
@property (TB,R,N,V_shouldDisableBanners) shouldDisableBanners;
@property (TB,R,N,V_shouldDisableControlCenter) shouldDisableControlCenter;
@property (TB,R,N,V_shouldDisableReachability) shouldDisableReachability;
@property (TB,R,N,V_shouldDisableInteractiveScreenshotGesture) shouldDisableInteractiveScreenshotGesture;
@property (TB,R,N,V_shouldDisableSiri) shouldDisableSiri;
@property (TB,R,N,V_shouldPendAlertItems) shouldPendAlertItems;
@property (TB,R,N,GisAttachedToWindowedAccessory,V_attachedToWindowedAccessory) attachedToWindowedAccessory;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_windowedAccessoryCutoutFrameInScreen) windowedAccessoryCutoutFrameInScreen;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBRemoteTransientOverlayHostViewController exportedInterface];
+[SBRemoteTransientOverlayHostViewController serviceViewControllerInterface];
```

## Instance methods

```
-[SBRemoteTransientOverlayHostViewController shouldPendAlertItems];
-[SBRemoteTransientOverlayHostViewController preferredSceneDeactivationReasonValue];
-[SBRemoteTransientOverlayHostViewController deactivate];
-[SBRemoteTransientOverlayHostViewController didTransitionToAttachedToWindowedAccessory:windowedAccessoryCutoutFrameInScreen:];
-[SBRemoteTransientOverlayHostViewController shouldDisableBanners];
-[SBRemoteTransientOverlayHostViewController dismiss];
-[SBRemoteTransientOverlayHostViewController succinctDescriptionBuilder];
-[SBRemoteTransientOverlayHostViewController handleDoubleHeightStatusBarTap];
-[SBRemoteTransientOverlayHostViewController viewServiceDidTerminateWithError:];
-[SBRemoteTransientOverlayHostViewController shouldDisableReachability];
-[SBRemoteTransientOverlayHostViewController becomeFirstResponder];
-[SBRemoteTransientOverlayHostViewController shouldDisableInteractiveScreenshotGesture];
-[SBRemoteTransientOverlayHostViewController shouldDisableOrientationUpdates];
-[SBRemoteTransientOverlayHostViewController descriptionWithMultilinePrefix:];
-[SBRemoteTransientOverlayHostViewController resignFirstResponder];
-[SBRemoteTransientOverlayHostViewController _preferredStatusBarVisibility];
-[SBRemoteTransientOverlayHostViewController initWithNibName:bundle:];
-[SBRemoteTransientOverlayHostViewController setAllowsCustomPresentationDismissalAnimations:];
-[SBRemoteTransientOverlayHostViewController shouldDisableSiri];
-[SBRemoteTransientOverlayHostViewController succinctDescription];
-[SBRemoteTransientOverlayHostViewController preferredBackgroundActivitiesToSuppress];
-[SBRemoteTransientOverlayHostViewController shouldDisableControlCenter];
-[SBRemoteTransientOverlayHostViewController shouldEnableFadeInAnimation];
-[SBRemoteTransientOverlayHostViewController invalidate];
-[SBRemoteTransientOverlayHostViewController shouldIgnoreContentOverlayInsetUpdates];
-[SBRemoteTransientOverlayHostViewController _canShowWhileLocked];
-[SBRemoteTransientOverlayHostViewController configureWithContext:completion:];
-[SBRemoteTransientOverlayHostViewController restoreInputViewsAnimated:];
-[SBRemoteTransientOverlayHostViewController setDelegate:];
-[SBRemoteTransientOverlayHostViewController didInvalidateForRemoteAlert];
-[SBRemoteTransientOverlayHostViewController shouldEnableFadeOutAnimation];
-[SBRemoteTransientOverlayHostViewController canResignFirstResponder];
-[SBRemoteTransientOverlayHostViewController isContentOpaque];
-[SBRemoteTransientOverlayHostViewController movesAutomaticallyToPrimaryDisplay];
-[SBRemoteTransientOverlayHostViewController delegate];
-[SBRemoteTransientOverlayHostViewController description];
-[SBRemoteTransientOverlayHostViewController windowedAccessoryCutoutFrameInScreen];
-[SBRemoteTransientOverlayHostViewController dismissForTransientOverlayAnimated:completion:];
-[SBRemoteTransientOverlayHostViewController setIdleTimerDisabled:forReason:];
-[SBRemoteTransientOverlayHostViewController dismissalAnimationStyle];
-[SBRemoteTransientOverlayHostViewController allowsStackingOverlayContentAbove];
-[SBRemoteTransientOverlayHostViewController preferredStatusBarStyle];
-[SBRemoteTransientOverlayHostViewController handleButtonActions:];
-[SBRemoteTransientOverlayHostViewController setWhitePointAdaptivityStyle:];
-[SBRemoteTransientOverlayHostViewController canBecomeFirstResponder];
-[SBRemoteTransientOverlayHostViewController preserveInputViewsAnimated:];
-[SBRemoteTransientOverlayHostViewController setShouldEnableFadeInAnimation:];
-[SBRemoteTransientOverlayHostViewController setShouldEnableFadeOutAnimation:];
-[SBRemoteTransientOverlayHostViewController presentForTransientOverlayAnimated:completion:];
-[SBRemoteTransientOverlayHostViewController isAttachedToWindowedAccessory];
-[SBRemoteTransientOverlayHostViewController allowsCustomPresentationDismissalAnimations];
-[SBRemoteTransientOverlayHostViewController setShouldIgnoreContentOverlayInsetUpdates:];
-[SBRemoteTransientOverlayHostViewController descriptionBuilderWithMultilinePrefix:];
-[SBRemoteTransientOverlayHostViewController swipeDismissalStyle];
-[SBRemoteTransientOverlayHostViewController _preferredStatusBarAxisDidChange];
-[SBRemoteTransientOverlayHostViewController _updateContentOverlayInsetsFromParentIfNecessary];
-[SBRemoteTransientOverlayHostViewController setShouldDismissOnUILock:];
-[SBRemoteTransientOverlayHostViewController setWallpaperStyle:withDuration:];
-[SBRemoteTransientOverlayHostViewController setDesiredHardwareButtonEvents:];
-[SBRemoteTransientOverlayHostViewController _participateInSystemAnimationFence:];
-[SBRemoteTransientOverlayHostViewController setAllowsAlertItems:];
-[SBRemoteTransientOverlayHostViewController setAllowsAlertStacking:];
-[SBRemoteTransientOverlayHostViewController setAllowsBanners:];
-[SBRemoteTransientOverlayHostViewController setAllowsControlCenter:];
-[SBRemoteTransientOverlayHostViewController setAllowsMenuButtonDismissal:];
-[SBRemoteTransientOverlayHostViewController setAllowsSiri:];
-[SBRemoteTransientOverlayHostViewController setBackgroundActivitiesToCancel:animationSettings:];
-[SBRemoteTransientOverlayHostViewController setBackgroundStyle:withDuration:];
-[SBRemoteTransientOverlayHostViewController setDesiredAutoLockDuration:];
-[SBRemoteTransientOverlayHostViewController setDesiredIdleTimerSettings:];
-[SBRemoteTransientOverlayHostViewController setDismissalAnimationStyle:];
-[SBRemoteTransientOverlayHostViewController setInteractiveScreenshotGestureDisabled:];
-[SBRemoteTransientOverlayHostViewController setLaunchingInterfaceOrientation:];
-[SBRemoteTransientOverlayHostViewController setMovesAutomaticallyToPrimaryDisplay:];
-[SBRemoteTransientOverlayHostViewController setOrientationChangedEventsEnabled:];
-[SBRemoteTransientOverlayHostViewController setReachabilityDisabled:];
-[SBRemoteTransientOverlayHostViewController setSceneDeactivationReason:];
-[SBRemoteTransientOverlayHostViewController setShouldDisableFadeInAnimation:];
-[SBRemoteTransientOverlayHostViewController setStatusBarHidden:withDuration:];
-[SBRemoteTransientOverlayHostViewController setStyleOverridesToCancel:animationSettings:];
-[SBRemoteTransientOverlayHostViewController setSupportedInterfaceOrientationOverride:];
-[SBRemoteTransientOverlayHostViewController setSwipeDismissalStyle:];
-[SBRemoteTransientOverlayHostViewController setWallpaperTunnelActive:];
-[SBRemoteTransientOverlayHostViewController _pendOrExecuteDelegateCallout:];
-[SBRemoteTransientOverlayHostViewController _setDesiredHardwareButtonEvents:];
-[SBRemoteTransientOverlayHostViewController allowsHomeButtonDismissal];
-[SBRemoteTransientOverlayHostViewController preferredHardwareButtonEvents];
-[SBRemoteTransientOverlayHostViewController prefersWallpaperTunnelActive];
-[SBRemoteTransientOverlayHostViewController prepareForActivationWithContext:presentationMode:completion:];
-[SBRemoteTransientOverlayHostViewController requestedBackgroundStyle];
```
