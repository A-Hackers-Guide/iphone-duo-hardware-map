# `_UITabBarVisualProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 9 properties, 77 instance methods, 1 class methods

## Instance variables

```
@"UITabBar" _tabBar;
q _hostedElements;
@? _hostedElementsLayoutHandler;
q _currentMorphTarget;
d _barMaterialFillProgress;
```

## Properties

```
@property (T@"UITabBar",R,N,V_tabBar) tabBar;
@property (TB,N) useModernAppearance;
@property (T@"<_UIBarAppearanceChangeObserver>",R,N) appearanceObserver;
@property (Td,N) minimumWidthForHorizontalLayout;
@property (Td,D,N) backgroundTransitionProgress;
@property (Tq,N,V_hostedElements) hostedElements;
@property (T@?,C,N,V_hostedElementsLayoutHandler) hostedElementsLayoutHandler;
@property (Tq,N,V_currentMorphTarget) currentMorphTarget;
@property (Td,N,V_barMaterialFillProgress) barMaterialFillProgress;
```

## Class methods

```
+[_UITabBarVisualProvider shouldDecodeSubviews];
```

## Instance methods

```
-[_UITabBarVisualProvider observeContentScrollView:];
-[_UITabBarVisualProvider tabMorphingHost];
-[_UITabBarVisualProvider setUseModernAppearance:];
-[_UITabBarVisualProvider sheetPresentationBarDetentValue];
-[_UITabBarVisualProvider hostedElements];
-[_UITabBarVisualProvider setBackgroundTransitionProgress:forceUpdate:animated:];
-[_UITabBarVisualProvider _shim_updateTabBarItemView:];
-[_UITabBarVisualProvider changeItemsTo:removingItems:selectedItem:oldSelectedItem:animate:];
-[_UITabBarVisualProvider useModernAppearance];
-[_UITabBarVisualProvider setBackgroundTransitionProgress:];
-[_UITabBarVisualProvider updateItem:];
-[_UITabBarVisualProvider _shim_accessoryView];
-[_UITabBarVisualProvider changeSelectedItem:fromItem:];
-[_UITabBarVisualProvider _shim_setAccessoryView:];
-[_UITabBarVisualProvider intrinsicContentSizeGivenSize:];
-[_UITabBarVisualProvider exchangeItem:withItem:];
-[_UITabBarVisualProvider backgroundTransitionProgress];
-[_UITabBarVisualProvider _shim_layoutItemsOnly];
-[_UITabBarVisualProvider glassGroupContainerDidChange:];
-[_UITabBarVisualProvider focusedTabBarItem];
-[_UITabBarVisualProvider initWithTabBar:];
-[_UITabBarVisualProvider currentMorphTarget];
-[_UITabBarVisualProvider minimumWidthForHorizontalLayout];
-[_UITabBarVisualProvider _shim_setShadowHidden:];
-[_UITabBarVisualProvider resolvedPresentationSourceItemForItem:];
-[_UITabBarVisualProvider didUpdateFocusInContext:withAnimationCoordinator:];
-[_UITabBarVisualProvider updateBackgroundGroupName];
-[_UITabBarVisualProvider tabBarItemAtPoint:];
-[_UITabBarVisualProvider willBeginCustomizingItems];
-[_UITabBarVisualProvider changeLayout];
-[_UITabBarVisualProvider layoutSubviews];
-[_UITabBarVisualProvider didEndCustomizingItems];
-[_UITabBarVisualProvider viewsForMorphingToTarget:];
-[_UITabBarVisualProvider _tabBarPlatterLayoutInfoInCoordinateSpace:];
-[_UITabBarVisualProvider selectCollapseTabIfPossible];
-[_UITabBarVisualProvider traitCollectionForChild:baseTraitCollection:];
-[_UITabBarVisualProvider setCurrentMorphTarget:];
-[_UITabBarVisualProvider updateProperties];
-[_UITabBarVisualProvider _shim_shadowHidden];
-[_UITabBarVisualProvider setSemanticContentAttribute:];
-[_UITabBarVisualProvider _shim_shadowAlpha];
-[_UITabBarVisualProvider setBarMaterialFillProgress:];
-[_UITabBarVisualProvider tabBar];
-[_UITabBarVisualProvider appearanceObserver];
-[_UITabBarVisualProvider borrowTabBarPlatterViewsSuppressingBackground:updateHandler:];
-[_UITabBarVisualProvider prepare];
-[_UITabBarVisualProvider setMinimumWidthForHorizontalLayout:];
-[_UITabBarVisualProvider setHostedElements:];
-[_UITabBarVisualProvider defaultTintColor];
-[_UITabBarVisualProvider changeAppearance];
-[_UITabBarVisualProvider minimizeBehaviorDidChange];
-[_UITabBarVisualProvider preferredFocusEnvironments];
-[_UITabBarVisualProvider updateConstraints];
-[_UITabBarVisualProvider traitCollectionDidChange:];
-[_UITabBarVisualProvider updateUnselectedItemTintColor];
-[_UITabBarVisualProvider wantsFocus];
-[_UITabBarVisualProvider defaultAnimationDuration];
-[_UITabBarVisualProvider shouldPassthroughTouches];
-[_UITabBarVisualProvider setMinimized:];
-[_UITabBarVisualProvider updateArchivedSubviews:];
-[_UITabBarVisualProvider _shim_heightForCustomizingItems];
-[_UITabBarVisualProvider morphAnimationsForHostedElementsDidEnd];
-[_UITabBarVisualProvider preferredFocusedView];
-[_UITabBarVisualProvider shouldUpdateFocusInContext:];
-[_UITabBarVisualProvider teardown];
-[_UITabBarVisualProvider passthroughScrollInteractionDelegate];
-[_UITabBarVisualProvider _shim_compatibilityBackgroundView];
-[_UITabBarVisualProvider _shim_setShadowAlpha:];
-[_UITabBarVisualProvider _shim_setCustomBackgroundView:];
-[_UITabBarVisualProvider barMaterialFillProgress];
-[_UITabBarVisualProvider createViewForTabBarItem:];
-[_UITabBarVisualProvider setHostedElementsLayoutHandler:];
-[_UITabBarVisualProvider _shim_shadowView];
-[_UITabBarVisualProvider _shim_updateFocusHighlightVisibility];
-[_UITabBarVisualProvider changeItemsTo:removingItems:selectedItem:animate:];
-[_UITabBarVisualProvider hostedElementsLayoutHandler];
-[_UITabBarVisualProvider tabBarSizeChanged:];
```
