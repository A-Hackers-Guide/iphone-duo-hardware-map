# `_SBStatusBarChanges`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 12 instance methods, 0 class methods

## Instance variables

```
B _statusBarStyleChanged;
B _statusBarPartStyleChanged;
q _statusBarStyle;
q _statusBarPartStyle;
@"NSString" _statusBarPartIdentifier;
```

## Properties

```
@property (TB,N,V_statusBarStyleChanged) statusBarStyleChanged;
@property (Tq,N,V_statusBarStyle) statusBarStyle;
@property (TB,N,V_statusBarPartStyleChanged) statusBarPartStyleChanged;
@property (Tq,N,V_statusBarPartStyle) statusBarPartStyle;
@property (T@"NSString",&,N,V_statusBarPartIdentifier) statusBarPartIdentifier;
```

## Instance methods

```
-[_SBStatusBarChanges invalidate];
-[_SBStatusBarChanges statusBarStyle];
-[_SBStatusBarChanges setStatusBarStyle:];
-[_SBStatusBarChanges setStatusBarPartIdentifier:];
-[_SBStatusBarChanges setStatusBarPartStyle:];
-[_SBStatusBarChanges setStatusBarPartStyle:forPartWithIdentifier:];
-[_SBStatusBarChanges setStatusBarPartStyleChanged:];
-[_SBStatusBarChanges setStatusBarStyleChanged:];
-[_SBStatusBarChanges statusBarPartIdentifier];
-[_SBStatusBarChanges statusBarPartStyle];
-[_SBStatusBarChanges statusBarPartStyleChanged];
-[_SBStatusBarChanges statusBarStyleChanged];
```
