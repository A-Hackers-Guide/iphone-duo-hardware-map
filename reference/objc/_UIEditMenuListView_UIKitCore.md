# `_UIEditMenuListView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UICollectionViewDelegate`, `UIGestureRecognizerDelegate`
- 32 instance variables, 31 properties, 85 instance methods, 2 class methods

## Instance variables

```
@"NSString" _backgroundMaterialGroupName;
d _largestPageWidth;
d _verticalContentHeight;
d _additionalWidthFromInteraction;
{CGSize="width"d"height"d} _paginationContainerSize;
{?="pagination"b1} _needsUpdate;
B _shouldHandoffOnLift;
@"<_UIEditMenuListViewDelegate>" _delegate;
q _arrowDirection;
q _axis;
Q _preferredElementDisplayMode;
@"UIView" _titleView;
@"UIMenu" _displayedMenu;
@"UIView" _customBackgroundPlatterView;
@"UIView" _backgroundView;
@"_UIDiffuseShadowView" _shadowView;
@"CAShapeLayer" _maskLayer;
@"UIView" _menuContainerView;
@"_UIEditMenuCollectionView" _collectionView;
@"UIView" _titleContainerView;
@"UIView" _titleSeparatorView;
@"UICollectionViewDiffableDataSource" _dataSource;
@"_UIEditMenuPageButton" _leftButton;
@"_UIEditMenuPageButton" _rightButton;
@"_UIContinuousSelectionGestureRecognizer" _selectionGestureRecognizer;
@"UIHoverGestureRecognizer" _hoverGestureRecognizer;
@"UIPanGestureRecognizer" _panGestureRecognizer;
@"UIImpactFeedbackGenerator" _feedbackGenerator;
d _lastFeedbackTime;
@"NSIndexPath" _highlightedIndexPath;
@"NSIndexPath" _hoveredIndexPath;
@"NSIndexPath" _scrubbedIndexPath;
```

## Properties

```
@property (T@"UIView",R,N,V_customBackgroundPlatterView) customBackgroundPlatterView;
@property (T@"UIView",R,N,V_backgroundView) backgroundView;
@property (T@"_UIDiffuseShadowView",R,N,V_shadowView) shadowView;
@property (T@"CAShapeLayer",R,N,V_maskLayer) maskLayer;
@property (T@"UIView",R,N,V_menuContainerView) menuContainerView;
@property (T@"_UIEditMenuCollectionView",R,N,V_collectionView) collectionView;
@property (T@"UIView",R,N,V_titleContainerView) titleContainerView;
@property (T@"UIView",R,N,V_titleSeparatorView) titleSeparatorView;
@property (T@"UICollectionViewDiffableDataSource",R,N,V_dataSource) dataSource;
@property (T@"_UIEditMenuPageButton",R,N,V_leftButton) leftButton;
@property (T@"_UIEditMenuPageButton",R,N,V_rightButton) rightButton;
@property (T@"_UIContinuousSelectionGestureRecognizer",R,N,V_selectionGestureRecognizer) selectionGestureRecognizer;
@property (T@"UIHoverGestureRecognizer",R,N,V_hoverGestureRecognizer) hoverGestureRecognizer;
@property (T@"UIPanGestureRecognizer",R,N,V_panGestureRecognizer) panGestureRecognizer;
@property (TB,R,N,V_shouldHandoffOnLift) shouldHandoffOnLift;
@property (T@"UIImpactFeedbackGenerator",R,N,V_feedbackGenerator) feedbackGenerator;
@property (Td,R,N,V_lastFeedbackTime) lastFeedbackTime;
@property (TB,R,N) scrubbingEnabled;
@property (T@"NSIndexPath",&,N,V_highlightedIndexPath) highlightedIndexPath;
@property (T@"NSIndexPath",&,N,V_hoveredIndexPath) hoveredIndexPath;
@property (T@"NSIndexPath",&,N,V_scrubbedIndexPath) scrubbedIndexPath;
@property (T@"<_UIEditMenuListViewDelegate>",R,W,N,V_delegate) delegate;
@property (Tq,N,V_arrowDirection) arrowDirection;
@property (Tq,N,V_axis) axis;
@property (TQ,N,V_preferredElementDisplayMode) preferredElementDisplayMode;
@property (T@"UIView",R,N,V_titleView) titleView;
@property (T@"UIMenu",R,N,V_displayedMenu) displayedMenu;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[_UIEditMenuListView _resolvedCornerRadiusForRect:userInterfaceIdiom:axis:];
+[_UIEditMenuListView minimumRequiredWidthForArrowInRoundedListViewForAxis:traitCollection:];
```

## Instance methods

