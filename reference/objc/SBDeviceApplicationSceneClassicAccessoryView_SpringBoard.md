# `SBDeviceApplicationSceneClassicAccessoryView`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `SBLayoutStateTransitionObserver`, `SBDeviceApplicationSceneHandleObserver`, `SBDeviceApplicationSceneStatusBarStateObserver`, `UIGestureRecognizerDelegate`, `BSInvalidatable`
- 30 instance variables, 9 properties, 46 instance methods, 0 class methods

## Instance variables

```
@"SBDeviceApplicationSceneHandle" _sceneHandle;
@"<SBDeviceApplicationSceneClassicAccessoryViewDelegate>" _delegate;
@"UIView" _buttonWrapperView;
@"UIButton" _zoomButton;
@"UIButton" _rotationButton;
q _buttonOrientation;
@"BSUIOrientationTransformWrapperView" _transformWrapperView;
B _rotatingFromButtonTap;
B _obscuredByKeyboardOverlay;
@"UIPanGestureRecognizer" _alignmentSwipeRecognizer;
@"SBSceneHandleBlockObserver" _sceneHandleObserver;
@"UIApplicationSceneClientSettingsDiffInspector" _clientSettingsInspector;
@"UIApplicationSceneSettingsDiffInspector" _sceneSettingsInspector;
@"NSLayoutConstraint" _rotationButtonHorizontalConstraint;
@"NSLayoutConstraint" _rotationButtonVerticalConstraint;
@"NSLayoutConstraint" _rotationButtonWidthConstraint;
@"NSLayoutConstraint" _rotationButtonHeightConstraint;
@"NSLayoutConstraint" _zoomButtonTopConstraint;
@"NSLayoutConstraint" _zoomButtonBottomConstraint;
@"NSLayoutConstraint" _zoomButtonLeadingConstraint;
@"NSLayoutConstraint" _zoomButtonTrailingConstraint;
@"NSLayoutConstraint" _zoomButtonHorizontalConstraint;
@"NSLayoutConstraint" _zoomButtonVerticalConstraint;
@"NSLayoutConstraint" _rotationButtonHorizontalConstraintMirrored;
@"NSLayoutConstraint" _zoomButtonHorizontalConstraintMirrored;
@"NSLayoutConstraint" _zoomButtonLeadingConstraintMirrored;
B _buttonsAutoHidden;
@"NSTimer" _buttonAutoHideTimer;
@"UITapGestureRecognizer" _toggleButtonsTapRecognizer;
@"SBDeviceApplicationSceneClassicWrapperView" _classicWrapperView;
```

## Properties

```
@property (T@"SBDeviceApplicationSceneHandle",R,&,N,V_sceneHandle) sceneHandle;
@property (Tq,N,V_buttonOrientation) buttonOrientation;
@property (T@"<SBDeviceApplicationSceneClassicAccessoryViewDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisObscuredByKeyboardOverlay,V_obscuredByKeyboardOverlay) obscuredByKeyboardOverlay;
@property (T@"SBDeviceApplicationSceneClassicWrapperView",W,N,V_classicWrapperView) classicWrapperView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDeviceApplicationSceneClassicAccessoryView sceneHandle];
-[SBDeviceApplicationSceneClassicAccessoryView gestureRecognizer:shouldReceiveTouch:];
-[SBDeviceApplicationSceneClassicAccessoryView isObscuredByKeyboardOverlay];
-[SBDeviceApplicationSceneClassicAccessoryView dealloc];
-[SBDeviceApplicationSceneClassicAccessoryView layoutSubviews];
-[SBDeviceApplicationSceneClassicAccessoryView setObscuredByKeyboardOverlay:];
-[SBDeviceApplicationSceneClassicAccessoryView invalidate];
-[SBDeviceApplicationSceneClassicAccessoryView setDelegate:];
-[SBDeviceApplicationSceneClassicAccessoryView gestureRecognizerShouldBegin:];
-[SBDeviceApplicationSceneClassicAccessoryView layoutStateTransitionCoordinator:transitionDidEndWithTransitionContext:];
-[SBDeviceApplicationSceneClassicAccessoryView _sceneHandleDidUpdateSettingsWithDiff:previousSettings:];
-[SBDeviceApplicationSceneClassicAccessoryView _sceneHandleDidUpdateClientSettings:];
-[SBDeviceApplicationSceneClassicAccessoryView delegate];
-[SBDeviceApplicationSceneClassicAccessoryView sceneHandle:didChangePreferredHingeEdge:];
-[SBDeviceApplicationSceneClassicAccessoryView sceneWithIdentifier:didChangeStatusBarHiddenTo:withAnimation:];
-[SBDeviceApplicationSceneClassicAccessoryView _changeZoom:];
-[SBDeviceApplicationSceneClassicAccessoryView _updateZoomButton];
-[SBDeviceApplicationSceneClassicAccessoryView _isZoomed];
-[SBDeviceApplicationSceneClassicAccessoryView _updateRotationButton];
-[SBDeviceApplicationSceneClassicAccessoryView _shouldDockButtonsToLeadingEdge];
-[SBDeviceApplicationSceneClassicAccessoryView _autoHideButtons];
-[SBDeviceApplicationSceneClassicAccessoryView _buttonAutoHideEnabled];
-[SBDeviceApplicationSceneClassicAccessoryView _buttonsAutoHiddenForHiddenStatusBar];
-[SBDeviceApplicationSceneClassicAccessoryView _cancelButtonAutoHideTimer];
-[SBDeviceApplicationSceneClassicAccessoryView _handleAlignmentSwipe:];
-[SBDeviceApplicationSceneClassicAccessoryView _handleToggleButtonsTap:];
-[SBDeviceApplicationSceneClassicAccessoryView _isPoint:withinButton:];
-[SBDeviceApplicationSceneClassicAccessoryView _isPointInLetterboxAreas:];
-[SBDeviceApplicationSceneClassicAccessoryView _rotateApplicationScene:];
-[SBDeviceApplicationSceneClassicAccessoryView _rotateButtonVisibilityFollowsZoomButton];
-[SBDeviceApplicationSceneClassicAccessoryView _rotationButtonShouldBeVisible];
-[SBDeviceApplicationSceneClassicAccessoryView _scheduleButtonAutoHideTimer];
-[SBDeviceApplicationSceneClassicAccessoryView _setButtonsAutoHidden:];
-[SBDeviceApplicationSceneClassicAccessoryView _setupPositioningAndRotationForInterfaceOrientation:offscreen:];
-[SBDeviceApplicationSceneClassicAccessoryView _suppressesRotateButton];
-[SBDeviceApplicationSceneClassicAccessoryView _suppressesZoomButton];
-[SBDeviceApplicationSceneClassicAccessoryView _updateButtonVisibilityAnimated:];
-[SBDeviceApplicationSceneClassicAccessoryView _updateOrientationFrom:toOrientation:animationSettings:];
-[SBDeviceApplicationSceneClassicAccessoryView _updateRotationButtonWithAnimationSettings:];
-[SBDeviceApplicationSceneClassicAccessoryView _updateZoomButtonConstraints];
-[SBDeviceApplicationSceneClassicAccessoryView _zoomButtonShouldBeVisible];
-[SBDeviceApplicationSceneClassicAccessoryView buttonOrientation];
-[SBDeviceApplicationSceneClassicAccessoryView classicWrapperView];
-[SBDeviceApplicationSceneClassicAccessoryView initWithFrame:sceneHandle:];
-[SBDeviceApplicationSceneClassicAccessoryView setButtonOrientation:];
-[SBDeviceApplicationSceneClassicAccessoryView setClassicWrapperView:];
```
