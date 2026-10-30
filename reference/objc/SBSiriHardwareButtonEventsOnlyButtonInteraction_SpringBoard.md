# `SBSiriHardwareButtonEventsOnlyButtonInteraction`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBHardwareButtonGestureParametersProviderBase`
- Protocols: `SBHardwareButtonInteraction`
- 2 instance variables, 6 properties, 5 instance methods, 1 class methods

## Instance variables

```
q _siriButtonIdentifier;
@"SBSiriHardwareButtonInteraction" _parentSiriInteraction;
```

## Properties

```
@property (Tq,N,V_siriButtonIdentifier) siriButtonIdentifier;
@property (T@"SBSiriHardwareButtonInteraction",W,N,V_parentSiriInteraction) parentSiriInteraction;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSiriHardwareButtonEventsOnlyButtonInteraction hardwareButtonInteractionForHomeButtonForwardingToInteraction:];
```

## Instance methods

```
-[SBSiriHardwareButtonEventsOnlyButtonInteraction siriButtonIdentifier];
-[SBSiriHardwareButtonEventsOnlyButtonInteraction consumeSinglePressUp];
-[SBSiriHardwareButtonEventsOnlyButtonInteraction parentSiriInteraction];
-[SBSiriHardwareButtonEventsOnlyButtonInteraction setParentSiriInteraction:];
-[SBSiriHardwareButtonEventsOnlyButtonInteraction setSiriButtonIdentifier:];
```
