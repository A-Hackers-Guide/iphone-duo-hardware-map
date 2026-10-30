# `UIInterfaceActionRepresentationView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIFocusEnvironment`, `UISpringLoadedInteractionSupporting`, `UIInterfaceActionDisplayPropertyObserver`
- 19 instance variables, 25 properties, 82 instance methods, 0 class methods

## Instance variables

```
B _hasLoadedBackgroundView;
B _canKeepContentsInHierarchy;
B _hasLoadedContentFirstTime;
B _enforcedCanRemoveContentFromHierarchyWhenNotVisible;
B _enforcedCanRemoveContentFromHierarchyWhenNotVisibleValue;
B _contentsInsertedIntoViewHierarchy;
B _ownsActionContent;
B _highlighted;
B _pressed;
B _canRemoveContentFromHierarchyWhenNotVisible;
@"UIInterfaceAction" _action;
Q _visualCornerPosition;
@ _actionViewStateContext;
@"NSLayoutConstraint" _minimumWidthConstraint;
@"NSLayoutConstraint" _minimumHeightConstraint;
@"NSArray" _viewsToDisappearWhenHighlighted;
@"NSString" _sectionID;
@"UIView<UIInterfaceActionVisualBackgroundDisplaying>" _backgroundHighlightView;
@"UISpringLoadedInteraction" _interactionForSpringLoading;
```

## Properties

```
@property (T@"NSLayoutConstraint",R,N,V_minimumWidthConstraint) minimumWidthConstraint;
@property (T@"NSLayoutConstraint",R,N,V_minimumHeightConstraint) minimumHeightConstraint;
@property (T@"NSArray",&,N,V_viewsToDisappearWhenHighlighted) viewsToDisappearWhenHighlighted;
@property (TB,N,V_canRemoveContentFromHierarchyWhenNotVisible) canRemoveContentFromHierarchyWhenNotVisible;
@property (T@"NSString",&,N,V_sectionID) sectionID;
@property (TB,N,S_setContentsInsertedIntoViewHierarchy:,V_contentsInsertedIntoViewHierarchy) _contentsInsertedIntoViewHierarchy;
@property (T@"UIView<UIInterfaceActionVisualBackgroundDisplaying>",R,N,V_backgroundHighlightView) backgroundHighlightView;
@property (T@"UISpringLoadedInteraction",&,N,V_interactionForSpringLoading) interactionForSpringLoading;
@property (T@"UIInterfaceAction",R,N,V_action) action;
@property (T@"UIInterfaceActionVisualStyle",R,N) visualStyle;
@property (TB,N,V_ownsActionContent) ownsActionContent;
@property (TQ,N,V_visualCornerPosition) visualCornerPosition;
@property (TB,N,GisHighlighted,V_highlighted) highlighted;
@property (TB,N,GisPressed,V_pressed) pressed;
@property (T@,&,N,V_actionViewStateContext) actionViewStateContext;
@property (T@"NSArray",R,C,N) preferredFocusEnvironments;
@property (T@"<UIFocusEnvironment>",R,W,N) parentFocusEnvironment;
@property (T@"<UIFocusItemContainer>",R,N) focusItemContainer;
@property (T@"UIView",?,R,W,N) preferredFocusedView;
@property (T@"NSString",?,R,C,N) focusGroupIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,D,N,GisSpringLoaded) springLoaded;
```

## Instance methods

