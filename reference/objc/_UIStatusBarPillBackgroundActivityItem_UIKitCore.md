# `_UIStatusBarPillBackgroundActivityItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarBackgroundActivityItem`
- 3 instance variables, 3 properties, 16 instance methods, 4 class methods

## Instance variables

```
@"_UIStatusBarPillView" _combinedView;
@"_UIStatusBarDisplayableContainerView" _iconsView;
{CGSize="width"d"height"d} _pillSize;
```

## Properties

```
@property (T@"_UIStatusBarPillView",&,N,V_combinedView) combinedView;
@property (T@"_UIStatusBarDisplayableContainerView",&,N,V_iconsView) iconsView;
@property (T{CGSize=dd},N,V_pillSize) pillSize;
```

## Class methods

```
+[_UIStatusBarPillBackgroundActivityItem _identifierContainsItemImage:];
+[_UIStatusBarPillBackgroundActivityItem _identifierContainsSecondaryItemImage:];
+[_UIStatusBarPillBackgroundActivityItem pillCombinedDisplayIdentifier];
+[_UIStatusBarPillBackgroundActivityItem shouldKeepIconVisibleForActivityType:];
```

## Instance methods

```
-[_UIStatusBarPillBackgroundActivityItem viewForIdentifier:];
-[_UIStatusBarPillBackgroundActivityItem shouldUpdateIndicatorForIdentifier:];
-[_UIStatusBarPillBackgroundActivityItem createDisplayItemForIdentifier:];
-[_UIStatusBarPillBackgroundActivityItem applyUpdate:toDisplayItem:];
-[_UIStatusBarPillBackgroundActivityItem setPillSize:];
-[_UIStatusBarPillBackgroundActivityItem pillSize];
-[_UIStatusBarPillBackgroundActivityItem _backgroundActivityViewForIdentifier:];
-[_UIStatusBarPillBackgroundActivityItem _backgroundColorForActivityType:];
-[_UIStatusBarPillBackgroundActivityItem _create_combinedView];
-[_UIStatusBarPillBackgroundActivityItem _create_iconsView];
-[_UIStatusBarPillBackgroundActivityItem _shouldBounceWhenTransitioningFromType:toType:];
-[_UIStatusBarPillBackgroundActivityItem _textLabelForActivityType:];
-[_UIStatusBarPillBackgroundActivityItem combinedView];
-[_UIStatusBarPillBackgroundActivityItem iconsView];
-[_UIStatusBarPillBackgroundActivityItem setCombinedView:];
-[_UIStatusBarPillBackgroundActivityItem setIconsView:];
```
