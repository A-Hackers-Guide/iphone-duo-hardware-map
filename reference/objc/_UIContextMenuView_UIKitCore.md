# `_UIContextMenuView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIGestureRecognizerDelegate`
- 35 instance variables, 41 properties, 119 instance methods, 0 class methods

## Instance variables

```
B _showsShadow;
B _reversesActionOrder;
B _scrubbingEnabled;
B _allowsBackgroundViewInteraction;
B _prefersVisibleImages;
B _shouldEnableTypeSelect;
B _isComputingPreferredSize;
B _retainHighlightOnMenuNavigation;
B _shouldAvoidInputViews;
B _hasTrackingTouch;
B _wantsFocusDeferralIfSupported;
@"<_UIContextMenuViewDelegate>" _delegate;
d _maximumMenuHeight;
Q _hierarchyStyle;
Q _attachmentEdge;
@"<_UIViewMaterial>" _preferredMenuMaterial;
q _itemSelectionHighlightStyle;
@"_UIContextMenuNode" _departingNode;
@"UICollectionViewDiffableDataSource" _collectionViewDataSource;
@"_UIContinuousSelectionGestureRecognizer" _selectionGestureRecognizer;
@"_UIContextMenuSelectionDelayGestureRecognizer" _selectionDelayGestureRecognizer;
@"NSDate" _appearanceDate;
@"UIHoverGestureRecognizer" _highlightHoverGestureRecognizer;
@"UISelectionFeedbackGenerator" _feedbackGenerator;
@"_UIContextMenuLinkedList" _submenus;
@"NSTimer" _autoNavigationTimer;
@"NSTimer" _autoUnhighlightTimer;
@"NSIndexPath" _unselectableIndexPath;
@"<_UIContextMenuHierarchyLayout>" _layout;
@"_UIContextMenuNode" _hoveredNode;
@"_UIVelocityIntegrator" _hoverVelocityIntegrator;
@"NSTimer" _hoverAutoExitTimer;
d _preferredScrollTruncationDetent;
{CGSize="width"d"height"d} _visibleContentSize;
{CGSize="width"d"height"d} _maxContainerSize;
```

## Properties

