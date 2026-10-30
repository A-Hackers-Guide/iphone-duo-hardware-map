# `_UIStatusBarVisualProvider_LegacyPhone`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarVisualProvider_Phone`
- Protocols: `_UIStatusBarCellularItemTypeStringProvider`
- 15 instance variables, 19 properties, 72 instance methods, 3 class methods

## Instance variables

```
@"NSDictionary" _orderedDisplayItemPlacements;
@"_UIStatusBarDisplayItemPlacementGroup" _lowerWifiGroup;
@"NSLayoutConstraint" _backgroundHeightConstraint;
@"_UIStatusBarCellularItem" _condensedCellularItem;
@"NSLayoutConstraint" _leadingTopConstraint;
@"NSLayoutConstraint" _leadingHeightConstraint;
@"_UIStatusBarRegionAxisStackingLayout" _leadingHorizontalLayout;
@"NSLayoutConstraint" _centerTopConstraint;
@"NSLayoutConstraint" _centerHeightConstraint;
@"_UIStatusBarRegionAxisCenteringLayout" _centerHorizontalLayout;
@"NSLayoutConstraint" _trailingTopConstraint;
@"NSLayoutConstraint" _trailingHeightConstraint;
@"_UIStatusBarRegionAxisStackingLayout" _trailingHorizontalLayout;
@"NSLayoutConstraint" _expandedLeadingBottomConstraint;
@"NSLayoutConstraint" _expandedTrailingBottomConstraint;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_orderedDisplayItemPlacements) orderedDisplayItemPlacements;
@property (T@"_UIStatusBarDisplayItemPlacementGroup",&,N,V_lowerWifiGroup) lowerWifiGroup;
@property (T@"NSLayoutConstraint",&,N,V_backgroundHeightConstraint) backgroundHeightConstraint;
@property (T@"_UIStatusBarCellularItem",&,N,V_condensedCellularItem) condensedCellularItem;
@property (T@"NSLayoutConstraint",&,N,V_leadingTopConstraint) leadingTopConstraint;
@property (T@"NSLayoutConstraint",&,N,V_leadingHeightConstraint) leadingHeightConstraint;
@property (T@"_UIStatusBarRegionAxisStackingLayout",&,N,V_leadingHorizontalLayout) leadingHorizontalLayout;
@property (T@"NSLayoutConstraint",&,N,V_centerTopConstraint) centerTopConstraint;
@property (T@"NSLayoutConstraint",&,N,V_centerHeightConstraint) centerHeightConstraint;
@property (T@"_UIStatusBarRegionAxisCenteringLayout",&,N,V_centerHorizontalLayout) centerHorizontalLayout;
@property (T@"NSLayoutConstraint",&,N,V_trailingTopConstraint) trailingTopConstraint;
@property (T@"NSLayoutConstraint",&,N,V_trailingHeightConstraint) trailingHeightConstraint;
@property (T@"_UIStatusBarRegionAxisStackingLayout",&,N,V_trailingHorizontalLayout) trailingHorizontalLayout;
@property (T@"NSLayoutConstraint",&,N,V_expandedLeadingBottomConstraint) expandedLeadingBottomConstraint;
@property (T@"NSLayoutConstraint",&,N,V_expandedTrailingBottomConstraint) expandedTrailingBottomConstraint;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIStatusBarVisualProvider_LegacyPhone height];
+[_UIStatusBarVisualProvider_LegacyPhone _heightExpanded:];
+[_UIStatusBarVisualProvider_LegacyPhone intrinsicLockScreenContentSizeForOrientation:];
```

## Instance methods

