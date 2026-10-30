# `_UIButtonBar`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIPointerInteractionDelegate`, `_UIButtonBarGroupOrderOwner`, `_UIBarButtonItemViewOwner`, `_UIBarButtonItemGroupOwner`, `NSCoding`
- 33 instance variables, 42 properties, 110 instance methods, 0 class methods

## Instance variables

```
@"_UIButtonBarStackView" _stackView;
@"NSLayoutDimension" _flexibleSpaceEqualSizeAnchor;
@"NSLayoutDimension" _minimumInterItemSpaceAnchor;
@"NSLayoutConstraint" _minimumInterItemSpaceConstraint;
@"UIView" _centeredView;
@"NSLayoutConstraint" _centeringConstraint;
@"_UIButtonBarLayoutMetrics" _layoutMetrics;
@"NSMutableArray" _groupLayouts;
@"NSMutableArray" _effectiveLayout;
@"NSMapTable" _groupLayoutMap;
@"NSMutableArray" _layoutViews;
@"NSMutableArray" _layoutGuides;
@"NSMutableArray" _layoutActiveConstraints;
@"NSMapTable" _senderActionMap;
{?="isInLayoutReentrancyGuard"b1"needsAppearanceUpdate"b1"plainAppearanceChanged"b1"doneAppearanceChanged"b1"denyPointerInteractions"b1"effectiveLayoutHasCriticalGroup"b1} _buttonBarFlags;
B _itemsInGroupUseSameSize;
B _forceFixedSpacing;
B _supportsOverflow;
B _supportsAlwaysOverflowGroups;
@"NSArray" _barButtonGroups;
d _minimumInterItemSpace;
@"NSArray" _fixedLeadingGroups;
@"NSArray" _fixedTrailingGroups;
@"<_UIButtonBarDelegate>" _delegate;
d _targetLayoutWidth;
@"_UIButtonBarGroupOrderer" _groupOrderer;
@? _defaultActionFilter;
@"<_UIButtonBarAppearanceDelegate>" __appearanceDelegate;
@"_UIBarButtonItemData" _plainItemAppearance;
@"_UIBarButtonItemData" _doneItemAppearance;
@"_UIPointerInteractionAssistant" _assistant;
@"UIBarButtonItem" _popOverPresentingSourceItem;
@? _viewUpdater;
```

## Properties

