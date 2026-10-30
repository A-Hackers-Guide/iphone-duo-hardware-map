# `_UISearchBarSearchContainerLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UISearchBarLayoutBase`
- 35 instance variables, 50 properties, 96 instance methods, 0 class methods

## Instance variables

```
{?="hasCancelButton"b1"hasDeleteButton"b1"hasLeftButton"b1"hasFloatingSearchIconBackgroundView"b1"isHostedInlineByNavigationBar"b1"isHostedInlineByToolbar"b1"isTextFieldManagedInNSToolbar"b1"drawsSearchIconOnly"b1"allowSearchFieldShrinkage"b1"searchFieldUsesCustomBackgroundImage"b1"searchFieldEffectivelySupportsDynamicType"b1"searchFieldRespectsReadableWidth"b1"searchFieldWidthIsReduced"b1} _searchContainerLayoutFlags;
d _searchFieldForegroundFadeAlpha;
d _searchFieldBackgroundFadeAlpha;
B _combinedScopeBar;
@"<_UISearchBarContainerSublayoutDelegate>" _delegate;
d _defaultMinimumWidth;
d _defaultInactiveWidth;
d _defaultActiveWidth;
d _overrideInactiveWidth;
d _overrideActiveWidth;
@"UISearchBarTextField" _searchField;
@"UIImageView" _floatingSearchIconView;
@"UIView" _floatingSearchIconBackgroundView;
@"UIView" _cancelButton;
@"UIView" _deleteButton;
@"UIView" _leftButton;
d _searchBarReadableWidth;
@"UIBarButtonItem" _searchIconBarButtonItem;
q _representedLayoutState;
d _searchBarFieldHeight;
d _floatingSearchIconAlpha;
d _floatingSearchIconBackgroundAlpha;
d _mainContentAlpha;
@? _delegateSearchFieldFrameForProposedFrame;
@? _layoutCustomizationDelegateSearchFieldContainerWillLayoutSubviewsCallback;
d _additionalPaddingForCancelButtonAtLeadingEdge;
d _additionalPaddingForSearchFieldAtLeadingEdge;
{UIOffset="horizontal"d"vertical"d} _searchFieldBackgroundPositionAdjustment;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _searchFieldLayoutFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _cancelButtonLayoutFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _deleteButtonLayoutFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _leftButtonLayoutFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _visibleCancelButtonSearchFieldLayoutFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _floatingSearchIconLayoutFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _floatingSearchIconBackgroundLayoutFrame;
```

## Properties

```
@property (T@"<_UISearchBarContainerSublayoutDelegate>",W,N,V_delegate) delegate;
@property (Td,R,N) naturalContainerHeight;
@property (Td,R,N) naturalSearchFieldHeight;
@property (Td,R,N) prescribedWidth;
@property (Td,R,N) idealWidth;
@property (Td,N,V_defaultMinimumWidth) defaultMinimumWidth;
@property (Td,N,V_defaultInactiveWidth) defaultInactiveWidth;
@property (Td,N,V_defaultActiveWidth) defaultActiveWidth;
@property (Td,N,V_overrideInactiveWidth) overrideInactiveWidth;
@property (Td,N,V_overrideActiveWidth) overrideActiveWidth;
@property (T@"UISearchBarTextField",&,N,V_searchField) searchField;
@property (T@"UIImageView",&,N,V_floatingSearchIconView) floatingSearchIconView;
@property (T@"UIView",&,N,V_floatingSearchIconBackgroundView) floatingSearchIconBackgroundView;
@property (T@"UIView",&,N,V_cancelButton) cancelButton;
@property (T@"UIView",&,N,V_deleteButton) deleteButton;
@property (T@"UIView",&,N,V_leftButton) leftButton;
@property (TB,N) hasCancelButton;
@property (TB,N) hasDeleteButton;
@property (TB,N) hasLeftButton;
@property (TB,N) hasFloatingSearchIconBackgroundView;
@property (TB,N,GisHostedInlineByNavigationBar) hostedInlineByNavigationBar;
@property (TB,N,GisHostedInlineByToolbar) hostedInlineByToolbar;
@property (TB,N,GisTextFieldManagedInNSToolbar) textFieldManagedInNSToolbar;
@property (TB,N) drawsSearchIconOnly;
@property (TB,N) allowSearchFieldShrinkage;
@property (TB,N) searchFieldUsesCustomBackgroundImage;
@property (TB,N) searchFieldEffectivelySupportsDynamicType;
@property (TB,N) searchFieldRespectsReadableWidth;
@property (Td,N,V_searchBarReadableWidth) searchBarReadableWidth;
@property (T{UIOffset=dd},N,V_searchFieldBackgroundPositionAdjustment) searchFieldBackgroundPositionAdjustment;
@property (T@"UIBarButtonItem",&,N,V_searchIconBarButtonItem) searchIconBarButtonItem;
@property (Tq,N,V_representedLayoutState) representedLayoutState;
@property (Td,N,V_searchBarFieldHeight) searchBarFieldHeight;
@property (TB,N,V_combinedScopeBar) combinedScopeBar;
@property (Td,R,N) fieldToCancelButtonSpacing;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_searchFieldLayoutFrame) searchFieldLayoutFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_cancelButtonLayoutFrame) cancelButtonLayoutFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_deleteButtonLayoutFrame) deleteButtonLayoutFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_leftButtonLayoutFrame) leftButtonLayoutFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_floatingSearchIconLayoutFrame) floatingSearchIconLayoutFrame;
@property (Td,R,N,V_floatingSearchIconAlpha) floatingSearchIconAlpha;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_floatingSearchIconBackgroundLayoutFrame) floatingSearchIconBackgroundLayoutFrame;
@property (Td,R,N,V_floatingSearchIconBackgroundAlpha) floatingSearchIconBackgroundAlpha;
@property (Td,R,N,V_mainContentAlpha) mainContentAlpha;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_visibleCancelButtonSearchFieldLayoutFrame) visibleCancelButtonSearchFieldLayoutFrame;
@property (TB,R,N) searchFieldWidthIsReduced;
@property (T@?,C,N,V_delegateSearchFieldFrameForProposedFrame) delegateSearchFieldFrameForProposedFrame;
@property (T@?,C,N,V_layoutCustomizationDelegateSearchFieldContainerWillLayoutSubviewsCallback) layoutCustomizationDelegateSearchFieldContainerWillLayoutSubviewsCallback;
@property (Td,N,V_additionalPaddingForCancelButtonAtLeadingEdge) additionalPaddingForCancelButtonAtLeadingEdge;
@property (Td,N,V_additionalPaddingForSearchFieldAtLeadingEdge) additionalPaddingForSearchFieldAtLeadingEdge;
```

