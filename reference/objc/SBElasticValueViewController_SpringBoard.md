# `SBElasticValueViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIGestureRecognizerDelegate`, `PTSettingsKeyObserver`, `SBHUDViewControlling`
- 45 instance variables, 14 properties, 112 instance methods, 0 class methods

## Instance variables

```
@"SBFTouchPassThroughView" _sliderContainerView;
q _previousState;
q _state;
@"_UILegibilityLabel" _leadingLabel;
@"_UILegibilityLabel" _trailingLabel;
@"UIView" _touchTrackingView;
@"UIView" _dimmingView;
@"UILongPressGestureRecognizer" _shortLongPressGestureRecognizer;
Q _sliderTrackingCount;
B _sliderIsEditing;
@"NSTimer" _dismissalTimer;
@"NSTimer" _sliderApplyValueTimer;
@"NSNumber" _pendingValueToApply;
@"CADisplayLink" _displayLinkForVisiblyOffscreenMonitoring;
B _initialTransitionCompleted;
B _lockState;
B _isDebugging;
B _isRotating;
B _reduceMotionEnabled;
B _upButtonPressed;
B _downButtonPressed;
@"UIView" _debugContainerView;
@"UILabel" _debugLabel;
@"UISegmentedControl" _debugStateSegmentedControl;
@"UILabel" _debugAutoDismissLabel;
@"UISwitch" _debugAutoDismissalSwitch;
@"UILabel" _debugLockStateLabel;
@"UISwitch" _debugLockStateSwitch;
@"UISlider" _debugWidthSlider;
@"UISlider" _debugHeightSlider;
@"UISlider" _debugPortraitYOriginSlider;
@"UIButton" _debugDumpButton;
@"UIButton" _debugNextAudioRouteButton;
@"UIButton" _debugResetAudioRouteButton;
@"<SBElasticRouteDisplaying>" _routeDisplayInfo;
@"BLSAssertion" _liveRenderingAssertion;
@"NSArray" _debugAutoLayoutConstraints;
@"<SBHUDAttachmentDelegate>" _attachmentDelegate;
B _isHUDAttached;
Q _axis;
@"<SBElasticValueDataSource>" _dataSource;
@"<SBElasticValueViewControllerDelegate>" _delegate;
@"SBElasticHUDSettings" _settings;
@"SBElasticSliderView" _sliderView;
{CGPoint="x"d"y"d} _positionOffset;
```

## Properties

```
@property (T@"SBElasticHUDSettings",R,N,V_settings) settings;
@property (T@"SBElasticSliderView",R,N,V_sliderView) sliderView;
@property (TB,R,N,GisSliderTracking) sliderTracking;
@property (TQ,R,N,V_axis) axis;
@property (T@"<SBElasticValueDataSource>",R,W,N,V_dataSource) dataSource;
@property (T@"<SBElasticValueViewControllerDelegate>",W,N,V_delegate) delegate;
@property (T{CGPoint=dd},R,N) centerForElasticHUDWhenInInteractingState;
@property (T{CGPoint=dd},N,V_positionOffset) positionOffset;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"<SBHUDAttachmentDelegate>",W,N,V_attachmentDelegate) attachmentDelegate;
@property (T@"NSArray",R,C,N) physicalButtonSceneTargets;
```

## Instance methods

