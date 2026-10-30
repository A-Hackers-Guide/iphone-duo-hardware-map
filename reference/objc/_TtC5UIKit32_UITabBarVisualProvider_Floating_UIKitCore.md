# `_TtC5UIKit32_UITabBarVisualProvider_Floating`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UITabBarVisualProvider`
- Protocols: `_UILendableViewContainerDelegate`, `_UITabMorphing`, `UIPointerInteractionDelegate`, `_UIPassthroughScrollInteractionDelegate`, `_TtP5UIKit32_UIScrollAwayInteractionDelegate_`, `_UIBarAppearanceChangeObserver`, `UIGestureRecognizerDelegate`
- 40 instance variables, 12 properties, 72 instance methods, 1 class methods

## Instance variables

```
UIKit.FloatingTabBarConfiguration ? $__lazy_storage_$_configuration;
_$sSo24_UILendableViewContainerC UIKit._UITabBarItemPlatterView lendablePlatterView;
_$sSo17_UILiquidLensViewC lensView;
_$sSo29UIViewFloatAnimatablePropertyCSg $__lazy_storage_$_lensViewTargetPosition;
__C.CGRect lensViewFrame;
Swift.Bool isLensViewHidden;
UIKit._UITabBarVisualProvider_Floating.SelectedContentView selectedContentView;
_$sSo33_UITabBarHostedPlatterViewsHandleCSgXw currentHostedPlatterViewsHandle;
UIKit._UITabBarAuxiliaryView ? auxiliaryView;
UIKit._UITabBarAuxiliaryDummyView ? auxiliaryDummyView;
Swift.Bool suppressAuxiliaryPlatterItem;
Swift.Bool isShowingCollapseButton;
Swift.Bool isShowingMinimizedPlatter;
_$sSo6UIViewCSg accessoryView;
UIKit._UITabBarPlatterView ? collapsePlatterView;
UIKit._UITabButton ? collapseButton;
UIKit._UIScrollAwayInteraction ? scrollAwayInteraction;
_$sSo26_UIScrollPocketInteractionCSg scrollPocketInteraction;
_$sSo12UITabBarItemCSgXw itemForCollapseButton;
_$sSa -> UIKit._UITabButton tabBarButtons;
_$sSDySo12UITabBarItemC UIKit._UITabButton tabBarButtonsForItem;
_$sSo19UIGestureRecognizerCSg selectionGestureRecognizer;
_$sSo20UIPointerInteractionCSg pointerInteraction;
_$sSD -> UIKit.FloatingTabBarConfiguration.LayoutMetrics.Key __C.CGSize idealContentSizeCache;
UIKit._UITabBarAnimationSettings ? $__lazy_storage_$_animationSettings;
Swift.Bool isHandlingItemsChange;
Swift.Bool isCustomizingTabBar;
Swift.Bool isUpdatingHostedPlatterViewsHandle;
CoreGraphics.CGFloat _backgroundTransitionProgress;
Swift.Bool _useModernAppearance;
_$sSo12UITabBarItemCSg highlightedItem;
_$sSiSg highlightedItemIndex;
__C.CGPoint highlightAnchorPoint;
__C.CGPoint selectionGestureOffset;
Swift.Bool isExpandedFromInteraction;
UIKit.TabBarInteractiveExpansionAssistant ? expansionAssistant;
UIKit._UITabBarExpansionPlatterContainer ? platterExpansionContainer;
Swift.Bool shouldReselectHighlightedItemOnLift;
__C.CGPoint selectionGestureInitialLocation;
Swift.Bool shouldFailSelectionOnLiftOutside;
```

## Properties

```
@property (T@"<_UIBarAppearanceChangeObserver>",N,R) appearanceObserver;
@property (T@"NSString",N,R) componentKey;
@property (T@"UIView",N,R) contentView;
@property (T@"UIView",N,R) backgroundView;
@property (T{CACornerRadii={CGSize=dd}{CGSize=dd}{CGSize=dd}{CGSize=dd}},N,R) contentCornerRadii;
@property (T@"_UIShadowProperties",N,R) shadowProperties;
@property (T@"UIViewSpringAnimationBehavior",N,R) morphTargetSpringBehavior;
@property (Tq,N) hostedElements;
@property (Tq,N) currentMorphTarget;
@property (Td,N) barMaterialFillProgress;
@property (TB,N) useModernAppearance;
@property (Td,N) backgroundTransitionProgress;
```

## Class methods

```
+[_TtC5UIKit32_UITabBarVisualProvider_Floating shouldDecodeSubviews];
```

## Instance methods

```
-[_TtC5UIKit32_UITabBarVisualProvider_Floating observeContentScrollView:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating contentCornerRadii];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating tabMorphingHost];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating setUseModernAppearance:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating lendableViewContainer:didBorrowView:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating sheetPresentationBarDetentValue];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating hostedElements];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating setBackgroundTransitionProgress:forceUpdate:animated:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating _shim_updateTabBarItemView:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating appearance:categoriesChanged:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating changeItemsTo:removingItems:selectedItem:oldSelectedItem:animate:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating lendableViewContainer:didReturnView:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating useModernAppearance];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating setBackgroundTransitionProgress:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating updateItem:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating _shim_accessoryView];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating changeSelectedItem:fromItem:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating _shim_setAccessoryView:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating intrinsicContentSizeGivenSize:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating exchangeItem:withItem:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating backgroundTransitionProgress];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating _shim_layoutItemsOnly];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating glassGroupContainerDidChange:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating focusedTabBarItem];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating shadowProperties];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating initWithTabBar:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating pointerInteraction:styleForRegion:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating currentMorphTarget];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating init];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating resolvedPresentationSourceItemForItem:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating pointerInteraction:willEnterRegion:animator:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating pointerInteraction:willExitRegion:animator:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating transitionDidEnd];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating tabBarItemAtPoint:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating willBeginCustomizingItems];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating changeLayout];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating layoutSubviews];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating performAlongsideTransitionToVisibility:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating didEndCustomizingItems];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating viewsForMorphingToTarget:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating _tabBarPlatterLayoutInfoInCoordinateSpace:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating selectCollapseTabIfPossible];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating setCurrentMorphTarget:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating updateProperties];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating morphTargetSpringBehavior];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating passthroughScrollInteractionDidRecognize:atLocation:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating setSemanticContentAttribute:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating passthroughScrollInteraction:shouldInteractAtLocation:withEvent:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating setBarMaterialFillProgress:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating gestureRecognizerShouldBegin:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating appearanceObserver];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating borrowTabBarPlatterViewsSuppressingBackground:updateHandler:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating prepare];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating componentKey];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating setHostedElements:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating pointerInteraction:regionForRequest:defaultRegion:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating contentView];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating prepareForTransitionToVisibility:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating changeAppearance];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating backgroundView];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating minimizeBehaviorDidChange];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating preferredFocusEnvironments];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating updateUnselectedItemTintColor];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating shouldPassthroughTouches];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating setMinimized:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating updateArchivedSubviews:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating scrollAwayInteraction:progressDidChange:tracking:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating morphAnimationsForHostedElementsDidEnd];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating teardown];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating passthroughScrollInteractionDelegate];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating handleSelectionGesture:];
-[_TtC5UIKit32_UITabBarVisualProvider_Floating barMaterialFillProgress];
```
