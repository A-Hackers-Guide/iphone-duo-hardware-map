# `_UINavigationBarVisualProviderModernCarPlay`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UINavigationBarVisualProvider`
- Protocols: `_UIButtonBarAppearanceDelegate`, `_UINavigationItemChangeObserver`
- 23 instance variables, 37 properties, 100 instance methods, 0 class methods

## Instance variables

```
B _compactMetrics;
B _havePrepared;
@"_UIBarButtonItemAppearanceStorage" _appearanceStorage;
@"UIView" _contentView;
@"_UICarTitleView" _titleView;
@"_UIButtonBar" _leadingBar;
@"_UIButtonBar" _trailingBar;
@"_UIButtonBarButton" _backBarButton;
@"NSLayoutConstraint" _leadingBarConstraint;
@"NSLayoutConstraint" _leadingBarNoItemsConstraint;
@"NSLayoutConstraint" _trailingBarConstraint;
@"NSLayoutConstraint" _trailingBarNoItemsConstraint;
@"NSArray" _backButtonConstraints;
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
@property (T@"_UIButtonBar",&,N,V_leadingBar) leadingBar;
@property (T@"_UIButtonBar",&,N,V_trailingBar) trailingBar;
@property (T@"_UIButtonBarButton",&,N,V_backBarButton) backBarButton;
@property (T@"NSLayoutConstraint",&,N,V_leadingBarConstraint) leadingBarConstraint;
@property (T@"NSLayoutConstraint",&,N,V_leadingBarNoItemsConstraint) leadingBarNoItemsConstraint;
@property (T@"NSLayoutConstraint",&,N,V_trailingBarConstraint) trailingBarConstraint;
@property (T@"NSLayoutConstraint",&,N,V_trailingBarNoItemsConstraint) trailingBarNoItemsConstraint;
@property (T@"NSArray",&,N,V_backButtonConstraints) backButtonConstraints;
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
-[_UINavigationBarVisualProviderModernCarPlay backBarButton];
-[_UINavigationBarVisualProviderModernCarPlay trailingBar];
-[_UINavigationBarVisualProviderModernCarPlay focusContainerGuide];
-[_UINavigationBarVisualProviderModernCarPlay setTitleView:];
-[_UINavigationBarVisualProviderModernCarPlay edgesPaddingBarButtonItem:];
-[_UINavigationBarVisualProviderModernCarPlay setContentView:];
-[_UINavigationBarVisualProviderModernCarPlay navigationItemUpdatedNavigationBarVisibility:];
-[_UINavigationBarVisualProviderModernCarPlay navigationItemUpdatedCanvasView:];
-[_UINavigationBarVisualProviderModernCarPlay intrinsicContentSize];
-[_UINavigationBarVisualProviderModernCarPlay defaultFontDescriptor];
-[_UINavigationBarVisualProviderModernCarPlay navigationItemUpdatedSearchController:oldSearchController:];
-[_UINavigationBarVisualProviderModernCarPlay backIndicatorMaskImage];
-[_UINavigationBarVisualProviderModernCarPlay setLargeTitleTrailingConstraint:];
-[_UINavigationBarVisualProviderModernCarPlay navigationItem:appearance:categoriesChanged:];
-[_UINavigationBarVisualProviderModernCarPlay presentHostedSearchWithTransitionCoordinator:];
-[_UINavigationBarVisualProviderModernCarPlay largeTitleLeadingConstraint];
-[_UINavigationBarVisualProviderModernCarPlay navigationItemUpdatedLargeTitleContent:];
-[_UINavigationBarVisualProviderModernCarPlay setLeadingBarWithTitleTrailingConstraint:];
-[_UINavigationBarVisualProviderModernCarPlay navigationItemUpdatedBackButtonContent:animated:];
-[_UINavigationBarVisualProviderModernCarPlay setLeadingBar:];
-[_UINavigationBarVisualProviderModernCarPlay appearanceStorage];
-[_UINavigationBarVisualProviderModernCarPlay navigationBarInvalidatedResolvedLayoutMargins];
-[_UINavigationBarVisualProviderModernCarPlay setFocusContainerGuide:];
-[_UINavigationBarVisualProviderModernCarPlay navigationItemUpdatedScrollEdgeProgress:];
-[_UINavigationBarVisualProviderModernCarPlay navigationItemUpdatedRightBarButtonItems:animated:];
-[_UINavigationBarVisualProviderModernCarPlay navigationItemUpdatedTitleContent:animated:];
-[_UINavigationBarVisualProviderModernCarPlay setBackBarButton:];
-[_UINavigationBarVisualProviderModernCarPlay leadingBar];
-[_UINavigationBarVisualProviderModernCarPlay absorptionForItem:];
-[_UINavigationBarVisualProviderModernCarPlay setTrailingBarNoItemsConstraint:];
-[_UINavigationBarVisualProviderModernCarPlay stackDidChangeFrom:];
-[_UINavigationBarVisualProviderModernCarPlay trailingBarConstraint];
-[_UINavigationBarVisualProviderModernCarPlay backButtonConstraints];
-[_UINavigationBarVisualProviderModernCarPlay barMetrics];
-[_UINavigationBarVisualProviderModernCarPlay setLeadingBarConstraint:];
-[_UINavigationBarVisualProviderModernCarPlay setTrailingBarWithTitleLeadingConstraint:];
-[_UINavigationBarVisualProviderModernCarPlay setTrailingBarConstraint:];
-[_UINavigationBarVisualProviderModernCarPlay navigationItemUpdatedPromptContent:];
-[_UINavigationBarVisualProviderModernCarPlay backButtonMargin];
-[_UINavigationBarVisualProviderModernCarPlay havePrepared];
-[_UINavigationBarVisualProviderModernCarPlay largeTitleTrailingConstraint];
-[_UINavigationBarVisualProviderModernCarPlay sizeThatFits:];
-[_UINavigationBarVisualProviderModernCarPlay setDebugViews:];
-[_UINavigationBarVisualProviderModernCarPlay navigationItemIsTopItem:];
-[_UINavigationBarVisualProviderModernCarPlay setLargeTitleLeadingConstraint:];
-[_UINavigationBarVisualProviderModernCarPlay leadingBarConstraint];
-[_UINavigationBarVisualProviderModernCarPlay setupTopNavigationItem];
-[_UINavigationBarVisualProviderModernCarPlay prepare];
-[_UINavigationBarVisualProviderModernCarPlay leadingBarWithTitleTrailingConstraint];
-[_UINavigationBarVisualProviderModernCarPlay shouldSearchControllerDeferPresentationTransitionForNavigationItem:];
-[_UINavigationBarVisualProviderModernCarPlay prepareForPop];
-[_UINavigationBarVisualProviderModernCarPlay regularTitleConstraint];
-[_UINavigationBarVisualProviderModernCarPlay centerTextButtons];
-[_UINavigationBarVisualProviderModernCarPlay setLeadingBarNoItemsConstraint:];
-[_UINavigationBarVisualProviderModernCarPlay pushAnimated:completion:];
-[_UINavigationBarVisualProviderModernCarPlay leadingBarNoItemsConstraint];
-[_UINavigationBarVisualProviderModernCarPlay contentView];
-[_UINavigationBarVisualProviderModernCarPlay setRegularTitleConstraint:];
-[_UINavigationBarVisualProviderModernCarPlay _updateContentForTopItem:backItem:animated:direction:];
-[_UINavigationBarVisualProviderModernCarPlay _updateContentAnimated:completion:direction:];
-[_UINavigationBarVisualProviderModernCarPlay changeAppearance];
-[_UINavigationBarVisualProviderModernCarPlay backgroundView];
-[_UINavigationBarVisualProviderModernCarPlay popAnimated:completion:];
-[_UINavigationBarVisualProviderModernCarPlay animateForSearchPresentation:];
-[_UINavigationBarVisualProviderModernCarPlay setBackButtonConstraints:];
-[_UINavigationBarVisualProviderModernCarPlay navigationItemUpdatedLeftBarButtonItems:animated:];
-[_UINavigationBarVisualProviderModernCarPlay tintColor];
-[_UINavigationBarVisualProviderModernCarPlay traitCollectionDidChange:];
-[_UINavigationBarVisualProviderModernCarPlay dismissHostedSearchWithTransitionCoordinator:];
-[_UINavigationBarVisualProviderModernCarPlay titleView];
-[_UINavigationBarVisualProviderModernCarPlay _configureBackground];
-[_UINavigationBarVisualProviderModernCarPlay navigationItemUpdatedBackgroundAppearance:];
-[_UINavigationBarVisualProviderModernCarPlay setTrailingBar:];
-[_UINavigationBarVisualProviderModernCarPlay updateTopNavigationItemAnimated:];
-[_UINavigationBarVisualProviderModernCarPlay leadingBarWithNoTitleTrailingConstraint];
-[_UINavigationBarVisualProviderModernCarPlay defaultEdgeSpacing];
-[_UINavigationBarVisualProviderModernCarPlay navigationItemUpdatedLargeTitleDisplayMode:];
-[_UINavigationBarVisualProviderModernCarPlay defaultTextPadding];
-[_UINavigationBarVisualProviderModernCarPlay navigationItemSearchControllerReadyForDeferredAutomaticShowsScopeBar:];
-[_UINavigationBarVisualProviderModernCarPlay trailingBarNoItemsConstraint];
-[_UINavigationBarVisualProviderModernCarPlay navigationItemUpdatedBottomPalette:oldPalette:];
-[_UINavigationBarVisualProviderModernCarPlay trailingBarWithNoTitleLeadingConstraint];
-[_UINavigationBarVisualProviderModernCarPlay prepareForPush];
-[_UINavigationBarVisualProviderModernCarPlay backIndicatorImage];
-[_UINavigationBarVisualProviderModernCarPlay navigationItemUpdatedContentLayout:animated:];
-[_UINavigationBarVisualProviderModernCarPlay navigationItemIsBackItem:];
-[_UINavigationBarVisualProviderModernCarPlay teardown];
-[_UINavigationBarVisualProviderModernCarPlay setBackgroundView:];
-[_UINavigationBarVisualProviderModernCarPlay __backButtonAction];
-[_UINavigationBarVisualProviderModernCarPlay isRTL];
-[_UINavigationBarVisualProviderModernCarPlay setLeadingBarWithNoTitleTrailingConstraint:];
-[_UINavigationBarVisualProviderModernCarPlay _installGradientLayerMaskForClippingView:];
-[_UINavigationBarVisualProviderModernCarPlay barType];
-[_UINavigationBarVisualProviderModernCarPlay compactMetrics];
-[_UINavigationBarVisualProviderModernCarPlay debugViews];
-[_UINavigationBarVisualProviderModernCarPlay setHavePrepared:];
-[_UINavigationBarVisualProviderModernCarPlay provideViewsForContents:topItem:backItem:];
-[_UINavigationBarVisualProviderModernCarPlay trailingBarWithTitleLeadingConstraint];
-[_UINavigationBarVisualProviderModernCarPlay backButtonMaximumWidth];
-[_UINavigationBarVisualProviderModernCarPlay setTrailingBarWithNoTitleLeadingConstraint:];
```
