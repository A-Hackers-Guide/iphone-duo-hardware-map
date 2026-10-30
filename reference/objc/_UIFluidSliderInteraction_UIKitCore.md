# `_UIFluidSliderInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIFluidSliderDrivable`, `UIInteraction`
- 24 instance variables, 35 properties, 69 instance methods, 0 class methods

## Instance variables

```
B _feedbackEnabled;
B _userInteractionEnabled;
B _locked;
B __shouldScaleOnIndirectInput;
@"UIView" _view;
d _presentationValue;
q _elasticity;
@"<_UIFluidSliderDirectDrivingDelegate>" _directDrivingDelegate;
d _lockedValue;
@"_UIFluidSliderInteractionConfiguration" _configuration;
@? __handler;
Q __axis;
@"NSArray" __drivers;
@"<_UIFluidSliderDriving>" __activeDriver;
@"<_UIFluidSliderDirectDriving>" __panDriver;
@"<_UIFluidSliderVolumeButtonDriving>" __volumeButtonDriver;
@"_UIFluidSliderFeedbackConductor" __feedbackConductor;
@"UIViewFloatAnimatableProperty" __animatedValue;
@"UIViewFloatAnimatableProperty" __trackWidth;
@"UIViewFloatAnimatableProperty" __trackLength;
@"UIViewFloatAnimatableProperty" __trackScale;
q __state;
{CGSize="width"d"height"d} __normalizedTrackSize;
{?="value"d"scale"d"state"q"type"q"currentSnappingTarget"d} __lastDriverUpdate;
```

## Properties

```
@property (T@?,C,N,V__handler) _handler;
@property (TQ,N,V__axis) _axis;
@property (T{CGSize=dd},N,V__normalizedTrackSize) _normalizedTrackSize;
@property (T@"NSArray",&,N,V__drivers) _drivers;
@property (T@"<_UIFluidSliderDriving>",W,N,V__activeDriver) _activeDriver;
@property (T@"<_UIFluidSliderDirectDriving>",W,N,V__panDriver) _panDriver;
@property (T@"<_UIFluidSliderVolumeButtonDriving>",W,N,V__volumeButtonDriver) _volumeButtonDriver;
@property (T@"_UIFluidSliderFeedbackConductor",&,N,V__feedbackConductor) _feedbackConductor;
@property (T@"UIViewFloatAnimatableProperty",&,N,V__animatedValue) _animatedValue;
@property (T@"UIViewFloatAnimatableProperty",&,N,V__trackWidth) _trackWidth;
@property (T@"UIViewFloatAnimatableProperty",&,N,V__trackLength) _trackLength;
@property (T@"UIViewFloatAnimatableProperty",&,N,V__trackScale) _trackScale;
@property (Tq,N,V__state) _state;
@property (T{?=ddqqd},N,V__lastDriverUpdate) _lastDriverUpdate;
@property (Td,N,V_lockedValue) _lockedValue;
@property (T@"UIPanGestureRecognizer",R,N) _panGestureRecognizer;
@property (T@"_UIPhysicalButtonInteraction",R,N) _volumeButtonInteraction;
@property (Tq,N,S_setElasticity:,V_elasticity) _elasticity;
@property (TB,N,S_setFeedbackEnabled:,V_feedbackEnabled) _feedbackEnabled;
@property (TB,N,S_setShouldScaleOnIndirectInput:,V__shouldScaleOnIndirectInput) _shouldScaleOnIndirectInput;
@property (T@"<_UIFluidSliderDirectDrivingDelegate>",W,N,S_setDirectDrivingDelegate:,V_directDrivingDelegate) _directDrivingDelegate;
@property (Td,N) value;
@property (TB,N,GisUserInteractionEnabled,V_userInteractionEnabled) userInteractionEnabled;
@property (TB,N,GisLocked,V_locked) locked;
@property (T@"_UIFluidSliderInteractionConfiguration",C,N,V_configuration) configuration;
@property (Td,R,N,V_presentationValue) presentationValue;
@property (Td,R,N) currentTrackLength;
@property (TQ,R,N) stepCount;
@property (Td,R,N) minValue;
@property (Td,R,N) maxValue;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,W,N,V_view) view;
```

## Instance methods

