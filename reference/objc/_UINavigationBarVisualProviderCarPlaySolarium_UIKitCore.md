# `_UINavigationBarVisualProviderCarPlaySolarium`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UINavigationBarVisualProvider`
- Protocols: `_UIButtonBarAppearanceDelegate`, `_UINavigationItemChangeObserver`
- 27 instance variables, 40 properties, 110 instance methods, 0 class methods

## Instance variables

```
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _desiredLayoutMargins;
B _compactMetrics;
B _havePrepared;
@"_UIBarButtonItemAppearanceStorage" _appearanceStorage;
@"_UIScrollPocketInteraction" _scrollPocketInteraction;
@"UIView" _contentView;
@"_UICarTitleView" _titleView;
@"_UINavigationButtonBarWrapperView" _leadingBarView;
@"_UINavigationButtonBarWrapperView" _trailingBarView;
@"_UIButtonBarButton" _backBarButton;
@"NSLayoutConstraint" _leadingBarConstraint;
@"NSLayoutConstraint" _leadingBarNoItemsConstraint;
@"NSLayoutConstraint" _trailingBarConstraint;
@"NSLayoutConstraint" _trailingBarNoItemsConstraint;
@"NSLayoutConstraint" _backButtonLeadingConstraint;
@"NSLayoutConstraint" _backButtonTrailingConstraint;
@"NSLayoutConstraint" _leadingBarAfterBackButtonConstraint;
@"NSLayoutConstraint" _largeTitleLeadingConstraint;
@"NSLayoutConstraint" _largeTitleTrailingConstraint;
@"NSLayoutConstraint" _regularTitleConstraint;
@"NSLayoutConstraint" _leadingBarWithTitleTrailingConstraint;
@"NSLayoutConstraint" _leadingBarWithNoTitleTrailingConstraint;
@"NSLayoutConstraint" _trailingBarWithTitleLeadingConstraint;
@"NSLayoutConstraint" _trailingBarWithNoTitleLeadingConstraint;
@"UIVisualEffectView" _backgroundView;
@"UIFocusContainerGuide" _focusContainerGuide;
@"NSArray" _debugViews;
```

## Properties

```
@property (TB,N,V_havePrepared) havePrepared;
@property (T@"UIView",&,N,V_contentView) contentView;
@property (T@"_UICarTitleView",&,N,V_titleView) titleView;
@property (T@"_UINavigationButtonBarWrapperView",&,N,V_leadingBarView) leadingBarView;
@property (T@"_UINavigationButtonBarWrapperView",&,N,V_trailingBarView) trailingBarView;
@property (T@"_UIButtonBarButton",&,N,V_backBarButton) backBarButton;
@property (T@"NSLayoutConstraint",&,N,V_leadingBarConstraint) leadingBarConstraint;
@property (T@"NSLayoutConstraint",&,N,V_leadingBarNoItemsConstraint) leadingBarNoItemsConstraint;
@property (T@"NSLayoutConstraint",&,N,V_trailingBarConstraint) trailingBarConstraint;
@property (T@"NSLayoutConstraint",&,N,V_trailingBarNoItemsConstraint) trailingBarNoItemsConstraint;
@property (T@"NSLayoutConstraint",&,N,V_backButtonLeadingConstraint) backButtonLeadingConstraint;
@property (T@"NSLayoutConstraint",&,N,V_backButtonTrailingConstraint) backButtonTrailingConstraint;
@property (T@"NSLayoutConstraint",&,N,V_leadingBarAfterBackButtonConstraint) leadingBarAfterBackButtonConstraint;
@property (T@"NSLayoutConstraint",&,N,V_largeTitleLeadingConstraint) largeTitleLeadingConstraint;
@property (T@"NSLayoutConstraint",&,N,V_largeTitleTrailingConstraint) largeTitleTrailingConstraint;
@property (T@"NSLayoutConstraint",&,N,V_regularTitleConstraint) regularTitleConstraint;
@property (T@"NSLayoutConstraint",&,N,V_leadingBarWithTitleTrailingConstraint) leadingBarWithTitleTrailingConstraint;
@property (T@"NSLayoutConstraint",&,N,V_leadingBarWithNoTitleTrailingConstraint) leadingBarWithNoTitleTrailingConstraint;
@property (T@"NSLayoutConstraint",&,N,V_trailingBarWithTitleLeadingConstraint) trailingBarWithTitleLeadingConstraint;
@property (T@"NSLayoutConstraint",&,N,V_trailingBarWithNoTitleLeadingConstraint) trailingBarWithNoTitleLeadingConstraint;
@property (T@"UIVisualEffectView",&,N,V_backgroundView) backgroundView;
@property (T@"UIFocusContainerGuide",&,N,V_focusContainerGuide) focusContainerGuide;
@property (T@"NSArray",&,N,V_debugViews) debugViews;
@property (T@"_UIScrollPocketInteraction",&,N,V_scrollPocketInteraction) scrollPocketInteraction;
@property (T@"_UIBarButtonItemAppearanceStorage",R,N,V_appearanceStorage) appearanceStorage;
@property (Tq,R,N) barType;
@property (TB,R,N,V_compactMetrics) compactMetrics;
@property (T@"UIColor",R,N) tintColor;
@property (TB,R,N) centerTextButtons;
@property (Td,R,N) defaultEdgeSpacing;
@property (Td,R,N) defaultTextPadding;
@property (Td,R,N) backButtonMargin;
@property (Td,R,N) backButtonMaximumWidth;
@property (T@"UIImageSymbolConfiguration",?,R,N) imageSymbolConfiguration;
@property (TB,?,R,N) _useLeadingAlignedTitle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) bounds;
```

