# `_UIToolbarContentView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIBarContentView`
- 11 instance variables, 5 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"_UIButtonBar" _buttonBar;
@"_UIPointerInteractionAssistant" _assistant;
@"NSLayoutConstraint" _buttonBarLeadingConstraint;
@"NSLayoutConstraint" _buttonBarTrailingConstraint;
@"NSMapTable" _absorptionTable;
d _standardEdgeSpacing;
B _compactMetrics;
q _itemDistribution;
@"_UIBarButtonItemData" _plainItemAppearance;
@"_UIBarButtonItemData" _doneItemAppearance;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _padding;
```

## Properties

```
@property (T{NSDirectionalEdgeInsets=dddd},N,V_padding) padding;
@property (Tq,N,V_itemDistribution) itemDistribution;
@property (TB,N,V_compactMetrics) compactMetrics;
@property (T@"_UIBarButtonItemData",C,N,V_plainItemAppearance) plainItemAppearance;
@property (T@"_UIBarButtonItemData",C,N,V_doneItemAppearance) doneItemAppearance;
```

## Instance methods

```
-[_UIToolbarContentView padding];
-[_UIToolbarContentView updateWithItems:fromOldItems:animate:];
-[_UIToolbarContentView edgesPaddingBarButtonItem:];
-[_UIToolbarContentView doneItemAppearance];
-[_UIToolbarContentView _UIAppearance_setBackButtonBackgroundImage:forState:barMetrics:];
-[_UIToolbarContentView _setBackButtonBackgroundVerticalPositionAdjustment:forBarMetrics:];
-[_UIToolbarContentView setItemDistribution:];
-[_UIToolbarContentView setPlainItemAppearance:];
-[_UIToolbarContentView _setBackButtonTitlePositionAdjustment:forBarMetrics:];
-[_UIToolbarContentView _UIAppearance_setBackButtonBackgroundVerticalPositionAdjustment:forBarMetrics:];
-[_UIToolbarContentView itemDistribution];
-[_UIToolbarContentView _UIAppearance_setBackButtonTitlePositionAdjustment:forBarMetrics:];
-[_UIToolbarContentView _updateThreeUpFlagsForItems:];
-[_UIToolbarContentView updateContent];
-[_UIToolbarContentView absorptionForItem:];
-[_UIToolbarContentView layoutMarginsDidChange];
-[_UIToolbarContentView _appearanceChanged];
-[_UIToolbarContentView setDoneItemAppearance:];
-[_UIToolbarContentView setPadding:];
-[_UIToolbarContentView _setBackButtonBackgroundImage:forState:barMetrics:];
-[_UIToolbarContentView reloadWithItems:];
-[_UIToolbarContentView _setButtonBarLeadingInset:trailingInset:];
-[_UIToolbarContentView plainItemAppearance];
-[_UIToolbarContentView tintColorDidChange];
-[_UIToolbarContentView setCompactMetrics:];
-[_UIToolbarContentView _ensureButtonBar];
-[_UIToolbarContentView _computeEdgeAbsorptionForItems:];
-[_UIToolbarContentView updateConstraints];
-[_UIToolbarContentView defaultEdgeSpacing];
-[_UIToolbarContentView defaultTextPadding];
-[_UIToolbarContentView _directionalSafeArea];
-[_UIToolbarContentView barType];
-[_UIToolbarContentView compactMetrics];
```
