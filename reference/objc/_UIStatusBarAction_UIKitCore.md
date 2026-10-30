# `_UIStatusBarAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 5 instance methods, 1 class methods

## Instance variables

```
B _enabled;
@? _block;
```

## Properties

```
@property (T@?,C,N,V_block) block;
@property (TB,N,GisEnabled,V_enabled) enabled;
```

## Class methods

```
+[_UIStatusBarAction actionWithBlock:];
```

## Instance methods

```
-[_UIStatusBarAction block];
-[_UIStatusBarAction setBlock:];
-[_UIStatusBarAction isEnabled];
-[_UIStatusBarAction setEnabled:];
-[_UIStatusBarAction performWithStatusBar:completionHandler:];
```
