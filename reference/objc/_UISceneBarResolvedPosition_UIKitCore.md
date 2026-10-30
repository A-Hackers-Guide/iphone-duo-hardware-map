# `_UISceneBarResolvedPosition`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
q _topBarSizeClass;
q _bottomBarSizeClass;
q _leadingBarSizeClass;
q _trailingBarSizeClass;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _barAlignmentInsets;
```

## Properties

```
@property (T{UIEdgeInsets=dddd},R,N,V_barAlignmentInsets) barAlignmentInsets;
@property (Tq,R,N,V_topBarSizeClass) topBarSizeClass;
@property (Tq,R,N,V_bottomBarSizeClass) bottomBarSizeClass;
@property (Tq,N,V_leadingBarSizeClass) leadingBarSizeClass;
@property (Tq,N,V_trailingBarSizeClass) trailingBarSizeClass;
```

## Instance methods

```
-[_UISceneBarResolvedPosition topBarSizeClass];
-[_UISceneBarResolvedPosition barAlignmentInsets];
-[_UISceneBarResolvedPosition bottomBarSizeClass];
-[_UISceneBarResolvedPosition initWithAlignmentInsets:topBarSizeClass:bottomBarSizeClass:];
-[_UISceneBarResolvedPosition trailingBarSizeClass];
-[_UISceneBarResolvedPosition leadingBarSizeClass];
-[_UISceneBarResolvedPosition setTrailingBarSizeClass:];
-[_UISceneBarResolvedPosition isEqual:];
-[_UISceneBarResolvedPosition setLeadingBarSizeClass:];
```
