# `SBRecordingIndicatorViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `SBBacklightControllerObserver`, `SBRecordingIndicatorSystemApertureElementDelegate`
- 33 instance variables, 14 properties, 27 instance methods, 0 class methods

## Instance variables

```
@"UIViewPropertyAnimator" _animatorScaleToOverscale;
@"UIViewPropertyAnimator" _animatorScaleToNormal;
@"UIViewPropertyAnimator" _animatorScaleToRest;
@"UIViewPropertyAnimator" _animatorScaleToZero;
@"UIViewPropertyAnimator" _animatorFastFade;
@"UIViewPropertyAnimator" _animatorSpringToOn;
@"UIViewPropertyAnimator" _animatorSpringToOff;
d _size;
d _sideOffset;
d _topOffset;
{CGPoint="x"d"y"d} _center;
@"SBRecordingIndicatorAboveBlankingWindow" _highLevelWindow;
@"CAContext" _highLevelContext;
@"CALayer" _highLevelContextRootLayer;
@"_SBRecordingIndicatorGainMapView" _defaultGainMapDefeatingView;
@"CAGainMapLayer" _defaultGainMapDefeatingLayer;
@"SBRecordingIndicatorRotationRateLimiter" _rateLimiter;
@"SBSecureIndicatorBacklightCoordinator" _backlightCoordinator;
@"<BSInvalidatable>" _backlightCoordinatorAssertion;
@"SBBacklightController" _backlightController;
q _incomingBacklightState;
d _aboveBlankingGainMapResolutionTransitionStrength;
@"<BSInvalidatable>" _streamBuddyDisplayLinkAssertion;
B _invalidated;
@"SBRecordingIndicatorVisualRepresentation" _indicator;
@"SBRecordingIndicatorVisualRepresentation" _secondaryIndicator;
Q _indicatorState;
q _activeInterfaceOrientation;
@"<SBRecordingIndicatorViewControllerDelegate>" _delegate;
Q _location;
@"SBWindowScene" _windowScene;
@"SBSystemApertureLayoutMetrics" _layoutMetrics;
@"SBSecureIndicatorMinimumOnTimeCoordinator" _minimumOnTimeCoordinator;
```

## Properties

```
@property (TQ,R,N,V_location) location;
@property (T@"SBWindowScene",R,W,N,V_windowScene) windowScene;
@property (T@"SBSystemApertureLayoutMetrics",R,N,V_layoutMetrics) layoutMetrics;
@property (T@"SBSecureIndicatorMinimumOnTimeCoordinator",R,N,V_minimumOnTimeCoordinator) minimumOnTimeCoordinator;
@property (T@"SBRecordingIndicatorVisualRepresentation",R,N,V_indicator) indicator;
@property (T@"SBRecordingIndicatorVisualRepresentation",R,N,V_secondaryIndicator) secondaryIndicator;
@property (TQ,R,N,V_indicatorState) indicatorState;
@property (Tq,R,N,V_activeInterfaceOrientation) activeInterfaceOrientation;
@property (T@"CAGainMapLayer",R,N) highLevelGainMapDefeatingLayer;
@property (T@"<SBRecordingIndicatorViewControllerDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBRecordingIndicatorViewController minimumOnTimeCoordinator];
-[SBRecordingIndicatorViewController backlightController:didTransitionToBacklightState:source:];
-[SBRecordingIndicatorViewController updateIndicatorVisibilityWithFastFadeAnimation:];
-[SBRecordingIndicatorViewController backlightController:willTransitionToBacklightState:source:];
-[SBRecordingIndicatorViewController willTransitionToTraitCollection:withTransitionCoordinator:];
-[SBRecordingIndicatorViewController _screen];
-[SBRecordingIndicatorViewController initForLocation:windowScene:indicatorDisplayPowerManaging:minimumOnTimeCoordinator:];
-[SBRecordingIndicatorViewController supportedInterfaceOrientations];
-[SBRecordingIndicatorViewController location];
-[SBRecordingIndicatorViewController dealloc];
-[SBRecordingIndicatorViewController recordingIndicatorSystemApertureElement:didChangeResolutionTransitionStrength:];
-[SBRecordingIndicatorViewController indicator];
-[SBRecordingIndicatorViewController layoutMetrics];
-[SBRecordingIndicatorViewController invalidate];
-[SBRecordingIndicatorViewController _canShowWhileLocked];
-[SBRecordingIndicatorViewController setDelegate:];
-[SBRecordingIndicatorViewController activeInterfaceOrientation];
-[SBRecordingIndicatorViewController delegate];
-[SBRecordingIndicatorViewController traitCollectionDidChange:];
-[SBRecordingIndicatorViewController indicatorState];
-[SBRecordingIndicatorViewController updateIndicatorType:];
-[SBRecordingIndicatorViewController highLevelGainMapDefeatingLayer];
-[SBRecordingIndicatorViewController setActiveInterfaceOrientation:withDuration:];
-[SBRecordingIndicatorViewController windowScene];
-[SBRecordingIndicatorViewController _overrideWindowActiveInterfaceOrientation];
-[SBRecordingIndicatorViewController secondaryIndicator];
-[SBRecordingIndicatorViewController updateIndicatorVisibility:];
```
