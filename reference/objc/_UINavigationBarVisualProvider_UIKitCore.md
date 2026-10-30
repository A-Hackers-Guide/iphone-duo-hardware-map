# `_UINavigationBarVisualProvider`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 30 properties, 168 instance methods, 1 class methods

## Instance variables

```
@"UINavigationBar" _navigationBar;
@"_UINavigationBarItemStack" _stack;
@"UINavigationItem" _itemForMeasuring;
B _activeTabBarHost;
@"_UITypedStorage" __typedStorage;
```

## Properties

```
@property (T@"UINavigationBar",R,N,V_navigationBar) navigationBar;
@property (T@"_UINavigationBarItemStack",&,N,V_stack) stack;
@property (TB,R,N) isInCustomization;
@property (Tq,R,N) currentContentSize;
@property (TB,R,N) permitsSearchBarPlacementIntegratedCentered;
@property (T@"_UINavigationControllerRefreshControlHost",&,N) refreshControlHost;
@property (TB,R,N) wantsLargeTitleDisplayed;
@property (TB,N) useInlineBackgroundHeightWhenLarge;
@property (Td,N) backgroundAlpha;
@property (Td,N) titleAlpha;
@property (Tq,N) appearanceAPIVersion;
@property (T@"<_UIBarAppearanceChangeObserver>",R,N) appearanceObserver;
@property (TB,N) forceScrollEdgeAppearance;
@property (TB,R,N) scrollEdgeAppearanceHasChromelessBehavior;
@property (TB,R,N) allowsUserInteractionDuringTransitions;
@property (TB,R,N) allowsLayoutWhileTransitioning;
@property (T@"_UITabContainerView",W,N) tabBarHostedView;
@property (TB,N) wantsHostedTabBarMetrics;
@property (TB,N,GisActiveTabBarHost,V_activeTabBarHost) activeTabBarHost;
@property (T@"UIBarButtonItem",&,N) staticNavBarButtonItem;
@property (T@"UIBarButtonItem",&,N) nullableStaticNavBarButtonItem;
@property (TB,R,N,GisContentViewHidden) contentViewHidden;
@property (TB,N) shouldFadeStaticNavBarButton;
@property (TB,N) staticNavBarButtonLingers;
@property (TB,R,N,GisAnimatingNavItemContentLayoutGuideForStaticButtonVisibilityChange) animatingNavItemContentLayoutGuideForStaticButtonVisibilityChange;
@property (Td,R,N) navItemContentLayoutGuideAnimationDistance;
@property (T@"UINavigationItem",R,N,V_itemForMeasuring) itemForMeasuring;
@property (Td,R,N) scrollAwayProgress;
@property (Td,R,N) barMinimizationTopSafeAreaOffset;
@property (TB,R,N) isScrollAwayEnabled;
```

## Class methods

```
+[_UINavigationBarVisualProvider shouldDecodeSubviews];
```

## Instance methods

