# `UIMoreNavigationController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UINavigationController`
- 3 instance variables, 5 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"UIMoreListController" _moreListController;
@"UINavigationController" _originalNavigationController;
@"UIViewController" _originalRootViewController;
```

## Properties

```
@property (T@"UIViewController",R,N,V_moreListController) moreListController;
@property (T@"NSArray",&,N) moreViewControllers;
@property (TB,N) allowsCustomizing;
@property (T@"UIViewController",N) displayedViewController;
@property (TB,N) moreViewControllersChanged;
```

## Class methods

```
+[UIMoreNavigationController _moreListControllerClass];
```

## Instance methods

```
-[UIMoreNavigationController init];
-[UIMoreNavigationController viewDidMoveToWindow:shouldAppearOrDisappear:];
-[UIMoreNavigationController pushViewController:animated:];
-[UIMoreNavigationController didShowViewController:animated:];
-[UIMoreNavigationController _ensureChildrenHaveParentViewController];
-[UIMoreNavigationController _preparedViewController:];
-[UIMoreNavigationController _redisplayMoreTableView];
-[UIMoreNavigationController _resolvedTab];
-[UIMoreNavigationController _restoreOriginalNavigationController];
-[UIMoreNavigationController _stateRestorationParentForChildViewController:index:];
-[UIMoreNavigationController _willChangeToIdiom:onScreen:];
-[UIMoreNavigationController allowsCustomizing];
-[UIMoreNavigationController displayedViewController];
-[UIMoreNavigationController moreListController];
-[UIMoreNavigationController moreViewControllers];
-[UIMoreNavigationController moreViewControllersChanged];
-[UIMoreNavigationController restoreOriginalNavigationControllerIfNecessary:];
-[UIMoreNavigationController setAllowsCustomizing:];
-[UIMoreNavigationController setDisplayedViewController:];
-[UIMoreNavigationController setMoreViewControllers:];
-[UIMoreNavigationController setMoreViewControllersChanged:];
```
