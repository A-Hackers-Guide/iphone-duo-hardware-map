# `_UIToolbarVisualProviderModernIOS`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIToolbarVisualProvider`
- Protocols: `_UIBarButtonItemViewOwner`, `_UIBarAppearanceChangeObserver`
- 7 instance variables, 4 properties, 35 instance methods, 0 class methods

## Instance variables

```
@"_UIBarBackground" _backgroundView;
@"_UIBarBackgroundLayout" _backgroundViewLayout;
@"UIView" _customBackgroundView;
@"_UIToolbarContentView" _contentView;
q _itemDistribution;
B _useModernAppearance;
d _backgroundTransitionProgress;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIToolbarVisualProviderModernIOS setUseModernAppearance:];
-[_UIToolbarVisualProviderModernIOS _itemDidChangeWidth:];
-[_UIToolbarVisualProviderModernIOS _itemDidChangeSelectionState:];
-[_UIToolbarVisualProviderModernIOS _itemStandardViewNeedsUpdate:];
-[_UIToolbarVisualProviderModernIOS updateWithItems:fromOldItems:animate:];
-[_UIToolbarVisualProviderModernIOS _itemDidChangeEnabledState:];
-[_UIToolbarVisualProviderModernIOS appearance:categoriesChanged:];
-[_UIToolbarVisualProviderModernIOS useModernAppearance];
-[_UIToolbarVisualProviderModernIOS setBackgroundTransitionProgress:];
-[_UIToolbarVisualProviderModernIOS _itemCustomViewDidChange:fromView:];
-[_UIToolbarVisualProviderModernIOS setCustomBackgroundView:];
-[_UIToolbarVisualProviderModernIOS _itemDidChangeHiddenState:];
-[_UIToolbarVisualProviderModernIOS backgroundTransitionProgress];
-[_UIToolbarVisualProviderModernIOS setItemDistribution:];
-[_UIToolbarVisualProviderModernIOS _currentCustomBackground];
-[_UIToolbarVisualProviderModernIOS itemDistribution];
-[_UIToolbarVisualProviderModernIOS updateBackgroundGroupName];
-[_UIToolbarVisualProviderModernIOS toolbarIsSmall];
-[_UIToolbarVisualProviderModernIOS layoutSubviews];
-[_UIToolbarVisualProviderModernIOS updateBarForStyle:];
-[_UIToolbarVisualProviderModernIOS traitCollectionForChild:baseTraitCollection:];
-[_UIToolbarVisualProviderModernIOS backgroundFrame];
-[_UIToolbarVisualProviderModernIOS defaultSizeForOrientation:];
-[_UIToolbarVisualProviderModernIOS currentBackgroundView];
-[_UIToolbarVisualProviderModernIOS updateBarBackground];
-[_UIToolbarVisualProviderModernIOS appearanceObserver];
-[_UIToolbarVisualProviderModernIOS updateAppearance];
-[_UIToolbarVisualProviderModernIOS updateBarBackgroundSize];
-[_UIToolbarVisualProviderModernIOS _updateBackgroundModern];
-[_UIToolbarVisualProviderModernIOS _updateContentView];
-[_UIToolbarVisualProviderModernIOS contentViewMargins];
-[_UIToolbarVisualProviderModernIOS updateArchivedSubviews:];
-[_UIToolbarVisualProviderModernIOS _setViewOwnersAndUpdateContentViewForItems:withOldItems:animated:];
-[_UIToolbarVisualProviderModernIOS _backgroundFrame];
-[_UIToolbarVisualProviderModernIOS _updateBackgroundLegacyForPosition:];
```
