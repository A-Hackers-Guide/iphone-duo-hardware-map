# `_UIStatusBarCellularCondensedItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarCellularItem`
- 7 instance variables, 7 properties, 34 instance methods, 7 class methods

## Instance variables

```
B _reducesFontSize;
@"_UIStatusBarDualCellularSignalView" _dualSignalView;
@"_UIStatusBarMultilineStringView" _dualNameView;
@"_UIStatusBarStringView" _dualSingleLineNameView;
@"_UIStatusBarStringView" _dualSingleLineNameAndTypeView;
@"_UIStatusBarEmergencySignalView" _sosSignalView;
@"_UIStatusBarCellularNetworkTypeView" _animatedNetworkTypeView;
```

## Properties

```
@property (T@"_UIStatusBarDualCellularSignalView",&,N,V_dualSignalView) dualSignalView;
@property (T@"_UIStatusBarMultilineStringView",&,N,V_dualNameView) dualNameView;
@property (T@"_UIStatusBarStringView",&,N,V_dualSingleLineNameView) dualSingleLineNameView;
@property (T@"_UIStatusBarStringView",&,N,V_dualSingleLineNameAndTypeView) dualSingleLineNameAndTypeView;
@property (T@"_UIStatusBarEmergencySignalView",&,N,V_sosSignalView) sosSignalView;
@property (T@"_UIStatusBarCellularNetworkTypeView",&,N,V_animatedNetworkTypeView) animatedNetworkTypeView;
@property (TB,N,V_reducesFontSize) reducesFontSize;
```

## Class methods

```
+[_UIStatusBarCellularCondensedItem dualSingleLineNameDisplayIdentifier];
+[_UIStatusBarCellularCondensedItem sosSignalStrengthDisplayIdentifier];
+[_UIStatusBarCellularCondensedItem dualSingleLineNameAndTypeDisplayIdentifier];
+[_UIStatusBarCellularCondensedItem animatedTypeDisplayIdentifier];
+[_UIStatusBarCellularCondensedItem groupWithHighPriority:lowPriority:typeClass:allowDualNetwork:];
+[_UIStatusBarCellularCondensedItem dualNameDisplayIdentifier];
+[_UIStatusBarCellularCondensedItem dualSignalStrengthDisplayIdentifier];
```

## Instance methods

```
-[_UIStatusBarCellularCondensedItem setDualSignalView:];
-[_UIStatusBarCellularCondensedItem animatedNetworkTypeView];
-[_UIStatusBarCellularCondensedItem _create_dualNameView];
-[_UIStatusBarCellularCondensedItem applyStyleAttributes:toDisplayItem:];
-[_UIStatusBarCellularCondensedItem initWithIdentifier:statusBar:];
-[_UIStatusBarCellularCondensedItem _create_dualSingleLineNameAndTypeView];
-[_UIStatusBarCellularCondensedItem viewForIdentifier:];
-[_UIStatusBarCellularCondensedItem sosSignalView];
-[_UIStatusBarCellularCondensedItem setReducesFontSize:];
-[_UIStatusBarCellularCondensedItem _nonCondensedFontRangeForEntry:];
-[_UIStatusBarCellularCondensedItem dualSingleLineNameAndTypeView];
-[_UIStatusBarCellularCondensedItem _stringForCellularType:];
-[_UIStatusBarCellularCondensedItem _create_animatedNetworkTypeView];
-[_UIStatusBarCellularCondensedItem _create_dualSingleLineNameView];
-[_UIStatusBarCellularCondensedItem dualSingleLineNameView];
-[_UIStatusBarCellularCondensedItem _create_dualSignalView];
-[_UIStatusBarCellularCondensedItem setDualSingleLineNameView:];
-[_UIStatusBarCellularCondensedItem entryForDisplayItemWithIdentifier:];
-[_UIStatusBarCellularCondensedItem _singleCellularEntryMatching:];
-[_UIStatusBarCellularCondensedItem _fontForEntry:styleAttributes:baselineOffset:];
-[_UIStatusBarCellularCondensedItem canEnableDisplayItem:fromData:];
-[_UIStatusBarCellularCondensedItem dualNameView];
-[_UIStatusBarCellularCondensedItem _create_sosSignalView];
-[_UIStatusBarCellularCondensedItem setDualSingleLineNameAndTypeView:];
-[_UIStatusBarCellularCondensedItem dependentEntryKeys];
-[_UIStatusBarCellularCondensedItem setDualNameView:];
-[_UIStatusBarCellularCondensedItem applyUpdate:toDisplayItem:];
-[_UIStatusBarCellularCondensedItem setSosSignalView:];
-[_UIStatusBarCellularCondensedItem setAnimatedNetworkTypeView:];
-[_UIStatusBarCellularCondensedItem reducesFontSize];
-[_UIStatusBarCellularCondensedItem prepareAnimation:forDisplayItem:];
-[_UIStatusBarCellularCondensedItem dualSignalView];
-[_UIStatusBarCellularCondensedItem _animateServiceType:prefixLength:currentType:];
-[_UIStatusBarCellularCondensedItem _showCallFowardingForEntry:];
```
