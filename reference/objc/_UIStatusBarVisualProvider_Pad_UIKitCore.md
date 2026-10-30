# `_UIStatusBarVisualProvider_Pad`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarVisualProvider_iOS`
- Protocols: `_UIStatusBarRegionCursorInsetProvider`
- 5 instance variables, 14 properties, 43 instance methods, 7 class methods

## Instance variables

```
@"NSDictionary" _orderedDisplayItemPlacements;
@"NSLayoutConstraint" _trailingRegionLeadingAnchorConstraint;
@"NSLayoutConstraint" _leadingRegionTrailingAnchorConstraint;
@"_UIStatusBarDisplayItemPlacement" _datePlacement;
@"_UIStatusBarDisplayItemPlacement" _timePlacement;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_orderedDisplayItemPlacements) orderedDisplayItemPlacements;
@property (T{NSDirectionalEdgeInsets=dddd},R,N) expandedEdgeInsets;
@property (T@"NSLayoutConstraint",&,N,V_trailingRegionLeadingAnchorConstraint) trailingRegionLeadingAnchorConstraint;
@property (T@"NSLayoutConstraint",&,N,V_leadingRegionTrailingAnchorConstraint) leadingRegionTrailingAnchorConstraint;
@property (T@"_UIStatusBarDisplayItemPlacement",&,N,V_datePlacement) datePlacement;
@property (T@"_UIStatusBarDisplayItemPlacement",&,N,V_timePlacement) timePlacement;
@property (T@"_UIStatusBar",W,N) statusBar;
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
+[_UIStatusBarVisualProvider_Pad baselineOffset];
+[_UIStatusBarVisualProvider_Pad edgeInsets];
+[_UIStatusBarVisualProvider_Pad height];
+[_UIStatusBarVisualProvider_Pad regionCursorCornerRadius];
+[_UIStatusBarVisualProvider_Pad regionCursorInsets];
+[_UIStatusBarVisualProvider_Pad regionCursorIsPill];
+[_UIStatusBarVisualProvider_Pad visualProviderSubclassForScreen:visualProviderInfo:];
```

## Instance methods

```
-[_UIStatusBarVisualProvider_Pad observeValueForKeyPath:ofObject:change:context:];
-[_UIStatusBarVisualProvider_Pad init];
-[_UIStatusBarVisualProvider_Pad dealloc];
-[_UIStatusBarVisualProvider_Pad styleAttributesForStyle:];
-[_UIStatusBarVisualProvider_Pad clockFont];
-[_UIStatusBarVisualProvider_Pad pillSize];
-[_UIStatusBarVisualProvider_Pad airplaneTravelOffsetInProposedPartWithIdentifier:animationType:];
-[_UIStatusBarVisualProvider_Pad _dateTimePreferencesUpdated];
-[_UIStatusBarVisualProvider_Pad _updateConstraintsForAvoidanceFrame:];
-[_UIStatusBarVisualProvider_Pad _updateDateAndTimePlacements];
-[_UIStatusBarVisualProvider_Pad actionable:highlighted:initialPress:];
-[_UIStatusBarVisualProvider_Pad airplaneShouldFadeForAnimationType:];
-[_UIStatusBarVisualProvider_Pad airplaneSpeedForAnimationType:];
-[_UIStatusBarVisualProvider_Pad avoidanceFrameUpdatedFromFrame:withAnimationSettings:options:];
-[_UIStatusBarVisualProvider_Pad clockBoundsForLayoutItem:];
-[_UIStatusBarVisualProvider_Pad datePlacement];
-[_UIStatusBarVisualProvider_Pad displayItemIdentifiersForPartWithIdentifier:];
-[_UIStatusBarVisualProvider_Pad expandedEdgeInsets];
-[_UIStatusBarVisualProvider_Pad expandedFont];
-[_UIStatusBarVisualProvider_Pad expandedPillFont];
-[_UIStatusBarVisualProvider_Pad expandedPillSize];
-[_UIStatusBarVisualProvider_Pad itemCreated:];
-[_UIStatusBarVisualProvider_Pad leadingRegionTrailingAnchorConstraint];
-[_UIStatusBarVisualProvider_Pad normalFont];
-[_UIStatusBarVisualProvider_Pad orderedDisplayItemPlacements];
-[_UIStatusBarVisualProvider_Pad orderedDisplayItemPlacementsInRegionWithIdentifier:];
-[_UIStatusBarVisualProvider_Pad overriddenStyleAttributesForDisplayItemWithIdentifier:];
-[_UIStatusBarVisualProvider_Pad pillFont];
-[_UIStatusBarVisualProvider_Pad pillSmallFont];
-[_UIStatusBarVisualProvider_Pad regionIdentifiersForPartWithIdentifier:];
-[_UIStatusBarVisualProvider_Pad regionSpacing];
-[_UIStatusBarVisualProvider_Pad setDatePlacement:];
-[_UIStatusBarVisualProvider_Pad setLeadingRegionTrailingAnchorConstraint:];
-[_UIStatusBarVisualProvider_Pad setOrderedDisplayItemPlacements:];
-[_UIStatusBarVisualProvider_Pad setTimePlacement:];
-[_UIStatusBarVisualProvider_Pad setTrailingRegionLeadingAnchorConstraint:];
-[_UIStatusBarVisualProvider_Pad setupInContainerView:];
-[_UIStatusBarVisualProvider_Pad sizeUpdatedFromSize:];
-[_UIStatusBarVisualProvider_Pad smallPillSize];
-[_UIStatusBarVisualProvider_Pad statusBarEnabledPartsUpdated];
-[_UIStatusBarVisualProvider_Pad timePlacement];
-[_UIStatusBarVisualProvider_Pad trailingRegionLeadingAnchorConstraint];
-[_UIStatusBarVisualProvider_Pad wantsPillInExpandedTrailingPlacements];
```
