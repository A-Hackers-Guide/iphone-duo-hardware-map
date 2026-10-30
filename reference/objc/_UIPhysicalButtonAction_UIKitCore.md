# `_UIPhysicalButtonAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDebugDescriptionProviding`
- 15 instance variables, 20 properties, 24 instance methods, 0 class methods

## Instance variables

```
Q _button;
Q _source;
Q _state;
Q _behavior;
q _driverSource;
d _timestamp;
@"_UIPhysicalButtonContact" _contact;
Q _stage;
Q _numberOfStages;
Q _stagePhase;
d _normalizedForce;
d _normalizedForceVelocity;
d _releaseStageNormalizedForceThreshold;
d _pressedStageNormalizedForceThreshold;
d _nextStageNormalizedForceThreshold;
```

## Properties

```
@property (TQ,R,N) _button;
@property (TQ,R,N) _source;
@property (TQ,R,N) _state;
@property (TQ,R,N) _behavior;
@property (Td,R,N) _timestamp;
@property (T@"_UIPhysicalButtonContact",R,N) _contact;
@property (T{CGPoint=dd},R,N) _position;
@property (T{CGPoint=dd},R,N) _positionDelta;
@property (TQ,R,N) _stage;
@property (TQ,R,N) _numberOfStages;
@property (TQ,R,N) _stagePhase;
@property (Td,R,N) _normalizedForce;
@property (Td,R,N) _normalizedForceVelocity;
@property (Td,R,N) _releaseStageNormalizedForceThreshold;
@property (Td,R,N) _pressedStageNormalizedForceThreshold;
@property (Td,R,N) _nextStageNormalizedForceThreshold;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIPhysicalButtonAction _state];
-[_UIPhysicalButtonAction debugDescription];
-[_UIPhysicalButtonAction succinctDescriptionBuilder];
-[_UIPhysicalButtonAction init];
-[_UIPhysicalButtonAction _button];
-[_UIPhysicalButtonAction descriptionWithMultilinePrefix:];
-[_UIPhysicalButtonAction _source];
-[_UIPhysicalButtonAction succinctDescription];
-[_UIPhysicalButtonAction debugDescriptionWithMultilinePrefix:];
-[_UIPhysicalButtonAction description];
-[_UIPhysicalButtonAction _behavior];
-[_UIPhysicalButtonAction descriptionBuilderWithMultilinePrefix:];
-[_UIPhysicalButtonAction _timestamp];
-[_UIPhysicalButtonAction _numberOfStages];
-[_UIPhysicalButtonAction _contact];
-[_UIPhysicalButtonAction _nextStageNormalizedForceThreshold];
-[_UIPhysicalButtonAction _normalizedForce];
-[_UIPhysicalButtonAction _normalizedForceVelocity];
-[_UIPhysicalButtonAction _position];
-[_UIPhysicalButtonAction _positionDelta];
-[_UIPhysicalButtonAction _pressedStageNormalizedForceThreshold];
-[_UIPhysicalButtonAction _releaseStageNormalizedForceThreshold];
-[_UIPhysicalButtonAction _stage];
-[_UIPhysicalButtonAction _stagePhase];
```
