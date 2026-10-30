# `_UIFluidSliderDiscreteButtonDriver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIFluidSliderDriving`
- 12 instance variables, 13 properties, 44 instance methods, 0 class methods

## Instance variables

```
B _enabled;
B _isRepeating;
@"<_UIFluidSliderDrivable>" _drivable;
@"UIView" _view;
d _stretchAmount;
d _velocityMultiplier;
Q _trackAxis;
@"BSAbsoluteMachTimer" _repeatTimer;
@"BSAbsoluteMachTimer" _releaseTimer;
Q __pressedButton;
d __value;
d __lastReleaseTimestamp;
```

## Properties

```
@property (T@"BSAbsoluteMachTimer",&,N,V_repeatTimer) _repeatTimer;
@property (T@"BSAbsoluteMachTimer",&,N,V_releaseTimer) _releaseTimer;
@property (TQ,N,V__pressedButton) _pressedButton;
@property (TB,N,V_isRepeating) _isRepeating;
@property (Td,N,V__value) _value;
@property (Td,N,V__lastReleaseTimestamp) _lastReleaseTimestamp;
@property (T@"UIView",W,N,V_view) view;
@property (TB,N,V_enabled) enabled;
@property (T@"NSString",R,N) name;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIFluidSliderDiscreteButtonDriver stretchAmount];
-[_UIFluidSliderDiscreteButtonDriver velocityMultiplier];
-[_UIFluidSliderDiscreteButtonDriver _value];
-[_UIFluidSliderDiscreteButtonDriver drivable];
-[_UIFluidSliderDiscreteButtonDriver setStretchAmount:];
-[_UIFluidSliderDiscreteButtonDriver enabled];
-[_UIFluidSliderDiscreteButtonDriver stop];
-[_UIFluidSliderDiscreteButtonDriver dealloc];
-[_UIFluidSliderDiscreteButtonDriver _trackLength];
-[_UIFluidSliderDiscreteButtonDriver setView:];
-[_UIFluidSliderDiscreteButtonDriver view];
-[_UIFluidSliderDiscreteButtonDriver setTrackAxis:];
-[_UIFluidSliderDiscreteButtonDriver setEnabled:];
-[_UIFluidSliderDiscreteButtonDriver setVelocityMultiplier:];
-[_UIFluidSliderDiscreteButtonDriver cancel];
-[_UIFluidSliderDiscreteButtonDriver trackAxis];
-[_UIFluidSliderDiscreteButtonDriver name];
-[_UIFluidSliderDiscreteButtonDriver _repeatDelay];
-[_UIFluidSliderDiscreteButtonDriver setDrivable:];
-[_UIFluidSliderDiscreteButtonDriver _incrementValue];
-[_UIFluidSliderDiscreteButtonDriver _overflowAmount];
-[_UIFluidSliderDiscreteButtonDriver pressUp];
-[_UIFluidSliderDiscreteButtonDriver _clearReleaseTimer];
-[_UIFluidSliderDiscreteButtonDriver _clearRepeatTimer];
-[_UIFluidSliderDiscreteButtonDriver _handleButton:state:];
-[_UIFluidSliderDiscreteButtonDriver _isRepeating];
-[_UIFluidSliderDiscreteButtonDriver _issueUpdateWithValue:];
-[_UIFluidSliderDiscreteButtonDriver _lastReleaseTimestamp];
-[_UIFluidSliderDiscreteButtonDriver _minimumPressDuration];
-[_UIFluidSliderDiscreteButtonDriver _pressedButton];
-[_UIFluidSliderDiscreteButtonDriver _range];
-[_UIFluidSliderDiscreteButtonDriver _releaseCurrentlyPressedButton];
-[_UIFluidSliderDiscreteButtonDriver _releaseTimer];
-[_UIFluidSliderDiscreteButtonDriver _repeatCadence];
-[_UIFluidSliderDiscreteButtonDriver _repeatTimer];
-[_UIFluidSliderDiscreteButtonDriver pressDown];
-[_UIFluidSliderDiscreteButtonDriver releaseDown];
-[_UIFluidSliderDiscreteButtonDriver releaseUp];
-[_UIFluidSliderDiscreteButtonDriver set_isRepeating:];
-[_UIFluidSliderDiscreteButtonDriver set_lastReleaseTimestamp:];
-[_UIFluidSliderDiscreteButtonDriver set_pressedButton:];
-[_UIFluidSliderDiscreteButtonDriver set_releaseTimer:];
-[_UIFluidSliderDiscreteButtonDriver set_repeatTimer:];
-[_UIFluidSliderDiscreteButtonDriver set_value:];
```