```
@property (T@"_UIContextMenuListView",R,N) currentListView;
@property (T@"_UIContextMenuNode",&,N,V_departingNode) departingNode;
@property (T@"UICollectionViewDiffableDataSource",&,N,V_collectionViewDataSource) collectionViewDataSource;
@property (T@"_UIContinuousSelectionGestureRecognizer",&,N,V_selectionGestureRecognizer) selectionGestureRecognizer;
@property (T@"_UIContextMenuSelectionDelayGestureRecognizer",&,N,V_selectionDelayGestureRecognizer) selectionDelayGestureRecognizer;
@property (T@"NSDate",&,N,V_appearanceDate) appearanceDate;
@property (T@"UIHoverGestureRecognizer",&,N,V_highlightHoverGestureRecognizer) highlightHoverGestureRecognizer;
@property (T@"UISelectionFeedbackGenerator",&,N,V_feedbackGenerator) feedbackGenerator;
@property (T@"_UIContextMenuLinkedList",&,N,V_submenus) submenus;
@property (TB,N,V_isComputingPreferredSize) isComputingPreferredSize;
@property (TB,N,V_retainHighlightOnMenuNavigation) retainHighlightOnMenuNavigation;
@property (TB,N,V_shouldAvoidInputViews) shouldAvoidInputViews;
@property (T@"NSTimer",&,N,V_autoNavigationTimer) autoNavigationTimer;
@property (T@"NSTimer",&,N,V_autoUnhighlightTimer) autoUnhighlightTimer;
@property (T@"NSIndexPath",C,N,V_unselectableIndexPath) unselectableIndexPath;
@property (TB,N,V_hasTrackingTouch) hasTrackingTouch;
@property (T{CGSize=dd},N,V_maxContainerSize) maxContainerSize;
@property (T@"<_UIContextMenuHierarchyLayout>",&,N,V_layout) layout;
@property (T@"_UIContextMenuNode",&,N,V_hoveredNode) hoveredNode;
@property (T@"_UIVelocityIntegrator",&,N,V_hoverVelocityIntegrator) hoverVelocityIntegrator;
@property (T@"NSTimer",&,N,V_hoverAutoExitTimer) hoverAutoExitTimer;
@property (Td,N,V_preferredScrollTruncationDetent) preferredScrollTruncationDetent;
@property (TB,N,V_wantsFocusDeferralIfSupported) wantsFocusDeferralIfSupported;
@property (T@"<_UIContextMenuViewDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_showsShadow) showsShadow;
@property (TB,N,V_reversesActionOrder) reversesActionOrder;
@property (TB,N,V_scrubbingEnabled) scrubbingEnabled;
@property (TB,N,V_allowsBackgroundViewInteraction) allowsBackgroundViewInteraction;
@property (Td,N,V_maximumMenuHeight) maximumMenuHeight;
@property (T{CGSize=dd},N,V_visibleContentSize) visibleContentSize;
@property (TQ,N,V_hierarchyStyle) hierarchyStyle;
@property (TQ,N,V_attachmentEdge) attachmentEdge;
@property (T@"NSArray",R,N) visibleMenus;
@property (T@"<_UIViewMaterial>",&,N,V_preferredMenuMaterial) preferredMenuMaterial;
@property (Tq,N,V_itemSelectionHighlightStyle) itemSelectionHighlightStyle;
@property (TB,N,V_prefersVisibleImages) prefersVisibleImages;
@property (TB,N,V_shouldEnableTypeSelect) shouldEnableTypeSelect;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIContextMenuView setUserInteractionEnabled:];
-[_UIContextMenuView _handleHoverGestureRecognizer:];
-[_UIContextMenuView setFeedbackGenerator:];
-[_UIContextMenuView feedbackGenerator];
-[_UIContextMenuView didMoveToWindow];
-[_UIContextMenuView gestureRecognizer:shouldRequireFailureOfGestureRecognizer:];
-[_UIContextMenuView gestureRecognizer:shouldReceiveTouch:];
-[_UIContextMenuView setScrubbingEnabled:];
-[_UIContextMenuView selectionGestureRecognizer];
-[_UIContextMenuView setPreferredMenuMaterial:];
-[_UIContextMenuView scrubbingEnabled];
-[_UIContextMenuView rootListView];
-[_UIContextMenuView shouldAvoidInputViews];
-[_UIContextMenuView layoutSubviews];
-[_UIContextMenuView selectionDelayGestureRecognizer];
-[_UIContextMenuView hitTest:withEvent:];
-[_UIContextMenuView keyCommands];
-[_UIContextMenuView setItemSelectionHighlightStyle:];
-[_UIContextMenuView setDelegate:];
-[_UIContextMenuView gestureRecognizerShouldBegin:];
-[_UIContextMenuView setMaximumMenuHeight:];
-[_UIContextMenuView _handleSelectionGesture:];
-[_UIContextMenuView gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UIContextMenuView delegate];
-[_UIContextMenuView visibleMenus];
-[_UIContextMenuView preferredFocusEnvironments];
-[_UIContextMenuView layout];
-[_UIContextMenuView maximumMenuHeight];
-[_UIContextMenuView preferredMenuMaterial];
-[_UIContextMenuView canBecomeFirstResponder];
-[_UIContextMenuView initWithFrame:];
-[_UIContextMenuView setShouldAvoidInputViews:];
-[_UIContextMenuView canPerformAction:withSender:];
-[_UIContextMenuView setLayout:];
-[_UIContextMenuView itemSelectionHighlightStyle];
-[_UIContextMenuView hoveredListView];
-[_UIContextMenuView setShowsShadow:];
-[_UIContextMenuView allowsBackgroundViewInteraction];
-[_UIContextMenuView currentListView];
-[_UIContextMenuView highlightHoverGestureRecognizer];
-[_UIContextMenuView preferredScrollTruncationDetent];
-[_UIContextMenuView retainHighlightOnMenuNavigation];
-[_UIContextMenuView setHoveredNode:];
-[_UIContextMenuView _allowsChangingFirstResponderForFocusUpdateWithContext:];
-[_UIContextMenuView _clearAutoNavigationTimer];
-[_UIContextMenuView _clearHoverAutoExitTimer];
-[_UIContextMenuView _displayMenu:inPlaceOfMenu:updateType:alongsideAnimations:];
-[_UIContextMenuView _handleEscapeKey:];
-[_UIContextMenuView _handleLeftArrowKey:];
-[_UIContextMenuView _handleMenuPressGesture:];
-[_UIContextMenuView _handleRightArrowKey:];
-[_UIContextMenuView _handleSelectPressGesture:];
-[_UIContextMenuView _handleSelectionForElement:];
-[_UIContextMenuView _newListViewWithMenu:position:];
-[_UIContextMenuView _performActionForElement:];
-[_UIContextMenuView _rectOfNodeParentElement:];
-[_UIContextMenuView _selectPreviousMenuIfPossible];
-[_UIContextMenuView _setAutoNavigationTimerIfNecessaryForElement:isTrackpadHover:];
-[_UIContextMenuView _setHighlightedIndexPath:playFeedback:atLocation:allowAutoNavigation:];
-[_UIContextMenuView _setHoverAutoExitTimer];
-[_UIContextMenuView _testing_tapAnAction];
-[_UIContextMenuView _touchSupportsAutoNavigation:];
-[_UIContextMenuView _updateSelectionGestureAllowableMovementForGestureBeginningAtIndexPath:];
-[_UIContextMenuView activeSubmenuFrameInCoordinateSpace:];
-[_UIContextMenuView appearanceDate];
-[_UIContextMenuView attachmentEdge];
-[_UIContextMenuView autoNavigationTimer];
-[_UIContextMenuView autoUnhighlightTimer];
-[_UIContextMenuView closestScrollTruncationDetentToHeight:];
-[_UIContextMenuView collectionViewDataSource];
-[_UIContextMenuView departingNode];
-[_UIContextMenuView didCompleteMenuAppearanceAnimation];
-[_UIContextMenuView displayMenu:updateType:alongsideAnimations:];
-[_UIContextMenuView flashScrollIndicators];
-[_UIContextMenuView hasTrackingTouch];
-[_UIContextMenuView hierarchyStyle];
-[_UIContextMenuView hoverAutoExitTimer];
-[_UIContextMenuView hoverVelocityIntegrator];
-[_UIContextMenuView hoveredNode];
-[_UIContextMenuView isComputingPreferredSize];
-[_UIContextMenuView kickstartActionScrubbingWithGesture:];
-[_UIContextMenuView maxContainerSize];
-[_UIContextMenuView preferredContentSizeWithinContainerSize:];
-[_UIContextMenuView prefersVisibleImages];
-[_UIContextMenuView replaceVisibleMenu:withMenu:alongsideAnimations:];
-[_UIContextMenuView resetHighlightStateAndTypeSelect];
-[_UIContextMenuView reversesActionOrder];
-[_UIContextMenuView scrollToFirstSignificantAction];
-[_UIContextMenuView setAllowsBackgroundViewInteraction:];
-[_UIContextMenuView setAppearanceDate:];
-[_UIContextMenuView setAttachmentEdge:];
-[_UIContextMenuView setAutoNavigationTimer:];
-[_UIContextMenuView setAutoUnhighlightTimer:];
-[_UIContextMenuView setCollectionViewDataSource:];
-[_UIContextMenuView setDepartingNode:];
-[_UIContextMenuView setHasTrackingTouch:];
-[_UIContextMenuView setHierarchyStyle:];
-[_UIContextMenuView setHighlightHoverGestureRecognizer:];
-[_UIContextMenuView setHoverAutoExitTimer:];
-[_UIContextMenuView setHoverVelocityIntegrator:];
-[_UIContextMenuView setIsComputingPreferredSize:];
-[_UIContextMenuView setMaxContainerSize:];
-[_UIContextMenuView setPreferredScrollTruncationDetent:];
-[_UIContextMenuView setPrefersVisibleImages:];
-[_UIContextMenuView setRetainHighlightOnMenuNavigation:];
-[_UIContextMenuView setReversesActionOrder:];
-[_UIContextMenuView setSelectionDelayGestureRecognizer:];
-[_UIContextMenuView setSelectionGestureRecognizer:];
-[_UIContextMenuView setShouldEnableTypeSelect:];
-[_UIContextMenuView setSubmenus:];
-[_UIContextMenuView setUnselectableIndexPath:];
-[_UIContextMenuView setVisibleContentSize:];
-[_UIContextMenuView setWantsFocusDeferralIfSupported:];
-[_UIContextMenuView shouldEnableTypeSelect];
-[_UIContextMenuView showsShadow];
-[_UIContextMenuView submenus];
-[_UIContextMenuView unselectableIndexPath];
-[_UIContextMenuView visibleContentSize];
-[_UIContextMenuView wantsFocusDeferralIfSupported];
```
