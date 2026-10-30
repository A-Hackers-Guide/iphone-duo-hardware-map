# `UIKBGraphCache`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIScreenBasedObject`
- 2 instance variables, 7 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"UIScreen" _screen;
@"NSMutableDictionary" _graphCache;
```

## Properties

```
@property (T@"NSMutableDictionary",R,N,V_graphCache) graphCache;
@property (T@"UIScreen",R) _intendedScreen;
@property (T@"NSDictionary",R) _options;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKBGraphCache graphCacheForScreen:];
```

## Instance methods

```
-[UIKBGraphCache _options];
-[UIKBGraphCache _initWithScreen:options:];
-[UIKBGraphCache _matchingOptions:];
-[UIKBGraphCache graphCache];
-[UIKBGraphCache _intendedScreen];
```
