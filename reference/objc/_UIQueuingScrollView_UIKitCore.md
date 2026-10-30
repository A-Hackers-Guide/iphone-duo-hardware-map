# `_UIQueuingScrollView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIScrollView`
- 12 instance variables, 5 properties, 57 instance methods, 0 class methods

## Instance variables

```
@"<_UIQueuingScrollViewDelegate>" _qDelegate;
@"<_UIQueuingScrollViewDataSource>" _qDataSource;
q _navigationOrientation;
@"NSArray" _views;
@"NSArray" _wrapperViews;
@"UIView" _pendingVisibleView;
d _pageSpacing;
@"NSMutableArray" _viewStateQueue;
@"NSMutableArray" _completionStateQueue;
B _manualScrollInProgress;
{?="delegateInterestedInPendingScrolls"b1"delegateInterestedInCommittedScrolls"b1"delegateInterestedInCompletedScrolls"b1"delegateInterestedInBailedOutScrolls"b1"delegateInterestedFinishedScrolling"b1"delegateCanVetoSubviewLayout"b1"dataSourceSuppliesBeforeView"b1"dataSourceSuppliesAfterView"b1"dataSourceInterestedInFlushedViews"b1} _delegateFlags;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _disabledScrollingRegion;
```

## Properties

```
@property (T@"UIView",R,N) visibleView;
@property (T@"<_UIQueuingScrollViewDelegate>",W,N,V_qDelegate) qDelegate;
@property (T@"<_UIQueuingScrollViewDataSource>",W,N,V_qDataSource) qDataSource;
@property (Td,N,V_pageSpacing) pageSpacing;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_disabledScrollingRegion) disabledScrollingRegion;
```

## Instance methods

```
-[_UIQueuingScrollView _scrollViewAnimationEnded:finished:];
-[_UIQueuingScrollView layoutSubviews];
-[_UIQueuingScrollView setBounds:];
-[_UIQueuingScrollView canBecomeFocused];
-[_UIQueuingScrollView _gestureRecognizer:shouldReceiveTouch:];
-[_UIQueuingScrollView setFrame:];
-[_UIQueuingScrollView setPageSpacing:];
-[_UIQueuingScrollView setQDataSource:];
-[_UIQueuingScrollView _viewAfterView:];
-[_UIQueuingScrollView _abuttedPagingEdges];
-[_UIQueuingScrollView _adjustContentInsets];
-[_UIQueuingScrollView _boundsDidChangeToSize:];
-[_UIQueuingScrollView _cleanUpCompletionState:didFinish:didComplete:];
-[_UIQueuingScrollView _commitGestureDrivenScrollRevealingView:concealingView:inDirection:canComplete:];
-[_UIQueuingScrollView _dataSourceProvidesViews];
-[_UIQueuingScrollView _dequeueViewForIndex:];
-[_UIQueuingScrollView _didEndDraggingManualScroll];
-[_UIQueuingScrollView _didEndManualScroll];
-[_UIQueuingScrollView _didEndProgrammaticScroll];
-[_UIQueuingScrollView _didEndScroll:];
-[_UIQueuingScrollView _didScrollWithAnimation:force:];
-[_UIQueuingScrollView _enqueueAnimatedScrollInDirection:withView:completion:];
-[_UIQueuingScrollView _enqueueCompletionState:];
-[_UIQueuingScrollView _flushView:animated:];
-[_UIQueuingScrollView _handleDirectionalPageWithHorizontalVelocity:verticalVelocity:];
-[_UIQueuingScrollView _invalidateOffscreenViews];
-[_UIQueuingScrollView _isDeceleratingInOppositionToNavigationDirection:];
-[_UIQueuingScrollView _isScrollInProgress:];
-[_UIQueuingScrollView _navigationDirectionForActiveScroll:];
-[_UIQueuingScrollView _navigationDirectionFromCurrentOffset];
-[_UIQueuingScrollView _notifyDelegateDidBailoutOfScrollAndRevealedView:];
-[_UIQueuingScrollView _notifyDelegateDidCommitManualScroll:toRevealView:concealView:direction:animated:canComplete:];
-[_UIQueuingScrollView _notifyDelegateDidEndManualScroll:toRevealView:direction:animated:didFinish:didComplete:];
-[_UIQueuingScrollView _notifyDelegateDidFinishScrolling];
-[_UIQueuingScrollView _notifyDelegateWillManuallyScroll:toRevealView:concealingView:animated:];
-[_UIQueuingScrollView _replaceViews:updatingContents:adjustContentInsets:animated:];
-[_UIQueuingScrollView _requestViewForIndex:];
-[_UIQueuingScrollView _scrollViewDidEndDecelerating];
-[_UIQueuingScrollView _scrollViewDidEndDraggingWithDeceleration:];
-[_UIQueuingScrollView _setFrameAndApplyPageSpacing:];
-[_UIQueuingScrollView _setWrappedViewAtIndex:withView:];
-[_UIQueuingScrollView _viewAtIndex:loadingIfNecessary:updatingContents:animated:];
-[_UIQueuingScrollView _viewBefore:view:];
-[_UIQueuingScrollView _viewBeforeView:];
-[_UIQueuingScrollView _visibleView];
-[_UIQueuingScrollView disabledScrollingRegion];
-[_UIQueuingScrollView initWithFrame:navigationOrientation:];
-[_UIQueuingScrollView isManualScrollInProgress];
-[_UIQueuingScrollView isPreviousScrollCompatibleWithScrollInDirection:];
-[_UIQueuingScrollView pageSpacing];
-[_UIQueuingScrollView qDataSource];
-[_UIQueuingScrollView qDelegate];
-[_UIQueuingScrollView scrollRectToVisible:animated:];
-[_UIQueuingScrollView setDisabledScrollingRegion:];
-[_UIQueuingScrollView setQDelegate:];
-[_UIQueuingScrollView setView:direction:animated:completion:];
-[_UIQueuingScrollView visibleView];
```