```
-[_UIStatusBarVisualProvider_LegacyPhone baselineOffset];
-[_UIStatusBarVisualProvider_LegacyPhone setExpanded:];
-[_UIStatusBarVisualProvider_LegacyPhone timeFont];
-[_UIStatusBarVisualProvider_LegacyPhone styleAttributesForStyle:];
-[_UIStatusBarVisualProvider_LegacyPhone lowerExpandedBaselineOffset];
-[_UIStatusBarVisualProvider_LegacyPhone edgeInsets];
-[_UIStatusBarVisualProvider_LegacyPhone clockFont];
-[_UIStatusBarVisualProvider_LegacyPhone setOnLockScreen:];
-[_UIStatusBarVisualProvider_LegacyPhone pillSize];
-[_UIStatusBarVisualProvider_LegacyPhone effectiveHeight];
-[_UIStatusBarVisualProvider_LegacyPhone expandedLeadingBottomConstraint];
-[_UIStatusBarVisualProvider_LegacyPhone _animationForSingleLineDualCarrier];
-[_UIStatusBarVisualProvider_LegacyPhone _backgroundActivityDetailRemovalAnimation];
-[_UIStatusBarVisualProvider_LegacyPhone _updateBackgroundHeight];
-[_UIStatusBarVisualProvider_LegacyPhone _updateExpandedTrailingRegion];
-[_UIStatusBarVisualProvider_LegacyPhone _updateLockScreenSizing];
-[_UIStatusBarVisualProvider_LegacyPhone _updateLowerRegionsWithData:];
-[_UIStatusBarVisualProvider_LegacyPhone actionable:highlighted:initialPress:];
-[_UIStatusBarVisualProvider_LegacyPhone additionAnimationForDisplayItemWithIdentifier:itemAnimation:];
-[_UIStatusBarVisualProvider_LegacyPhone animatedTypeDisplayItemSpacingFactorForCellularType:];
-[_UIStatusBarVisualProvider_LegacyPhone backgroundHeightConstraint];
-[_UIStatusBarVisualProvider_LegacyPhone centerHeightConstraint];
-[_UIStatusBarVisualProvider_LegacyPhone centerHorizontalLayout];
-[_UIStatusBarVisualProvider_LegacyPhone centerTopConstraint];
-[_UIStatusBarVisualProvider_LegacyPhone clockBoundsForLayoutItem:];
-[_UIStatusBarVisualProvider_LegacyPhone condensedCellularItem];
-[_UIStatusBarVisualProvider_LegacyPhone condensedFontForCellularType:defaultFont:baselineOffset:];
-[_UIStatusBarVisualProvider_LegacyPhone dataUpdated:];
-[_UIStatusBarVisualProvider_LegacyPhone displayItemIdentifiersForPartWithIdentifier:];
-[_UIStatusBarVisualProvider_LegacyPhone dualLineExpandedBaselineOffset];
-[_UIStatusBarVisualProvider_LegacyPhone expandedBaselineOffset];
-[_UIStatusBarVisualProvider_LegacyPhone expandedFont];
-[_UIStatusBarVisualProvider_LegacyPhone expandedTrailingBottomConstraint];
-[_UIStatusBarVisualProvider_LegacyPhone itemCreated:];
-[_UIStatusBarVisualProvider_LegacyPhone leadingHeightConstraint];
-[_UIStatusBarVisualProvider_LegacyPhone leadingHorizontalLayout];
-[_UIStatusBarVisualProvider_LegacyPhone leadingTopConstraint];
-[_UIStatusBarVisualProvider_LegacyPhone lowerWifiGroup];
-[_UIStatusBarVisualProvider_LegacyPhone normalFont];
-[_UIStatusBarVisualProvider_LegacyPhone orderedDisplayItemPlacements];
-[_UIStatusBarVisualProvider_LegacyPhone orderedDisplayItemPlacementsInRegionWithIdentifier:];
-[_UIStatusBarVisualProvider_LegacyPhone orientationUpdatedFromOrientation:];
-[_UIStatusBarVisualProvider_LegacyPhone overriddenStyleAttributesForDisplayItemWithIdentifier:];
-[_UIStatusBarVisualProvider_LegacyPhone pillFont];
-[_UIStatusBarVisualProvider_LegacyPhone regionIdentifiersForPartWithIdentifier:];
-[_UIStatusBarVisualProvider_LegacyPhone regionSpacing];
-[_UIStatusBarVisualProvider_LegacyPhone removalAnimationForDisplayItemWithIdentifier:itemAnimation:];
-[_UIStatusBarVisualProvider_LegacyPhone setBackgroundHeightConstraint:];
-[_UIStatusBarVisualProvider_LegacyPhone setCenterHeightConstraint:];
-[_UIStatusBarVisualProvider_LegacyPhone setCenterHorizontalLayout:];
-[_UIStatusBarVisualProvider_LegacyPhone setCenterTopConstraint:];
-[_UIStatusBarVisualProvider_LegacyPhone setCondensedCellularItem:];
-[_UIStatusBarVisualProvider_LegacyPhone setExpandedLeadingBottomConstraint:];
-[_UIStatusBarVisualProvider_LegacyPhone setExpandedTrailingBottomConstraint:];
-[_UIStatusBarVisualProvider_LegacyPhone setLeadingHeightConstraint:];
-[_UIStatusBarVisualProvider_LegacyPhone setLeadingHorizontalLayout:];
-[_UIStatusBarVisualProvider_LegacyPhone setLeadingTopConstraint:];
-[_UIStatusBarVisualProvider_LegacyPhone setLowerWifiGroup:];
-[_UIStatusBarVisualProvider_LegacyPhone setOrderedDisplayItemPlacements:];
-[_UIStatusBarVisualProvider_LegacyPhone setTrailingHeightConstraint:];
-[_UIStatusBarVisualProvider_LegacyPhone setTrailingHorizontalLayout:];
-[_UIStatusBarVisualProvider_LegacyPhone setTrailingTopConstraint:];
-[_UIStatusBarVisualProvider_LegacyPhone setupInContainerView:];
-[_UIStatusBarVisualProvider_LegacyPhone smallPillSize];
-[_UIStatusBarVisualProvider_LegacyPhone statusBarRegionsUpdated];
-[_UIStatusBarVisualProvider_LegacyPhone stringForCellularType:condensed:];
-[_UIStatusBarVisualProvider_LegacyPhone trailingHeightConstraint];
-[_UIStatusBarVisualProvider_LegacyPhone trailingHorizontalLayout];
-[_UIStatusBarVisualProvider_LegacyPhone trailingTopConstraint];
-[_UIStatusBarVisualProvider_LegacyPhone updateDataForService:];
-[_UIStatusBarVisualProvider_LegacyPhone wantsExpandedLeadingPlacements];
-[_UIStatusBarVisualProvider_LegacyPhone willUpdateWithData:];
```
