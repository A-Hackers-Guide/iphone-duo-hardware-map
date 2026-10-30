# `SBRotationDodgingModifierEvent`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBDodgingModifierEvent`
- 4 instance variables, 4 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSUUID" _identifier;
q _fromOrientation;
q _toOrientation;
Q _phase;
```

## Properties

```
@property (T@"NSUUID",R,N,V_identifier) identifier;
@property (Tq,R,N,V_fromOrientation) fromOrientation;
@property (Tq,R,N,V_toOrientation) toOrientation;
@property (TQ,R,N,V_phase) phase;
```

## Instance methods

```
-[SBRotationDodgingModifierEvent phase];
-[SBRotationDodgingModifierEvent identifier];
-[SBRotationDodgingModifierEvent type];
-[SBRotationDodgingModifierEvent fromOrientation];
-[SBRotationDodgingModifierEvent toOrientation];
-[SBRotationDodgingModifierEvent initWithIdentifier:fromOrientation:toOrientation:phase:];
```
