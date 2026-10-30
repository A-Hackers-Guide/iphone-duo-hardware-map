# `_UITabBarVisualProviderLegacyIOS`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UITabBarVisualProvider`
- Protocols: `_UIBarAppearanceChangeObserver`, `UIPointerInteractionDelegate`, `PTSettingsKeyObserver`
- 9 instance variables, 4 properties, 52 instance methods, 0 class methods

## Instance variables

```
@"UIPointerInteraction" _pointerInteraction;
@"_UIBarBackground" _backgroundView;
@"_UIBarBackgroundLayout" _backgroundViewLayout;
@"UIView" _customBackgroundView;
@"UIView" _accessoryView;
d _minimumWidthForHorizontalLayout;
B _useModernAppearance;
q _style;
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
-[_UITabBarVisualProviderLegacyIOS setUseModernAppearance:];
-[_UITabBarVisualProviderLegacyIOS _updateAccessoryView];
-[_UITabBarVisualProviderLegacyIOS _updateBackgroundAnimated:];
-[_UITabBarVisualProviderLegacyIOS setBackgroundTransitionProgress:forceUpdate:animated:];
-[_UITabBarVisualProviderLegacyIOS _shim_updateTabBarItemView:];
-[_UITabBarVisualProviderLegacyIOS appearance:categoriesChanged:];
-[_UITabBarVisualProviderLegacyIOS changeItemsTo:removingItems:selectedItem:oldSelectedItem:animate:];
-[_UITabBarVisualProviderLegacyIOS useModernAppearance];
-[_UITabBarVisualProviderLegacyIOS setBackgroundTransitionProgress:];
-[_UITabBarVisualProviderLegacyIOS _shim_accessoryView];
-[_UITabBarVisualProviderLegacyIOS changeSelectedItem:fromItem:];
-[_UITabBarVisualProviderLegacyIOS _shim_setAccessoryView:];
-[_UITabBarVisualProviderLegacyIOS intrinsicContentSizeGivenSize:];
-[_UITabBarVisualProviderLegacyIOS exchangeItem:withItem:];
-[_UITabBarVisualProviderLegacyIOS backgroundTransitionProgress];
-[_UITabBarVisualProviderLegacyIOS _preferredFocusedViewiOS];
-[_UITabBarVisualProviderLegacyIOS _shim_layoutItemsOnly];
-[_UITabBarVisualProviderLegacyIOS _preferredFocusedViewCarplay];
-[_UITabBarVisualProviderLegacyIOS pointerInteraction:styleForRegion:];
-[_UITabBarVisualProviderLegacyIOS minimumWidthForHorizontalLayout];
-[_UITabBarVisualProviderLegacyIOS _shim_setShadowHidden:];
-[_UITabBarVisualProviderLegacyIOS _layoutTabBarItems];
-[_UITabBarVisualProviderLegacyIOS updateBackgroundGroupName];
-[_UITabBarVisualProviderLegacyIOS changeLayout];
-[_UITabBarVisualProviderLegacyIOS _updateBackgroundLegacy];
-[_UITabBarVisualProviderLegacyIOS layoutSubviews];
-[_UITabBarVisualProviderLegacyIOS traitCollectionForChild:baseTraitCollection:];
-[_UITabBarVisualProviderLegacyIOS _shim_shadowHidden];
-[_UITabBarVisualProviderLegacyIOS _configureItems:];
-[_UITabBarVisualProviderLegacyIOS setSemanticContentAttribute:];
-[_UITabBarVisualProviderLegacyIOS _shim_shadowAlpha];
-[_UITabBarVisualProviderLegacyIOS _shadowFrameForBounds:height:];
-[_UITabBarVisualProviderLegacyIOS appearanceObserver];
-[_UITabBarVisualProviderLegacyIOS prepare];
-[_UITabBarVisualProviderLegacyIOS _updateBackgroundModern];
-[_UITabBarVisualProviderLegacyIOS setMinimumWidthForHorizontalLayout:];
-[_UITabBarVisualProviderLegacyIOS pointerInteraction:regionForRequest:defaultRegion:];
-[_UITabBarVisualProviderLegacyIOS changeAppearance];
-[_UITabBarVisualProviderLegacyIOS _applyAppearanceCustomizationsToItem:];
-[_UITabBarVisualProviderLegacyIOS _layoutRegion];
-[_UITabBarVisualProviderLegacyIOS _styleForTraitCollection:];
-[_UITabBarVisualProviderLegacyIOS traitCollectionDidChange:];
-[_UITabBarVisualProviderLegacyIOS _updateAppearanceForTransitionFromItem:toItem:];
-[_UITabBarVisualProviderLegacyIOS updateArchivedSubviews:];
-[_UITabBarVisualProviderLegacyIOS _shim_heightForCustomizingItems];
-[_UITabBarVisualProviderLegacyIOS preferredFocusedView];
-[_UITabBarVisualProviderLegacyIOS _focusedItemHighlightView];
-[_UITabBarVisualProviderLegacyIOS teardown];
-[_UITabBarVisualProviderLegacyIOS _shim_compatibilityBackgroundView];
-[_UITabBarVisualProviderLegacyIOS _shim_setShadowAlpha:];
-[_UITabBarVisualProviderLegacyIOS _shim_setCustomBackgroundView:];
-[_UITabBarVisualProviderLegacyIOS createViewForTabBarItem:];
```