```
@property (T@"NSArray",C,N,V_fixedLeadingGroups) fixedLeadingGroups;
@property (T@"NSArray",C,N,V_fixedTrailingGroups) fixedTrailingGroups;
@property (T@"<_UIButtonBarDelegate>",W,N,V_delegate) delegate;
@property (T{?=ddd},R,N) widthInfo;
@property (Td,N,V_targetLayoutWidth) targetLayoutWidth;
@property (TB,N,V_itemsInGroupUseSameSize) itemsInGroupUseSameSize;
@property (TB,N,V_forceFixedSpacing) forceFixedSpacing;
@property (TB,N,V_supportsOverflow) supportsOverflow;
@property (T@"_UIButtonBarGroupOrderer",&,N,V_groupOrderer) groupOrderer;
@property (T@"NSArray",R,C,N) groupRealizedOrder;
@property (TB,R,N) hasVisibleContent;
@property (TB,N,V_supportsAlwaysOverflowGroups) supportsAlwaysOverflowGroups;
@property (TB,R,N) hasAlwaysOverflowGroups;
@property (T@"NSArray",R,C,N) elementsForOverflowMenu;
@property (T@"NSArray",R,C,N) elementsRepresentingOrderedGroups;
@property (TB,R,N) needsLeadingSpacer;
@property (TB,R,N) needsTrailingSpacer;
@property (T@"UIBarButtonItem",R,N) leadingVisibleItem;
@property (T@"UIBarButtonItem",R,N) trailingVisibleItem;
@property (T@"UIBarButtonItem",R,N) trailingClippingItem;
@property (T@?,C,N,V_defaultActionFilter) defaultActionFilter;
@property (T@"<_UIButtonBarAppearanceDelegate>",W,N,V__appearanceDelegate) _appearanceDelegate;
@property (T@"_UIBarButtonItemData",&,N,V_plainItemAppearance) plainItemAppearance;
@property (TB,R,N) plainItemAppearanceNeedsUpdate;
@property (T@"_UIBarButtonItemData",&,N,V_doneItemAppearance) doneItemAppearance;
@property (TB,R,N) doneItemAppearanceNeedsUpdate;
@property (T@"UIView<UIPointerInteractionDelegate>",R,N) assistantView;
@property (T@"_UIPointerInteractionAssistant",W,N,V_assistant) assistant;
@property (T@"UIView",R,N) _viewForOverlayRects;
@property (T@"UIBarButtonItem",W,N,V_popOverPresentingSourceItem) popOverPresentingSourceItem;
@property (T@?,C,N,V_viewUpdater) viewUpdater;
@property (T@"UIView",R,N) view;
@property (T@"NSArray",C,N,V_barButtonGroups) barButtonGroups;
@property (Td,N,V_minimumInterItemSpace) minimumInterItemSpace;
@property (TB,N) allowsViewWrappers;
@property (Tq,N) itemDistribution;
@property (T{UIEdgeInsets=dddd},N) hitTestInsets;
@property (T{NSDirectionalEdgeInsets=dddd},N) hitTestDirectionalInsets;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIButtonBar assistant];
-[_UIButtonBar setViewUpdater:];
-[_UIButtonBar hasVisibleContent];
-[_UIButtonBar _groupDidUpdateVisibility:];
-[_UIButtonBar _itemDidChangeWidth:];
-[_UIButtonBar viewUpdater];
-[_UIButtonBar hitTestInsets];
-[_UIButtonBar _itemDidChangeSelectionState:];
-[_UIButtonBar _item:removeSymbolEffectOfType:options:animated:];
-[_UIButtonBar _validateAllItems];
-[_UIButtonBar setFixedTrailingGroups:];
-[_UIButtonBar _itemStandardViewNeedsUpdate:];
-[_UIButtonBar setHitTestInsets:];
-[_UIButtonBar _viewForOverlayRects];
-[_UIButtonBar setAssistant:];
-[_UIButtonBar _itemDidChangeEnabledState:];
-[_UIButtonBar _item:addSymbolEffect:options:animated:];
-[_UIButtonBar _groupDidUpdateItems:removedItems:];
-[_UIButtonBar _groupDidUpdateRepresentative:fromRepresentative:];
-[_UIButtonBar _contextMenuInteractionForItem:];
-[_UIButtonBar _item:applyContentTransition:options:];
-[_UIButtonBar _itemCustomViewDidChange:fromView:];
-[_UIButtonBar _buttonBarStackViewDidLayoutSubviews:];
-[_UIButtonBar _groupDidUpdatePlatterizationPreference:];
-[_UIButtonBar doneItemAppearance];
-[_UIButtonBar _itemDidChangeHiddenState:];
-[_UIButtonBar _layoutIfNeeded];
-[_UIButtonBar _item:removeAllSymbolEffectsWithOptions:animated:];
-[_UIButtonBar hasAlwaysOverflowGroups];
-[_UIButtonBar doneItemAppearanceNeedsUpdate];
-[_UIButtonBar setSupportsAlwaysOverflowGroups:];
-[_UIButtonBar setItemDistribution:];
-[_UIButtonBar pointerInteraction:styleForRegion:];
-[_UIButtonBar elementsForOverflowMenu];
-[_UIButtonBar setBarButtonGroups:];
-[_UIButtonBar setPlainItemAppearance:];
-[_UIButtonBar needsLeadingSpacer];
-[_UIButtonBar init];
-[_UIButtonBar pointerInteraction:willEnterRegion:animator:];
-[_UIButtonBar widthInfo];
-[_UIButtonBar pointerInteraction:willExitRegion:animator:];
-[_UIButtonBar itemDistribution];
-[_UIButtonBar setItemsInGroupUseSameSize:];
-[_UIButtonBar _targetActionForBarButtonItem:];
-[_UIButtonBar dealloc];
-[_UIButtonBar defaultActionFilter];
-[_UIButtonBar _layoutBar];
-[_UIButtonBar groupOrderer];
-[_UIButtonBar _numberOfGroups];
-[_UIButtonBar _preferredRegionRectForButton:];
-[_UIButtonBar trailingVisibleItem];
-[_UIButtonBar set_appearanceDelegate:];
-[_UIButtonBar leadingVisibleItem];
-[_UIButtonBar _appearanceChanged];
-[_UIButtonBar setDoneItemAppearance:];
-[_UIButtonBar needsTrailingSpacer];
-[_UIButtonBar _updatedViewForBarButtonItem:withView:];
-[_UIButtonBar _updateHitRects];
-[_UIButtonBar assistantView];
-[_UIButtonBar _itemDidUpdateMenu:fromMenu:];
-[_UIButtonBar itemAtPoint:inView:];
-[_UIButtonBar setMinimumInterItemSpace:];
-[_UIButtonBar _groupOrdererGroups:];
-[_UIButtonBar view];
-[_UIButtonBar plainItemAppearance];
-[_UIButtonBar supportsOverflow];
-[_UIButtonBar setDelegate:];
-[_UIButtonBar _overflowFallbackItem];
-[_UIButtonBar setAllowsViewWrappers:];
-[_UIButtonBar itemsInGroupUseSameSize];
-[_UIButtonBar elementsRepresentingOrderedGroups];
-[_UIButtonBar _setNeedsVisualUpdate];
-[_UIButtonBar setHitTestDirectionalInsets:];
-[_UIButtonBar minimumInterItemSpace];
-[_UIButtonBar encodeWithCoder:];
-[_UIButtonBar hitTestDirectionalInsets];
-[_UIButtonBar setGroupOrderer:];
-[_UIButtonBar pointerInteraction:regionForRequest:defaultRegion:];
-[_UIButtonBar delegate];
-[_UIButtonBar popOverPresentingSourceItem];
-[_UIButtonBar setNeedsHitTestUpdate];
-[_UIButtonBar _invalidateAssistant:];
-[_UIButtonBar setFixedLeadingGroups:];
-[_UIButtonBar _appearanceDelegate];
-[_UIButtonBar description];
-[_UIButtonBar setForceFixedSpacing:];
-[_UIButtonBar _enumerateAllGroups:];
-[_UIButtonBar initWithCoder:];
-[_UIButtonBar setSupportsOverflow:];
-[_UIButtonBar _disablePointerInteractions];
-[_UIButtonBar _enumerateLayoutGroups:];
-[_UIButtonBar trailingClippingItem];
-[_UIButtonBar setBarButtonGroups:animated:];
-[_UIButtonBar targetLayoutWidth];
-[_UIButtonBar setDefaultActionFilter:];
-[_UIButtonBar _setNeedsAppearanceUpdate];
-[_UIButtonBar setPopOverPresentingSourceItem:];
-[_UIButtonBar plainItemAppearanceNeedsUpdate];
-[_UIButtonBar forceFixedSpacing];
-[_UIButtonBar _confirmOwnershipOfFixedGroups];
-[_UIButtonBar _enablePointerInteractions];
-[_UIButtonBar fixedTrailingGroups];
-[_UIButtonBar setTargetLayoutWidth:];
-[_UIButtonBar allowsViewWrappers];
-[_UIButtonBar fixedLeadingGroups];
-[_UIButtonBar supportsAlwaysOverflowGroups];
-[_UIButtonBar _layoutForGroup:];
-[_UIButtonBar groupRealizedOrder];
-[_UIButtonBar _groupOrdererDidUpdate:];
-[_UIButtonBar barButtonGroups];
```