## Instance methods

```
-[_UINavigationBarVisualProviderCarPlaySolarium backBarButton];
-[_UINavigationBarVisualProviderCarPlaySolarium focusContainerGuide];
-[_UINavigationBarVisualProviderCarPlaySolarium setTitleView:];
-[_UINavigationBarVisualProviderCarPlaySolarium edgesPaddingBarButtonItem:];
-[_UINavigationBarVisualProviderCarPlaySolarium setContentView:];
-[_UINavigationBarVisualProviderCarPlaySolarium setLeadingBarView:];
-[_UINavigationBarVisualProviderCarPlaySolarium navigationItemUpdatedNavigationBarVisibility:];
-[_UINavigationBarVisualProviderCarPlaySolarium navigationItemUpdatedCanvasView:];
-[_UINavigationBarVisualProviderCarPlaySolarium intrinsicContentSize];
-[_UINavigationBarVisualProviderCarPlaySolarium minimumTopPaddingWithTraitCollection:parentView:];
-[_UINavigationBarVisualProviderCarPlaySolarium defaultFontDescriptor];
-[_UINavigationBarVisualProviderCarPlaySolarium navigationItemUpdatedSearchController:oldSearchController:];
-[_UINavigationBarVisualProviderCarPlaySolarium backIndicatorMaskImage];
-[_UINavigationBarVisualProviderCarPlaySolarium setLargeTitleTrailingConstraint:];
-[_UINavigationBarVisualProviderCarPlaySolarium navigationItem:appearance:categoriesChanged:];
-[_UINavigationBarVisualProviderCarPlaySolarium presentHostedSearchWithTransitionCoordinator:];
-[_UINavigationBarVisualProviderCarPlaySolarium largeTitleLeadingConstraint];
-[_UINavigationBarVisualProviderCarPlaySolarium navigationItemUpdatedLargeTitleContent:];
-[_UINavigationBarVisualProviderCarPlaySolarium setLeadingBarWithTitleTrailingConstraint:];
-[_UINavigationBarVisualProviderCarPlaySolarium navigationItemUpdatedBackButtonContent:animated:];
-[_UINavigationBarVisualProviderCarPlaySolarium appearanceStorage];
-[_UINavigationBarVisualProviderCarPlaySolarium navigationBarInvalidatedResolvedLayoutMargins];
-[_UINavigationBarVisualProviderCarPlaySolarium setFocusContainerGuide:];
-[_UINavigationBarVisualProviderCarPlaySolarium trailingBarView];
-[_UINavigationBarVisualProviderCarPlaySolarium navigationItemUpdatedScrollEdgeProgress:];
-[_UINavigationBarVisualProviderCarPlaySolarium navigationItemUpdatedRightBarButtonItems:animated:];
-[_UINavigationBarVisualProviderCarPlaySolarium navigationItemUpdatedTitleContent:animated:];
-[_UINavigationBarVisualProviderCarPlaySolarium setBackBarButton:];
-[_UINavigationBarVisualProviderCarPlaySolarium absorptionForItem:];
-[_UINavigationBarVisualProviderCarPlaySolarium setTrailingBarNoItemsConstraint:];
-[_UINavigationBarVisualProviderCarPlaySolarium stackDidChangeFrom:];
-[_UINavigationBarVisualProviderCarPlaySolarium navigationItemUpdatedMinimumContentMargins:];
-[_UINavigationBarVisualProviderCarPlaySolarium trailingBarConstraint];
-[_UINavigationBarVisualProviderCarPlaySolarium _effectiveLayoutMargins];
-[_UINavigationBarVisualProviderCarPlaySolarium barMetrics];
-[_UINavigationBarVisualProviderCarPlaySolarium setTrailingBarView:];
-[_UINavigationBarVisualProviderCarPlaySolarium setLeadingBarConstraint:];
-[_UINavigationBarVisualProviderCarPlaySolarium setTrailingBarWithTitleLeadingConstraint:];
-[_UINavigationBarVisualProviderCarPlaySolarium updateProperties];
-[_UINavigationBarVisualProviderCarPlaySolarium setTrailingBarConstraint:];
-[_UINavigationBarVisualProviderCarPlaySolarium navigationItemUpdatedPromptContent:];
-[_UINavigationBarVisualProviderCarPlaySolarium backButtonMargin];
-[_UINavigationBarVisualProviderCarPlaySolarium backButtonLeadingConstraint];
-[_UINavigationBarVisualProviderCarPlaySolarium havePrepared];
-[_UINavigationBarVisualProviderCarPlaySolarium largeTitleTrailingConstraint];
-[_UINavigationBarVisualProviderCarPlaySolarium leadingBarView];
-[_UINavigationBarVisualProviderCarPlaySolarium sizeThatFits:];
-[_UINavigationBarVisualProviderCarPlaySolarium setDebugViews:];
-[_UINavigationBarVisualProviderCarPlaySolarium navigationItemIsTopItem:];
-[_UINavigationBarVisualProviderCarPlaySolarium setLargeTitleLeadingConstraint:];
-[_UINavigationBarVisualProviderCarPlaySolarium setBackButtonTrailingConstraint:];
-[_UINavigationBarVisualProviderCarPlaySolarium leadingBarConstraint];
-[_UINavigationBarVisualProviderCarPlaySolarium setupTopNavigationItem];
-[_UINavigationBarVisualProviderCarPlaySolarium prepare];
-[_UINavigationBarVisualProviderCarPlaySolarium leadingBarWithTitleTrailingConstraint];
-[_UINavigationBarVisualProviderCarPlaySolarium shouldSearchControllerDeferPresentationTransitionForNavigationItem:];
-[_UINavigationBarVisualProviderCarPlaySolarium prepareForPop];
-[_UINavigationBarVisualProviderCarPlaySolarium regularTitleConstraint];
-[_UINavigationBarVisualProviderCarPlaySolarium centerTextButtons];
-[_UINavigationBarVisualProviderCarPlaySolarium setLeadingBarNoItemsConstraint:];
-[_UINavigationBarVisualProviderCarPlaySolarium pushAnimated:completion:];
-[_UINavigationBarVisualProviderCarPlaySolarium leadingBarNoItemsConstraint];
-[_UINavigationBarVisualProviderCarPlaySolarium contentView];
-[_UINavigationBarVisualProviderCarPlaySolarium updateScrollPocketInteraction];
-[_UINavigationBarVisualProviderCarPlaySolarium setRegularTitleConstraint:];
-[_UINavigationBarVisualProviderCarPlaySolarium _updateContentForTopItem:backItem:animated:direction:];
-[_UINavigationBarVisualProviderCarPlaySolarium _updateContentAnimated:completion:direction:];
-[_UINavigationBarVisualProviderCarPlaySolarium changeAppearance];
-[_UINavigationBarVisualProviderCarPlaySolarium backgroundView];
-[_UINavigationBarVisualProviderCarPlaySolarium popAnimated:completion:];
-[_UINavigationBarVisualProviderCarPlaySolarium animateForSearchPresentation:];
-[_UINavigationBarVisualProviderCarPlaySolarium navigationItemUpdatedLeftBarButtonItems:animated:];
-[_UINavigationBarVisualProviderCarPlaySolarium traitCollectionDidChange:];
-[_UINavigationBarVisualProviderCarPlaySolarium dismissHostedSearchWithTransitionCoordinator:];
-[_UINavigationBarVisualProviderCarPlaySolarium titleView];
-[_UINavigationBarVisualProviderCarPlaySolarium _configureBackground];
-[_UINavigationBarVisualProviderCarPlaySolarium navigationItemUpdatedBackgroundAppearance:];
-[_UINavigationBarVisualProviderCarPlaySolarium updateTopNavigationItemAnimated:];
-[_UINavigationBarVisualProviderCarPlaySolarium leadingBarWithNoTitleTrailingConstraint];
-[_UINavigationBarVisualProviderCarPlaySolarium defaultEdgeSpacing];
-[_UINavigationBarVisualProviderCarPlaySolarium scrollPocketInteraction];
-[_UINavigationBarVisualProviderCarPlaySolarium navigationItemUpdatedLargeTitleDisplayMode:];
-[_UINavigationBarVisualProviderCarPlaySolarium defaultTextPadding];
-[_UINavigationBarVisualProviderCarPlaySolarium navigationItemSearchControllerReadyForDeferredAutomaticShowsScopeBar:];
-[_UINavigationBarVisualProviderCarPlaySolarium trailingBarNoItemsConstraint];
-[_UINavigationBarVisualProviderCarPlaySolarium navigationItemUpdatedBottomPalette:oldPalette:];
-[_UINavigationBarVisualProviderCarPlaySolarium trailingBarWithNoTitleLeadingConstraint];
-[_UINavigationBarVisualProviderCarPlaySolarium prepareForPush];
-[_UINavigationBarVisualProviderCarPlaySolarium backIndicatorImage];
-[_UINavigationBarVisualProviderCarPlaySolarium navigationItemUpdatedContentLayout:animated:];
-[_UINavigationBarVisualProviderCarPlaySolarium navigationItemIsBackItem:];
-[_UINavigationBarVisualProviderCarPlaySolarium teardown];
-[_UINavigationBarVisualProviderCarPlaySolarium setScrollPocketInteraction:];
-[_UINavigationBarVisualProviderCarPlaySolarium setBackgroundView:];
-[_UINavigationBarVisualProviderCarPlaySolarium __backButtonAction];
-[_UINavigationBarVisualProviderCarPlaySolarium isRTL];
-[_UINavigationBarVisualProviderCarPlaySolarium setLeadingBarWithNoTitleTrailingConstraint:];
-[_UINavigationBarVisualProviderCarPlaySolarium _installGradientLayerMaskForClippingView:];
-[_UINavigationBarVisualProviderCarPlaySolarium barType];
-[_UINavigationBarVisualProviderCarPlaySolarium compactMetrics];
-[_UINavigationBarVisualProviderCarPlaySolarium debugViews];
-[_UINavigationBarVisualProviderCarPlaySolarium setHavePrepared:];
-[_UINavigationBarVisualProviderCarPlaySolarium provideViewsForContents:topItem:backItem:];
-[_UINavigationBarVisualProviderCarPlaySolarium backButtonTrailingConstraint];
-[_UINavigationBarVisualProviderCarPlaySolarium trailingBarWithTitleLeadingConstraint];
-[_UINavigationBarVisualProviderCarPlaySolarium leadingBarAfterBackButtonConstraint];
-[_UINavigationBarVisualProviderCarPlaySolarium backButtonMaximumWidth];
-[_UINavigationBarVisualProviderCarPlaySolarium setBackButtonLeadingConstraint:];
-[_UINavigationBarVisualProviderCarPlaySolarium setTrailingBarWithNoTitleLeadingConstraint:];
-[_UINavigationBarVisualProviderCarPlaySolarium setLeadingBarAfterBackButtonConstraint:];
```