```
-[UIInterfaceActionRepresentationView setSpringLoaded:];
-[UIInterfaceActionRepresentationView isSpringLoaded];
-[UIInterfaceActionRepresentationView setSectionID:];
-[UIInterfaceActionRepresentationView updateContentsInsertedIntoHierarchy];
-[UIInterfaceActionRepresentationView intrinsicContentSize];
-[UIInterfaceActionRepresentationView invalidateIntrinsicContentSize];
-[UIInterfaceActionRepresentationView visualCornerPosition];
-[UIInterfaceActionRepresentationView sectionID];
-[UIInterfaceActionRepresentationView visualStyle];
-[UIInterfaceActionRepresentationView setVisualCornerPosition:];
-[UIInterfaceActionRepresentationView didUpdateFocusInContext:withAnimationCoordinator:];
-[UIInterfaceActionRepresentationView pressesCancelled:withEvent:];
-[UIInterfaceActionRepresentationView isHighlighted];
-[UIInterfaceActionRepresentationView pressesEnded:withEvent:];
-[UIInterfaceActionRepresentationView dealloc];
-[UIInterfaceActionRepresentationView layoutSubviews];
-[UIInterfaceActionRepresentationView layoutMarginsDidChange];
-[UIInterfaceActionRepresentationView action];
-[UIInterfaceActionRepresentationView isFocused];
-[UIInterfaceActionRepresentationView minimumWidthConstraint];
-[UIInterfaceActionRepresentationView canBecomeFocused];
-[UIInterfaceActionRepresentationView pressesBegan:withEvent:];
-[UIInterfaceActionRepresentationView pressesChanged:withEvent:];
-[UIInterfaceActionRepresentationView sizeThatFits:];
-[UIInterfaceActionRepresentationView initWithAction:];
-[UIInterfaceActionRepresentationView setHighlighted:];
-[UIInterfaceActionRepresentationView _applyVisualStyle];
-[UIInterfaceActionRepresentationView isPressed];
-[UIInterfaceActionRepresentationView _fittingContentSizingView];
-[UIInterfaceActionRepresentationView description];
-[UIInterfaceActionRepresentationView interfaceAction:reloadDisplayedContentVisualStyle:];
-[UIInterfaceActionRepresentationView updateConstraints];
-[UIInterfaceActionRepresentationView hasLayoutHeightConstraintsIdenticalToRepresentationView:];
-[UIInterfaceActionRepresentationView actionViewStateContext];
-[UIInterfaceActionRepresentationView systemLayoutSizeFittingSize:withHorizontalFittingPriority:verticalFittingPriority:];
-[UIInterfaceActionRepresentationView interfaceAction:reloadDisplayedContentActionProperties:];
-[UIInterfaceActionRepresentationView minimumHeightConstraint];
-[UIInterfaceActionRepresentationView setPressed:];
-[UIInterfaceActionRepresentationView setInteractionForSpringLoading:];
-[UIInterfaceActionRepresentationView viewsToDisappearWhenHighlighted];
-[UIInterfaceActionRepresentationView __fittingContentSizingViewAllowingSelf];
-[UIInterfaceActionRepresentationView __fittingContentSizingViewIfNotSelf];
-[UIInterfaceActionRepresentationView _actionViewState];
-[UIInterfaceActionRepresentationView _addLoadedContentsToHierarchyFirstTime];
-[UIInterfaceActionRepresentationView _addLoadedContentsToHierarchyIfAllowed];
-[UIInterfaceActionRepresentationView _applyVisualStyleToBackgroundViewAndHighlighting];
-[UIInterfaceActionRepresentationView _applyVisualStyleToLayoutMargins];
-[UIInterfaceActionRepresentationView _applyVisualStyleToMinimumSizeConstraints];
-[UIInterfaceActionRepresentationView _canLoadContentsIntoHierarchy];
-[UIInterfaceActionRepresentationView _clearBackgroundPressedState];
-[UIInterfaceActionRepresentationView _contentsInsertedIntoViewHierarchy];
-[UIInterfaceActionRepresentationView _didScroll];
-[UIInterfaceActionRepresentationView _enforceActionRepresentationViewsCanRemoveContentFromHierarchyWhenNotVisible:];
-[UIInterfaceActionRepresentationView _fittingContentSizeWithFittingViewSize:];
-[UIInterfaceActionRepresentationView _fittingContentSizingViewFrameInBounds:];
-[UIInterfaceActionRepresentationView _fittingContentSizingViewMargins];
-[UIInterfaceActionRepresentationView _fittingContentViewHasItsOwnActiveMinimumSizeConstraintsWithSize:];
-[UIInterfaceActionRepresentationView _handleVisualFeedbackForPress:pressed:];
-[UIInterfaceActionRepresentationView _initializeHorizontalMarginsForAction];
-[UIInterfaceActionRepresentationView _isVisibleWithinContainmentAncestor];
-[UIInterfaceActionRepresentationView _loadContentsIntoHierarchyAndPrepareIfNecessary];
-[UIInterfaceActionRepresentationView _reloadBackgroundHighlightView];
-[UIInterfaceActionRepresentationView _removeLoadedContentsFromHierarchyIfNotVisible];
-[UIInterfaceActionRepresentationView _setContentsInsertedIntoViewHierarchy:];
-[UIInterfaceActionRepresentationView _setHorizontalMargins:preservesSuperviewLayoutMargins:];
-[UIInterfaceActionRepresentationView _shouldShowPressFeedbackForEventWithPresses:];
-[UIInterfaceActionRepresentationView _showVisualFeedbackForPressed:];
-[UIInterfaceActionRepresentationView _showsFocusForFocusedView:];
-[UIInterfaceActionRepresentationView _updateFittingContentSizingViewToFitSize];
-[UIInterfaceActionRepresentationView _updateHighlightAndPressedFeedback];
-[UIInterfaceActionRepresentationView _updateLoadedContentsHierarchyByInsertingOrRemovingIfNecessary];
-[UIInterfaceActionRepresentationView _viewDisplayingBackground];
-[UIInterfaceActionRepresentationView backgroundHighlightView];
-[UIInterfaceActionRepresentationView canRemoveContentFromHierarchyWhenNotVisible];
-[UIInterfaceActionRepresentationView interactionForSpringLoading];
-[UIInterfaceActionRepresentationView invokeInterfaceAction];
-[UIInterfaceActionRepresentationView loadContents];
-[UIInterfaceActionRepresentationView ownsActionContent];
-[UIInterfaceActionRepresentationView setActionViewStateContext:];
-[UIInterfaceActionRepresentationView setCanRemoveContentFromHierarchyWhenNotVisible:];
-[UIInterfaceActionRepresentationView setOwnsActionContent:];
-[UIInterfaceActionRepresentationView setViewsToDisappearWhenHighlighted:];
```