```
-[_UIFluidSliderInteraction setUserInteractionEnabled:];
-[_UIFluidSliderInteraction _state];
-[_UIFluidSliderInteraction _directDrivingDelegate];
-[_UIFluidSliderInteraction minValue];
-[_UIFluidSliderInteraction maxValue];
-[_UIFluidSliderInteraction _feedbackEnabled];
-[_UIFluidSliderInteraction _targetNewScale:];
-[_UIFluidSliderInteraction _volumeButtonDriver];
-[_UIFluidSliderInteraction _animate:withSpring:];
-[_UIFluidSliderInteraction isLocked];
-[_UIFluidSliderInteraction _shouldScaleOnIndirectInput];
-[_UIFluidSliderInteraction isUserInteractionEnabled];
-[_UIFluidSliderInteraction setLocked:];
-[_UIFluidSliderInteraction _activeDriver];
-[_UIFluidSliderInteraction _setElasticity:];
-[_UIFluidSliderInteraction _drivers];
-[_UIFluidSliderInteraction presentationValue];
-[_UIFluidSliderInteraction set_drivers:];
-[_UIFluidSliderInteraction _cancelDriversExcludingDriver:];
-[_UIFluidSliderInteraction stepCount];
-[_UIFluidSliderInteraction _lastDriverUpdate];
-[_UIFluidSliderInteraction set_axis:];
-[_UIFluidSliderInteraction _setFeedbackEnabled:];
-[_UIFluidSliderInteraction set_feedbackConductor:];
-[_UIFluidSliderInteraction _volumeButtonInteraction];
-[_UIFluidSliderInteraction setConfiguration:];
-[_UIFluidSliderInteraction _targetNewValue:];
-[_UIFluidSliderInteraction _trackLength];
-[_UIFluidSliderInteraction value];
-[_UIFluidSliderInteraction _panGestureRecognizer];
-[_UIFluidSliderInteraction _feedbackEpsilon];
-[_UIFluidSliderInteraction set_trackWidth:];
-[_UIFluidSliderInteraction set_normalizedTrackSize:];
-[_UIFluidSliderInteraction fluidSliderDriver:didGenerateUpdate:];
-[_UIFluidSliderInteraction _driftFactor];
-[_UIFluidSliderInteraction view];
-[_UIFluidSliderInteraction initWithConfiguration:handler:];
-[_UIFluidSliderInteraction _rebuildDrivers];
-[_UIFluidSliderInteraction set_lockedValue:];
-[_UIFluidSliderInteraction _elasticity];
-[_UIFluidSliderInteraction setValue:];
-[_UIFluidSliderInteraction configuration];
-[_UIFluidSliderInteraction _trackWidth];
-[_UIFluidSliderInteraction set_panDriver:];
-[_UIFluidSliderInteraction currentTrackLength];
-[_UIFluidSliderInteraction set_trackLength:];
-[_UIFluidSliderInteraction _axis];
-[_UIFluidSliderInteraction _lockedValue];
-[_UIFluidSliderInteraction set_state:];
-[_UIFluidSliderInteraction _removeAllDrivers];
-[_UIFluidSliderInteraction willMoveToView:];
-[_UIFluidSliderInteraction set_lastDriverUpdate:];
-[_UIFluidSliderInteraction _feedbackConductor];
-[_UIFluidSliderInteraction _normalizedTrackSize];
-[_UIFluidSliderInteraction set_handler:];
-[_UIFluidSliderInteraction _animatedValue];
-[_UIFluidSliderInteraction _minSquishedWidthForWidth:];
-[_UIFluidSliderInteraction _setDirectDrivingDelegate:];
-[_UIFluidSliderInteraction description];
-[_UIFluidSliderInteraction _trackScale];
-[_UIFluidSliderInteraction _handler];
-[_UIFluidSliderInteraction _setShouldScaleOnIndirectInput:];
-[_UIFluidSliderInteraction set_trackScale:];
-[_UIFluidSliderInteraction _panDriver];
-[_UIFluidSliderInteraction set_volumeButtonDriver:];
-[_UIFluidSliderInteraction set_activeDriver:];
-[_UIFluidSliderInteraction didMoveToView:];
-[_UIFluidSliderInteraction _issueUpdate];
-[_UIFluidSliderInteraction set_animatedValue:];
```
