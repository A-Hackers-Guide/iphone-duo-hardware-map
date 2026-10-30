# `_UIStatusBarVisualProvider_iOS`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIStatusBarVisualProvider`
- 11 instance variables, 28 properties, 47 instance methods, 6 class methods

## Instance variables

```
B _wantsPillInExpandedTrailingPlacements;
B _expanded;
B _onLockScreen;
@"_UIStatusBar" _statusBar;
d _leadingItemSpacing;
@"_UIStatusBarDisplayItemPlacementNetworkGroup" _expandedNetworkGroup;
@"NSArray" _expandedCellularPlacementsAffectedByAirplaneMode;
@"NSArray" _expandedLeadingPlacements;
@"NSArray" _expandedTrailingPlacements;
@"_UIStatusBarDisplayItemPlacement" _expandedPillPlacement;
@"_UIStatusBarDisplayItemPlacementGroup" _secondaryWifiGroup;
```

## Properties

```
@property (T@"_UIStatusBarDisplayItemPlacementGroup",&,N,V_secondaryWifiGroup) secondaryWifiGroup;
@property (TB,R) hasCellularCapability;
@property (TB,R) wantsExpandedLeadingPlacements;
@property (TB,R,V_wantsPillInExpandedTrailingPlacements) wantsPillInExpandedTrailingPlacements;
@property (Td,R,V_leadingItemSpacing) leadingItemSpacing;
@property (Td,R) itemSpacing;
@property (Td,R) expandedItemSpacing;
@property (Td,R) regionSpacing;
@property (Td,R) bluetoothPaddingInset;
@property (TB,N,V_expanded) expanded;
@property (TB,N,V_onLockScreen) onLockScreen;
@property (T@"_UIStatusBarDisplayItemPlacementNetworkGroup",R,N,V_expandedNetworkGroup) expandedNetworkGroup;
@property (T@"NSArray",R,N,V_expandedCellularPlacementsAffectedByAirplaneMode) expandedCellularPlacementsAffectedByAirplaneMode;
@property (T@"NSArray",R,N,V_expandedLeadingPlacements) expandedLeadingPlacements;
@property (T@"NSArray",R,N,V_expandedTrailingPlacements) expandedTrailingPlacements;
@property (T@"_UIStatusBarDisplayItemPlacement",R,N,V_expandedPillPlacement) expandedPillPlacement;
@property (T@"_UIStatusBarAnimation",R,N) animationForAirplaneMode;
@property (Td,R,N) airplaneObstacleFadeOutDuration;
@property (Td,R,N) airplaneObstacleFadeInDuration;
@property (T@"_UIStatusBarAnimation",R,N) animationForProminentLocation;
@property (T@"_UIStatusBar",W,N,V_statusBar) statusBar;
@property (TB,R,N) supportsIndirectPointerTouchActions;
@property (T@"UIFont",R,N) clockFont;
@property (TB,?,R,N) canFixupDisplayItemAttributes;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIStatusBarVisualProvider_iOS cornerRadius];
+[_UIStatusBarVisualProvider_iOS height];
+[_UIStatusBarVisualProvider_iOS requiresIterativeOverflowLayout];
+[_UIStatusBarVisualProvider_iOS intrinsicContentSizeForOrientation:];
+[_UIStatusBarVisualProvider_iOS scalesWithScreenNativeScale];
+[_UIStatusBarVisualProvider_iOS visualProviderSubclassForScreen:visualProviderInfo:];
```

## Instance methods

```
-[_UIStatusBarVisualProvider_iOS statusBar];
-[_UIStatusBarVisualProvider_iOS setExpanded:];
-[_UIStatusBarVisualProvider_iOS setStatusBar:];
-[_UIStatusBarVisualProvider_iOS init];
-[_UIStatusBarVisualProvider_iOS styleAttributesForStyle:];
-[_UIStatusBarVisualProvider_iOS hasCellularCapability];
-[_UIStatusBarVisualProvider_iOS itemSpacing];
-[_UIStatusBarVisualProvider_iOS clockFont];
-[_UIStatusBarVisualProvider_iOS setOnLockScreen:];
-[_UIStatusBarVisualProvider_iOS expanded];
-[_UIStatusBarVisualProvider_iOS airplaneTravelOffsetInProposedPartWithIdentifier:animationType:];
-[_UIStatusBarVisualProvider_iOS _applyToAppearingRegions:block:];
-[_UIStatusBarVisualProvider_iOS airplaneObstacleFadeOutDuration];
-[_UIStatusBarVisualProvider_iOS _createExpandedPlacements];
-[_UIStatusBarVisualProvider_iOS actionable:highlighted:initialPress:];
-[_UIStatusBarVisualProvider_iOS additionAnimationForDisplayItemWithIdentifier:itemAnimation:];
-[_UIStatusBarVisualProvider_iOS airplaneObstacleFadeInDuration];
-[_UIStatusBarVisualProvider_iOS airplaneShouldFadeForAnimationType:];
-[_UIStatusBarVisualProvider_iOS airplaneSpeedForAnimationType:];
-[_UIStatusBarVisualProvider_iOS animationForAirplaneMode];
-[_UIStatusBarVisualProvider_iOS animationForProminentLocation];
-[_UIStatusBarVisualProvider_iOS bluetoothPaddingInset];
-[_UIStatusBarVisualProvider_iOS defaultAnimationForDisplayItemWithIdentifier:];
-[_UIStatusBarVisualProvider_iOS displayItemIdentifiersForPartWithIdentifier:];
-[_UIStatusBarVisualProvider_iOS expandedCellularPlacementsAffectedByAirplaneMode];
-[_UIStatusBarVisualProvider_iOS expandedItemSpacing];
-[_UIStatusBarVisualProvider_iOS expandedLeadingPlacements];
-[_UIStatusBarVisualProvider_iOS expandedNetworkGroup];
-[_UIStatusBarVisualProvider_iOS expandedPillPlacement];
-[_UIStatusBarVisualProvider_iOS expandedTrailingPlacements];
-[_UIStatusBarVisualProvider_iOS hasCustomAnimationForDisplayItemWithIdentifier:removal:];
-[_UIStatusBarVisualProvider_iOS leadingItemSpacing];
-[_UIStatusBarVisualProvider_iOS modeUpdatedFromMode:];
-[_UIStatusBarVisualProvider_iOS onLockScreen];
-[_UIStatusBarVisualProvider_iOS orderedDisplayItemPlacementsInRegionWithIdentifier:];
-[_UIStatusBarVisualProvider_iOS regionSpacing];
-[_UIStatusBarVisualProvider_iOS removalAnimationForDisplayItemWithIdentifier:itemAnimation:];
-[_UIStatusBarVisualProvider_iOS secondaryWifiGroup];
-[_UIStatusBarVisualProvider_iOS setSecondaryWifiGroup:];
-[_UIStatusBarVisualProvider_iOS setupInContainerView:];
-[_UIStatusBarVisualProvider_iOS supportsIndirectPointerTouchActions];
-[_UIStatusBarVisualProvider_iOS updateDataForService:];
-[_UIStatusBarVisualProvider_iOS updateDataForSystemNavigation:];
-[_UIStatusBarVisualProvider_iOS wantsBackgroundActivityPillInExpandedTrailingPlacements];
-[_UIStatusBarVisualProvider_iOS wantsExpandedLeadingPlacements];
-[_UIStatusBarVisualProvider_iOS wantsPillInExpandedTrailingPlacements];
-[_UIStatusBarVisualProvider_iOS willUpdateWithData:];
```
