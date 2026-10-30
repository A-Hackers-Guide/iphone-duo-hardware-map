# `_UIStatusBarVisualProvider` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 27 instance methods, 3 class methods

## Properties

```
@property (T@"_UIStatusBar",W,N) statusBar;
@property (TB,R,N) supportsIndirectPointerTouchActions;
@property (T@"UIFont",R,N) clockFont;
@property (TB,?,R,N) canFixupDisplayItemAttributes;
@property (class, TB,R,N) scalesWithScreenNativeScale;
@property (class, TB,R,N) requiresIterativeOverflowLayout;
```

## Class methods

```
+[_UIStatusBarVisualProvider requiresIterativeOverflowLayout];
+[_UIStatusBarVisualProvider intrinsicContentSizeForOrientation:];
+[_UIStatusBarVisualProvider scalesWithScreenNativeScale];
```

## Instance methods

```
-[_UIStatusBarVisualProvider statusBar];
-[_UIStatusBarVisualProvider setStatusBar:];
-[_UIStatusBarVisualProvider styleAttributesForStyle:];
-[_UIStatusBarVisualProvider clockFont];
-[_UIStatusBarVisualProvider orderedDisplayItemPlacementsInRegionWithIdentifier:];
-[_UIStatusBarVisualProvider setupInContainerView:];
-[_UIStatusBarVisualProvider supportsIndirectPointerTouchActions];
-[_UIStatusBarVisualProvider actionable:highlighted:initialPress:];
-[_UIStatusBarVisualProvider additionAnimationForDisplayItemWithIdentifier:itemAnimation:];
-[_UIStatusBarVisualProvider avoidanceFrameUpdatedFromFrame:withAnimationSettings:options:];
-[_UIStatusBarVisualProvider canFixupDisplayItemAttributes];
-[_UIStatusBarVisualProvider clockBoundsForLayoutItem:];
-[_UIStatusBarVisualProvider dataUpdated:];
-[_UIStatusBarVisualProvider displayItemIdentifiersForPartWithIdentifier:];
-[_UIStatusBarVisualProvider itemCreated:];
-[_UIStatusBarVisualProvider modeUpdatedFromMode:];
-[_UIStatusBarVisualProvider orientationUpdatedFromOrientation:];
-[_UIStatusBarVisualProvider overriddenStyleAttributesForDisplayItemWithIdentifier:];
-[_UIStatusBarVisualProvider region:willSetDisplayItems:];
-[_UIStatusBarVisualProvider regionIdentifiersForPartWithIdentifier:];
-[_UIStatusBarVisualProvider removalAnimationForDisplayItemWithIdentifier:itemAnimation:];
-[_UIStatusBarVisualProvider showSensorActivityIndicatorWithoutPortalView];
-[_UIStatusBarVisualProvider sizeUpdatedFromSize:];
-[_UIStatusBarVisualProvider statusBarEnabledPartsUpdated];
-[_UIStatusBarVisualProvider statusBarRegionsUpdated];
-[_UIStatusBarVisualProvider styleUpdatedFromStyle:];
-[_UIStatusBarVisualProvider willUpdateWithData:];
```
