# `_UINavigationBarVisualProviderLegacyIOS`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UINavigationBarVisualProvider`
- Protocols: `_UIBasicAnimationFactory`, `_UINavigationBarGestureHandlerDelegate`
- 17 instance variables, 4 properties, 98 instance methods, 0 class methods

## Instance variables

```
@"_UIBarBackground" _backgroundView;
@"_UIBarBackgroundLayoutLegacy" _backgroundViewLayout;
@"UIView" _customBackgroundView;
@"UIView" _titleView;
@"NSArray" _leftViews;
@"NSArray" _rightViews;
@"UIImageView" _backIndicatorView;
@"_UINavBarPrompt" _prompt;
@"_UINavigationBarGestureHandler" _gestureHandler;
@"NSMutableArray" _slideTransitionClippingViews;
@"<UIViewControllerTransitionCoordinator>" _transitionCoordinator;
@"_UINavigationBarLegacyContentView" _layoutView;
@"UIView" _contentView;
@"UILayoutGuide" _userContentGuide;
@"NSLayoutConstraint" _userContentGuideLeading;
@"NSLayoutConstraint" _userContentGuideTrailing;
@"UIFocusContainerGuide" _contentFocusContainerGuide;
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
-[_UINavigationBarVisualProviderLegacyIOS _shim_touchesMoved:withEvent:];
-[_UINavigationBarVisualProviderLegacyIOS backButtonViewAtPoint:];
-[_UINavigationBarVisualProviderLegacyIOS _handleMouseDownAtPoint:];
-[_UINavigationBarVisualProviderLegacyIOS _handleMouseUpAtPoint:];
-[_UINavigationBarVisualProviderLegacyIOS setBackButtonVisible:animated:];
-[_UINavigationBarVisualProviderLegacyIOS _shim_updateBackIndicator];
-[_UINavigationBarVisualProviderLegacyIOS _shim_userContentGuide];
-[_UINavigationBarVisualProviderLegacyIOS _shim_pressBackIndicator:initialPress:];
-[_UINavigationBarVisualProviderLegacyIOS invalidateIntrinsicContentSize];
-[_UINavigationBarVisualProviderLegacyIOS _completeNavigationTransitionWithIncomingViews:outgoingViews:transitionAssistant:completion:];
-[_UINavigationBarVisualProviderLegacyIOS _shim_setPromptText:animated:];
-[_UINavigationBarVisualProviderLegacyIOS _shim_popForCarplayPressAtFakePoint:];
-[_UINavigationBarVisualProviderLegacyIOS _subviewIndexAboveBackground];
-[_UINavigationBarVisualProviderLegacyIOS _shim_34415965];
-[_UINavigationBarVisualProviderLegacyIOS _completeTopItemTransitionWithIncomingViews:outgoingViews:previousLeftViews:previousRightViews:enableUserInteraction:transitionAssistant:];
-[_UINavigationBarVisualProviderLegacyIOS _effectiveBackIndicatorTransitionMaskImage];
-[_UINavigationBarVisualProviderLegacyIOS updateBackgroundGroupName];
-[_UINavigationBarVisualProviderLegacyIOS _shim_backgroundHeight];
-[_UINavigationBarVisualProviderLegacyIOS _getTitleViewFrame:leftViewFrames:rightViewFrames:forPreviousItem:item:];
-[_UINavigationBarVisualProviderLegacyIOS updateTopNavigationItemTitleView];
-[_UINavigationBarVisualProviderLegacyIOS _shim_customHitTest:forView:];
-[_UINavigationBarVisualProviderLegacyIOS layoutSubviews];
-[_UINavigationBarVisualProviderLegacyIOS _shim_throwConstraintExceptions];
-[_UINavigationBarVisualProviderLegacyIOS _shim_disableBlurTinting];
-[_UINavigationBarVisualProviderLegacyIOS _setUpContentFocusContainerGuide];
-[_UINavigationBarVisualProviderLegacyIOS _backButtonForBackItem:topItem:];
-[_UINavigationBarVisualProviderLegacyIOS intrinsicContentSizeInvalidatedForChildView:];
-[_UINavigationBarVisualProviderLegacyIOS _shim_30244716];
-[_UINavigationBarVisualProviderLegacyIOS setSemanticContentAttribute:];
-[_UINavigationBarVisualProviderLegacyIOS _updateBackground];
-[_UINavigationBarVisualProviderLegacyIOS canHandleStatusBarTouchAtPoint:];
-[_UINavigationBarVisualProviderLegacyIOS _shim_wantsCustomTouchHandlingForTouches:];
-[_UINavigationBarVisualProviderLegacyIOS sizeThatFits:];
-[_UINavigationBarVisualProviderLegacyIOS _preferredContentSizeForItem:];
-[_UINavigationBarVisualProviderLegacyIOS _shim_backdropStyle];
-[_UINavigationBarVisualProviderLegacyIOS _shouldPopForTouchAtPoint:];
-[_UINavigationBarVisualProviderLegacyIOS _shim_shadowAlpha];
-[_UINavigationBarVisualProviderLegacyIOS hitTest:defaultViewHit:];
-[_UINavigationBarVisualProviderLegacyIOS _shim_layoutView];
-[_UINavigationBarVisualProviderLegacyIOS setupTopNavigationItem];
-[_UINavigationBarVisualProviderLegacyIOS prepare];
-[_UINavigationBarVisualProviderLegacyIOS _shouldShowBackButtonForNavigationItem:];
-[_UINavigationBarVisualProviderLegacyIOS _shim_setDisableBlurTinting:];
-[_UINavigationBarVisualProviderLegacyIOS _shim_displayViewsIncludingHiddenBackButtonViews:];
-[_UINavigationBarVisualProviderLegacyIOS prepareForPop];
-[_UINavigationBarVisualProviderLegacyIOS _shim_touchesBegan:withEvent:];
-[_UINavigationBarVisualProviderLegacyIOS _contentViewFrameInBounds:style:];
-[_UINavigationBarVisualProviderLegacyIOS _suppressBackIndicator];
-[_UINavigationBarVisualProviderLegacyIOS pushAnimated:completion:];
-[_UINavigationBarVisualProviderLegacyIOS _updateBackIndicatorImage];
-[_UINavigationBarVisualProviderLegacyIOS _getLeftMargin:rightMargin:forNavigationItem:showingBackButton:visualStyle:];
-[_UINavigationBarVisualProviderLegacyIOS _updateBackIndicatorViewTintColor];
-[_UINavigationBarVisualProviderLegacyIOS _shim_107516167];
-[_UINavigationBarVisualProviderLegacyIOS _setViewsAnimated:forTopNavigationItem:backNavigationItem:previousTopItem:];
-[_UINavigationBarVisualProviderLegacyIOS changeAppearance];
-[_UINavigationBarVisualProviderLegacyIOS popAnimated:completion:];
-[_UINavigationBarVisualProviderLegacyIOS gestureRecognizerShouldBegin:defaultAnswer:];
-[_UINavigationBarVisualProviderLegacyIOS _shim_promptText];
-[_UINavigationBarVisualProviderLegacyIOS _popForTouchAtPoint:];
-[_UINavigationBarVisualProviderLegacyIOS _shim_updateUserContentGuideForTopItem:backItem:];
-[_UINavigationBarVisualProviderLegacyIOS _shim_backIndicatorView];
-[_UINavigationBarVisualProviderLegacyIOS _shim_touchesCancelled:withEvent:];
-[_UINavigationBarVisualProviderLegacyIOS traitCollectionDidChange:];
-[_UINavigationBarVisualProviderLegacyIOS _shim_touchesEnded:withEvent:];
-[_UINavigationBarVisualProviderLegacyIOS updateTopNavigationItemAnimated:];
-[_UINavigationBarVisualProviderLegacyIOS _shim_setUseContentView:];
-[_UINavigationBarVisualProviderLegacyIOS _layoutSubviewsFromContentView];
-[_UINavigationBarVisualProviderLegacyIOS _effectiveBackIndicatorImage];
-[_UINavigationBarVisualProviderLegacyIOS _wrapView:inClippingViewWithLeftBoundary:rightBoundary:leftMaskImage:leftMaskIsChevron:rightMaskImage:];
-[_UINavigationBarVisualProviderLegacyIOS _startPushAnimationFromOldBackItem:oldTopItem:newBackItem:newTopItem:withTransitionAssistant:completion:];
-[_UINavigationBarVisualProviderLegacyIOS _getTitleViewFrame:leftViewFrames:rightViewFrames:forPreviousItem:item:returnedIdealWidthOfTextContent:availableLayoutWidthForTextContent:idealBackButtonWidth:];
-[_UINavigationBarVisualProviderLegacyIOS _navigationItemAtPoint:];
-[_UINavigationBarVisualProviderLegacyIOS prepareForPush];
-[_UINavigationBarVisualProviderLegacyIOS updateArchivedSubviews:];
-[_UINavigationBarVisualProviderLegacyIOS barSizeChanged];
-[_UINavigationBarVisualProviderLegacyIOS _timingFunctionForAnimationInView:withKeyPath:];
-[_UINavigationBarVisualProviderLegacyIOS statusBarStyle];
-[_UINavigationBarVisualProviderLegacyIOS frameOriginForStatusBarLocatedAt:];
-[_UINavigationBarVisualProviderLegacyIOS gestureHandler:recognizedPopAtLocation:];
-[_UINavigationBarVisualProviderLegacyIOS preferredFocusedView];
-[_UINavigationBarVisualProviderLegacyIOS _shim_updateBackgroundViewIgnoringFlag];
-[_UINavigationBarVisualProviderLegacyIOS teardown];
-[_UINavigationBarVisualProviderLegacyIOS _shim_compatibilityBackgroundView];
-[_UINavigationBarVisualProviderLegacyIOS _shim_setShadowAlpha:];
-[_UINavigationBarVisualProviderLegacyIOS _shim_setCustomBackgroundView:];
-[_UINavigationBarVisualProviderLegacyIOS _backTitleWidthOverTitleWidthForMatchingBackButtonView:titleView:withBackButtonWidth:];
-[_UINavigationBarVisualProviderLegacyIOS _startPopAnimationFromOldBackItem:oldTopItem:newBackItem:newTopItem:withTransitionAssistant:completion:];
-[_UINavigationBarVisualProviderLegacyIOS _supportsCanvasView];
-[_UINavigationBarVisualProviderLegacyIOS removeContentForItem:];
-[_UINavigationBarVisualProviderLegacyIOS _basicAnimationForView:withKeyPath:];
-[_UINavigationBarVisualProviderLegacyIOS _backIndicatorClippingMargin];
-[_UINavigationBarVisualProviderLegacyIOS _effectiveBackIndicatorLeftMargin];
-[_UINavigationBarVisualProviderLegacyIOS _layoutInBounds:withVisualStyle:];
-[_UINavigationBarVisualProviderLegacyIOS _shim_contentView];
-[_UINavigationBarVisualProviderLegacyIOS provideViewsForContents:topItem:backItem:];
-[_UINavigationBarVisualProviderLegacyIOS shouldGestureHandler:recognizedPopAtLocation:];
-[_UINavigationBarVisualProviderLegacyIOS _defaultTitleFontForItem:fittingHeight:withScaleAdjustment:];
-[_UINavigationBarVisualProviderLegacyIOS shouldUseHeightRangeFittingWidth];
```
