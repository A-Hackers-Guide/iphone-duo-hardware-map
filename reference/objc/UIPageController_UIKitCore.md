# `UIPageController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- 10 instance variables, 7 properties, 75 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _viewControllers;
[3@"UIView"] _wrapperViews;
[3i] _notificationState;
@"UIScrollView" _scrollView;
@"UIPageControl" _pageControl;
@"<UIPageControllerDelegate>" _delegate;
i _pageSpacing;
q _visibleIndex;
q _pageCount;
{?="delegateViewControllerAtIndex"b1"delegateWillBeginPaging"b1"delegateDidEndPaging"b1"displaysPageControl"b1"wraps"b1} _pageControllerFlags;
```

## Properties

```
@property (T@"<UIPageControllerDelegate>",N,V_delegate) delegate;
@property (Td,N) pageSpacing;
@property (TB,N) displaysPageControl;
@property (T@"UIViewController",R,&,N) visibleViewController;
@property (Tq,N) pageCount;
@property (Tq,N) visibleIndex;
@property (TB,N) wraps;
```

## Instance methods

```
-[UIPageController willRotateToInterfaceOrientation:duration:];
-[UIPageController _scrollView];
-[UIPageController willAnimateRotationToInterfaceOrientation:duration:];
-[UIPageController didRotateFromInterfaceOrientation:];
-[UIPageController pageCount];
-[UIPageController shouldAutorotateToInterfaceOrientation:];
-[UIPageController viewWillDisappear:];
-[UIPageController dealloc];
-[UIPageController viewWillAppear:];
-[UIPageController setDelegate:];
-[UIPageController viewDidAppear:];
-[UIPageController setPageCount:];
-[UIPageController loadView];
-[UIPageController delegate];
-[UIPageController viewDidDisappear:];
-[UIPageController visibleViewController];
-[UIPageController viewDidUnload];
-[UIPageController _getRotationContentSettings:];
-[UIPageController _needToLoadNext];
-[UIPageController setPageSpacing:];
-[UIPageController _adjustScrollViewContentInsets];
-[UIPageController _allowsAutorotation];
-[UIPageController _createPageControl];
-[UIPageController _doesVisibleViewControllerSupportInterfaceOrientation:];
-[UIPageController _hasNextViewController];
-[UIPageController _hasPreviousViewController];
-[UIPageController _hasVisibleViewController];
-[UIPageController _isSupportedInterfaceOrientation:];
-[UIPageController _isViewControllerBeingUnloaded:atIndex:];
-[UIPageController _loadNextViewController];
-[UIPageController _loadPreviousViewController];
-[UIPageController _loadVisibleViewControllerAndNotify:];
-[UIPageController _needToLoadPrevious];
-[UIPageController _needToLoadVisible];
-[UIPageController _nextViewController];
-[UIPageController _nextViewControllerNotificationState];
-[UIPageController _notifyNextViewController:animated:];
-[UIPageController _notifyPreviousViewController:animated:];
-[UIPageController _notifyViewController:ofState:previousState:animated:];
-[UIPageController _notifyVisibleViewController:animated:];
-[UIPageController _pageChanged:];
-[UIPageController _pageControllerScrollView];
-[UIPageController _previousViewController];
-[UIPageController _previousViewControllerNotificationState];
-[UIPageController _replaceViewControllerAtIndex:withViewController:];
-[UIPageController _scrollView:boundsDidChangeToSize:];
-[UIPageController _scrollViewDidEndPaging];
-[UIPageController _scrollViewDidScroll:forceUpdate:];
-[UIPageController _scrollViewFrame];
-[UIPageController _scrollViewWillBeginPaging];
-[UIPageController _setNextViewController:];
-[UIPageController _setNextViewControllerNotificationState:];
-[UIPageController _setPreviousViewController:];
-[UIPageController _setPreviousViewControllerNotificationState:];
-[UIPageController _setVisibleViewController:];
-[UIPageController _setVisibleViewControllerNotificationState:];
-[UIPageController _shouldUseOnePartRotation];
-[UIPageController _visibleViewController];
-[UIPageController _visibleViewControllerNotificationState];
-[UIPageController didAnimateFirstHalfOfRotationToInterfaceOrientation:];
-[UIPageController displaysPageControl];
-[UIPageController indexOfViewController:];
-[UIPageController pageSpacing];
-[UIPageController reloadViewControllerAtIndex:];
-[UIPageController rotatingFooterView];
-[UIPageController rotatingHeaderView];
-[UIPageController setDisplaysPageControl:];
-[UIPageController setVisibleIndex:];
-[UIPageController setVisibleIndex:animated:];
-[UIPageController setVisibleIndex:preservingLoadedViewControllers:animated:];
-[UIPageController setWraps:];
-[UIPageController visibleIndex];
-[UIPageController willAnimateFirstHalfOfRotationToInterfaceOrientation:duration:];
-[UIPageController willAnimateSecondHalfOfRotationFromInterfaceOrientation:duration:];
-[UIPageController wraps];
```
