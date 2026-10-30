# `UIAlertControllerVisualStyle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 5 instance variables, 5 properties, 99 instance methods, 2 class methods

## Instance variables

```
@"UIAlertControllerDescriptor" _descriptor;
q _forcedInterfaceIdiom;
@"UIInterfaceActionVisualStyle" _interfaceActionVisualStyle;
@"UITraitCollection" _traitCollection;
@"UIWindow" _window;
```

## Properties

```
@property (Tq,N,V_forcedInterfaceIdiom) forcedInterfaceIdiom;
@property (T@"UIInterfaceActionVisualStyle",R,N,V_interfaceActionVisualStyle) interfaceActionVisualStyle;
@property (T@"UITraitCollection",&,N,V_traitCollection) traitCollection;
@property (T@"UIWindow",W,N,V_window) window;
@property (T@"UIAlertControllerDescriptor",&,N,V_descriptor) descriptor;
```

## Class methods

```
+[UIAlertControllerVisualStyle interfaceActionPresentationStyle];
+[UIAlertControllerVisualStyle positionContentsOfAlertController:alertContentView:availableSpaceView:visualStyle:updatableConstraints:];
```

## Instance methods

```
-[UIAlertControllerVisualStyle titleLabelColor];
-[UIAlertControllerVisualStyle _topItemsViewBottomMargin];
-[UIAlertControllerVisualStyle titleLabelFont];
-[UIAlertControllerVisualStyle placementAvoidsKeyboard];
-[UIAlertControllerVisualStyle marginAboveTitleLabelFirstBaseline];
-[UIAlertControllerVisualStyle permittedActionLayoutDirection];
-[UIAlertControllerVisualStyle marginBelowMessageLabelLastBaseline];
-[UIAlertControllerVisualStyle messageLabelColor];
-[UIAlertControllerVisualStyle marginAboveMessageLabelFirstBaseline];
-[UIAlertControllerVisualStyle transitionDurationForPresentation:ofAlertController:];
-[UIAlertControllerVisualStyle _shouldApplyGlassToAlertView];
-[UIAlertControllerVisualStyle _spacingBetweenDismissButtonAndContent];
-[UIAlertControllerVisualStyle marginBelowTitleLabelLastBaseline];
-[UIAlertControllerVisualStyle setDescriptor:];
-[UIAlertControllerVisualStyle marginBelowLastLabelLastBaseline];
-[UIAlertControllerVisualStyle hideCancelAction:inAlertController:];
-[UIAlertControllerVisualStyle contentInsetsForContainerView:];
-[UIAlertControllerVisualStyle maximumWidth];
-[UIAlertControllerVisualStyle _marginBelowDetailMessage];
-[UIAlertControllerVisualStyle setTraitCollection:];
-[UIAlertControllerVisualStyle contentHasShadow];
-[UIAlertControllerVisualStyle contentBackdropView];
-[UIAlertControllerVisualStyle minimumWidth];
-[UIAlertControllerVisualStyle transitionOfType:shouldBeInteractiveForAlertController:];
-[UIAlertControllerVisualStyle descriptor];
-[UIAlertControllerVisualStyle traitCollection];
-[UIAlertControllerVisualStyle shouldRespectContentViewControllerClippingPreference];
-[UIAlertControllerVisualStyle init];
-[UIAlertControllerVisualStyle _minimumSpacingAboveTopmostLabelSafeAscender];
-[UIAlertControllerVisualStyle _labelHorizontalInsets];
-[UIAlertControllerVisualStyle shouldCenterVertically];
-[UIAlertControllerVisualStyle dimmingViewForAlertController:];
-[UIAlertControllerVisualStyle messageCompositingFilter];
-[UIAlertControllerVisualStyle textFieldHorizontalMargin];
-[UIAlertControllerVisualStyle _marginAroundActionGroup];
-[UIAlertControllerVisualStyle window];
-[UIAlertControllerVisualStyle contentShadowOpacity];
-[UIAlertControllerVisualStyle _marginAboveDetailMessageFirstBaseline];
-[UIAlertControllerVisualStyle tintColorForAlertController:];
-[UIAlertControllerVisualStyle _keyCommandInputForCancelAction];
-[UIAlertControllerVisualStyle textFieldContentInset];
-[UIAlertControllerVisualStyle vibrancyEffectForTitleAndMessageLabel];
-[UIAlertControllerVisualStyle actionWidthForMinimumActionWidth:availableWidth:];
-[UIAlertControllerVisualStyle textFieldContainingViewWithTextField:position:];
-[UIAlertControllerVisualStyle actionSequenceEdgeInsets];
-[UIAlertControllerVisualStyle animateRevealOfAlertControllerView:alertController:inContainerView:duration:completionBlock:];
-[UIAlertControllerVisualStyle shouldPreserveRespondersAcrossWindows];
-[UIAlertControllerVisualStyle configureAttributesForTitleLabel:classificationLabel:actionViewState:];
-[UIAlertControllerVisualStyle minimumWidthFittingContentView:titleLabel:minimumWidthForAllActions:preferredSizeForContentContainers:];
-[UIAlertControllerVisualStyle contentShadowRadius];
-[UIAlertControllerVisualStyle maximumContentHeight];
-[UIAlertControllerVisualStyle _shouldReverseActions];
-[UIAlertControllerVisualStyle contentClipsToBounds];
-[UIAlertControllerVisualStyle contentShadowColor];
-[UIAlertControllerVisualStyle configureAttributesForImageView:imageProperty:actionViewState:];
-[UIAlertControllerVisualStyle contentCornerRadius];
-[UIAlertControllerVisualStyle shouldOccludeDuringPresentation];
-[UIAlertControllerVisualStyle animateAlertControllerView:ofAlertController:forPresentation:inContainerView:descendantOfContainerView:duration:completionBlock:];
-[UIAlertControllerVisualStyle focusAvoidsNonDefaultActionsIfPossible];
-[UIAlertControllerVisualStyle preferredActionForActions:suggestedPreferredAction:];
-[UIAlertControllerVisualStyle minimumContentHeight];
-[UIAlertControllerVisualStyle accessibilityWidth];
-[UIAlertControllerVisualStyle maximumNumberOfLinesInMessageLabel];
-[UIAlertControllerVisualStyle minimumActionContentSize];
-[UIAlertControllerVisualStyle maximumWidthForTitleAndMessageContentView];
-[UIAlertControllerVisualStyle messageLabelFont];
-[UIAlertControllerVisualStyle copyWithZone:];
-[UIAlertControllerVisualStyle isEqual:];
-[UIAlertControllerVisualStyle _detailMessageFont];
-[UIAlertControllerVisualStyle setWindow:];
-[UIAlertControllerVisualStyle interactionProgressForTransitionOfType:forAlertController:];
-[UIAlertControllerVisualStyle contentShadowOffset];
-[UIAlertControllerVisualStyle definesWidthByContentFitting];
-[UIAlertControllerVisualStyle contentHorizontalMargin];
-[UIAlertControllerVisualStyle maximumNumberOfLinesInTitleLabel];
-[UIAlertControllerVisualStyle _scaledMarginBelowDetailMessage];
-[UIAlertControllerVisualStyle _reloadInterfaceActionVisualStyle];
-[UIAlertControllerVisualStyle _scaledMarginAboveDetailMessageFirstBaseline];
-[UIAlertControllerVisualStyle _scaledMarginAboveMessageLabelFirstBaseline];
-[UIAlertControllerVisualStyle _scaledMarginAboveTitleLabelFirstBaselineInAlertControllerView:titleText:];
-[UIAlertControllerVisualStyle _scaledMarginBelowLastLabelLastBaseline];
-[UIAlertControllerVisualStyle _scaledMarginBelowMessageLabelLastBaseline];
-[UIAlertControllerVisualStyle _scaledMarginBelowTitleLabelLastBaseline];
-[UIAlertControllerVisualStyle _scaledMessageSafeBaselineHeightInAlertControllerView:];
-[UIAlertControllerVisualStyle _scaledSafeBaselineHeightForLabelFont:inAlertControllerView:];
-[UIAlertControllerVisualStyle _scaledTitleLabelSafeBaselineHeightInAlertControllerView:];
-[UIAlertControllerVisualStyle actionImageMarginForAction];
-[UIAlertControllerVisualStyle actionSpacingForHorizontalLayout:];
-[UIAlertControllerVisualStyle collectionViewOutsetSize];
-[UIAlertControllerVisualStyle contentCornerCurve];
-[UIAlertControllerVisualStyle contentVerticalMargin];
-[UIAlertControllerVisualStyle defaultActionFont];
-[UIAlertControllerVisualStyle forcedInterfaceIdiom];
-[UIAlertControllerVisualStyle interfaceActionVisualStyle];
-[UIAlertControllerVisualStyle interfaceActionVisualStyleClassForManagingConcreteVisualStyle];
-[UIAlertControllerVisualStyle preferredActionFont];
-[UIAlertControllerVisualStyle regularActionFont];
-[UIAlertControllerVisualStyle setForcedInterfaceIdiom:];
-[UIAlertControllerVisualStyle textFieldCornerRadius];
```