```
-[SBElasticValueViewController _displayLinkFired:];
-[SBElasticValueViewController initWithDataSource:];
-[SBElasticValueViewController axis];
-[SBElasticValueViewController physicalButtonSceneTargets];
-[SBElasticValueViewController triggerButton];
-[SBElasticValueViewController sliderView];
-[SBElasticValueViewController transitionToState:animated:completion:];
-[SBElasticValueViewController supportedInterfaceOrientations];
-[SBElasticValueViewController settings];
-[SBElasticValueViewController dealloc];
-[SBElasticValueViewController viewDidLoad];
-[SBElasticValueViewController currentValue];
-[SBElasticValueViewController setPositionOffset:];
-[SBElasticValueViewController initWithNibName:bundle:];
-[SBElasticValueViewController settings:changedValueForKey:];
-[SBElasticValueViewController _sliderEditingDidEnd:];
-[SBElasticValueViewController reloadData];
-[SBElasticValueViewController viewWillAppear:];
-[SBElasticValueViewController _canShowWhileLocked];
-[SBElasticValueViewController definesAnimatedDismissal];
-[SBElasticValueViewController setDelegate:];
-[SBElasticValueViewController dismissAnimatedWithCompletion:];
-[SBElasticValueViewController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[SBElasticValueViewController viewDidAppear:];
-[SBElasticValueViewController gestureRecognizerShouldBegin:];
-[SBElasticValueViewController isHUDAttached];
-[SBElasticValueViewController dataSource];
-[SBElasticValueViewController createSliderView];
-[SBElasticValueViewController viewWillTransitionToSize:withTransitionCoordinator:];
-[SBElasticValueViewController loadView];
-[SBElasticValueViewController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[SBElasticValueViewController delegate];
-[SBElasticValueViewController _sliderValueDidChange:];
-[SBElasticValueViewController attachmentIgnoredOrientations];
-[SBElasticValueViewController viewWillLayoutSubviews];
-[SBElasticValueViewController setAttachmentDelegate:];
-[SBElasticValueViewController viewDidDisappear:];
-[SBElasticValueViewController initWithCoder:];
-[SBElasticValueViewController _reloadData];
-[SBElasticValueViewController log];
-[SBElasticValueViewController attachmentDelegate];
-[SBElasticValueViewController _sliderEditingDidBegin:];
-[SBElasticValueViewController positionOffset];
-[SBElasticValueViewController updateValue:];
-[SBElasticValueViewController _reduceMotionStatusDidChange];
-[SBElasticValueViewController _noteSliderViewDidBeginTracking];
-[SBElasticValueViewController setHUDAttached:];
-[SBElasticValueViewController _actuallyDismiss];
-[SBElasticValueViewController _animateFromState:toState:primaryAnimations:primaryCompletion:positionAnimations:positionCompletion:finalCompletion:];
-[SBElasticValueViewController _beginDeflationDismissalAnimation];
-[SBElasticValueViewController _changeValue:];
-[SBElasticValueViewController _computeCachedRouteDisplayInformation];
-[SBElasticValueViewController _debugAutoDismissalSwitchValueChanged:];
-[SBElasticValueViewController _debugChangingStateFromSegmentedControl:];
-[SBElasticValueViewController _debugDidTapNextRoute:];
-[SBElasticValueViewController _debugDidTapResetRoute:];
-[SBElasticValueViewController _debugDimensionSliderValueDidChange:];
-[SBElasticValueViewController _debugDump:];
-[SBElasticValueViewController _debugHandleNextRoute];
-[SBElasticValueViewController _debugHandleResetRoute];
-[SBElasticValueViewController _debugLockStateSwitchValueChanged:];
-[SBElasticValueViewController _dismissalTimerFired:];
-[SBElasticValueViewController _handleShortLongPressGestureRecognizer:];
-[SBElasticValueViewController _hardwareButtonPressedStateDidChange];
-[SBElasticValueViewController _invalidateDismissalTimerForReason:];
-[SBElasticValueViewController _isStateChangeAllowedFrom:toState:];
-[SBElasticValueViewController _noteSliderViewDidEndTracking];
-[SBElasticValueViewController _refreshDebugUI:];
-[SBElasticValueViewController _scheduleDismissal:];
-[SBElasticValueViewController _scheduleDismissal:afterInterval:];
-[SBElasticValueViewController _sliderIndirectInputDidBegin:];
-[SBElasticValueViewController _sliderIndirectInputDidEnd:];
-[SBElasticValueViewController _sliderTrackingDidBegin:];
-[SBElasticValueViewController _sliderTrackingDidEnd:];
-[SBElasticValueViewController _sliderViewMetricsUpdatersForState:bounds:primaryMetricsUpdater:positionUpdater:];
-[SBElasticValueViewController _startMonitoringForSliderVisiblyOffscreen];
-[SBElasticValueViewController _stopMonitoringForSliderVisiblyOffscreen];
-[SBElasticValueViewController _updateDebugString:];
-[SBElasticValueViewController _updateDebugUIPositions];
-[SBElasticValueViewController _updateDimmingVisible:];
-[SBElasticValueViewController _updateForAxisChange:];
-[SBElasticValueViewController _updateGlyphStateIfNecessaryForValue:];
-[SBElasticValueViewController _updateLabelsForAxis:];
-[SBElasticValueViewController _updateLiveRenderingAssertion];
-[SBElasticValueViewController _updateSliderTracking];
-[SBElasticValueViewController _updateSliderValue:animated:];
-[SBElasticValueViewController _updateSliderValue:animated:transitioningStateContextuallyIfNecessary:];
-[SBElasticValueViewController _updateSliderViewMetricsForState:bounds:];
-[SBElasticValueViewController _updateSliderWithAxis:];
-[SBElasticValueViewController _updateTouchTrackingArea];
-[SBElasticValueViewController centerForElasticHUDWhenInInteractingState];
-[SBElasticValueViewController centerForState:sliderSize:bounds:];
-[SBElasticValueViewController changeValue:animated:];
-[SBElasticValueViewController glyphScaleForState:];
-[SBElasticValueViewController hudPresentationOrientation];
-[SBElasticValueViewController interactiveValueUpdateDiscontinuityInterval];
-[SBElasticValueViewController isSliderTracking];
-[SBElasticValueViewController layoutAxisForInterfaceOrientation:];
-[SBElasticValueViewController majorAxisCenterWithButtons:forInterfaceOrientation:bounds:];
-[SBElasticValueViewController maximumSizeForSlider];
-[SBElasticValueViewController noteContinuousValueInteractionDidEnd];
-[SBElasticValueViewController noteContinuousValueInteractionWillBegin];
-[SBElasticValueViewController noteDownButtonPressed:];
-[SBElasticValueViewController noteUpButtonPressed:];
-[SBElasticValueViewController overrideDisplayNameForRoute:];
-[SBElasticValueViewController positionsAtTrailingEdgeForInterfaceOrientation:];
-[SBElasticValueViewController setButtonStepCount:];
-[SBElasticValueViewController setupFailureRelationshipForGestureRecognizer:];
-[SBElasticValueViewController sizeForState:];
-[SBElasticValueViewController sliderAccessibilityIdentifier];
-[SBElasticValueViewController transitionStateContextuallyForValueChangeEvent];
-[SBElasticValueViewController updateActiveRouteDisplay:];
```
