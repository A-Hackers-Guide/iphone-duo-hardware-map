# `UIPageViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `UIGestureRecognizerDelegate`, `_UIQueuingScrollViewDelegate`, `_UIQueuingScrollViewDataSource`, `UIScrollViewDelegate`
- 30 instance variables, 21 properties, 120 instance methods, 7 class methods

## Instance variables

```
@"<UIPageViewControllerDelegate>" _delegate;
@"<UIPageViewControllerDataSource>" _dataSource;
q _transitionStyle;
q _navigationOrientation;
q _spineLocation;
B _doubleSided;
B _pageControlRequiresValidation;
@"NSArray" _viewControllers;
@"_UIPageCurl" _pageCurl;
@"UIPanGestureRecognizer" _panGestureRecognizer;
@"UITapGestureRecognizer" _tapGestureRecognizer;
B _stashingViewControllersForRotation;
@"NSArray" _viewControllersStashedForRotation;
B _interfaceRotating;
@"NSMutableArray" _rotationSnapshotViews;
q _spineLocationPriorToInterfaceRotation;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _tapRegionInsets;
{CGSize="width"d"height"d} _tapRegionBreadths;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _effectiveTapRegionInsets;
{CGSize="width"d"height"d} _effectiveTapRegionBreadths;
^{CGRect={CGPoint=dd}{CGSize=dd}} _tapRegions;
d _pageSpacing;
@"NSMutableDictionary" _cachedViewControllersForCurl;
@"NSHashTable" _cachedViewControllersForScroll;
@"NSDictionary" _incomingAndOutgoingViewControllersForManualTransition;
q _lastKnownNavigationDirection;
q _disableAutorotationCount;
{?="delegateWantsTransitionWillBegin"b1"delegateWantsTransitionCompleted"b1"delegateWantsTransitionsFinished"b1"delegateWantsScrollProgress"b1"delegateCustomizesSpineLocationForInterfaceOrientation"b1"delegateSupportedInterfaceOrientations"b1"delegatePreferredInterfaceOrientationForPresentation"b1"dataSourceSuppliesBeforeViewController"b1"dataSourceSuppliesAfterViewController"b1"dataSourceSuppliesPageCount"b1"dataSourceSuppliesPageNumber"b1} _delegateFlags;
@"<UIPageViewControllerDataSource>" _unsafeUnretainedDataSource;
@"<UIPageViewControllerDelegate>" _unsafeUnretainedDelegate;
```

## Properties

```
@property (Tq,R,N) _transitionStyle;
@property (Tq,R,N) _navigationOrientation;
@property (T@"NSArray",&,N,S_setViewControllers:,V_viewControllers) _viewControllers;
@property (T@"NSArray",&,N,S_setViewControllersStashedForRotation:,V_viewControllersStashedForRotation) _viewControllersStashedForRotation;
@property (TB,R,N,G_isPageControlVisible) _pageControlVisible;
@property (T@"_UIPageViewControllerContentView",R,N) _contentView;
@property (T@"_UIQueuingScrollView",R,N) _scrollView;
@property (Td,N,S_setPageSpacing:) _pageSpacing;
@property (TB,R,N,G_isInterfaceRotating,V_interfaceRotating) _interfaceRotating;
@property (T@"<UIPageViewControllerDelegate>",W,N) delegate;
@property (T@"<UIPageViewControllerDataSource>",W,N) dataSource;
@property (Tq,R,N) transitionStyle;
@property (Tq,R,N) navigationOrientation;
@property (Tq,R,N) spineLocation;
@property (TB,N,GisDoubleSided) doubleSided;
@property (T@"NSArray",R,N) gestureRecognizers;
@property (T@"NSArray",R,N) viewControllers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIPageViewController _incomingViewControllerKeys];
+[UIPageViewController _isNavigationOrientation:supportedForTransitionStyle:];
+[UIPageViewController _isSpineLocation:supportedForTransitionStyle:];
+[UIPageViewController _isSupportedTransitionStyle:];
+[UIPageViewController _outgoingViewControllerKeys];
+[UIPageViewController doesOverridePreferredInterfaceOrientationForPresentation];
+[UIPageViewController stringForSpineLocation:];
```