```
-[_UINavigationBarVisualProvider _shim_touchesMoved:withEvent:];
-[_UINavigationBarVisualProvider sheetPresentationBarDetentValue];
-[_UINavigationBarVisualProvider setStaticNavBarButtonItem:];
-[_UINavigationBarVisualProvider setRefreshControlHost:];
-[_UINavigationBarVisualProvider supportsRefreshControlHosting];
-[_UINavigationBarVisualProvider presentSearchWithTransitionCoordinator:];
-[_UINavigationBarVisualProvider beginAnimatingNavItemContentLayoutGuideForStaticButtonVisibilityChange];
-[_UINavigationBarVisualProvider endAnimatingNavItemContentLayoutGuideForStaticButtonVisibilityChange];
-[_UINavigationBarVisualProvider setStaticLeadingItemGroups:trailingItemGroups:animated:];
-[_UINavigationBarVisualProvider tabBarHostedView];
-[_UINavigationBarVisualProvider setBackButtonVisible:animated:];
-[_UINavigationBarVisualProvider _shim_updateBackIndicator];
-[_UINavigationBarVisualProvider intrinsicContentSize];
-[_UINavigationBarVisualProvider minimumTopPaddingWithTraitCollection:parentView:];
-[_UINavigationBarVisualProvider _shim_userContentGuide];
-[_UINavigationBarVisualProvider navigationBar];
-[_UINavigationBarVisualProvider _shim_pressBackIndicator:initialPress:];
-[_UINavigationBarVisualProvider wantsLargeTitleDisplayed];
-[_UINavigationBarVisualProvider _accessibility_controlToActivateForHUDGestureLiftAtPoint:];
-[_UINavigationBarVisualProvider nullableStaticNavBarButtonItem];
-[_UINavigationBarVisualProvider setShouldFadeStaticNavBarButton:];
-[_UINavigationBarVisualProvider layoutHeightsFittingWidth:];
-[_UINavigationBarVisualProvider currentContentSize];
-[_UINavigationBarVisualProvider invalidateIntrinsicContentSize];
-[_UINavigationBarVisualProvider presentHostedSearchWithTransitionCoordinator:];
-[_UINavigationBarVisualProvider setWantsHostedTabBarMetrics:];
-[_UINavigationBarVisualProvider _shim_setPromptText:animated:];
-[_UINavigationBarVisualProvider _shim_popForCarplayPressAtFakePoint:];
-[_UINavigationBarVisualProvider glassUserInterfaceStyle];
-[_UINavigationBarVisualProvider _immediatelyFinishRunningTransition];
-[_UINavigationBarVisualProvider _observedScrollViewDidAdjustContentOffsetForLayoutPreservation];
-[_UINavigationBarVisualProvider traitCollectionDidChangeOnSubtree:];
-[_UINavigationBarVisualProvider setBackgroundAlpha:];
-[_UINavigationBarVisualProvider _shim_34415965];
-[_UINavigationBarVisualProvider _installContentClippingView:];
-[_UINavigationBarVisualProvider updateBackgroundGroupName];
-[_UINavigationBarVisualProvider _shim_backgroundHeight];
-[_UINavigationBarVisualProvider navigationBarInvalidatedResolvedLayoutMargins];
-[_UINavigationBarVisualProvider setTabBarHostedView:];
-[_UINavigationBarVisualProvider navigationItemUpdatedSearchBarPlacementAllowsToolbarIntegration:];
-[_UINavigationBarVisualProvider updateTopNavigationItemTitleView];
-[_UINavigationBarVisualProvider setNeedsExternalRepresentationUpdate];
-[_UINavigationBarVisualProvider changeLayout];
-[_UINavigationBarVisualProvider _beginRenaming];
-[_UINavigationBarVisualProvider _removeContentClippingView];
-[_UINavigationBarVisualProvider allowsLayoutWhileTransitioning];
-[_UINavigationBarVisualProvider layoutSubviews];
-[_UINavigationBarVisualProvider prepareForStackChange];
-[_UINavigationBarVisualProvider _shim_throwConstraintExceptions];
-[_UINavigationBarVisualProvider setUseInlineBackgroundHeightWhenLarge:];
-[_UINavigationBarVisualProvider stackDidChangeFrom:];
-[_UINavigationBarVisualProvider _accessibility_HUDItemForPoint:];
-[_UINavigationBarVisualProvider _shim_disableBlurTinting];
-[_UINavigationBarVisualProvider _supportsCustomization];
-[_UINavigationBarVisualProvider scrollEdgeAppearanceHasChromelessBehavior];
-[_UINavigationBarVisualProvider traitCollectionForChild:baseTraitCollection:];
-[_UINavigationBarVisualProvider updateProperties];
-[_UINavigationBarVisualProvider overrideIsNavigationBarEffectivelyVisible:];
-[_UINavigationBarVisualProvider setTitleAlpha:];
-[_UINavigationBarVisualProvider _refreshBackButtonMenu];
-[_UINavigationBarVisualProvider restingHeights];
-[_UINavigationBarVisualProvider intrinsicContentSizeInvalidatedForChildView:];
-[_UINavigationBarVisualProvider _observedScrollViewDidScroll];
-[_UINavigationBarVisualProvider _shim_30244716];
-[_UINavigationBarVisualProvider setSemanticContentAttribute:];
-[_UINavigationBarVisualProvider staticNavBarButtonLingers];
-[_UINavigationBarVisualProvider setStaticNavBarButtonLingers:];
-[_UINavigationBarVisualProvider canHandleStatusBarTouchAtPoint:];
-[_UINavigationBarVisualProvider _shim_wantsCustomTouchHandlingForTouches:];
-[_UINavigationBarVisualProvider setNullableStaticNavBarButtonItem:];
-[_UINavigationBarVisualProvider backgroundAlpha];
-[_UINavigationBarVisualProvider setStaticNavBarButtonItem:trailingPosition:];
-[_UINavigationBarVisualProvider sizeThatFits:];
-[_UINavigationBarVisualProvider _observeScrollViewWillScrollToTop];
-[_UINavigationBarVisualProvider resolvedSearchBarMargins];
-[_UINavigationBarVisualProvider isEffectivelyEmpty];
-[_UINavigationBarVisualProvider isActiveTabBarHost];
-[_UINavigationBarVisualProvider _shim_backdropStyle];
-[_UINavigationBarVisualProvider _shim_shadowAlpha];
-[_UINavigationBarVisualProvider allowsUserInteractionDuringTransitions];
-[_UINavigationBarVisualProvider contentViewVisualProvider];
-[_UINavigationBarVisualProvider _beginCustomization];
-[_UINavigationBarVisualProvider setForceScrollEdgeAppearance:];
-[_UINavigationBarVisualProvider appearanceObserver];
-[_UINavigationBarVisualProvider hitTest:defaultViewHit:];
-[_UINavigationBarVisualProvider isScrollAwayEnabled];
-[_UINavigationBarVisualProvider safeAreaInsetsDidChange];
-[_UINavigationBarVisualProvider titleAlpha];
-[_UINavigationBarVisualProvider adjustedSafeAreaInsets:];
-[_UINavigationBarVisualProvider _shim_layoutView];
-[_UINavigationBarVisualProvider _accessibility_shouldBeginHUDGestureAtPoint:];
-[_UINavigationBarVisualProvider updateScrollAwayForBarDetentProgress:isDragging:];
-[_UINavigationBarVisualProvider setupTopNavigationItem];
-[_UINavigationBarVisualProvider prepare];
-[_UINavigationBarVisualProvider _shim_setDisableBlurTinting:];
-[_UINavigationBarVisualProvider shouldFadeStaticNavBarButton];
-[_UINavigationBarVisualProvider _shim_displayViewsIncludingHiddenBackButtonViews:];
-[_UINavigationBarVisualProvider barMinimizationTopSafeAreaOffset];
-[_UINavigationBarVisualProvider updateNavItemContentLayoutGuideAnimationConstraintConstant:];
-[_UINavigationBarVisualProvider wantsHostedTabBarMetrics];
-[_UINavigationBarVisualProvider prepareForPop];
-[_UINavigationBarVisualProvider _shim_touchesBegan:withEvent:];
-[_UINavigationBarVisualProvider updateBarVisibilityForTopItem];
-[_UINavigationBarVisualProvider wantsScrollPocketContainerInteraction];
-[_UINavigationBarVisualProvider isInCustomization];
-[_UINavigationBarVisualProvider pushAnimated:completion:];
-[_UINavigationBarVisualProvider recordBarSize:];
-[_UINavigationBarVisualProvider itemForMeasuring];
-[_UINavigationBarVisualProvider deferSearchSuggestionsMenuRefreshForGeometryChange];
-[_UINavigationBarVisualProvider _shim_107516167];
-[_UINavigationBarVisualProvider setActiveTabBarHost:];
-[_UINavigationBarVisualProvider changeAppearance];
-[_UINavigationBarVisualProvider popAnimated:completion:];
-[_UINavigationBarVisualProvider staticNavBarButtonItem];
-[_UINavigationBarVisualProvider animateForSearchPresentation:];
-[_UINavigationBarVisualProvider gestureRecognizerShouldBegin:defaultAnswer:];
-[_UINavigationBarVisualProvider refreshSearchSuggestionsMenuAfterGeometryChange];
-[_UINavigationBarVisualProvider description];
-[_UINavigationBarVisualProvider _shim_promptText];
-[_UINavigationBarVisualProvider _shim_updateUserContentGuideForTopItem:backItem:];
-[_UINavigationBarVisualProvider updateConstraints];
-[_UINavigationBarVisualProvider _shim_backIndicatorView];
-[_UINavigationBarVisualProvider searchScopeBarWillManuallyShowOrHideForNavigationItem:];
-[_UINavigationBarVisualProvider _shim_touchesCancelled:withEvent:];
-[_UINavigationBarVisualProvider traitCollectionDidChange:];
-[_UINavigationBarVisualProvider dismissHostedSearchWithTransitionCoordinator:];
-[_UINavigationBarVisualProvider baseContentViewHeight];
-[_UINavigationBarVisualProvider _shim_touchesEnded:withEvent:];
-[_UINavigationBarVisualProvider scrollAwayProgress];
-[_UINavigationBarVisualProvider permitsSearchBarPlacementIntegratedCentered];
-[_UINavigationBarVisualProvider updateTopNavigationItemAnimated:];
-[_UINavigationBarVisualProvider _shim_setUseContentView:];
-[_UINavigationBarVisualProvider leadingMarginForContentViewsWithContentMargin:];
-[_UINavigationBarVisualProvider setAppearanceAPIVersion:];
-[_UINavigationBarVisualProvider resolvedLargeTitleMargins];
-[_UINavigationBarVisualProvider isContentViewHidden];
-[_UINavigationBarVisualProvider updateSearchBarForPlacementChangeIfApplicable];
-[_UINavigationBarVisualProvider setNeedsStaticNavBarButtonUpdate];
-[_UINavigationBarVisualProvider setStack:];
-[_UINavigationBarVisualProvider useInlineBackgroundHeightWhenLarge];
-[_UINavigationBarVisualProvider _endRenaming];
-[_UINavigationBarVisualProvider prepareForPush];
-[_UINavigationBarVisualProvider refreshControlHost];
-[_UINavigationBarVisualProvider updateArchivedSubviews:];
-[_UINavigationBarVisualProvider barDidMoveToWindow];
-[_UINavigationBarVisualProvider barSizeChanged];
-[_UINavigationBarVisualProvider statusBarStyle];
-[_UINavigationBarVisualProvider canCollapseToZeroHeight];
-[_UINavigationBarVisualProvider preferredFocusedView];
-[_UINavigationBarVisualProvider forceScrollEdgeAppearance];
-[_UINavigationBarVisualProvider _shim_updateBackgroundViewIgnoringFlag];
-[_UINavigationBarVisualProvider teardown];
-[_UINavigationBarVisualProvider _shim_compatibilityBackgroundView];
-[_UINavigationBarVisualProvider heightForRestoringFromCancelledTransition];
-[_UINavigationBarVisualProvider _shim_setShadowAlpha:];
-[_UINavigationBarVisualProvider _shim_setCustomBackgroundView:];
-[_UINavigationBarVisualProvider appendToDescription:];
-[_UINavigationBarVisualProvider removeContentForItem:];
-[_UINavigationBarVisualProvider stack];
-[_UINavigationBarVisualProvider appearanceAPIVersion];
-[_UINavigationBarVisualProvider isAnimatingNavItemContentLayoutGuideForStaticButtonVisibilityChange];
-[_UINavigationBarVisualProvider _shim_contentView];
-[_UINavigationBarVisualProvider provideViewsForContents:topItem:backItem:];
-[_UINavigationBarVisualProvider initWithNavigationBar:];
-[_UINavigationBarVisualProvider shouldUseHeightRangeFittingWidth];
-[_UINavigationBarVisualProvider topItemHasVariableHeight];
-[_UINavigationBarVisualProvider barDidAddSubview:];
-[_UINavigationBarVisualProvider navItemContentLayoutGuideAnimationDistance];
```
