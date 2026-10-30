# `_UIStatusBarDualIndicatorItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIStatusBarItem`
- 7 instance variables, 7 properties, 27 instance methods, 0 class methods

## Instance variables

```
d _itemSpacing;
d _additionRemovalScale;
d _additionRemovalDuration;
@"_UIStatusBarDisplayableContainerView" _iconsView;
@"_UIStatusBarImageView" _iconView;
@"_UIStatusBarImageView" _secondaryIconView;
@"NSLayoutConstraint" _itemSpacingConstraint;
```

## Properties

```
@property (T@"_UIStatusBarDisplayableContainerView",&,N,V_iconsView) iconsView;
@property (T@"_UIStatusBarImageView",&,N,V_iconView) iconView;
@property (T@"_UIStatusBarImageView",&,N,V_secondaryIconView) secondaryIconView;
@property (T@"NSLayoutConstraint",&,N,V_itemSpacingConstraint) itemSpacingConstraint;
@property (Td,N,V_itemSpacing) itemSpacing;
@property (Td,N,V_additionRemovalScale) additionRemovalScale;
@property (Td,N,V_additionRemovalDuration) additionRemovalDuration;
```

## Instance methods

```
-[_UIStatusBarDualIndicatorItem viewForIdentifier:];
-[_UIStatusBarDualIndicatorItem iconView];
-[_UIStatusBarDualIndicatorItem setIconView:];
-[_UIStatusBarDualIndicatorItem createDisplayItemForIdentifier:];
-[_UIStatusBarDualIndicatorItem indicatorEntryKey];
-[_UIStatusBarDualIndicatorItem itemSpacing];
-[_UIStatusBarDualIndicatorItem setItemSpacing:];
-[_UIStatusBarDualIndicatorItem dependentEntryKeys];
-[_UIStatusBarDualIndicatorItem applyUpdate:toDisplayItem:];
-[_UIStatusBarDualIndicatorItem systemImageNameForUpdate:];
-[_UIStatusBarDualIndicatorItem _create_iconView];
-[_UIStatusBarDualIndicatorItem _create_iconsView];
-[_UIStatusBarDualIndicatorItem _create_secondaryIconView];
-[_UIStatusBarDualIndicatorItem additionRemovalAnimationForSubItem:image:update:displayItem:];
-[_UIStatusBarDualIndicatorItem additionRemovalDuration];
-[_UIStatusBarDualIndicatorItem additionRemovalScale];
-[_UIStatusBarDualIndicatorItem iconsView];
-[_UIStatusBarDualIndicatorItem imageForUpdate:secondary:];
-[_UIStatusBarDualIndicatorItem itemSpacingConstraint];
-[_UIStatusBarDualIndicatorItem secondaryIconView];
-[_UIStatusBarDualIndicatorItem secondaryIndicatorEntryKey];
-[_UIStatusBarDualIndicatorItem secondarySystemImageNameForUpdate:];
-[_UIStatusBarDualIndicatorItem setAdditionRemovalDuration:];
-[_UIStatusBarDualIndicatorItem setAdditionRemovalScale:];
-[_UIStatusBarDualIndicatorItem setIconsView:];
-[_UIStatusBarDualIndicatorItem setItemSpacingConstraint:];
-[_UIStatusBarDualIndicatorItem setSecondaryIconView:];
```
