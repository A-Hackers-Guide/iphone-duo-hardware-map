# `_UIStatusBarDisplayItemPlacementNetworkGroup`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarDisplayItemPlacementGroup`
- 2 instance variables, 2 properties, 2 instance methods, 4 class methods

## Instance variables

```
@"_UIStatusBarDisplayItemPlacementCellularGroup" _cellularGroup;
@"_UIStatusBarDisplayItemPlacementWifiGroup" _wifiGroup;
```

## Properties

```
@property (T@"_UIStatusBarDisplayItemPlacementCellularGroup",R,N,V_cellularGroup) cellularGroup;
@property (T@"_UIStatusBarDisplayItemPlacementWifiGroup",R,N,V_wifiGroup) wifiGroup;
```

## Class methods

```
+[_UIStatusBarDisplayItemPlacementNetworkGroup _groupWithCellularGroup:wifiGroup:includeCellularName:];
+[_UIStatusBarDisplayItemPlacementNetworkGroup groupWithHighPriority:lowPriority:cellularItemClass:wifiItemClass:cellularTypeClass:includeCellularName:allowDualNetwork:];
+[_UIStatusBarDisplayItemPlacementNetworkGroup groupWithHighPriority:lowPriority:cellularItemClass:wifiItemClass:includeCellularName:];
+[_UIStatusBarDisplayItemPlacementNetworkGroup secondaryGroupWithHighPriority:lowPriority:cellularItemClass:wifiItemClass:];
```

## Instance methods

```
-[_UIStatusBarDisplayItemPlacementNetworkGroup cellularGroup];
-[_UIStatusBarDisplayItemPlacementNetworkGroup wifiGroup];
```
