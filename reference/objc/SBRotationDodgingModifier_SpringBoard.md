# `SBRotationDodgingModifier`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBDodgingModifier`
- 4 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _identifier;
q _fromOrientation;
q _toOrientation;
Q _phase;
```

## Properties

```
@property (T@"NSUUID",&,N,V_identifier) identifier;
@property (Tq,N,V_fromOrientation) fromOrientation;
@property (Tq,N,V_toOrientation) toOrientation;
@property (TQ,N,V_phase) phase;
```

## Instance methods

```
-[SBRotationDodgingModifier phase];
-[SBRotationDodgingModifier identifier];
-[SBRotationDodgingModifier setIdentifier:];
-[SBRotationDodgingModifier setPhase:];
-[SBRotationDodgingModifier fromOrientation];
-[SBRotationDodgingModifier setFromOrientation:];
-[SBRotationDodgingModifier setToOrientation:];
-[SBRotationDodgingModifier toOrientation];
-[SBRotationDodgingModifier animationBehaviorModeForIdentifier:];
-[SBRotationDodgingModifier handleRotationEvent:];
-[SBRotationDodgingModifier initWithIdentifier:fromOrientation:toOrientation:];
```
