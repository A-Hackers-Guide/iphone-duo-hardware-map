# `SBModalUIFluidDismissGestureWorkspaceTransaction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSystemGestureWorkspaceTransaction`
- 18 instance variables, 6 properties, 44 instance methods, 0 class methods

## Instance variables

```
@"SBAppSwitcherSettings" _settings;
@"SBWindowSceneStatusBarSettingsAssertion" _statusBarAssertion;
@"UINotificationFeedbackGenerator" _dismissalFeedbackGenerator;
@"SBAssistantRootViewController" _assistantRootViewController;
@"<SBTransientOverlayPresenting>" _transientOverlayPresenter;
@"SBTransientOverlayViewController" _transientOverlayViewController;
{CGPoint="x"d"y"d} _dismissingViewTouchOffset;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _originalBounds;
{CGPoint="x"d"y"d} _originalCenter;
B _initiatedFromBottomEdge;
B _hasPreservedInputViews;
B _isDismissing;
B _animateGestureCancelationOrFailure;
@"SBWindowScene" _windowScene;
d _dismissalThreshold;
@"<SBAssistantSceneControlling>" _assistantController;
q _dismissalType;
@"SBMainWorkspaceTransaction" _currentTransaction;
```

## Properties

```
@property (T@"SBWindowScene",W,N,V_windowScene) windowScene;
@property (T@"<SBAssistantSceneControlling>",&,N,V_assistantController) assistantController;
@property (Tq,R,N,V_dismissalType) dismissalType;
@property (T@"SBMainWorkspaceTransaction",&,N,V_currentTransaction) currentTransaction;
@property (Td,N,V_dismissalThreshold) dismissalThreshold;
@property (TB,N,V_animateGestureCancelationOrFailure) animateGestureCancelationOrFailure;
```

## Instance methods

```
-[SBModalUIFluidDismissGestureWorkspaceTransaction currentTransaction];
-[SBModalUIFluidDismissGestureWorkspaceTransaction canInterruptForTransitionRequest:];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _canBeInterrupted];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _didComplete];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _begin];
-[SBModalUIFluidDismissGestureWorkspaceTransaction setWindowScene:];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _layoutSettings];
-[SBModalUIFluidDismissGestureWorkspaceTransaction assistantController];
-[SBModalUIFluidDismissGestureWorkspaceTransaction setAssistantController:];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _finishWithGesture:];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _homeScreenAnimator];
-[SBModalUIFluidDismissGestureWorkspaceTransaction setCurrentTransaction:];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _beginWithGesture:];
-[SBModalUIFluidDismissGestureWorkspaceTransaction windowScene];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _didInterruptWithReason:];
-[SBModalUIFluidDismissGestureWorkspaceTransaction dismissalType];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _viewForGesture];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _backgroundWeightingForDismissal:];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _backgroundWeightingForGestureProgress];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _cleanupHierarchyForDismissal:];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _clientAnimationsDelay];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _dismissClientAnimated:completion:];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _dismissalFeedbackGenerator];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _finishInteractionAndDismiss:animated:];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _finishWithCompletionType:];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _hapticDelay];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _notificationFeedbackType];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _scaleForDismissal];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _scaleForGestureProgress];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _setFluidDismissalState:];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _shouldDismissImmmediatelyAtFullGestureProgress];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _shouldFinishImmediately];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _swipeUpGestureProgress];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _swipeUpGestureTranslation];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _updateDismissingViewLayoutAndStyleForGesture];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _updateWithGesture:];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _yOffsetForGestureProgress];
-[SBModalUIFluidDismissGestureWorkspaceTransaction _zoomOutDelay];
-[SBModalUIFluidDismissGestureWorkspaceTransaction animateGestureCancelationOrFailure];
-[SBModalUIFluidDismissGestureWorkspaceTransaction dismissalThreshold];
-[SBModalUIFluidDismissGestureWorkspaceTransaction initWithTransitionRequest:windowScene:dismissalType:initiatedFromBottomEdge:];
-[SBModalUIFluidDismissGestureWorkspaceTransaction setAnimateGestureCancelationOrFailure:];
-[SBModalUIFluidDismissGestureWorkspaceTransaction setDismissalThreshold:];
-[SBModalUIFluidDismissGestureWorkspaceTransaction systemGestureStateChanged:];
```
