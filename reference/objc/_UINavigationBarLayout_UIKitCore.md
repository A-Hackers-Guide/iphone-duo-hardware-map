# `_UINavigationBarLayout`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `_UINavigationBarTransitionContextParticipant`
- 50 instance variables, 4 properties, 25 instance methods, 0 class methods

## Instance variables

```
@"_UIBarInsertLayoutData" _topWhitespaceLayoutData;
@"_UIBarInsertLayoutData" _promptLayoutData;
@"_UIBarInsertLayoutData" _contentLayoutData;
@"_UIBarInsertLayoutData" _largeTitleLayoutData;
@"_UIBarInsertLayoutData" _refreshControlLayoutData;
@"_UIBarInsertLayoutData" _searchBarLayoutData;
@"_UIBarInsertLayoutData" _scopeBarLayoutData;
@"_UIBarInsertLayoutData" _topPaletteLayoutData;
@"_UIBarInsertLayoutData" _bottomPaletteLayoutData;
@"NSMutableArray" _priorityOrderedLayout;
@"NSMutableArray" _stackingOrderedLayout;
@"NSArray" _restingHeights;
{?="layoutIsValid"b1} _flags;
B _largeTitleViewOverlaysContentView;
B _backgroundCoversContentOnly;
B _clientWantsBackgroundHidden;
B _useManualScrollEdgeAppearance;
B _clientUsesManualScrollEdgeAppearanceProgressSPI;
B _clientCanUpdateChromelessTransitionProgress;
B _hasInlineSearchBar;
B _clientWantsToPreserveSearchBarAcrossTransitions;
B _hidesSearchBarWhenScrolling;
B _adjustForTabBar;
@"_UINavigationBarModernPromptView" _promptView;
@"_UINavigationBarContentView" _contentView;
@"UIView" _animationContentClippingView;
@"_UINavigationBarLargeTitleView" _largeTitleView;
@"<_UINavigationBarContentViewVisualProvider>" _contentViewVisualProvider;
@"_UINavigationBarContentViewLayout" _contentViewLayout;
@"_UINavigationBarLargeTitleViewLayout" _largeTitleViewLayout;
@"_UIBarBackground" _backgroundView;
@"_UIBarBackgroundLayout" _compactBackgroundViewLayout;
@"_UIBarBackgroundLayout" _standardBackgroundViewLayout;
d _backgroundExtension;
d _requestedBackgroundViewAlpha;
d _manualScrollEdgeAppearanceProgress;
@"_UINavigationControllerRefreshControlHost" _refreshControlHost;
@"UILabel" _weeTitleLabel;
@"UISearchBar" _searchBar;
q _representedSearchLayoutState;
@"_UINavigationBarPalette" _topPalette;
@"_UINavigationBarPalette" _bottomPalette;
d _largeTitleExposure;
d _largeTitleTransitionProgress;
d _chromelessTransitionProgress;
d _computedBackgroundViewAlpha;
q _apiVersion;
{CGSize="width"d"height"d} _layoutSize;
{NSDirectionalEdgeInsets="top"d"leading"d"bottom"d"trailing"d} _largeTitleViewInsets;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _originLayoutFrame;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UINavigationBarLayout prepareToRecordToState:];
-[_UINavigationBarLayout recordFromStateForTransition:];
-[_UINavigationBarLayout recordToStateForTransition:];
-[_UINavigationBarLayout ensureBackButtonTruncationOccursWithContext:];
-[_UINavigationBarLayout init];
-[_UINavigationBarLayout initWithLayout:];
-[_UINavigationBarLayout finalizeStateFromTransition:];
-[_UINavigationBarLayout description];
-[_UINavigationBarLayout copyWithZone:];
-[_UINavigationBarLayout _addLayoutItem:];
-[_UINavigationBarLayout _updateLargeTitleViewLayoutItem];
-[_UINavigationBarLayout _updateRefreshControlLayoutData];
-[_UINavigationBarLayout _includeContentLayoutDataInLayout:];
-[_UINavigationBarLayout _insertLayoutDataForNavigationBarPart:];
-[_UINavigationBarLayout _layoutFrameFor:withOrder:];
-[_UINavigationBarLayout _promptOrder];
-[_UINavigationBarLayout _removeLayoutItem:];
-[_UINavigationBarLayout _reorderLayoutItem:toOrder:];
-[_UINavigationBarLayout _reprioritizeLayoutItem:toPriority:];
-[_UINavigationBarLayout _topPaletteOrder];
-[_UINavigationBarLayout _updateContentViewLayoutItem];
-[_UINavigationBarLayout _updateLayoutOutputs];
-[_UINavigationBarLayout _updateLayoutParametersForWidth:];
-[_UINavigationBarLayout _updateWhitespaceLayoutItems];
-[_UINavigationBarLayout topWhitespaceLayoutFrame];
```
