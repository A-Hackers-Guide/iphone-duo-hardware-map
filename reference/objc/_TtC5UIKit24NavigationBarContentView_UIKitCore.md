# `_TtC5UIKit24NavigationBarContentView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIBarContentView`
- Protocols: `_TtP5UIKit41_UIToolbarVerticalBarOverlayInsetObserver_`, `UIEditMenuInteractionDelegate`, `_UINavigationBarTitleViewDataSource`, `_UIButtonBarButtonChangeObserver`, `_UIBarButtonItemViewOwner`
- 87 instance variables, 8 properties, 60 instance methods, 0 class methods

## Instance variables

```
UIKit.NavigationBarContentView.Delegate ? delegate;
UIKit.NavigationBarTransitionContext ? _transitionContext;
UIKit.NavigationBarTransitionContainer transitionContainer;
__C.UIBarPreferredContentSize resolvedContentSize;
__C.UIBarMetrics resolvedBarMetrics;
UIKit.NavigationBarContentView.Content.Metrics metrics;
_$sSaySo13_UIBarSectionCGSg leadingBarSections;
Swift.Bool leadingItemsSupplementBackItem;
_$sSaySo13_UIBarSectionCGSg centerBarSections;
UIKit.NavigationBarContentView.LayoutResult ? lastLayoutResult;
_$sSSSg customizationIdentifier;
CoreGraphics.CGFloat resolvedExtension;
CoreGraphics.CGFloat resolvedHeight;
Swift.Bool isCollapsed;
_$sSaySo13_UIBarSectionCGSg trailingBarSections;
_$sSo20UIBarButtonItemGroupCSg pinnedTrailingGroup;
_$sSo6UIViewCSg titleIconView;
UIKit.NavigationBarContentView.Content.TitleContent titleContent;
_$sSo28_UINavigationBarTitleControlCSg inlineLargeTitleControl;
UIKit.NavigationBarContentView.Content.InlineLargeTitleContent ? inlineLargeTitleContent;
UIKit.NavigationBarSubtitleView ? inlineLargeSubtitleView;
UIKit.NavigationBarContentView.SubtitleContent ? inlineLargeSubtitleContent;
Swift.Bool renderInlineLargeTitle;
_$sSo17UITraitCollectionCSg augmentedTitleNavigationBarTraits;
UIKit.NavigationBarContentView.Content.InlineSearchConfiguration ? inlineSearchConfiguration;
Swift.Bool hidesNavigationBarDuringPresentation;
_$sSo15_UIBarItemGroupCSg syntheticSearchPlacementGroup;
_$sSD -> __C.Key Any titleAttributes;
__C.UIOffset titlePositionAdjustment;
Swift.Bool isDeferringSearchSuggestionsMenuRefreshForGeometryChange;
_$sSo20UIBarButtonItemGroupCSg overflowGroup;
Swift.Bool isTitleHidden;
Swift.Bool titleEnabled;
_$sSo20UIDocumentPropertiesCSg documentProperties;
_$sSo30_UINavigationItemRenameHandlerCSg renameHandler;
_$sSo35_UINavigationBarTitleRenamerSessionCSg activeRenamerSession;
(objc_protocol 0x18642f880) _$s_So6UIViewCXcSg renamingContentView;
UIKit.NavigationBarContentView.AugmentedTitleViewHost ? augmentedTitleViewHost;
_$sSo8UIActionCSg backAction;
Swift.Bool useInlineLargeTitleMetrics;
UIKit.NavigationBarContentView.Content.TabBarContext tabBarContext;
_$sSo18_UIButtonBarButtonCSg backButton;
Foundation.UUID ? $__lazy_storage_$_backButtonSectionID;
Swift.Bool shouldAnimateNextLayout;
Swift.Bool ignoreNeedsUpdate;
UIKit.NavigationBarContentView.Flags flags;
Swift.Bool shouldPassThroughTouches;
__C.UIBarPreferredContentSize requestedContentSize;
__C.ItemStyle toolbarStyle;
__C._UINavigationBarContentViewLayoutGroupMode staticLeadingGroupsMode;
UIKit.NavigationButtonBar ? _staticLeadingBar;
__C._UINavigationBarContentViewLayoutGroupMode leadingGroupsMode;
UIKit.NavigationButtonBar ? _leadingBar;
__C._UINavigationBarContentViewLayoutGroupMode centerGroupsMode;
CoreGraphics.CGFloat centerBarAlpha;
UIKit.NavigationButtonBar ? _centerBar;
Swift.Bool trailingGroupsEnabled;
UIKit.NavigationButtonBar ? _trailingBar;
_$sSo15UIBarButtonItemCSg $__lazy_storage_$_overflowItem;
_$sSo21UIDeferredMenuElementCSg additionalOverflowItems;
Swift.Bool overflowContainsOverflowedButtons;
_$sSo28_UINavigationBarTitleControlCSg _titleControl;
_$sSaySo20UIBarButtonItemGroupCG staticLeadingItemGroups;
_$sSaySo20UIBarButtonItemGroupCG staticTrailingItemGroups;
_$sSo15UIBarButtonItemCSg backButtonItem;
Swift.Bool backButtonHidden;
_$sSo15UIBarButtonItemCSg _backActionItem;
Swift.Bool titleElementsHidden;
Swift.Bool titleElementsHiddenVariesByScrollEdge;
CoreGraphics.CGFloat inlineTitleViewAlpha;
Swift.Bool hideTitleElementsForLargeTitle;
UIKit.NavigationBarSubtitleView ? subtitleView;
UIKit.NavigationBarContentView.Margins margins;
Swift.Bool isPerformingLayout;
UIKit.NavigationBarContentView.DebugVisualizer ? debugVisualizer;
_$sSo7UIImageCSg _backIndicatorImage;
CoreGraphics.CGFloat _backButtonMaximumWidth;
_$sSo20_UIBarButtonItemDataCSg _plainItemAppearance;
_$sSo20_UIBarButtonItemDataCSg _prominentItemAppearance;
_$sSo20_UIBarButtonItemDataCSg _backButtonAppearance;
_$sSo30_UIPointerInteractionAssistantC assistant;
Swift.Bool augmentedTitleViewIsOnlyContent;
_$sSd floatingTabBarPadding;
CoreGraphics.CGFloat largeTitleHeight;
__C.UIFloatRange largeTitleHeightRange;
_$sSo26_UIScrollPocketInteractionCSg scrollPocketInteraction;
CoreGraphics.CGFloat scrollAwayProgress;
```

