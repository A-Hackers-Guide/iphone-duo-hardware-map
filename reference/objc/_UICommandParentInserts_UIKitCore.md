# `_UICommandParentInserts`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSMutableDictionary" _childInserts;
@"NSMutableArray" _fallbackBeforeElements;
@"NSMutableArray" _fallbackAfterElements;
@"NSArray" _atStartElements;
@"NSArray" _atEndElements;
```

## Properties

```
@property (T@"NSArray",R,N,V_atStartElements) atStartElements;
@property (T@"NSArray",R,N,V_atEndElements) atEndElements;
@property (T@"NSDictionary",R,N,V_childInserts) childInserts;
@property (T@"NSArray",R,N,V_fallbackBeforeElements) fallbackBeforeElements;
@property (T@"NSArray",R,N,V_fallbackAfterElements) fallbackAfterElements;
```

## Instance methods

```
-[_UICommandParentInserts atStartElements];
-[_UICommandParentInserts _addFallbackBeforeElements:fallbackAfterElements:];
-[_UICommandParentInserts _setAtStartElements:atEndElements:];
-[_UICommandParentInserts _setBeforeElements:afterElements:aroundElement:];
-[_UICommandParentInserts atEndElements];
-[_UICommandParentInserts childInserts];
-[_UICommandParentInserts fallbackAfterElements];
-[_UICommandParentInserts fallbackBeforeElements];
```
