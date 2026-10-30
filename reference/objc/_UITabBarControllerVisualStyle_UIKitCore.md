# `_UITabBarControllerVisualStyle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIGestureRecognizerDelegate`, `_UIVisualStyleProviding`, `_UITabContentProviding`
- 8 instance variables, 19 properties, 96 instance methods, 0 class methods

## Instance variables

```
@"UITapGestureRecognizer" _backGestureRecognizer;
@"UITapGestureRecognizer" _selectGestureRecognizer;
@"UILongPressGestureRecognizer" _accessibilityLongPressGestureRecognizer;
@"_UIScrollPocketContainerInteraction" _tabBarScrollPocketContainerInteraction;
B _suppressTabBarControllerNotification;
B _barHidden;
B _isBottomBarSuppressedByNavigation;
@"UITabBarController" _tabBarController;
```

## Properties

```
@property (T@"UITabBarController",R,W,N,V_tabBarController) tabBarController;
@property (TB,R,N) wantsDefaultTabBar;
@property (TB,R,N) supportsShowingMoreItem;
@property (TB,R,N) suppressesEditingUI;
@property (TB,R,N) ignoresDefaultTabBarVisibilityAnimation;
@property (TB,R,N) overrideUISplitViewControllerToCompact;
@property (TB,R,N) prefersTabBarFocusedOnViewDidLoad;
@property (TB,R,N) removeTabBarFocusedOnViewDidDisappear;
@property (TB,R,N) supportsFocusGestures;
@property (TB,R,N) updatesTabBarFocusHeadingOnChange;
@property (TQ,R,N) tabBarFocusSpeedBumpEdges;
@property (Tq,R,N) backGestureRecognizerPressType;
@property (TB,N,GisBarHidden,V_barHidden) barHidden;
@property (TB,R,N,V_isBottomBarSuppressedByNavigation) isBottomBarSuppressedByNavigation;
@property (TB,R,N) isTabBarEffectivelyHidden;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITabBarControllerVisualStyle tabContentDidChange:];
-[_UITabBarControllerVisualStyle observeContentScrollView:];
-[_UITabBarControllerVisualStyle supportsFocusGestures];
-[_UITabBarControllerVisualStyle defaultMaxItems];
-[_UITabBarControllerVisualStyle tabBarPosition];
-[_UITabBarControllerVisualStyle updateBottomAccessoryAnimated:];
-[_UITabBarControllerVisualStyle supportsShowingMoreItem];
-[_UITabBarControllerVisualStyle bottomAccessoryInsets];
-[_UITabBarControllerVisualStyle contentLayoutGuideFrame];
-[_UITabBarControllerVisualStyle updateViewControllers:];
-[_UITabBarControllerVisualStyle tabBarView];
-[_UITabBarControllerVisualStyle loadViews];
-[_UITabBarControllerVisualStyle updateViewControllerForReselection:];
-[_UITabBarControllerVisualStyle willUpdateViewControllers];
-[_UITabBarControllerVisualStyle defaultAnimatorForFromViewController:toViewController:];
-[_UITabBarControllerVisualStyle tabBarDidChange];
-[_UITabBarControllerVisualStyle preferredSidebarModeDidChange];
-[_UITabBarControllerVisualStyle resolvedPopoverPresentationControllerSourceItemForTab:];
-[_UITabBarControllerVisualStyle ignoresDefaultTabBarVisibilityAnimation];
-[_UITabBarControllerVisualStyle canDisplaySidebar];
-[_UITabBarControllerVisualStyle viewWillDisappear:];
-[_UITabBarControllerVisualStyle updateTabBarLayout];
-[_UITabBarControllerVisualStyle didUpdateFocusInContext:withAnimationCoordinator:];
-[_UITabBarControllerVisualStyle preferredTrailingStatusBarStyle];
-[_UITabBarControllerVisualStyle wantsDefaultTabBar];
-[_UITabBarControllerVisualStyle preferredCenterStatusBarStyle];
-[_UITabBarControllerVisualStyle edgeInsetsForChildViewController:];
-[_UITabBarControllerVisualStyle viewDidLoad];
-[_UITabBarControllerVisualStyle tabBarPresentationPreferenceDidChange];
-[_UITabBarControllerVisualStyle editingStateDidChange];
-[_UITabBarControllerVisualStyle sheetPresentationDetentProgressDidChange:];
-[_UITabBarControllerVisualStyle adjustedTransitionViewFrame:];
-[_UITabBarControllerVisualStyle canDisplayUITabBar];
-[_UITabBarControllerVisualStyle canToggleSidebar];
-[_UITabBarControllerVisualStyle navigationControllerDidUpdate:];
-[_UITabBarControllerVisualStyle tabBarController];
-[_UITabBarControllerVisualStyle viewWillAppear:];
-[_UITabBarControllerVisualStyle setBottomBarSuppressedByNavigation:animated:];
-[_UITabBarControllerVisualStyle viewDidAppear:];
-[_UITabBarControllerVisualStyle gestureRecognizerShouldBegin:];
-[_UITabBarControllerVisualStyle overrideUISplitViewControllerToCompact];
-[_UITabBarControllerVisualStyle adjustedTabBarFrame:];
-[_UITabBarControllerVisualStyle splitViewControllerDidUpdate:];
-[_UITabBarControllerVisualStyle prepare];
-[_UITabBarControllerVisualStyle gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UITabBarControllerVisualStyle updateGestureRecognizers];
-[_UITabBarControllerVisualStyle sidebarLayoutDidChange];
-[_UITabBarControllerVisualStyle canDisplayTabBar];
-[_UITabBarControllerVisualStyle viewDidDisappear:];
-[_UITabBarControllerVisualStyle updateConstraints];
-[_UITabBarControllerVisualStyle _tabCustomizationProxy];
-[_UITabBarControllerVisualStyle wantsScrollPocketForTabBar];
-[_UITabBarControllerVisualStyle shouldSuppressPresses:withEvent:];
-[_UITabBarControllerVisualStyle setBarHidden:animated:];
-[_UITabBarControllerVisualStyle initWithTabBarController:];
-[_UITabBarControllerVisualStyle preferredTrafficLightStyle];
-[_UITabBarControllerVisualStyle updateFocusForSelectedViewControllerChange];
-[_UITabBarControllerVisualStyle sheetPresentationBarDetentValueForContext:];
-[_UITabBarControllerVisualStyle preferredLeadingStatusBarStyle];
-[_UITabBarControllerVisualStyle updatesTabBarFocusHeadingOnChange];
-[_UITabBarControllerVisualStyle traitOverridesForChildViewController:];
-[_UITabBarControllerVisualStyle teardown];
-[_UITabBarControllerVisualStyle selectedViewControllerDidChange];
-[_UITabBarControllerVisualStyle sidebarVisibilityDidChangeWithAnimator:];
-[_UITabBarControllerVisualStyle childViewControllerForStatusBarStyle];
-[_UITabBarControllerVisualStyle shouldEnforceChildSelectionInGroupTabs];
-[_UITabBarControllerVisualStyle _accessibilityLongPressChanged:];
-[_UITabBarControllerVisualStyle _installScrollPocketInteractionIfNeeded];
-[_UITabBarControllerVisualStyle _performBackGesture:];
-[_UITabBarControllerVisualStyle _performSelectGesture:];
-[_UITabBarControllerVisualStyle _updateAccessibilityGestureEnableState];
-[_UITabBarControllerVisualStyle additionalContentMargins];
-[_UITabBarControllerVisualStyle adjustTabBarForContentScrollView:];
-[_UITabBarControllerVisualStyle adjustedContentViewFrame:viewController:];
-[_UITabBarControllerVisualStyle backGestureRecognizerPressType];
-[_UITabBarControllerVisualStyle configureTransitionView:];
-[_UITabBarControllerVisualStyle isBarHidden];
-[_UITabBarControllerVisualStyle isBottomBarSuppressedByNavigation];
-[_UITabBarControllerVisualStyle isDisplayingSidebar];
-[_UITabBarControllerVisualStyle isScrollViewObservationInCompatibilityMode];
-[_UITabBarControllerVisualStyle isTabBarEffectivelyHidden];
-[_UITabBarControllerVisualStyle occlusionStateMayHaveChanged];
-[_UITabBarControllerVisualStyle overlayInsetsAdjustment];
-[_UITabBarControllerVisualStyle performWithoutNotifyingTabBarController:];
-[_UITabBarControllerVisualStyle prefersTabBarFocusedOnViewDidLoad];
-[_UITabBarControllerVisualStyle removeTabBarFocusedOnViewDidDisappear];
-[_UITabBarControllerVisualStyle sendSelectionEventsForControl:];
-[_UITabBarControllerVisualStyle setBarHidden:];
-[_UITabBarControllerVisualStyle shouldForgetRememberedFocusItemForSelectedViewController:context:];
-[_UITabBarControllerVisualStyle shouldTrackContentScrollView:viewController:tabBarBackgroundRequired:];
-[_UITabBarControllerVisualStyle sidebarVisibilityDidChange];
-[_UITabBarControllerVisualStyle suppressesEditingUI];
-[_UITabBarControllerVisualStyle tabBarFocusSpeedBumpEdges];
-[_UITabBarControllerVisualStyle transitionFromViewController:toViewController:animated:completion:];
-[_UITabBarControllerVisualStyle updateTabForChildViewController:];
-[_UITabBarControllerVisualStyle viewControllerForObservableScrollViewFromViewController:];
```
