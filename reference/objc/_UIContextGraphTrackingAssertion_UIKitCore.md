# `_UIContextGraphTrackingAssertion`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BSSimpleAssertion`
- 3 instance variables, 1 properties, 5 instance methods, 0 class methods

## Instance variables

```
I _contextID;
@"NSArray" _contextIDGraph;
@? _clientHandlerBlock;
```

## Properties

```
@property (TI,R,N,V_contextID) contextID;
```

## Instance methods

```
-[_UIContextGraphTrackingAssertion contextID];
-[_UIContextGraphTrackingAssertion setWindowGraph:];
-[_UIContextGraphTrackingAssertion _setWindowGraph:callHandler:];
-[_UIContextGraphTrackingAssertion initWithContextID:windowGraph:clientHandlerBlock:invalidationBlock:];
-[_UIContextGraphTrackingAssertion isContextIDRelevant:];
```
