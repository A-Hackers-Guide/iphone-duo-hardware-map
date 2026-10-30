# `_UIStatusBarVisualProvider_Split`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarVisualProvider_Phone`
- Protocols: `_UIStatusBarCellularItemTypeStringProvider`
- 14 instance variables, 37 properties, 93 instance methods, 10 class methods

## Instance variables

```
B _delayedSystemUpdateData;
@"NSDictionary" _orderedDisplayItemPlacements;
d _animatedTypeDisplayItemSpacingFactor;
@"_UIStatusBarDisplayItemPlacement" _serviceNamePlacement;
@"_UIStatusBarDisplayItemPlacement" _dualServiceNamePlacement;
@"_UIStatusBarDisplayItemPlacementGroup" _lowerWifiGroup;
@"_UIStatusBarDisplayItemPlacement" _batteryChargingPlacement;
@"UILayoutGuide" _cutoutLayoutGuide;
@"UILayoutGuide" _mainRegionsLayoutGuide;
@"NSLayoutConstraint" _expandedLeadingLowerTopConstraint;
@"NSLayoutConstraint" _expandedTrailingBottomConstraint;
@"NSTimer" _systemUpdatesTimer;
@"NSTimer" _batteryExpansionTimer;
@"NSTimer" _airplaneModeIgnoreChangesTimer;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_orderedDisplayItemPlacements) orderedDisplayItemPlacements;
@property (T{CGSize=dd},R) smallPillSize;
@property (T@"UIFont",R) normalFont;
@property (T@"UIFont",R) expandedFont;
@property (T@"UIFont",R) emphasizedFont;
@property (T@"UIFont",R) smallFont;
@property (T@"UIFont",R) voiceControlFont;
@property (T@"UIFont",R) systemUpdateFont;
@property (Td,R) baselineBottomInset;
@property (Td,R) lowerExpandedBaselineOffset;
@property (Td,R) bottomLeadingSpace;
@property (Td,R) bottomLeadingTopOffset;
@property (Td,R) normalIconScale;
@property (Td,R) expandedIconScale;
@property (Tq,R) normalIconSize;
@property (Tq,R) expandedIconSize;
@property (T{NSDirectionalEdgeInsets=dddd},R) expandedEdgeInsets;
@property (TB,R) supportsAnimatedCellularNetworkType;
@property (Td,R,V_animatedTypeDisplayItemSpacingFactor) animatedTypeDisplayItemSpacingFactor;
@property (TB,R) supportsCondensedBatteryPercentage;
@property (T@"_UIStatusBarDisplayItemPlacement",&,N,V_serviceNamePlacement) serviceNamePlacement;
@property (T@"_UIStatusBarDisplayItemPlacement",&,N,V_dualServiceNamePlacement) dualServiceNamePlacement;
@property (T@"_UIStatusBarDisplayItemPlacementGroup",&,N,V_lowerWifiGroup) lowerWifiGroup;
@property (T@"_UIStatusBarDisplayItemPlacement",&,N,V_batteryChargingPlacement) batteryChargingPlacement;
@property (T@"UILayoutGuide",&,N,V_cutoutLayoutGuide) cutoutLayoutGuide;
@property (T@"UILayoutGuide",&,N,V_mainRegionsLayoutGuide) mainRegionsLayoutGuide;
@property (T@"NSLayoutConstraint",&,N,V_expandedLeadingLowerTopConstraint) expandedLeadingLowerTopConstraint;
@property (T@"NSLayoutConstraint",&,N,V_expandedTrailingBottomConstraint) expandedTrailingBottomConstraint;
@property (T@"NSTimer",&,N,V_systemUpdatesTimer) systemUpdatesTimer;
@property (T@"NSTimer",&,N,V_batteryExpansionTimer) batteryExpansionTimer;
@property (T@"NSTimer",&,N,V_airplaneModeIgnoreChangesTimer) airplaneModeIgnoreChangesTimer;
@property (TB,N,V_delayedSystemUpdateData) delayedSystemUpdateData;
@property (Td,R) cornerRadius;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIStatusBarVisualProvider_Split expandedFontSize];
+[_UIStatusBarVisualProvider_Split baseFontSize];
+[_UIStatusBarVisualProvider_Split height];
+[_UIStatusBarVisualProvider_Split LTEAPlusFontSize];
+[_UIStatusBarVisualProvider_Split expandedEdgeInset];
+[_UIStatusBarVisualProvider_Split intrinsicContentSizeForOrientation:];
+[_UIStatusBarVisualProvider_Split scalesWithScreenNativeScale];
+[_UIStatusBarVisualProvider_Split showsLargeBatteryChargingAnimation];
+[_UIStatusBarVisualProvider_Split shrinksSingleCharacterTypes];
+[_UIStatusBarVisualProvider_Split visualProviderSubclassForScreen:visualProviderInfo:];
```

