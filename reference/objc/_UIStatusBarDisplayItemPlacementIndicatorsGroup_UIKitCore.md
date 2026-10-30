# `_UIStatusBarDisplayItemPlacementIndicatorsGroup`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarDisplayItemPlacementGroup`
- 3 instance variables, 3 properties, 3 instance methods, 2 class methods

## Instance variables

```
@"NSArray" _stablePlacements;
@"NSArray" _unstablePlacements;
@"_UIStatusBarDisplayItemPlacement" _bluetoothInsetPaddingItem;
```

## Properties

```
@property (T@"NSArray",R,C,N,V_stablePlacements) stablePlacements;
@property (T@"NSArray",R,C,N,V_unstablePlacements) unstablePlacements;
@property (T@"_UIStatusBarDisplayItemPlacement",R,N,V_bluetoothInsetPaddingItem) bluetoothInsetPaddingItem;
```

## Class methods

```
+[_UIStatusBarDisplayItemPlacementIndicatorsGroup activityItemDisplayIdentifier];
+[_UIStatusBarDisplayItemPlacementIndicatorsGroup groupWithHighPriority:lowPriority:bluetoothPaddingInset:];
```

## Instance methods

```
-[_UIStatusBarDisplayItemPlacementIndicatorsGroup bluetoothInsetPaddingItem];
-[_UIStatusBarDisplayItemPlacementIndicatorsGroup stablePlacements];
-[_UIStatusBarDisplayItemPlacementIndicatorsGroup unstablePlacements];
```