```
-[_UIEditMenuListView panGestureRecognizer];
-[_UIEditMenuListView hasShadow];
-[_UIEditMenuListView maskLayer];
-[_UIEditMenuListView feedbackGenerator];
-[_UIEditMenuListView leftButton];
-[_UIEditMenuListView axis];
-[_UIEditMenuListView _updateArrowEdgeInsets];
-[_UIEditMenuListView hoveredIndexPath];
-[_UIEditMenuListView _effectivePaginationContainerSize];
-[_UIEditMenuListView setAxis:];
-[_UIEditMenuListView scrubbedIndexPath];
-[_UIEditMenuListView gestureRecognizer:shouldReceiveTouch:];
-[_UIEditMenuListView _titleViewSizeForFittingWidth:];
-[_UIEditMenuListView effectiveBackgroundView];
-[_UIEditMenuListView setScrubbingEnabled:];
-[_UIEditMenuListView lastFeedbackTime];
-[_UIEditMenuListView setArrowDirection:];
-[_UIEditMenuListView collectionView:willDisplayCell:forItemAtIndexPath:];
-[_UIEditMenuListView selectionGestureRecognizer];
-[_UIEditMenuListView backgroundMaterialGroupName];
-[_UIEditMenuListView scrubbingEnabled];
-[_UIEditMenuListView _updateHighlightState];
-[_UIEditMenuListView _performHandoffFromSourceView:];
-[_UIEditMenuListView rightButton];
-[_UIEditMenuListView _indexPathForGestureRecognizer:];
-[_UIEditMenuListView _didTapRightDirectionalButton:];
-[_UIEditMenuListView displayedMenu];
-[_UIEditMenuListView _updatePaginationForSnapshot:containerSize:];
-[_UIEditMenuListView preferredElementDisplayMode];
-[_UIEditMenuListView initWithDelegate:menu:titleView:preferredElementDisplayMode:];
-[_UIEditMenuListView collectionView];
-[_UIEditMenuListView _didTapLeftDirectionalButton:];
-[_UIEditMenuListView _didTapHandoffButton:];
-[_UIEditMenuListView collectionViewLayout];
-[_UIEditMenuListView _contentSizeCategoryDidChange];
-[_UIEditMenuListView titleSeparatorView];
-[_UIEditMenuListView layoutSubviews];
-[_UIEditMenuListView hitTest:withEvent:];
-[_UIEditMenuListView _createViewHierarchy];
-[_UIEditMenuListView _hasDisplayedMenu];
-[_UIEditMenuListView titleContainerView];
-[_UIEditMenuListView _prefersZoomTransitionsForPopoverPresentations];
-[_UIEditMenuListView _isPaginationDirtyForContainerSize:];
-[_UIEditMenuListView intrinsicContentSizeForContainer:containerSize:];
-[_UIEditMenuListView _setNeedsPaginationUpdate];
-[_UIEditMenuListView setBounds:];
-[_UIEditMenuListView _reloadMenuAnimated:];
-[_UIEditMenuListView _intrinsicHorizontalContentSizeForTraitCollection:containerSize:];
-[_UIEditMenuListView _collectionViewWidthForPageProgress:];
-[_UIEditMenuListView shouldHandoffOnLift];
-[_UIEditMenuListView scrollViewWillEndDragging:withVelocity:targetContentOffset:];
-[_UIEditMenuListView gestureRecognizerShouldBegin:];
-[_UIEditMenuListView dataSource];
-[_UIEditMenuListView _resolvedCornerRadiusForRect:];
-[_UIEditMenuListView _createDataSource];
-[_UIEditMenuListView _canSelectItemAtIndexPath:];
-[_UIEditMenuListView arrowSizeForDirection:];
-[_UIEditMenuListView _verticalMenuContentSizeFittingContainerSize:traits:];
-[_UIEditMenuListView shadowView];
-[_UIEditMenuListView _highlightItemAtIndexPath:];
-[_UIEditMenuListView _handleSelectionGesture:];
-[_UIEditMenuListView gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UIEditMenuListView delegate];
-[_UIEditMenuListView backgroundView];
-[_UIEditMenuListView menuContainerView];
-[_UIEditMenuListView _handleHoverGesture:];
-[_UIEditMenuListView _intrinsicVerticalContentSizeForContainer:containerSize:];
-[_UIEditMenuListView arrowDirection];
-[_UIEditMenuListView _playFeedbackForHandoff];
-[_UIEditMenuListView titleView];
-[_UIEditMenuListView customBackgroundPlatterView];
-[_UIEditMenuListView hoverGestureRecognizer];
-[_UIEditMenuListView _handlePanGesture:];
-[_UIEditMenuListView setPreferredElementDisplayMode:];
-[_UIEditMenuListView _selectItemAtIndexPath:];
-[_UIEditMenuListView _hasPasteAuthentication];
-[_UIEditMenuListView setHoveredIndexPath:];
-[_UIEditMenuListView _minimumRequiredWidthForArrowInRoundedListViewForAxis:];
-[_UIEditMenuListView scrollViewDidScroll:];
-[_UIEditMenuListView _updateMaskingLayerWithFrame:];
-[_UIEditMenuListView setScrubbedIndexPath:];
-[_UIEditMenuListView _unhighlightCurrentlyHighlightedItem];
-[_UIEditMenuListView highlightedIndexPath];
-[_UIEditMenuListView reloadWithMenu:titleView:animated:];
-[_UIEditMenuListView setHighlightedIndexPath:];
```