## Instance methods

```
-[_UISearchBarSearchContainerLayout isHostedInlineByToolbar];
-[_UISearchBarSearchContainerLayout setHasLeftButton:];
-[_UISearchBarSearchContainerLayout combinedScopeBar];
-[_UISearchBarSearchContainerLayout additionalPaddingForCancelButtonAtLeadingEdge];
-[_UISearchBarSearchContainerLayout searchIconBarButtonItem];
-[_UISearchBarSearchContainerLayout searchBarReadableWidth];
-[_UISearchBarSearchContainerLayout searchFieldBackgroundPositionAdjustment];
-[_UISearchBarSearchContainerLayout hasCancelButton];
-[_UISearchBarSearchContainerLayout setCancelButton:];
-[_UISearchBarSearchContainerLayout setLayoutCustomizationDelegateSearchFieldContainerWillLayoutSubviewsCallback:];
-[_UISearchBarSearchContainerLayout setSearchField:];
-[_UISearchBarSearchContainerLayout applyLayout];
-[_UISearchBarSearchContainerLayout naturalSearchFieldHeight];
-[_UISearchBarSearchContainerLayout setHostedInlineByToolbar:];
-[_UISearchBarSearchContainerLayout hasLeftButton];
-[_UISearchBarSearchContainerLayout restoreSearchField:];
-[_UISearchBarSearchContainerLayout setRepresentedLayoutState:];
-[_UISearchBarSearchContainerLayout drawsSearchIconOnly];
-[_UISearchBarSearchContainerLayout setDefaultMinimumWidth:];
-[_UISearchBarSearchContainerLayout defaultInactiveWidth];
-[_UISearchBarSearchContainerLayout setOverrideActiveWidth:];
-[_UISearchBarSearchContainerLayout setCombinedScopeBar:];
-[_UISearchBarSearchContainerLayout defaultMinimumWidth];
-[_UISearchBarSearchContainerLayout floatingSearchIconBackgroundView];
-[_UISearchBarSearchContainerLayout representedLayoutState];
-[_UISearchBarSearchContainerLayout setHostedInlineByNavigationBar:];
-[_UISearchBarSearchContainerLayout setDeleteButton:];
-[_UISearchBarSearchContainerLayout isTextFieldManagedInNSToolbar];
-[_UISearchBarSearchContainerLayout setSearchFieldBackgroundPositionAdjustment:];
-[_UISearchBarSearchContainerLayout overrideActiveWidth];
-[_UISearchBarSearchContainerLayout hasFloatingSearchIconBackgroundView];
-[_UISearchBarSearchContainerLayout allowSearchFieldShrinkage];
-[_UISearchBarSearchContainerLayout leftButton];
-[_UISearchBarSearchContainerLayout floatingSearchIconView];
-[_UISearchBarSearchContainerLayout setTextFieldManagedInNSToolbar:];
-[_UISearchBarSearchContainerLayout overrideInactiveWidth];
-[_UISearchBarSearchContainerLayout setFloatingSearchIconView:];
-[_UISearchBarSearchContainerLayout setHasDeleteButton:];
-[_UISearchBarSearchContainerLayout setLeftButton:];
-[_UISearchBarSearchContainerLayout setHasCancelButton:];
-[_UISearchBarSearchContainerLayout setFloatingSearchIconBackgroundView:];
-[_UISearchBarSearchContainerLayout defaultActiveWidth];
-[_UISearchBarSearchContainerLayout setOverrideInactiveWidth:];
-[_UISearchBarSearchContainerLayout setSearchIconBarButtonItem:];
-[_UISearchBarSearchContainerLayout setAdditionalPaddingForCancelButtonAtLeadingEdge:];
-[_UISearchBarSearchContainerLayout updateLayout];
-[_UISearchBarSearchContainerLayout additionalPaddingForSearchFieldAtLeadingEdge];
-[_UISearchBarSearchContainerLayout deleteButton];
-[_UISearchBarSearchContainerLayout setSearchFieldUsesCustomBackgroundImage:];
-[_UISearchBarSearchContainerLayout setAdditionalPaddingForSearchFieldAtLeadingEdge:];
-[_UISearchBarSearchContainerLayout isHostedInlineByNavigationBar];
-[_UISearchBarSearchContainerLayout cancelButton];
-[_UISearchBarSearchContainerLayout cancelButtonLayoutFrame];
-[_UISearchBarSearchContainerLayout searchBarFieldHeight];
-[_UISearchBarSearchContainerLayout deleteButtonLayoutFrame];
-[_UISearchBarSearchContainerLayout searchFieldRespectsReadableWidth];
-[_UISearchBarSearchContainerLayout searchField];
-[_UISearchBarSearchContainerLayout _effectiveActiveWidth];
-[_UISearchBarSearchContainerLayout setSearchBarReadableWidth:];
-[_UISearchBarSearchContainerLayout mainContentAlpha];
-[_UISearchBarSearchContainerLayout setSearchFieldRespectsReadableWidth:];
-[_UISearchBarSearchContainerLayout floatingSearchIconBackgroundAlpha];
-[_UISearchBarSearchContainerLayout idealWidth];
-[_UISearchBarSearchContainerLayout leftButtonLayoutFrame];
-[_UISearchBarSearchContainerLayout layoutCustomizationDelegateSearchFieldContainerWillLayoutSubviewsCallback];
-[_UISearchBarSearchContainerLayout _updateGlassGroupSmoothness];
-[_UISearchBarSearchContainerLayout setDelegateSearchFieldFrameForProposedFrame:];
-[_UISearchBarSearchContainerLayout disownSearchField];
-[_UISearchBarSearchContainerLayout setDefaultActiveWidth:];
-[_UISearchBarSearchContainerLayout searchFieldLayoutFrame];
-[_UISearchBarSearchContainerLayout setSearchBarFieldHeight:];
-[_UISearchBarSearchContainerLayout floatingSearchIconLayoutFrame];
-[_UISearchBarSearchContainerLayout visibleCancelButtonSearchFieldLayoutFrame];
-[_UISearchBarSearchContainerLayout naturalContainerHeight];
-[_UISearchBarSearchContainerLayout setDelegate:];
-[_UISearchBarSearchContainerLayout searchFieldWidthIsReduced];
-[_UISearchBarSearchContainerLayout delegateSearchFieldFrameForProposedFrame];
-[_UISearchBarSearchContainerLayout setAllowSearchFieldShrinkage:];
-[_UISearchBarSearchContainerLayout widthForSearchFieldWidth:];
-[_UISearchBarSearchContainerLayout searchFieldUsesCustomBackgroundImage];
-[_UISearchBarSearchContainerLayout setDefaultInactiveWidth:];
-[_UISearchBarSearchContainerLayout setDrawsSearchIconOnly:];
-[_UISearchBarSearchContainerLayout delegate];
-[_UISearchBarSearchContainerLayout fieldToCancelButtonSpacing];
-[_UISearchBarSearchContainerLayout description];
-[_UISearchBarSearchContainerLayout setSearchFieldEffectivelySupportsDynamicType:];
-[_UISearchBarSearchContainerLayout setHasFloatingSearchIconBackgroundView:];
-[_UISearchBarSearchContainerLayout sendWillLayoutSubviewsForSearchFieldContainerView:];
-[_UISearchBarSearchContainerLayout hasDeleteButton];
-[_UISearchBarSearchContainerLayout prescribedWidth];
-[_UISearchBarSearchContainerLayout copyWithZone:];
-[_UISearchBarSearchContainerLayout searchFieldEffectivelySupportsDynamicType];
-[_UISearchBarSearchContainerLayout floatingSearchIconAlpha];
-[_UISearchBarSearchContainerLayout _effectiveInactiveWidth];
-[_UISearchBarSearchContainerLayout floatingSearchIconBackgroundLayoutFrame];
-[_UISearchBarSearchContainerLayout searchFieldHeightUpdatingShrinkageAndFadeAlphas];
```
