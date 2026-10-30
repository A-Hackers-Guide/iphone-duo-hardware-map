# `_UIMainMenuState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIMainMenuElementGroupState_Internal`, `_UIMainMenuElementGroupState`, `NSSecureCoding`
- 3 instance variables, 7 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _childMenuStates;
@"NSDictionary" _fulfilledDeferredElementStates;
@"NSDictionary" _commandStates;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_childMenuStates) childMenuStates;
@property (T@"NSDictionary",&,N,V_fulfilledDeferredElementStates) fulfilledDeferredElementStates;
@property (T@"NSDictionary",&,N,V_commandStates) commandStates;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIMainMenuState supportsSecureCoding];
```

## Instance methods

```
-[_UIMainMenuState _init];
-[_UIMainMenuState encodeWithCoder:];
-[_UIMainMenuState hash];
-[_UIMainMenuState description];
-[_UIMainMenuState initWithCoder:];
-[_UIMainMenuState isEqual:];
-[_UIMainMenuState childMenuStates];
-[_UIMainMenuState _initWithChildMenuStates:fulfilledDeferredElementStates:commandStates:];
-[_UIMainMenuState commandStates];
-[_UIMainMenuState fulfilledDeferredElementStates];
-[_UIMainMenuState setChildMenuStates:];
-[_UIMainMenuState setCommandStates:];
-[_UIMainMenuState setFulfilledDeferredElementStates:];
```