## Properties

```
@property (T{CGSize=dd},N,R) intrinsicContentSize;
@property (T{UIEdgeInsets=dddd},N) layoutMargins;
@property (T{NSDirectionalEdgeInsets=dddd},N) directionalLayoutMargins;
@property (Td,N,R) defaultEdgeSpacing;
@property (Tq,N,R) barType;
@property (T@"UIImage",N,&) backIndicatorImage;
@property (Td,N) backButtonMaximumWidth;
@property (T@"NSString",N,R) description;
```

## Instance methods

```
-[_TtC5UIKit24NavigationBarContentView titleViewChangedMaximumBackButtonWidth:];
-[_TtC5UIKit24NavigationBarContentView titleViewChangedLayout:];
-[_TtC5UIKit24NavigationBarContentView titleViewChangedStandardDisplayItems:];
-[_TtC5UIKit24NavigationBarContentView titleViewChangedHeight:];
-[_TtC5UIKit24NavigationBarContentView _itemDidChangeWidth:];
-[_TtC5UIKit24NavigationBarContentView layoutMargins];
-[_TtC5UIKit24NavigationBarContentView titleViewLargeTitleHeightRange:];
-[_TtC5UIKit24NavigationBarContentView _traitCollectionForChildEnvironment:];
-[_TtC5UIKit24NavigationBarContentView _itemDidChangeSelectionState:];
-[_TtC5UIKit24NavigationBarContentView titleViewChangedTabBarSizingDisposition:];
-[_TtC5UIKit24NavigationBarContentView _item:removeSymbolEffectOfType:options:animated:];
-[_TtC5UIKit24NavigationBarContentView titleViewContentBaseHeight:];
-[_TtC5UIKit24NavigationBarContentView titleViewBackButtonMenu:];
-[_TtC5UIKit24NavigationBarContentView titleViewLargeTitleHeight:];
-[_TtC5UIKit24NavigationBarContentView backButtonTitleDidChange];
-[_TtC5UIKit24NavigationBarContentView titleViewChangedDisplayItemAlpha:];
-[_TtC5UIKit24NavigationBarContentView titleViewChangedPreferredDisplaySize:];
-[_TtC5UIKit24NavigationBarContentView _itemStandardViewNeedsUpdate:];
-[_TtC5UIKit24NavigationBarContentView titleViewFloatingTabBarHeight:];
-[_TtC5UIKit24NavigationBarContentView titleView:needsUpdatedContentOverlayRects:];
-[_TtC5UIKit24NavigationBarContentView _itemDidChangeEnabledState:];
-[_TtC5UIKit24NavigationBarContentView __backButtonAction:];
-[_TtC5UIKit24NavigationBarContentView layoutSublayersOfLayer:];
-[_TtC5UIKit24NavigationBarContentView _item:addSymbolEffect:options:animated:];
-[_TtC5UIKit24NavigationBarContentView titleViewContentBaselineOffsetFromTop:];
-[_TtC5UIKit24NavigationBarContentView _contextMenuInteractionForItem:];
-[_TtC5UIKit24NavigationBarContentView setBackIndicatorImage:];
-[_TtC5UIKit24NavigationBarContentView _item:applyContentTransition:options:];
-[_TtC5UIKit24NavigationBarContentView edgesPaddingBarButtonItem:];
-[_TtC5UIKit24NavigationBarContentView _itemCustomViewDidChange:fromView:];
-[_TtC5UIKit24NavigationBarContentView directionalLayoutMargins];
-[_TtC5UIKit24NavigationBarContentView _itemDidChangeHiddenState:];
-[_TtC5UIKit24NavigationBarContentView titleViewChangedDisplayLayer:];
-[_TtC5UIKit24NavigationBarContentView _item:removeAllSymbolEffectsWithOptions:animated:];
-[_TtC5UIKit24NavigationBarContentView _layoutMarginsForButtonBarButton:compact:];
-[_TtC5UIKit24NavigationBarContentView _intrinsicContentSizeInvalidatedForChildView:];
-[_TtC5UIKit24NavigationBarContentView traitCollectionForResolvingButtonBarButtonBackgroundColor:];
-[_TtC5UIKit24NavigationBarContentView setDirectionalLayoutMargins:];
-[_TtC5UIKit24NavigationBarContentView intrinsicContentSize];
-[_TtC5UIKit24NavigationBarContentView setLayoutMargins:];
-[_TtC5UIKit24NavigationBarContentView _toolbarVerticalBarOverlayInsetsDidChange];
-[_TtC5UIKit24NavigationBarContentView tintColorForButtonBarButton:];
-[_TtC5UIKit24NavigationBarContentView _safeAreaInsetsDidChangeFromOldInsets:];
-[_TtC5UIKit24NavigationBarContentView layoutSubviews];
-[_TtC5UIKit24NavigationBarContentView hitTest:withEvent:];
-[_TtC5UIKit24NavigationBarContentView updateProperties];
-[_TtC5UIKit24NavigationBarContentView sizeThatFits:];
-[_TtC5UIKit24NavigationBarContentView tintColorDidChange];
-[_TtC5UIKit24NavigationBarContentView description];
-[_TtC5UIKit24NavigationBarContentView initWithCoder:];
-[_TtC5UIKit24NavigationBarContentView defaultEdgeSpacing];
-[_TtC5UIKit24NavigationBarContentView _backButtonContentPaddingInButtonBarButton:];
-[_TtC5UIKit24NavigationBarContentView backIndicatorImage];
-[_TtC5UIKit24NavigationBarContentView editMenuInteraction:menuForConfiguration:suggestedActions:];
-[_TtC5UIKit24NavigationBarContentView _clippedSafeAreaCornerInsetsDidChangeFromOldCornerInsets:];
-[_TtC5UIKit24NavigationBarContentView initWithFrame:];
-[_TtC5UIKit24NavigationBarContentView canPerformAction:withSender:];
-[_TtC5UIKit24NavigationBarContentView barType];
-[_TtC5UIKit24NavigationBarContentView setBackButtonMaximumWidth:];
-[_TtC5UIKit24NavigationBarContentView backButtonMaximumWidth];
```
