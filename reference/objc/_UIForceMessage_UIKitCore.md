# `_UIForceMessage`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIForceObservationMessageConstructing`
- 4 instance variables, 8 properties, 7 instance methods, 2 class methods

## Instance variables

```
B _reset;
d touchForce;
Q stage;
d timestamp;
```

## Properties

```
@property (Td,N,VtouchForce) touchForce;
@property (TQ,N,Vstage) stage;
@property (Td,N,Vtimestamp) timestamp;
@property (TB,R,N,GisReset,V_reset) reset;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIForceMessage reset];
+[_UIForceMessage observe:];
```

## Instance methods

```
-[_UIForceMessage setTimestamp:];
-[_UIForceMessage stage];
-[_UIForceMessage timestamp];
-[_UIForceMessage touchForce];
-[_UIForceMessage isReset];
-[_UIForceMessage setStage:];
-[_UIForceMessage setTouchForce:];
```
