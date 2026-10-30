# `_UIMainMenuDeferredElementState`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIMainMenuElementGroupState_Internal`, `_UIMainMenuElementGroupState`, `NSSecureCoding`
- 4 instance variables, 8 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _childMenuStates;
@"NSDictionary" _fulfilledDeferredElementStates;
@"NSDictionary" _commandStates;
@"NSArray" _providedElements;
```

## Properties

```
@property (T@"NSArray",R,N,V_providedElements) providedElements;
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
+[_UIMainMenuDeferredElementState supportsSecureCoding];
```

## Instance methods

```
-[_UIMainMenuDeferredElementState encodeWithCoder:];
-[_UIMainMenuDeferredElementState hash];
-[_UIMainMenuDeferredElementState description];
-[_UIMainMenuDeferredElementState initWithCoder:];
-[_UIMainMenuDeferredElementState isEqual:];
-[_UIMainMenuDeferredElementState childMenuStates];
-[_UIMainMenuDeferredElementState _initWithProvidedElements:];
-[_UIMainMenuDeferredElementState _initWithProvidedElements:childMenuStates:fulfilledDeferredElementStates:commandStates:];
-[_UIMainMenuDeferredElementState commandStates];
-[_UIMainMenuDeferredElementState fulfilledDeferredElementStates];
-[_UIMainMenuDeferredElementState providedElements];
-[_UIMainMenuDeferredElementState setChildMenuStates:];
-[_UIMainMenuDeferredElementState setCommandStates:];
-[_UIMainMenuDeferredElementState setFulfilledDeferredElementStates:];
```
