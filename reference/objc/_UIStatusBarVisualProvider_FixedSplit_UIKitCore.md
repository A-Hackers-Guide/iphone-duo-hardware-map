# `_UIStatusBarVisualProvider_FixedSplit`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarVisualProvider_Split`
- 1 instance variables, 15 properties, 39 instance methods, 8 class methods

## Instance variables

```
@"NSLayoutConstraint" _leadingBottomConstraint;
```

## Properties

```
@property (Td,R) nativeDisplayWidth;
@property (Td,R) leadingPillSpacing;
@property (Td,R) leadingPillInset;
@property (Td,R) leadingSmallPillSpacing;
@property (Td,R) leadingCenteringEdgeInset;
@property (Td,R) trailingCenteringEdgeInset;
@property (Td,R) pillCenteringEdgeInset;
@property (T{CGSize=dd},R) pillSize;
@property (T@"UIFont",R) pillFont;
@property (T@"UIFont",R) pillSmallFont;
@property (Td,R) bottomLeadingWidth;
@property (Td,R) bottomLeadingBaseline;
@property (T{NSDirectionalEdgeInsets=dddd},R) leadingEdgeInsets;
@property (T{NSDirectionalEdgeInsets=dddd},R) trailingEdgeInsets;
@property (T@"NSLayoutConstraint",&,N,V_leadingBottomConstraint) leadingBottomConstraint;
```

## Class methods

```
+[_UIStatusBarVisualProvider_FixedSplit additionalBottomLeadingMargin];
+[_UIStatusBarVisualProvider_FixedSplit expandedPillFontSize];
+[_UIStatusBarVisualProvider_FixedSplit leadingCenteringOffset];
+[_UIStatusBarVisualProvider_FixedSplit pillCenteringOffset];
+[_UIStatusBarVisualProvider_FixedSplit pillFontSize];
+[_UIStatusBarVisualProvider_FixedSplit showsLargeBatteryChargingAnimation];
+[_UIStatusBarVisualProvider_FixedSplit trailingCenteringOffset];
+[_UIStatusBarVisualProvider_FixedSplit trailingEdgeInsetLeadingAdjustment];
```

## Instance methods

```
-[_UIStatusBarVisualProvider_FixedSplit styleAttributesForStyle:];
-[_UIStatusBarVisualProvider_FixedSplit pillSize];
-[_UIStatusBarVisualProvider_FixedSplit _edgeInsetsFromCenteringEdgeInset:trailing:];
-[_UIStatusBarVisualProvider_FixedSplit _orderedDisplayItemPlacements];
-[_UIStatusBarVisualProvider_FixedSplit _updateLowerRegionsWithData:];
-[_UIStatusBarVisualProvider_FixedSplit _updateSystemNavigationWithData:];
-[_UIStatusBarVisualProvider_FixedSplit animationForBackgroundActivityPillAnimation:duration:scale:];
-[_UIStatusBarVisualProvider_FixedSplit bottomLeadingBaseline];
-[_UIStatusBarVisualProvider_FixedSplit bottomLeadingWidth];
-[_UIStatusBarVisualProvider_FixedSplit dataUpdated:];
-[_UIStatusBarVisualProvider_FixedSplit expandedEdgeInsets];
-[_UIStatusBarVisualProvider_FixedSplit expandedPillFont];
-[_UIStatusBarVisualProvider_FixedSplit expandedPillSize];
-[_UIStatusBarVisualProvider_FixedSplit itemCreated:];
-[_UIStatusBarVisualProvider_FixedSplit leadingBottomConstraint];
-[_UIStatusBarVisualProvider_FixedSplit leadingCenteringEdgeInset];
-[_UIStatusBarVisualProvider_FixedSplit leadingEdgeInsets];
-[_UIStatusBarVisualProvider_FixedSplit leadingItemSpacing];
-[_UIStatusBarVisualProvider_FixedSplit leadingPillInset];
-[_UIStatusBarVisualProvider_FixedSplit leadingPillSpacing];
-[_UIStatusBarVisualProvider_FixedSplit leadingSmallPillSpacing];
-[_UIStatusBarVisualProvider_FixedSplit nativeDisplayWidth];
-[_UIStatusBarVisualProvider_FixedSplit notchRect];
-[_UIStatusBarVisualProvider_FixedSplit notchSize];
-[_UIStatusBarVisualProvider_FixedSplit orderedDisplayItemPlacementsInRegionWithIdentifier:];
-[_UIStatusBarVisualProvider_FixedSplit orientationUpdatedFromOrientation:];
-[_UIStatusBarVisualProvider_FixedSplit overriddenStyleAttributesForDisplayItemWithIdentifier:];
-[_UIStatusBarVisualProvider_FixedSplit pillCenteringEdgeInset];
-[_UIStatusBarVisualProvider_FixedSplit pillFont];
-[_UIStatusBarVisualProvider_FixedSplit pillSmallFont];
-[_UIStatusBarVisualProvider_FixedSplit referenceWidth];
-[_UIStatusBarVisualProvider_FixedSplit region:willSetDisplayItems:];
-[_UIStatusBarVisualProvider_FixedSplit regionIdentifiersForPartWithIdentifier:];
-[_UIStatusBarVisualProvider_FixedSplit setLeadingBottomConstraint:];
-[_UIStatusBarVisualProvider_FixedSplit setupInContainerView:];
-[_UIStatusBarVisualProvider_FixedSplit smallPillSize];
-[_UIStatusBarVisualProvider_FixedSplit trailingCenteringEdgeInset];
-[_UIStatusBarVisualProvider_FixedSplit trailingEdgeInsets];
-[_UIStatusBarVisualProvider_FixedSplit wantsPillInExpandedTrailingPlacements];
```
