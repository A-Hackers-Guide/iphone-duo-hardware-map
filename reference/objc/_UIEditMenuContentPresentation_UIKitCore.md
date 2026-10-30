# `_UIEditMenuContentPresentation`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIEditMenuPresentation`
- Protocols: `_UIEditMenuListViewDelegate`, `_UIGeometryChangeObserver`
- 6 instance variables, 7 properties, 41 instance methods, 0 class methods

## Instance variables

```
B _observingSourceView;
q _userInterfaceStyle;
@"_UIEditMenuListView" _currentListView;
@"_UIEditMenuListView" _dismissingListView;
@"_UIEditMenuPresentationLayout" _currentMenuLayout;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _targetRectInSourceView;
```

## Properties

```
@property (T@"_UIEditMenuListView",R,N,V_currentListView) currentListView;
@property (T@"_UIEditMenuListView",R,N,V_dismissingListView) dismissingListView;
@property (T@"_UIEditMenuPresentationLayout",&,N,V_currentMenuLayout) currentMenuLayout;
@property (T@"_UIEditMenuContainerView",&,D,N) containerView;
@property (TB,R,N,V_observingSourceView) observingSourceView;
@property (Tq,N,V_userInterfaceStyle) userInterfaceStyle;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_targetRectInSourceView) targetRectInSourceView;
```

## Instance methods

```
-[_UIEditMenuContentPresentation canPresentEditMenu];
-[_UIEditMenuContentPresentation didTransitionFrom:to:];
-[_UIEditMenuContentPresentation _currentPlatformMetrics];
-[_UIEditMenuContentPresentation menuFrameInCoordinateSpace:];
-[_UIEditMenuContentPresentation _geometryChanged:forAncestor:];
-[_UIEditMenuContentPresentation userInterfaceStyle];
-[_UIEditMenuContentPresentation setUserInterfaceStyle:];
-[_UIEditMenuContentPresentation intelligentAssistantServiceSessionDelegate];
-[_UIEditMenuContentPresentation teardownContainerView];
-[_UIEditMenuContentPresentation configureContainerViewWithConfiguration:];
-[_UIEditMenuContentPresentation currentListView];
-[_UIEditMenuContentPresentation _convertSourceRectToContainerView:];
-[_UIEditMenuContentPresentation _displayMenu:reason:];
-[_UIEditMenuContentPresentation _displayPreparedMenu:titleView:reason:didDismissMenu:configuration:];
-[_UIEditMenuContentPresentation _endSourceViewObservation];
-[_UIEditMenuContentPresentation _listViewAxisForTraitCollection:];
-[_UIEditMenuContentPresentation _observeSourceViewIfNeeded];
-[_UIEditMenuContentPresentation _performContextMenuHandoffForMenu:sourceView:];
-[_UIEditMenuContentPresentation _preferredContentInsetsForContainerViewWithConfiguration:];
-[_UIEditMenuContentPresentation _queryMenuSourceRectForConfiguration:reuseTargetRect:isValid:];
-[_UIEditMenuContentPresentation _queryMenuSourceRectsPreferredLayoutRectsForConfiguration:];
-[_UIEditMenuContentPresentation _reloadMenuLayoutWithSourceRect:animated:];
-[_UIEditMenuContentPresentation _resolvedLayoutForMenuWithConfiguration:sourceRect:axis:];
-[_UIEditMenuContentPresentation _resolvedMenuPositionForArrowDirection:availableBounds:sourceRect:menuSize:menuPosition:anchorPoint:];
-[_UIEditMenuContentPresentation _shouldReuseVisibleMenu];
-[_UIEditMenuContentPresentation _updateMenuPositionAnimated:reuseTargetRect:forced:];
-[_UIEditMenuContentPresentation contentSizeCategoryDidChangeInEditMenuListView:];
-[_UIEditMenuContentPresentation currentMenuLayout];
-[_UIEditMenuContentPresentation dismissingListView];
-[_UIEditMenuContentPresentation displayMenu:configuration:];
-[_UIEditMenuContentPresentation editMenuListView:didSelectMenuElement:source:];
-[_UIEditMenuContentPresentation editMenuListViewDidActivateHandoff:source:];
-[_UIEditMenuContentPresentation hideMenuWithReason:];
-[_UIEditMenuContentPresentation initialUserInterfaceStyle];
-[_UIEditMenuContentPresentation observingSourceView];
-[_UIEditMenuContentPresentation replaceVisibleMenuWithMenu:reason:];
-[_UIEditMenuContentPresentation setCurrentMenuLayout:];
-[_UIEditMenuContentPresentation sourceViewDidUpdateFromTraitCollection:];
-[_UIEditMenuContentPresentation targetRectInSourceView];
-[_UIEditMenuContentPresentation updateMenuPositionAnimated:];
-[_UIEditMenuContentPresentation wantsPasteTouchAuthenticationInEditMenuListView:];
```
