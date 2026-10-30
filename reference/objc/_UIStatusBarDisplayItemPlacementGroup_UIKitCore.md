# `_UIStatusBarDisplayItemPlacementGroup`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _placements;
q _minimumPriority;
q _maximumPriority;
```

## Properties

```
@property (T@"NSArray",C,N,V_placements) placements;
@property (TB,N) enabled;
@property (Tq,R,N,V_minimumPriority) minimumPriority;
@property (Tq,R,N,V_maximumPriority) maximumPriority;
```

## Class methods

```
+[_UIStatusBarDisplayItemPlacementGroup groupWithPriority:placements:];
```

## Instance methods

```
-[_UIStatusBarDisplayItemPlacementGroup enabled];
-[_UIStatusBarDisplayItemPlacementGroup setEnabled:];
-[_UIStatusBarDisplayItemPlacementGroup maximumPriority];
-[_UIStatusBarDisplayItemPlacementGroup minimumPriority];
-[_UIStatusBarDisplayItemPlacementGroup placements];
-[_UIStatusBarDisplayItemPlacementGroup setPlacements:];
```
