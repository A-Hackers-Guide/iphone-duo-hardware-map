# `UICollectionViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIViewController`
- Protocols: `_UIKeyboardAutoRespondingScrollViewController`, `UIGestureRecognizerDelegate`, `UICollectionViewFocusDelegate_Legacy`, `UIViewControllerPreviewingDelegate`, `UIViewControllerPreviewingDelegate_Deprecated`, `UICollectionViewDelegate`, `UICollectionViewDataSource`
- 5 instance variables, 10 properties, 56 instance methods, 0 class methods

## Instance variables

```
@"UICollectionViewLayout" _layout;
@"UICollectionView" _collectionView;
@"UILongPressGestureRecognizer" _reorderingGesture;
@"UIAutoRespondingScrollViewControllerKeyboardSupport" _keyboardSupport;
{?="clearsSelectionOnViewWillAppear"b1"useLayoutToLayoutNavigationTransitions"b1"installsStandardReorderingGesture"b1} _collectionViewControllerFlags;
```

## Properties

```
@property (T@"UICollectionView",&,N) collectionView;
@property (TB,N) clearsSelectionOnViewWillAppear;
@property (TB,N) useLayoutToLayoutNavigationTransitions;
@property (T@"UICollectionViewLayout",R,N) collectionViewLayout;
@property (TB,N) installsStandardGestureForInteractiveMovement;
@property (T@"UIScrollView<_UIKeyboardAutoRespondingScrollView>",R,&,N,G_scrollView) scrollView;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UICollectionViewController _scrollView];
-[UICollectionViewController gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[UICollectionViewController contentScrollViewForEdge:];
-[UICollectionViewController gestureRecognizer:shouldReceiveTouch:];
-[UICollectionViewController collectionView:numberOfItemsInSection:];
-[UICollectionViewController viewWillDisappear:];
-[UICollectionViewController collectionView:cellForItemAtIndexPath:];
-[UICollectionViewController initWithCollectionViewLayout:];
-[UICollectionViewController dealloc];
-[UICollectionViewController collectionView];
-[UICollectionViewController collectionViewLayout];
-[UICollectionViewController setEditing:animated:];
-[UICollectionViewController setView:];
-[UICollectionViewController initWithNibName:bundle:];
-[UICollectionViewController setCollectionView:];
-[UICollectionViewController viewWillAppear:];
-[UICollectionViewController viewDidAppear:];
-[UICollectionViewController gestureRecognizerShouldBegin:];
-[UICollectionViewController collectionView:didBeginMultipleSelectionInteractionAtIndexPath:];
-[UICollectionViewController dataSource];
-[UICollectionViewController loadView];
-[UICollectionViewController encodeWithCoder:];
-[UICollectionViewController shouldCrossFadeBottomBars];
-[UICollectionViewController delegate];
-[UICollectionViewController shouldCrossFadeNavigationBar];
-[UICollectionViewController initWithCoder:];
-[UICollectionViewController willPresentPreviewViewController:forLocation:inSourceView:];
-[UICollectionViewController preferredFocusedView];
-[UICollectionViewController clearsSelectionOnViewWillAppear];
-[UICollectionViewController __viewDidAppear:];
-[UICollectionViewController __viewWillAppear:];
-[UICollectionViewController _animatorForOperation:fromViewController:toViewController:];
-[UICollectionViewController _clearSharedView];
-[UICollectionViewController _handleReorderingGesture:];
-[UICollectionViewController _installReorderingGestureIfNecessary];
-[UICollectionViewController _newCollectionViewWithFrame:collectionViewLayout:];
-[UICollectionViewController _setNeedsUpdateContentUnavailableConfiguration];
-[UICollectionViewController _setSharedCollectionView:];
-[UICollectionViewController _setUseLayoutToLayoutNavigationTransitions:withCheck:];
-[UICollectionViewController _shim_contentScrollView];
-[UICollectionViewController _shouldRespondToPreviewingMethods];
-[UICollectionViewController _uiCollectionView];
-[UICollectionViewController _updateCollectionViewLayoutAndDelegate:];
-[UICollectionViewController _wrappingView];
-[UICollectionViewController installsStandardGestureForInteractiveMovement];
-[UICollectionViewController previewViewControllerForItemAtIndexPath:];
-[UICollectionViewController previewViewControllerForLocation:inSourceView:];
-[UICollectionViewController previewingContext:commitViewController:];
-[UICollectionViewController previewingContext:viewControllerForLocation:];
-[UICollectionViewController setClearsSelectionOnViewWillAppear:];
-[UICollectionViewController setInstallsStandardGestureForInteractiveMovement:];
-[UICollectionViewController setUseLayoutToLayoutNavigationTransitions:];
-[UICollectionViewController useLayoutToLayoutNavigationTransitions];
-[UICollectionViewController viewWillUnload];
-[UICollectionViewController willPresentPreviewViewController:forItemAtIndexPath:];
-[UICollectionViewController willPresentPreviewViewController:forPosition:inSourceView:];
```