## Instance methods

```
-[_UIStatusBarVisualProvider_Split setExpanded:];
-[_UIStatusBarVisualProvider_Split bottomLeadingTopOffset];
-[_UIStatusBarVisualProvider_Split dealloc];
-[_UIStatusBarVisualProvider_Split styleAttributesForStyle:];
-[_UIStatusBarVisualProvider_Split emphasizedFont];
-[_UIStatusBarVisualProvider_Split cornerRadius];
-[_UIStatusBarVisualProvider_Split smallFont];
-[_UIStatusBarVisualProvider_Split itemSpacing];
-[_UIStatusBarVisualProvider_Split normalIconScale];
-[_UIStatusBarVisualProvider_Split expandedIconScale];
-[_UIStatusBarVisualProvider_Split lowerExpandedBaselineOffset];
-[_UIStatusBarVisualProvider_Split clockFont];
-[_UIStatusBarVisualProvider_Split airplaneTravelOffsetInProposedPartWithIdentifier:animationType:];
-[_UIStatusBarVisualProvider_Split airplaneObstacleFadeOutDuration];
-[_UIStatusBarVisualProvider_Split _additionAnimationForBatteryCharging];
-[_UIStatusBarVisualProvider_Split _collapseBattery];
-[_UIStatusBarVisualProvider_Split _collapseChargingBoltTransformForDisplayItem:];
-[_UIStatusBarVisualProvider_Split _delaySystemUpdateData];
-[_UIStatusBarVisualProvider_Split _disableSystemUpdates];
-[_UIStatusBarVisualProvider_Split _expandedChargingBoltTransformForDisplayItem:];
-[_UIStatusBarVisualProvider_Split _orderedDisplayItemPlacements];
-[_UIStatusBarVisualProvider_Split _removalAnimationForBatteryCharging];
-[_UIStatusBarVisualProvider_Split _resetBattery];
-[_UIStatusBarVisualProvider_Split _resumeSystemUpdateData];
-[_UIStatusBarVisualProvider_Split _setupExpandedRegionsInContainerView:sensorHeight:constraints:regions:];
-[_UIStatusBarVisualProvider_Split _shouldShowSystemUpdateForDisplayItemWithIdentifier:];
-[_UIStatusBarVisualProvider_Split _stopBatteryCollapseTimer];
-[_UIStatusBarVisualProvider_Split _systemUpdateAnimationForDisplayItemWithIdentifier:];
-[_UIStatusBarVisualProvider_Split _systemUpdateDelayedDataIdentifiers];
-[_UIStatusBarVisualProvider_Split _updateDataForBatteryCharging:];
-[_UIStatusBarVisualProvider_Split _updateDataForSystemUpdates:];
-[_UIStatusBarVisualProvider_Split _updateExpandedTrailingRegion];
-[_UIStatusBarVisualProvider_Split _updateLowerRegionsWithData:];
-[_UIStatusBarVisualProvider_Split additionAnimationForDisplayItemWithIdentifier:itemAnimation:];
-[_UIStatusBarVisualProvider_Split airplaneModeIgnoreChangesTimer];
-[_UIStatusBarVisualProvider_Split airplaneShouldFadeForAnimationType:];
-[_UIStatusBarVisualProvider_Split airplaneSpeedForAnimationType:];
-[_UIStatusBarVisualProvider_Split animatedTypeDisplayItemSpacingFactor];
-[_UIStatusBarVisualProvider_Split animatedTypeDisplayItemSpacingFactorForCellularType:];
-[_UIStatusBarVisualProvider_Split animationForAirplaneMode];
-[_UIStatusBarVisualProvider_Split animationForProminentLocation];
-[_UIStatusBarVisualProvider_Split baselineBottomInset];
-[_UIStatusBarVisualProvider_Split batteryChargingPlacement];
-[_UIStatusBarVisualProvider_Split batteryExpansionTimer];
-[_UIStatusBarVisualProvider_Split bottomLeadingSpace];
-[_UIStatusBarVisualProvider_Split canFixupDisplayItemAttributes];
-[_UIStatusBarVisualProvider_Split condensedFontForCellularType:defaultFont:baselineOffset:];
-[_UIStatusBarVisualProvider_Split condensedPointSizeForCellularType:defaultPointSize:baselineOffset:];
-[_UIStatusBarVisualProvider_Split cutoutLayoutGuide];
-[_UIStatusBarVisualProvider_Split defaultAnimationForDisplayItemWithIdentifier:];
-[_UIStatusBarVisualProvider_Split delayedSystemUpdateData];
-[_UIStatusBarVisualProvider_Split displayItemIdentifiersForPartWithIdentifier:];
-[_UIStatusBarVisualProvider_Split dualServiceNamePlacement];
-[_UIStatusBarVisualProvider_Split expandedEdgeInsets];
-[_UIStatusBarVisualProvider_Split expandedFont];
-[_UIStatusBarVisualProvider_Split expandedIconSize];
-[_UIStatusBarVisualProvider_Split expandedLeadingLowerTopConstraint];
-[_UIStatusBarVisualProvider_Split expandedTrailingBottomConstraint];
-[_UIStatusBarVisualProvider_Split hasCustomAnimationForDisplayItemWithIdentifier:removal:];
-[_UIStatusBarVisualProvider_Split itemCreated:];
-[_UIStatusBarVisualProvider_Split lowerWifiGroup];
-[_UIStatusBarVisualProvider_Split mainRegionsLayoutGuide];
-[_UIStatusBarVisualProvider_Split normalFont];
-[_UIStatusBarVisualProvider_Split normalIconSize];
-[_UIStatusBarVisualProvider_Split orderedDisplayItemPlacements];
-[_UIStatusBarVisualProvider_Split orderedDisplayItemPlacementsInRegionWithIdentifier:];
-[_UIStatusBarVisualProvider_Split overriddenStyleAttributesForDisplayItemWithIdentifier:];
-[_UIStatusBarVisualProvider_Split regionIdentifiersForPartWithIdentifier:];
-[_UIStatusBarVisualProvider_Split removalAnimationForDisplayItemWithIdentifier:itemAnimation:];
-[_UIStatusBarVisualProvider_Split serviceNamePlacement];
-[_UIStatusBarVisualProvider_Split setAirplaneModeIgnoreChangesTimer:];
-[_UIStatusBarVisualProvider_Split setBatteryChargingPlacement:];
-[_UIStatusBarVisualProvider_Split setBatteryExpansionTimer:];
-[_UIStatusBarVisualProvider_Split setCutoutLayoutGuide:];
-[_UIStatusBarVisualProvider_Split setDelayedSystemUpdateData:];
-[_UIStatusBarVisualProvider_Split setDualServiceNamePlacement:];
-[_UIStatusBarVisualProvider_Split setExpandedLeadingLowerTopConstraint:];
-[_UIStatusBarVisualProvider_Split setExpandedTrailingBottomConstraint:];
-[_UIStatusBarVisualProvider_Split setLowerWifiGroup:];
-[_UIStatusBarVisualProvider_Split setMainRegionsLayoutGuide:];
-[_UIStatusBarVisualProvider_Split setOrderedDisplayItemPlacements:];
-[_UIStatusBarVisualProvider_Split setServiceNamePlacement:];
-[_UIStatusBarVisualProvider_Split setSystemUpdatesTimer:];
-[_UIStatusBarVisualProvider_Split smallPillSize];
-[_UIStatusBarVisualProvider_Split statusBarRegionsUpdated];
-[_UIStatusBarVisualProvider_Split stringForCellularType:condensed:];
-[_UIStatusBarVisualProvider_Split supportsAnimatedCellularNetworkType];
-[_UIStatusBarVisualProvider_Split supportsCondensedBatteryPercentage];
-[_UIStatusBarVisualProvider_Split systemUpdateFont];
-[_UIStatusBarVisualProvider_Split systemUpdatesTimer];
-[_UIStatusBarVisualProvider_Split updateDataForService:];
-[_UIStatusBarVisualProvider_Split voiceControlFont];
-[_UIStatusBarVisualProvider_Split willUpdateWithData:];
```
