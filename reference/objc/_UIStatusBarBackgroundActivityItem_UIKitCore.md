# `_UIStatusBarBackgroundActivityItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarIndicatorItem`
- 4 instance variables, 4 properties, 36 instance methods, 6 class methods

## Instance variables

```
@"_UIStatusBarPillView" _backgroundView;
@"_UIStatusBarActivityIconView" _iconView;
@"_UIStatusBarImageView" _secondaryIconView;
q _previousType;
```

## Properties

```
@property (T@"_UIStatusBarPillView",&,N,V_backgroundView) backgroundView;
@property (T@"_UIStatusBarActivityIconView",&,N,V_iconView) iconView;
@property (T@"_UIStatusBarImageView",&,N,V_secondaryIconView) secondaryIconView;
@property (Tq,N,V_previousType) previousType;
```

## Class methods

```
+[_UIStatusBarBackgroundActivityItem _verticalOffsetForActivityType:];
+[_UIStatusBarBackgroundActivityItem _fontSizeAdjustmentForActivityType:];
+[_UIStatusBarBackgroundActivityItem _identifierContainsItemImage:];
+[_UIStatusBarBackgroundActivityItem _identifierContainsSecondaryItemImage:];
+[_UIStatusBarBackgroundActivityItem backgroundDisplayIdentifier];
+[_UIStatusBarBackgroundActivityItem secondaryIconDisplayIdentifier];
```

## Instance methods

```
-[_UIStatusBarBackgroundActivityItem previousType];
-[_UIStatusBarBackgroundActivityItem applyStyleAttributes:toDisplayItem:];
-[_UIStatusBarBackgroundActivityItem initWithIdentifier:statusBar:];
-[_UIStatusBarBackgroundActivityItem viewForIdentifier:];
-[_UIStatusBarBackgroundActivityItem iconView];
-[_UIStatusBarBackgroundActivityItem additionAnimationForDisplayItemWithIdentifier:];
-[_UIStatusBarBackgroundActivityItem setIconView:];
-[_UIStatusBarBackgroundActivityItem imageForUpdate:];
-[_UIStatusBarBackgroundActivityItem createDisplayItemForIdentifier:];
-[_UIStatusBarBackgroundActivityItem canEnableDisplayItem:fromData:];
-[_UIStatusBarBackgroundActivityItem setPreviousType:];
-[_UIStatusBarBackgroundActivityItem indicatorEntryKey];
-[_UIStatusBarBackgroundActivityItem backgroundView];
-[_UIStatusBarBackgroundActivityItem removalAnimationForDisplayItemWithIdentifier:];
-[_UIStatusBarBackgroundActivityItem applyUpdate:toDisplayItem:];
-[_UIStatusBarBackgroundActivityItem imageView];
-[_UIStatusBarBackgroundActivityItem imageNameForUpdate:];
-[_UIStatusBarBackgroundActivityItem setBackgroundView:];
-[_UIStatusBarBackgroundActivityItem systemImageNameForUpdate:];
-[_UIStatusBarBackgroundActivityItem _backgroundActivityViewForIdentifier:];
-[_UIStatusBarBackgroundActivityItem _backgroundColorForActivityType:];
-[_UIStatusBarBackgroundActivityItem _create_backgroundView];
-[_UIStatusBarBackgroundActivityItem _create_iconView];
-[_UIStatusBarBackgroundActivityItem _create_secondaryIconView];
-[_UIStatusBarBackgroundActivityItem _imageNameForActivityType:];
-[_UIStatusBarBackgroundActivityItem _secondarySystemImageNameForActivityType:];
-[_UIStatusBarBackgroundActivityItem _shouldPulseForActivityType:traitCollection:];
-[_UIStatusBarBackgroundActivityItem _shouldRingForActivityType:traitCollection:];
-[_UIStatusBarBackgroundActivityItem _systemImageNameForActivityType:];
-[_UIStatusBarBackgroundActivityItem _textLabelForActivityType:];
-[_UIStatusBarBackgroundActivityItem _visualEffectForActivityType:traitCollection:];
-[_UIStatusBarBackgroundActivityItem crossfadeForUpdate:];
-[_UIStatusBarBackgroundActivityItem secondaryIconView];
-[_UIStatusBarBackgroundActivityItem secondaryImageForUpdate:];
-[_UIStatusBarBackgroundActivityItem setSecondaryIconView:];
-[_UIStatusBarBackgroundActivityItem updatedDisplayItemsWithData:];
```
