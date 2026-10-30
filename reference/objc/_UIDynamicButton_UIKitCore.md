# `_UIDynamicButton`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIEventComponent`, `BSDebugDescriptionProviding`, `BSDescriptionStreamable`
- 21 instance variables, 26 properties, 33 instance methods, 0 class methods

## Instance variables

```
B _touching;
S _usagePage;
S _usage;
@"UIWindow" _window;
Q _physicalButton;
Q _physicalButtonSource;
d _touchMajorRadius;
d _touchMinorRadius;
Q _touchPositionHints;
Q _stage;
Q _stageTransition;
Q _phase;
d _normalizedForce;
d _normalizedForceVelocity;
d _releaseStageNormalizedForceThreshold;
d _pressedStageNormalizedForceThreshold;
d _nextStageNormalizedForceThreshold;
d _timestamp;
@"BKSHIDEventBaseAttributes" _hidEventAttributes;
{CGPoint="x"d"y"d} _position;
{CGPoint="x"d"y"d} _positionDelta;
```

## Properties

```
@property (TQ,R,N,V_physicalButton) _physicalButton;
@property (TQ,R,N,V_physicalButtonSource) _physicalButtonSource;
@property (TS,R,N,V_usagePage) _usagePage;
@property (TS,R,N,V_usage) _usage;
@property (TB,R,N,G_isTouching,V_touching) _touching;
@property (Td,R,N,V_touchMajorRadius) _touchMajorRadius;
@property (Td,R,N,V_touchMinorRadius) _touchMinorRadius;
@property (T{CGPoint=dd},R,N,V_position) _position;
@property (T{CGPoint=dd},R,N,V_positionDelta) _positionDelta;
@property (TQ,R,N,V_touchPositionHints) _touchPositionHints;
@property (TQ,R,N,V_stage) _stage;
@property (TQ,R,N) _phase;
@property (Td,R,N,V_normalizedForce) _normalizedForce;
@property (Td,R,N,V_normalizedForceVelocity) _normalizedForceVelocity;
@property (Td,R,N,V_releaseStageNormalizedForceThreshold) _releaseStageNormalizedForceThreshold;
@property (Td,R,N,V_pressedStageNormalizedForceThreshold) _pressedStageNormalizedForceThreshold;
@property (Td,R,N,V_nextStageNormalizedForceThreshold) _nextStageNormalizedForceThreshold;
@property (Td,R,N,V_timestamp) _timestamp;
@property (T@"BKSHIDEventBaseAttributes",R,C,N,V_hidEventAttributes) _hidEventAttributes;
@property (T@"UIWindow",R,N) _window;
@property (TQ,R,N) _eventComponentType;
@property (T@"_UIEventComponentPhaseValue",&,N,S_setEventComponentPhase:) _eventComponentPhase;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIDynamicButton _window];
-[_UIDynamicButton debugDescription];
-[_UIDynamicButton succinctDescriptionBuilder];
-[_UIDynamicButton init];
-[_UIDynamicButton appendDescriptionToFormatter:];
-[_UIDynamicButton descriptionWithMultilinePrefix:];
-[_UIDynamicButton succinctDescription];
-[_UIDynamicButton debugDescriptionWithMultilinePrefix:];
-[_UIDynamicButton _eventComponentPhaseForValue:];
-[_UIDynamicButton description];
-[_UIDynamicButton _eventComponentPhase];
-[_UIDynamicButton _eventComponentType];
-[_UIDynamicButton _setEventComponentPhase:];
-[_UIDynamicButton descriptionBuilderWithMultilinePrefix:];
-[_UIDynamicButton _timestamp];
-[_UIDynamicButton _physicalButton];
-[_UIDynamicButton _hidEventAttributes];
-[_UIDynamicButton _isTouching];
-[_UIDynamicButton _nextStageNormalizedForceThreshold];
-[_UIDynamicButton _normalizedForce];
-[_UIDynamicButton _normalizedForceVelocity];
-[_UIDynamicButton _phase];
-[_UIDynamicButton _physicalButtonSource];
-[_UIDynamicButton _position];
-[_UIDynamicButton _positionDelta];
-[_UIDynamicButton _pressedStageNormalizedForceThreshold];
-[_UIDynamicButton _releaseStageNormalizedForceThreshold];
-[_UIDynamicButton _stage];
-[_UIDynamicButton _touchMajorRadius];
-[_UIDynamicButton _touchMinorRadius];
-[_UIDynamicButton _touchPositionHints];
-[_UIDynamicButton _usage];
-[_UIDynamicButton _usagePage];
```