## Instance methods

```
-[UIPageViewController willRotateToInterfaceOrientation:duration:];
-[UIPageViewController setDoubleSided:];
-[UIPageViewController _scrollView];
-[UIPageViewController willAnimateRotationToInterfaceOrientation:duration:];
-[UIPageViewController didRotateFromInterfaceOrientation:];
-[UIPageViewController gestureRecognizers];
-[UIPageViewController shouldAutorotateToInterfaceOrientation:];
-[UIPageViewController preferredInterfaceOrientationForPresentation];
-[UIPageViewController viewWillDisappear:];
-[UIPageViewController supportedInterfaceOrientations];
-[UIPageViewController dealloc];
-[UIPageViewController _contentView];
-[UIPageViewController setDataSource:];
-[UIPageViewController initWithNibName:bundle:];
-[UIPageViewController viewWillAppear:];
-[UIPageViewController transitionStyle];
-[UIPageViewController setDelegate:];
-[UIPageViewController viewDidAppear:];
-[UIPageViewController dataSource];
-[UIPageViewController _handleTapGesture:];
-[UIPageViewController loadView];
-[UIPageViewController _deepestActionResponder];
-[UIPageViewController encodeWithCoder:];
-[UIPageViewController _shouldPersistViewWhenCoding];
-[UIPageViewController delegate];
-[UIPageViewController viewDidDisappear:];
-[UIPageViewController initWithCoder:];
-[UIPageViewController viewControllers];
-[UIPageViewController _handlePanGesture:];
-[UIPageViewController _gestureRecognizerShouldBegin:];
-[UIPageViewController shouldAutomaticallyForwardRotationMethods];
-[UIPageViewController isDoubleSided];
-[UIPageViewController _edgeInsetsForChildViewController:insetsAreAbsolute:];
-[UIPageViewController preferredFocusedView];
-[UIPageViewController scrollViewDidScroll:];
-[UIPageViewController _hasPreferredInterfaceOrientationForPresentation];
-[UIPageViewController shouldAutomaticallyForwardAppearanceMethods];
-[UIPageViewController _beginDisablingInterfaceAutorotation];
-[UIPageViewController _cacheViewControllerForScroll:];
-[UIPageViewController _canHandleGestures];
-[UIPageViewController _child:beginAppearanceTransition:animated:];
-[UIPageViewController _child:beginAppearanceTransitionIfPossible:animated:];
-[UIPageViewController _child:canBeginAppearanceTransition:];
-[UIPageViewController _child:didRotateFromInterfaceOrientation:];
-[UIPageViewController _child:endAppearanceTransitionIfPossible:];
-[UIPageViewController _child:willAnimateRotationToInterfaceOrientation:duration:];
-[UIPageViewController _child:willRotateToInterfaceOrientation:duration:];
-[UIPageViewController _childCanEndAppearanceTransition:];
-[UIPageViewController _childEndAppearanceTransition:];
-[UIPageViewController _contentSizeForSize:];
-[UIPageViewController _contentViewFrameOrBoundsDidChange];
-[UIPageViewController _disabledScrollingRegion];
-[UIPageViewController _effectiveTapRegionBreadths];
-[UIPageViewController _effectiveTapRegionInsets];
-[UIPageViewController _endDisablingInterfaceAutorotation];
-[UIPageViewController _flushViewController:animated:];
-[UIPageViewController _handlePagingInDirection:animated:completion:];
-[UIPageViewController _incomingViewControllersForGestureDrivenCurlInDirection:];
-[UIPageViewController _invalidateEffectiveTapRegions];
-[UIPageViewController _invalidatePageCurl];
-[UIPageViewController _invalidateViewControllersStashedForCurlFromDataSource];
-[UIPageViewController _isCurrentViewControllerStateValid];
-[UIPageViewController _isInterfaceRotating];
-[UIPageViewController _isPageControlVisible];
-[UIPageViewController _marginInfoForChild:leftMargin:rightMargin:];
-[UIPageViewController _navigationEndDirectionInResponseToPanGestureRecognizer:suggestedVelocity:];
-[UIPageViewController _navigationOrientation];
-[UIPageViewController _pageControl];
-[UIPageViewController _pageControlValueChanged:];
-[UIPageViewController _pageSpacing];
-[UIPageViewController _populateIncomingViewControllersInMap:withViewControllers:forCurlInDirection:];
-[UIPageViewController _populateOutgoingViewControllersInMap:];
-[UIPageViewController _queuingScrollView:viewBefore:view:];
-[UIPageViewController _requestSpineLocationForInterfaceOrientationAndUpdateStashedViewControllers:];
-[UIPageViewController _sendChildViewWill:appear:animated:];
-[UIPageViewController _setDisabledScrollingRegion:];
-[UIPageViewController _setPageSpacing:];
-[UIPageViewController _setSpineLocation:];
-[UIPageViewController _setTapRegionBreadths:];
-[UIPageViewController _setTapRegionInsets:];
-[UIPageViewController _setViewControllers:];
-[UIPageViewController _setViewControllers:withCurlOfType:fromLocation:direction:animated:notifyDelegate:completion:];
-[UIPageViewController _setViewControllers:withScrollInDirection:animated:completion:];
-[UIPageViewController _setViewControllersStashedForRotation:];
-[UIPageViewController _shouldBeginNavigationInDirection:inResponseToPanGestureRecognizer:];
-[UIPageViewController _shouldCompleteManualCurlWithSuggestedVelocity:];
-[UIPageViewController _shouldFlipInRightToLeft];
-[UIPageViewController _shouldGenerateAppearanceCallbacksWhenScrolling];
-[UIPageViewController _shouldNavigateInDirection:inResponseToTapGestureRecognizer:];
-[UIPageViewController _shouldNavigateInDirection:inResponseToVelocity:ofGestureRecognizedByPanGestureRecognizer:];
-[UIPageViewController _tapRegionBreadths];
-[UIPageViewController _tapRegionInsets];
-[UIPageViewController _tapRegions];
-[UIPageViewController _transitionStyle];
-[UIPageViewController _updatePageControlViaDataSourceIfNecessary];
-[UIPageViewController _validRangeForPresentationOfViewControllersWithSpineLocation:];
-[UIPageViewController _validatedViewControllersForPresentationOfViewControllers:validRange:];
-[UIPageViewController _validatedViewControllersForTransitionWithViewControllers:animated:];
-[UIPageViewController _viewControllerAfterViewController:];
-[UIPageViewController _viewControllerBefore:viewController:];
-[UIPageViewController _viewControllerBeforeViewController:];
-[UIPageViewController _viewControllers];
-[UIPageViewController _viewControllersForCurlWithViewControllers:direction:];
-[UIPageViewController _viewControllersForPendingSpineLocation:];
-[UIPageViewController _viewControllersStashedForRotation];
-[UIPageViewController initWithTransitionStyle:navigationOrientation:options:];
-[UIPageViewController navigationOrientation];
-[UIPageViewController queuingScrollView:attemptToPageInDirection:];
-[UIPageViewController queuingScrollView:didBailoutOfScrollAndRevealedView:];
-[UIPageViewController queuingScrollView:didCommitManualScroll:toRevealView:concealView:direction:animated:canComplete:];
-[UIPageViewController queuingScrollView:didEndManualScroll:toRevealView:direction:animated:didFinish:didComplete:];
-[UIPageViewController queuingScrollView:didFlushView:animated:];
-[UIPageViewController queuingScrollView:viewAfterView:];
-[UIPageViewController queuingScrollView:viewBeforeView:];
-[UIPageViewController queuingScrollView:willManuallyScroll:toRevealView:concealView:animated:];
-[UIPageViewController queuingScrollViewDidFinishScrolling:];
-[UIPageViewController queuingScrollViewShouldLayoutSubviews:];
-[UIPageViewController setViewControllers:direction:animated:completion:];
-[UIPageViewController spineLocation];
-[UIPageViewController viewWillUnload];
```
