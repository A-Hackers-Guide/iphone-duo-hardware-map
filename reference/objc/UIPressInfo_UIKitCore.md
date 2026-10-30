# `UIPressInfo`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 11 instance variables, 11 properties, 25 instance methods, 1 class methods

## Instance variables

```
B _longClick;
I _contextID;
d _timestamp;
q _phase;
q _type;
Q _source;
Q _gameControllerComponent;
d _force;
Q _clickCount;
@"UIKey" _key;
q _modifierFlags;
```

## Properties

```
@property (Td,N,V_timestamp) timestamp;
@property (Tq,N,V_phase) phase;
@property (Tq,N,V_type) type;
@property (TQ,N,V_source) source;
@property (TQ,N,V_gameControllerComponent) gameControllerComponent;
@property (Td,N,V_force) force;
@property (TQ,N,V_clickCount) clickCount;
@property (TB,N,GisLongClick,V_longClick) longClick;
@property (TI,N,V_contextID) contextID;
@property (T@"UIKey",&,N,V_key) key;
@property (Tq,N,V_modifierFlags) modifierFlags;
```

## Class methods

```
+[UIPressInfo _keyboardPressInfoForType:isKeyDown:timestamp:contextID:modifierFlags:];
```

## Instance methods

```
-[UIPressInfo setTimestamp:];
-[UIPressInfo clickCount];
-[UIPressInfo phase];
-[UIPressInfo setContextID:];
-[UIPressInfo init];
-[UIPressInfo isLongClick];
-[UIPressInfo timestamp];
-[UIPressInfo modifierFlags];
-[UIPressInfo setKey:];
-[UIPressInfo setModifierFlags:];
-[UIPressInfo setSource:];
-[UIPressInfo setClickCount:];
-[UIPressInfo setType:];
-[UIPressInfo type];
-[UIPressInfo gameControllerComponent];
-[UIPressInfo description];
-[UIPressInfo setPhase:];
-[UIPressInfo setGameControllerComponent:];
-[UIPressInfo force];
-[UIPressInfo contextID];
-[UIPressInfo setLongClick:];
-[UIPressInfo setForce:];
-[UIPressInfo _sourceDescription];
-[UIPressInfo source];
-[UIPressInfo key];
```
