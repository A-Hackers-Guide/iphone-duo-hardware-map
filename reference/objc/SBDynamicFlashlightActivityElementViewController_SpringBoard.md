# `SBDynamicFlashlightActivityElementViewController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIGestureRecognizerDelegate`
- 19 instance variables, 13 properties, 41 instance methods, 0 class methods

## Instance variables

```
{CGPoint="x"d"y"d} _torchState;
{CGPoint="x"d"y"d} _persistedState;
{CGPoint="x"d"y"d} _gesturePoint;
d _gestureXMultiplier;
{CGPoint="x"d"y"d} _gestureScaling;
@"<SBDynamicFlashlightOptionsProvider>" _optionsProvider;
@"SBFFluidBehaviorSettings" _fluidBehaviorSettings;
@"_SBDynamicFlashlightZeroDelayPanGestureRecognizer" _panGestureRecognizer;
{CGPoint="x"d"y"d} _gestureOrigin;
@"NSDate" _gestureStartTime;
@"NSTimer" _persistenceTimer;
@"NSTimer" _dismissalTimer;
B _expanded;
B _shouldDismissWhenOff;
B _fixedWidth;
@"SBDynamicFlashlightActivityElementView" _elementView;
@"<SBDynamicFlashlightActivityElementViewControllerDelegate>" _delegate;
q _elementOrientation;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _preferredContentRect;
```

## Properties

```
@property (T@"SBDynamicFlashlightActivityElementView",&,N,V_elementView) elementView;
@property (T@"<SBDynamicFlashlightActivityElementViewControllerDelegate>",W,N,V_delegate) delegate;
@property (Tq,N,V_elementOrientation) elementOrientation;
@property (Td,R,N) currentIntensity;
@property (Td,R,N) currentWidth;
@property (TB,R,N,GisBeamOn) beamOn;
@property (TB,N,GisExpanded) expanded;
@property (TB,R,N,V_shouldDismissWhenOff) shouldDismissWhenOff;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_preferredContentRect) preferredContentRect;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBDynamicFlashlightActivityElementViewController _saveTorchState];
-[SBDynamicFlashlightActivityElementViewController _updatePreferredContentRectForUnconstrainedPoint:];
-[SBDynamicFlashlightActivityElementViewController initWithOptionsProvider:state:fixedWidth:];
-[SBDynamicFlashlightActivityElementViewController setElementView:];
-[SBDynamicFlashlightActivityElementViewController gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[SBDynamicFlashlightActivityElementViewController setElementOrientation:];
-[SBDynamicFlashlightActivityElementViewController setState:];
-[SBDynamicFlashlightActivityElementViewController _animateUntracked:completion:];
-[SBDynamicFlashlightActivityElementViewController setExpanded:];
-[SBDynamicFlashlightActivityElementViewController gestureRecognizer:shouldReceiveTouch:];
-[SBDynamicFlashlightActivityElementViewController isExpanded];
-[SBDynamicFlashlightActivityElementViewController viewIsAppearing:];
-[SBDynamicFlashlightActivityElementViewController _startDismissalTimer];
-[SBDynamicFlashlightActivityElementViewController _invalidateDismissalTimer];
-[SBDynamicFlashlightActivityElementViewController _overshootForNormalized:];
-[SBDynamicFlashlightActivityElementViewController _invalidatePersistenceTimer];
-[SBDynamicFlashlightActivityElementViewController _toggleBeamState];
-[SBDynamicFlashlightActivityElementViewController dealloc];
-[SBDynamicFlashlightActivityElementViewController shouldDismissWhenOff];
-[SBDynamicFlashlightActivityElementViewController isBeamOn];
-[SBDynamicFlashlightActivityElementViewController _canShowWhileLocked];
-[SBDynamicFlashlightActivityElementViewController setDelegate:];
-[SBDynamicFlashlightActivityElementViewController elementView];
-[SBDynamicFlashlightActivityElementViewController _startPersistenceTimer];
-[SBDynamicFlashlightActivityElementViewController currentIntensity];
-[SBDynamicFlashlightActivityElementViewController loadView];
-[SBDynamicFlashlightActivityElementViewController _dismissalTimerDidFire:];
-[SBDynamicFlashlightActivityElementViewController currentWidth];
-[SBDynamicFlashlightActivityElementViewController gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[SBDynamicFlashlightActivityElementViewController delegate];
-[SBDynamicFlashlightActivityElementViewController _updateDelegateStateAnimated:];
-[SBDynamicFlashlightActivityElementViewController _beamStateForState:currentBeamState:];
-[SBDynamicFlashlightActivityElementViewController _panGestureHandler];
-[SBDynamicFlashlightActivityElementViewController _hasActiveTouches];
-[SBDynamicFlashlightActivityElementViewController _tapGestureHandler];
-[SBDynamicFlashlightActivityElementViewController setPanEnabled:];
-[SBDynamicFlashlightActivityElementViewController _accessibilitySetTorchState:];
-[SBDynamicFlashlightActivityElementViewController updateOrientation];
-[SBDynamicFlashlightActivityElementViewController preferredContentRect];
-[SBDynamicFlashlightActivityElementViewController _animateTracked:completion:];
-[SBDynamicFlashlightActivityElementViewController elementOrientation];
```
