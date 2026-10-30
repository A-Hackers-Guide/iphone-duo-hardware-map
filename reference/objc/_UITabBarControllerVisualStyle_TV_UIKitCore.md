# `_UITabBarControllerVisualStyle_TV`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UITabBarControllerVisualStyle`
- Protocols: `_UITVScrollViewManagerDelegate`, `UIGestureRecognizerDelegate`
- 6 instance variables, 4 properties, 39 instance methods, 0 class methods

## Instance variables

```
@"UIView" _tabBarContainerView;
@"UIFocusContainerGuide" _contentFocusContainerGuide;
@"UIFocusGuide" _tabBarOffscreenFocusGuide;
@"UIGestureRecognizer" _touchDetectionGestureRecognizer;
@"_UITVScrollViewManager" _scrollViewManager;
{?="hidNavigationBar"b1} _flags;
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
-[_UITabBarControllerVisualStyle_TV tabContentDidChange:];
-[_UITabBarControllerVisualStyle_TV supportsFocusGestures];
-[_UITabBarControllerVisualStyle_TV defaultMaxItems];
-[_UITabBarControllerVisualStyle_TV tabBarPosition];
-[_UITabBarControllerVisualStyle_TV supportsShowingMoreItem];
-[_UITabBarControllerVisualStyle_TV updateViewControllers:];
-[_UITabBarControllerVisualStyle_TV tabBarView];
-[_UITabBarControllerVisualStyle_TV loadViews];
-[_UITabBarControllerVisualStyle_TV updateViewControllerForReselection:];
-[_UITabBarControllerVisualStyle_TV defaultAnimatorForFromViewController:toViewController:];
-[_UITabBarControllerVisualStyle_TV viewWillDisappear:];
-[_UITabBarControllerVisualStyle_TV updateTabBarLayout];
-[_UITabBarControllerVisualStyle_TV didUpdateFocusInContext:withAnimationCoordinator:];
-[_UITabBarControllerVisualStyle_TV edgeInsetsForChildViewController:];
-[_UITabBarControllerVisualStyle_TV viewDidLoad];
-[_UITabBarControllerVisualStyle_TV viewWillAppear:];
-[_UITabBarControllerVisualStyle_TV adjustedTabBarFrame:];
-[_UITabBarControllerVisualStyle_TV gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UITabBarControllerVisualStyle_TV updateGestureRecognizers];
-[_UITabBarControllerVisualStyle_TV updateFocusForSelectedViewControllerChange];
-[_UITabBarControllerVisualStyle_TV teardown];
-[_UITabBarControllerVisualStyle_TV _childViewControllerModernBarTopInset];
-[_UITabBarControllerVisualStyle_TV _isModernBar];
-[_UITabBarControllerVisualStyle_TV _performTouchDetectionGesture:];
-[_UITabBarControllerVisualStyle_TV _scrollViewManagerDidFinishScrolling:];
-[_UITabBarControllerVisualStyle_TV _shouldAdjustContentViewFrameForOffscreenFocus:adjustedTabBarFrame:];
-[_UITabBarControllerVisualStyle_TV _updateOffscreenState:withFocusAnimationCoordinator:];
-[_UITabBarControllerVisualStyle_TV adjustTabBarForContentScrollView:];
-[_UITabBarControllerVisualStyle_TV adjustedContentViewFrame:viewController:];
-[_UITabBarControllerVisualStyle_TV backGestureRecognizerPressType];
-[_UITabBarControllerVisualStyle_TV isScrollViewObservationInCompatibilityMode];
-[_UITabBarControllerVisualStyle_TV overlayInsetsAdjustment];
-[_UITabBarControllerVisualStyle_TV prefersTabBarFocusedOnViewDidLoad];
-[_UITabBarControllerVisualStyle_TV removeTabBarFocusedOnViewDidDisappear];
-[_UITabBarControllerVisualStyle_TV sendSelectionEventsForControl:];
-[_UITabBarControllerVisualStyle_TV shouldForgetRememberedFocusItemForSelectedViewController:context:];
-[_UITabBarControllerVisualStyle_TV shouldTrackContentScrollView:viewController:tabBarBackgroundRequired:];
-[_UITabBarControllerVisualStyle_TV tabBarFocusSpeedBumpEdges];
-[_UITabBarControllerVisualStyle_TV viewControllerForObservableScrollViewFromViewController:];
```
