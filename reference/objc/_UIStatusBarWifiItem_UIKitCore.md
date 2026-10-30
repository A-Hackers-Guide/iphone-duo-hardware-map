# `_UIStatusBarWifiItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarItem`
- 3 instance variables, 3 properties, 18 instance methods, 4 class methods

## Instance variables

```
@"_UIStatusBarWifiSignalView" _signalView;
@"_UIStatusBarImageView" _networkIconView;
@"_UIStatusBarStringView" _rawStringView;
```

## Properties

```
@property (T@"_UIStatusBarWifiSignalView",&,N,V_signalView) signalView;
@property (T@"_UIStatusBarImageView",&,N,V_networkIconView) networkIconView;
@property (T@"_UIStatusBarStringView",&,N,V_rawStringView) rawStringView;
```

## Class methods

```
+[_UIStatusBarWifiItem signalStrengthDisplayIdentifier];
+[_UIStatusBarWifiItem groupWithPriority:];
+[_UIStatusBarWifiItem iconDisplayIdentifier];
+[_UIStatusBarWifiItem rawDisplayIdentifier];
```

## Instance methods

```
-[_UIStatusBarWifiItem _barThicknessForUpdate:];
-[_UIStatusBarWifiItem _create_rawStringView];
-[_UIStatusBarWifiItem viewForIdentifier:];
-[_UIStatusBarWifiItem setRawStringView:];
-[_UIStatusBarWifiItem _interspaceForUpdate:];
-[_UIStatusBarWifiItem signalView];
-[_UIStatusBarWifiItem rawStringView];
-[_UIStatusBarWifiItem setSignalView:];
-[_UIStatusBarWifiItem _totalWidthForUpdate:];
-[_UIStatusBarWifiItem _create_signalView];
-[_UIStatusBarWifiItem dependentEntryKeys];
-[_UIStatusBarWifiItem _backgroundColorForUpdate:entry:];
-[_UIStatusBarWifiItem setNetworkIconView:];
-[_UIStatusBarWifiItem applyUpdate:toDisplayItem:];
-[_UIStatusBarWifiItem _create_networkIconView];
-[_UIStatusBarWifiItem _fillColorForUpdate:entry:];
-[_UIStatusBarWifiItem networkIconView];
-[_UIStatusBarWifiItem _barCountForUpdate:];
```
