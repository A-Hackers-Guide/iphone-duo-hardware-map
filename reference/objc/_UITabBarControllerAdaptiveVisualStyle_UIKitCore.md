# `_UITabBarControllerAdaptiveVisualStyle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UITabBarControllerVisualStyle_iOS`
- Protocols: `_UITabContainerViewDelegate`, `_UIFloatingBarChangeObserver`
- 8 instance variables, 12 properties, 87 instance methods, 0 class methods

## Instance variables

```
B _needsContentLayout;
B _isUpdatingTabBarLayout;
B _hasTabGroups;
B _allowVerticalBarInSheets;
@"_UITabBarControllerAdaptiveConfiguration" _configuration;
@"_UITabContainerView" _tabContainerView;
@"UIBarButtonItemGroup" _sidebarToggleBarButtonItemGroup;
@"UINavigationBar" _hostingNavigationBarForSidebarToggleButton;
```

## Properties

```
@property (T@"_UITabContainerView",R,N,V_tabContainerView) tabContainerView;
@property (T@"UIBarButtonItemGroup",R,N,V_sidebarToggleBarButtonItemGroup) sidebarToggleBarButtonItemGroup;
@property (T@"UINavigationBar",R,W,N,V_hostingNavigationBarForSidebarToggleButton) hostingNavigationBarForSidebarToggleButton;
@property (TB,N,V_allowVerticalBarInSheets) allowVerticalBarInSheets;
@property (T@"_UITabBarControllerAdaptiveConfiguration",R,N,V_configuration) configuration;
@property (T@"UIAction",&,N) overrideTidebarButtonAction;
@property (T{UIEdgeInsets=dddd},N) additionalSidebarInsets;
@property (T{UIEdgeInsets=dddd},N) absoluteSidebarInsets;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITabBarControllerAdaptiveVisualStyle tabContentDidChange:];
-[_UITabBarControllerAdaptiveVisualStyle observeContentScrollView:];
-[_UITabBarControllerAdaptiveVisualStyle overrideTidebarButtonAction];
-[_UITabBarControllerAdaptiveVisualStyle sidebar];
-[_UITabBarControllerAdaptiveVisualStyle setAbsoluteSidebarInsets:];
-[_UITabBarControllerAdaptiveVisualStyle defaultMaxItems];
-[_UITabBarControllerAdaptiveVisualStyle tabBarPosition];
-[_UITabBarControllerAdaptiveVisualStyle updateBottomAccessoryAnimated:];
-[_UITabBarControllerAdaptiveVisualStyle setOverrideTidebarButtonAction:];
-[_UITabBarControllerAdaptiveVisualStyle bottomAccessoryInsets];
-[_UITabBarControllerAdaptiveVisualStyle contentLayoutGuideFrame];
-[_UITabBarControllerAdaptiveVisualStyle updateViewControllers:];
-[_UITabBarControllerAdaptiveVisualStyle tabBarView];
-[_UITabBarControllerAdaptiveVisualStyle loadViews];
-[_UITabBarControllerAdaptiveVisualStyle absoluteSidebarInsets];
-[_UITabBarControllerAdaptiveVisualStyle _horizontalSizeClassDidChange];
-[_UITabBarControllerAdaptiveVisualStyle _updateContentLayoutForSidebarAppearanceIfNeeded];
-[_UITabBarControllerAdaptiveVisualStyle updateViewControllerForReselection:];
-[_UITabBarControllerAdaptiveVisualStyle willUpdateViewControllers];
-[_UITabBarControllerAdaptiveVisualStyle _floatingBarToolbarOverlayInsetsDidChange:];
-[_UITabBarControllerAdaptiveVisualStyle updateContentLayoutForSidebarAppearanceWithTransitionCoordinator:];
-[_UITabBarControllerAdaptiveVisualStyle tabBarDidChange];
-[_UITabBarControllerAdaptiveVisualStyle preferredSidebarModeDidChange];
-[_UITabBarControllerAdaptiveVisualStyle resolvedPopoverPresentationControllerSourceItemForTab:];
-[_UITabBarControllerAdaptiveVisualStyle ignoresDefaultTabBarVisibilityAnimation];
-[_UITabBarControllerAdaptiveVisualStyle _removeSidebarToggleButtonFromHostingNavigationBarAnimated:];
-[_UITabBarControllerAdaptiveVisualStyle _updateFloatingBarContainerProxy:previousCollection:];
-[_UITabBarControllerAdaptiveVisualStyle canDisplaySidebar];
-[_UITabBarControllerAdaptiveVisualStyle updateTabBarLayout];
-[_UITabBarControllerAdaptiveVisualStyle preferredTrailingStatusBarStyle];
-[_UITabBarControllerAdaptiveVisualStyle wantsDefaultTabBar];
-[_UITabBarControllerAdaptiveVisualStyle preferredCenterStatusBarStyle];
-[_UITabBarControllerAdaptiveVisualStyle hostingNavigationBarForSidebarToggleButton];
-[_UITabBarControllerAdaptiveVisualStyle _floatingBarDidInvalidateExternalRepresentation:];
-[_UITabBarControllerAdaptiveVisualStyle tabContainerView];
-[_UITabBarControllerAdaptiveVisualStyle edgeInsetsForChildViewController:];
-[_UITabBarControllerAdaptiveVisualStyle tabBarPresentationPreferenceDidChange];
-[_UITabBarControllerAdaptiveVisualStyle _updateSidebarResolvedLayout];
-[_UITabBarControllerAdaptiveVisualStyle editingStateDidChange];
-[_UITabBarControllerAdaptiveVisualStyle _updateBarsWithWantsHostedTabBarMetrics:];
-[_UITabBarControllerAdaptiveVisualStyle sheetPresentationDetentProgressDidChange:];
-[_UITabBarControllerAdaptiveVisualStyle adjustedTransitionViewFrame:];
-[_UITabBarControllerAdaptiveVisualStyle canDisplayUITabBar];
-[_UITabBarControllerAdaptiveVisualStyle canToggleSidebar];
-[_UITabBarControllerAdaptiveVisualStyle navigationControllerDidUpdate:];
-[_UITabBarControllerAdaptiveVisualStyle viewWillAppear:];
-[_UITabBarControllerAdaptiveVisualStyle setBottomBarSuppressedByNavigation:animated:];
-[_UITabBarControllerAdaptiveVisualStyle _updateSidebarToggleBarButtonItemForHostingNavigationBarAnimated:];
-[_UITabBarControllerAdaptiveVisualStyle _updateBarAvailabilityAnimated:];
-[_UITabBarControllerAdaptiveVisualStyle configuration];
-[_UITabBarControllerAdaptiveVisualStyle overrideUISplitViewControllerToCompact];
-[_UITabBarControllerAdaptiveVisualStyle safeAreaInsetsDidChange];
-[_UITabBarControllerAdaptiveVisualStyle splitViewControllerDidUpdate:];
-[_UITabBarControllerAdaptiveVisualStyle _setNeedsContentLayout];
-[_UITabBarControllerAdaptiveVisualStyle _shouldShowSidebarToggleInNavigationBar];
-[_UITabBarControllerAdaptiveVisualStyle additionalSidebarInsets];
-[_UITabBarControllerAdaptiveVisualStyle didLayoutSidebarView];
-[_UITabBarControllerAdaptiveVisualStyle setAdditionalSidebarInsets:];
-[_UITabBarControllerAdaptiveVisualStyle setAllowVerticalBarInSheets:];
-[_UITabBarControllerAdaptiveVisualStyle sidebarLayoutDidChange];
-[_UITabBarControllerAdaptiveVisualStyle canDisplayTabBar];
-[_UITabBarControllerAdaptiveVisualStyle _canDisplayFloatingTabBar];
-[_UITabBarControllerAdaptiveVisualStyle _tabCustomizationProxy];
-[_UITabBarControllerAdaptiveVisualStyle _updateBadgeValueForSidebarBarButtonItem:];
-[_UITabBarControllerAdaptiveVisualStyle didUpdateVisibleAppearance];
-[_UITabBarControllerAdaptiveVisualStyle sidebarToggleBarButtonItemGroup];
-[_UITabBarControllerAdaptiveVisualStyle setBarHidden:animated:];
-[_UITabBarControllerAdaptiveVisualStyle _resolvedSidebarStyle];
-[_UITabBarControllerAdaptiveVisualStyle initWithTabBarController:];
-[_UITabBarControllerAdaptiveVisualStyle preferredTrafficLightStyle];
-[_UITabBarControllerAdaptiveVisualStyle _resolvedSidebarToggleBarButtonItemGroup];
-[_UITabBarControllerAdaptiveVisualStyle updateFocusForSelectedViewControllerChange];
-[_UITabBarControllerAdaptiveVisualStyle _updateHostedElementsFromContainerViewControllerUpdate];
-[_UITabBarControllerAdaptiveVisualStyle prepareConfiguration];
-[_UITabBarControllerAdaptiveVisualStyle sheetPresentationBarDetentValueForContext:];
-[_UITabBarControllerAdaptiveVisualStyle preferredLeadingStatusBarStyle];
-[_UITabBarControllerAdaptiveVisualStyle traitOverridesForChildViewController:];
-[_UITabBarControllerAdaptiveVisualStyle teardown];
-[_UITabBarControllerAdaptiveVisualStyle _updateNavigationBarHostingWithSelectionChanged:];
-[_UITabBarControllerAdaptiveVisualStyle selectedViewControllerDidChange];
-[_UITabBarControllerAdaptiveVisualStyle sidebarVisibilityDidChangeWithAnimator:];
-[_UITabBarControllerAdaptiveVisualStyle _verticalBarAvailabilityDidChange];
-[_UITabBarControllerAdaptiveVisualStyle allowVerticalBarInSheets];
-[_UITabBarControllerAdaptiveVisualStyle childViewControllerForStatusBarStyle];
-[_UITabBarControllerAdaptiveVisualStyle _effectivePartStyleForEdge:];
-[_UITabBarControllerAdaptiveVisualStyle _isInVerticalBarTraitEnvironment];
-[_UITabBarControllerAdaptiveVisualStyle shouldEnforceChildSelectionInGroupTabs];
```
