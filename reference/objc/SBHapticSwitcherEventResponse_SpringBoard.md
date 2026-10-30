# `SBHapticSwitcherEventResponse`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `SBSwitcherModifierEventResponse`
- 3 instance variables, 3 properties, 7 instance methods, 0 class methods

## Instance variables

```
q _hapticType;
q _phase;
Q _hidEventSenderID;
```

## Properties

```
@property (Tq,R,N,V_hapticType) hapticType;
@property (Tq,R,N,V_phase) phase;
@property (TQ,N,V_hidEventSenderID) hidEventSenderID;
```

## Instance methods

```
-[SBHapticSwitcherEventResponse phase];
-[SBHapticSwitcherEventResponse type];
-[SBHapticSwitcherEventResponse hapticType];
-[SBHapticSwitcherEventResponse descriptionBuilderWithMultilinePrefix:];
-[SBHapticSwitcherEventResponse hidEventSenderID];
-[SBHapticSwitcherEventResponse initWithHapticType:phase:];
-[SBHapticSwitcherEventResponse setHidEventSenderID:];
```
