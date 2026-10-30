# `_UIStatusBarVisualProvider_DynamicSplit`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarVisualProvider_Split`
- Protocols: `_UIStatusBarRegionAxisSquishyLayoutDynamicHidingDelegate`
- 5 instance variables, 9 properties, 46 instance methods, 4 class methods

## Instance variables

```
@"NSLayoutConstraint" _cutoutWidthConstraint;
@"NSLayoutConstraint" _cutoutCenterConstraint;
@"NSLayoutConstraint" _leadingCenterYConstraint;
@? _deferredAvoidanceFrameUpdateBlock;
@"BSAnimationSettings" _currentAnimationSettings;
```

## Properties

```
@property (T@"NSLayoutConstraint",&,N,V_cutoutWidthConstraint) cutoutWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_cutoutCenterConstraint) cutoutCenterConstraint;
@property (T@"NSLayoutConstraint",&,N,V_leadingCenterYConstraint) leadingCenterYConstraint;
@property (T@?,C,N,V_deferredAvoidanceFrameUpdateBlock) deferredAvoidanceFrameUpdateBlock;
@property (T@"BSAnimationSettings",&,N,V_currentAnimationSettings) currentAnimationSettings;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIStatusBarVisualProvider_DynamicSplit expandedFontSize];
+[_UIStatusBarVisualProvider_DynamicSplit baseFontSize];
+[_UIStatusBarVisualProvider_DynamicSplit height];
+[_UIStatusBarVisualProvider_DynamicSplit visualProviderSubclassForScreen:visualProviderInfo:];
```

## Instance methods

```
-[_UIStatusBarVisualProvider_DynamicSplit trailingItemCutoffWidths];
-[_UIStatusBarVisualProvider_DynamicSplit bottomLeadingTopOffset];
-[_UIStatusBarVisualProvider_DynamicSplit itemSpacing];
-[_UIStatusBarVisualProvider_DynamicSplit normalIconScale];
-[_UIStatusBarVisualProvider_DynamicSplit expandedIconScale];
-[_UIStatusBarVisualProvider_DynamicSplit edgeInsets];
-[_UIStatusBarVisualProvider_DynamicSplit leadingItemCutoffWidths];
-[_UIStatusBarVisualProvider_DynamicSplit cutoutEdgeInset];
-[_UIStatusBarVisualProvider_DynamicSplit normalRoundFont];
-[_UIStatusBarVisualProvider_DynamicSplit _needsUpdateOfConstraintsForAvoidanceFrame:cutoutOffset:cutoutWidth:];
-[_UIStatusBarVisualProvider_DynamicSplit _orderedDisplayItemPlacements];
-[_UIStatusBarVisualProvider_DynamicSplit _updateSystemNavigationWithData:avoidanceFrame:];
-[_UIStatusBarVisualProvider_DynamicSplit additionAnimationForDisplayItemWithIdentifier:itemAnimation:];
-[_UIStatusBarVisualProvider_DynamicSplit avoidanceFrameUpdatedFromFrame:withAnimationSettings:options:];
-[_UIStatusBarVisualProvider_DynamicSplit currentAnimationSettings];
-[_UIStatusBarVisualProvider_DynamicSplit cutoutCenterConstraint];
-[_UIStatusBarVisualProvider_DynamicSplit cutoutWidthConstraint];
-[_UIStatusBarVisualProvider_DynamicSplit dataUpdated:];
-[_UIStatusBarVisualProvider_DynamicSplit deferredAvoidanceFrameUpdateBlock];
-[_UIStatusBarVisualProvider_DynamicSplit effectiveTargetDisplayWidth];
-[_UIStatusBarVisualProvider_DynamicSplit expandedEdgeInsets];
-[_UIStatusBarVisualProvider_DynamicSplit leadingCenterYConstraint];
-[_UIStatusBarVisualProvider_DynamicSplit leadingItemSpacing];
-[_UIStatusBarVisualProvider_DynamicSplit leadingNumberOfItemsForWidth:];
-[_UIStatusBarVisualProvider_DynamicSplit leadingScaleForWidth:];
-[_UIStatusBarVisualProvider_DynamicSplit minimumBottomLeadingWidth];
-[_UIStatusBarVisualProvider_DynamicSplit minimumItemScaleFactor];
-[_UIStatusBarVisualProvider_DynamicSplit orientationUpdatedFromOrientation:];
-[_UIStatusBarVisualProvider_DynamicSplit overriddenStyleAttributesForDisplayItemWithIdentifier:];
-[_UIStatusBarVisualProvider_DynamicSplit region:willSetDisplayItems:];
-[_UIStatusBarVisualProvider_DynamicSplit removalAnimationForDisplayItemWithIdentifier:itemAnimation:];
-[_UIStatusBarVisualProvider_DynamicSplit sensorAreaCenterOffsetFromTrailing];
-[_UIStatusBarVisualProvider_DynamicSplit sensorAreaRect];
-[_UIStatusBarVisualProvider_DynamicSplit sensorAreaSize];
-[_UIStatusBarVisualProvider_DynamicSplit setCurrentAnimationSettings:];
-[_UIStatusBarVisualProvider_DynamicSplit setCutoutCenterConstraint:];
-[_UIStatusBarVisualProvider_DynamicSplit setCutoutWidthConstraint:];
-[_UIStatusBarVisualProvider_DynamicSplit setDeferredAvoidanceFrameUpdateBlock:];
-[_UIStatusBarVisualProvider_DynamicSplit setLeadingCenterYConstraint:];
-[_UIStatusBarVisualProvider_DynamicSplit setupInContainerView:];
-[_UIStatusBarVisualProvider_DynamicSplit smallPillSize];
-[_UIStatusBarVisualProvider_DynamicSplit topLeadingCenterOffset];
-[_UIStatusBarVisualProvider_DynamicSplit trailingNumberOfItemsForWidth:includingPrivacyIndicator:];
-[_UIStatusBarVisualProvider_DynamicSplit trailingScaleForWidth:includingPrivacyIndicator:];
-[_UIStatusBarVisualProvider_DynamicSplit updateDisplayItem:toDynamicallyHidden:scale:];
-[_UIStatusBarVisualProvider_DynamicSplit updateDisplayItem:toScale:];
```
