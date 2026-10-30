# `PKPaletteHostView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UIGestureRecognizerDelegate`, `UIScrollViewDelegate`, `PKPaletteViewInternalDelegate`, `UIPopoverPresentationControllerDelegate`, `PKPalettePencilInteractionFeedbackHostViewDelegate`, `PKPaletteTransitionDelegate`, `PKPaletteViewHosting`
- 41 instance variables, 40 properties, 146 instance methods, 1 class methods

## Instance variables

```
@"UILayoutGuide" _paletteViewLayoutGuide;
@"NSLayoutConstraint" _paletteViewLayoutGuideTopConstraint;
@"NSLayoutConstraint" _paletteViewLayoutGuideLeftConstraint;
@"NSLayoutConstraint" _paletteViewLayoutGuideRightConstraint;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _paletteViewLayoutGuideInsets;
B _paletteDockedToHorizontalEdge;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _lastWindowBoundsForCornerRadius;
Q _registeredMenuAvoidanceEdge;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _registeredMenuAvoidanceFrame;
B _paletteVisible;
B _effectivePaletteVisible;
B _panGestureDidStartInPaletteScrollView;
B _panGestureShouldDragPaletteView;
B _paletteScrollGestureShouldScroll;
@"PKPaletteTooltipPresentationHandle" _tooltipPresentationHandle;
@"PKPaletteView" _paletteView;
d _paletteViewBottomEdgeSpacing;
@"<PKPaletteHostViewDelegate>" _delegate;
@"NSLayoutConstraint" _paletteWidthConstraint;
@"NSLayoutConstraint" _paletteHeightConstraint;
@"NSLayoutConstraint" _paletteTopConstraint;
@"NSLayoutConstraint" _paletteBottomConstraint;
@"NSLayoutConstraint" _paletteLeftConstraint;
@"NSLayoutConstraint" _paletteLeftConstraintInCompact;
@"NSLayoutConstraint" _paletteRightConstraint;
@"NSLayoutConstraint" _paletteRightConstraintInCompact;
@"NSLayoutConstraint" _paletteCenterXConstraint;
@"NSLayoutConstraint" _paletteCenterYConstraint;
@"UIPanGestureRecognizer" _panGestureRecognizer;
@"UITapGestureRecognizer" _tapToExpandPaletteFromMinimizedGestureRecognizer;
@"UILongPressGestureRecognizer" _touchDownFeedbackGestureRecognizer;
q _paletteDraggingBehavior;
q _paletteVisualState;
q _palettePosition;
q _lastNonCompactPalettePosition;
q _draggingPendingPaletteVisualState;
@"PKPaletteTransition" _paletteTransition;
@"PKPalettePencilInteractionFeedbackHostView" _pencilInteractionFeedbackHostView;
@"<_UIInvalidatable>" _menuAvoidanceAssertion;
@"UIPointerInteraction" _pointerInteraction;
{CGPoint="x"d"y"d} _draggingInitialPaletteCenterInSelf;
```

## Properties

```
@property (T@"<PKPaletteHostViewDelegate>",W,N,V_delegate) delegate;
@property (TB,N,GisPaletteVisible,V_paletteVisible) paletteVisible;
@property (TB,N,GisEffectivePaletteVisible,V_effectivePaletteVisible) effectivePaletteVisible;
@property (T@"NSLayoutConstraint",&,N,V_paletteWidthConstraint) paletteWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_paletteHeightConstraint) paletteHeightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_paletteTopConstraint) paletteTopConstraint;
@property (T@"NSLayoutConstraint",&,N,V_paletteBottomConstraint) paletteBottomConstraint;
@property (T@"NSLayoutConstraint",&,N,V_paletteLeftConstraint) paletteLeftConstraint;
@property (T@"NSLayoutConstraint",&,N,V_paletteLeftConstraintInCompact) paletteLeftConstraintInCompact;
@property (T@"NSLayoutConstraint",&,N,V_paletteRightConstraint) paletteRightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_paletteRightConstraintInCompact) paletteRightConstraintInCompact;
@property (T@"NSLayoutConstraint",&,N,V_paletteCenterXConstraint) paletteCenterXConstraint;
@property (T@"NSLayoutConstraint",&,N,V_paletteCenterYConstraint) paletteCenterYConstraint;
@property (T@"UIPanGestureRecognizer",&,N,V_panGestureRecognizer) panGestureRecognizer;
@property (T@"UITapGestureRecognizer",&,N,V_tapToExpandPaletteFromMinimizedGestureRecognizer) tapToExpandPaletteFromMinimizedGestureRecognizer;
@property (T@"UILongPressGestureRecognizer",&,N,V_touchDownFeedbackGestureRecognizer) touchDownFeedbackGestureRecognizer;
@property (Tq,N,V_paletteDraggingBehavior) paletteDraggingBehavior;
@property (Tq,N,S_setPaletteVisualState:,V_paletteVisualState) paletteVisualState;
@property (Tq,N,V_palettePosition) palettePosition;
@property (Tq,N,V_lastNonCompactPalettePosition) lastNonCompactPalettePosition;
@property (Tq,N,V_draggingPendingPaletteVisualState) draggingPendingPaletteVisualState;
@property (T{CGPoint=dd},N,V_draggingInitialPaletteCenterInSelf) draggingInitialPaletteCenterInSelf;
@property (T@"PKPaletteTransition",&,N,V_paletteTransition) paletteTransition;
@property (T@"PKPalettePencilInteractionFeedbackHostView",&,N,V_pencilInteractionFeedbackHostView) pencilInteractionFeedbackHostView;
@property (T@"PKPaletteView",&,N,V_paletteView) paletteView;
@property (TB,N,V_panGestureDidStartInPaletteScrollView) panGestureDidStartInPaletteScrollView;
@property (TB,N,V_panGestureShouldDragPaletteView) panGestureShouldDragPaletteView;
@property (TB,N,V_paletteScrollGestureShouldScroll) paletteScrollGestureShouldScroll;
@property (T@"<_UIInvalidatable>",&,N,V_menuAvoidanceAssertion) menuAvoidanceAssertion;
@property (T@"UIPointerInteraction",&,N,V_pointerInteraction) pointerInteraction;
@property (Td,N,V_paletteViewBottomEdgeSpacing) paletteViewBottomEdgeSpacing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"UIView",R,N) hostingView;
@property (TB,R,N,GisPaletteDragging) paletteDragging;
@property (TB,R,N,GisPaletteVisualStateMinimized) paletteVisualStateMinimized;
@property (Td,R,N) compactPaletteAvailableWidth;
@property (T@"PKPaletteTooltipPresentationHandle",R,N,V_tooltipPresentationHandle) tooltipPresentationHandle;
```

## Class methods

```
+[PKPaletteHostView _allowsHitTestAsOpaqueForRemoteEffects];
```

## Instance methods

```
-[PKPaletteHostView panGestureRecognizer];
-[PKPaletteHostView setPointerInteraction:];
-[PKPaletteHostView didMoveToWindow];
-[PKPaletteHostView setPanGestureRecognizer:];
-[PKPaletteHostView pointerInteraction:styleForRegion:];
-[PKPaletteHostView pointerInteraction:willEnterRegion:animator:];
-[PKPaletteHostView pointerInteraction:willExitRegion:animator:];
-[PKPaletteHostView layoutSubviews];
-[PKPaletteHostView hitTest:withEvent:];
-[PKPaletteHostView hostingView];
-[PKPaletteHostView setDelegate:];
-[PKPaletteHostView gestureRecognizerShouldBegin:];
-[PKPaletteHostView safeAreaInsetsDidChange];
-[PKPaletteHostView pointerInteraction];
-[PKPaletteHostView gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[PKPaletteHostView delegate];
-[PKPaletteHostView traitCollectionDidChange:];
-[PKPaletteHostView pointInside:withEvent:];
-[PKPaletteHostView _dockPaletteToPosition:animated:];
-[PKPaletteHostView paletteRightConstraintInCompact];
-[PKPaletteHostView _updateContextMenuAvoidanceRect];
-[PKPaletteHostView palettePosition];
-[PKPaletteHostView panGestureShouldDragPaletteView];
-[PKPaletteHostView setPaletteView:];
-[PKPaletteHostView _activatePaletteCenterConstraints];
-[PKPaletteHostView _cancelPanGestureIfNecessary];
-[PKPaletteHostView _compactHorizontalEdgePosition];
-[PKPaletteHostView _deactivatePaletteCenterConstraints];
-[PKPaletteHostView _deactivatePaletteEdgeConstraints];
-[PKPaletteHostView _deactivatePaletteEdgeConstraintsForCompact];
-[PKPaletteHostView _dockPaletteToAutoHideCornerAnimated:];
-[PKPaletteHostView _dockPaletteToPosition:isFromUserReposition:animated:];
-[PKPaletteHostView _fixToHorizontalEdge:];
-[PKPaletteHostView _installPencilInteractionFeedbackHostViewIfNeeded];
-[PKPaletteHostView _isPaletteAnimating];
-[PKPaletteHostView _paletteDidDockToPosition:fromUserReposition:];
-[PKPaletteHostView _paletteEdgeMarginForEdge:isMinimized:];
-[PKPaletteHostView _paletteSizeForVisualState:];
-[PKPaletteHostView _paletteViewCompactHeight];
-[PKPaletteHostView _paletteWillDockToPosition:prepareForExpansion:];
-[PKPaletteHostView _panGestureHandler:];
-[PKPaletteHostView _performAnimated:tracking:animations:completion:];
-[PKPaletteHostView _processPendingDraggingTransition];
-[PKPaletteHostView _projectedLandingPointForGestureRecognizerEnd:];
-[PKPaletteHostView _scheduleDraggingTransitionToVisualState:];
-[PKPaletteHostView _setPaletteDockedToHorizontalEdge:];
-[PKPaletteHostView _setPaletteVisualState:];
-[PKPaletteHostView _setPaletteVisualState:usingTransition:];
-[PKPaletteHostView _tapToExpandPaletteFromMinimizedGestureHandler:];
-[PKPaletteHostView _touchDownFeedbackGestureHandler:];
-[PKPaletteHostView _updateConstraintsToDockPaletteToPosition:];
-[PKPaletteHostView _updateConstraintsToFixToHorizontalEdge:];
-[PKPaletteHostView _updatePaletteAppearanceAnimated:];
-[PKPaletteHostView _updatePaletteContentAlpha];
-[PKPaletteHostView _updatePaletteHeightConstraint];
-[PKPaletteHostView _updatePaletteSizeAnimated:];
-[PKPaletteHostView _updatePaletteViewCornerRadiusForVisualState:];
-[PKPaletteHostView _updatePaletteViewLayoutGuideInsets];
-[PKPaletteHostView _updatePaletteViewSizeConstraints];
-[PKPaletteHostView _updateToolPreviewMinimizedStateAnimated:];
-[PKPaletteHostView _updateToolPreviewRotationAnimated:];
-[PKPaletteHostView _usesCompactPaletteWidth];
-[PKPaletteHostView avoidanceEdgeForPaletteVisualState:];
-[PKPaletteHostView compactPaletteAvailableWidth];
-[PKPaletteHostView draggingInitialPaletteCenterInSelf];
-[PKPaletteHostView draggingPendingPaletteVisualState];
-[PKPaletteHostView initWithPaletteView:];
-[PKPaletteHostView isEffectivePaletteVisible];
-[PKPaletteHostView isPaletteDragging];
-[PKPaletteHostView isPaletteVisible];
-[PKPaletteHostView isPaletteVisualStateMinimized];
-[PKPaletteHostView lastNonCompactPalettePosition];
-[PKPaletteHostView menuAvoidanceAssertion];
-[PKPaletteHostView paletteBorderColor];
-[PKPaletteHostView paletteBorderWidth];
-[PKPaletteHostView paletteBottomConstraint];
-[PKPaletteHostView paletteCenterXConstraint];
-[PKPaletteHostView paletteCenterYConstraint];
-[PKPaletteHostView paletteDraggingBehavior];
-[PKPaletteHostView paletteEdgeSpacing];
-[PKPaletteHostView paletteEdgeSpacingForMinimized];
-[PKPaletteHostView paletteHeightConstraint];
-[PKPaletteHostView paletteLeftConstraint];
-[PKPaletteHostView paletteLeftConstraintInCompact];
-[PKPaletteHostView paletteRightConstraint];
-[PKPaletteHostView paletteScrollGestureShouldScroll];
-[PKPaletteHostView paletteShadowColor];
-[PKPaletteHostView paletteShadowOffset];
-[PKPaletteHostView paletteShadowOpacity];
-[PKPaletteHostView paletteShadowRadius];
-[PKPaletteHostView paletteSpringAnimationDampingRatio];
-[PKPaletteHostView paletteSpringAnimationResponse];
-[PKPaletteHostView paletteTopConstraint];
-[PKPaletteHostView paletteTransition];
-[PKPaletteHostView paletteView];
-[PKPaletteHostView paletteViewBottomEdgeSpacing];
-[PKPaletteHostView paletteViewContentSizeDidChange:];
-[PKPaletteHostView paletteViewReturnKeyTypeDidChange:];
-[PKPaletteHostView paletteViewShowFeedbackForToolChange:];
-[PKPaletteHostView paletteViewStateDidChange:];
-[PKPaletteHostView paletteViewStateDidChange:updatePaletteAppearance:];
-[PKPaletteHostView paletteViewStateDidChangeAutoHide:];
-[PKPaletteHostView paletteViewStateDidChangeEnableKeyboardButtons:];
-[PKPaletteHostView paletteViewStateDidChangeInputAssistantItems:];
-[PKPaletteHostView paletteViewStateDidChangeIsVisible:];
-[PKPaletteHostView paletteViewStateDidChangeScaleFactor:];
-[PKPaletteHostView paletteViewStateDidChangeSelectedTool:];
-[PKPaletteHostView paletteViewStateDidChangeShowsHandwritingTool:];
-[PKPaletteHostView paletteVisualState];
-[PKPaletteHostView paletteWidthConstraint];
-[PKPaletteHostView panGestureDidStartInPaletteScrollView];
-[PKPaletteHostView pencilInteractionFeedbackHostView];
-[PKPaletteHostView setDraggingInitialPaletteCenterInSelf:];
-[PKPaletteHostView setDraggingPendingPaletteVisualState:];
-[PKPaletteHostView setEffectivePaletteVisible:];
-[PKPaletteHostView setLastNonCompactPalettePosition:];
-[PKPaletteHostView setMenuAvoidanceAssertion:];
-[PKPaletteHostView setPaletteBottomConstraint:];
-[PKPaletteHostView setPaletteCenterXConstraint:];
-[PKPaletteHostView setPaletteCenterYConstraint:];
-[PKPaletteHostView setPaletteDraggingBehavior:];
-[PKPaletteHostView setPaletteHeightConstraint:];
-[PKPaletteHostView setPaletteLeftConstraint:];
-[PKPaletteHostView setPaletteLeftConstraintInCompact:];
-[PKPaletteHostView setPalettePosition:];
-[PKPaletteHostView setPaletteRightConstraint:];
-[PKPaletteHostView setPaletteRightConstraintInCompact:];
-[PKPaletteHostView setPaletteScrollGestureShouldScroll:];
-[PKPaletteHostView setPaletteTopConstraint:];
-[PKPaletteHostView setPaletteTransition:];
-[PKPaletteHostView setPaletteViewBottomEdgeSpacing:];
-[PKPaletteHostView setPaletteVisible:];
-[PKPaletteHostView setPaletteVisible:animated:completion:];
-[PKPaletteHostView setPaletteWidthConstraint:];
-[PKPaletteHostView setPanGestureDidStartInPaletteScrollView:];
-[PKPaletteHostView setPanGestureShouldDragPaletteView:];
-[PKPaletteHostView setPencilInteractionFeedbackHostView:];
-[PKPaletteHostView setTapToExpandPaletteFromMinimizedGestureRecognizer:];
-[PKPaletteHostView setTouchDownFeedbackGestureRecognizer:];
-[PKPaletteHostView tapToExpandPaletteFromMinimizedGestureRecognizer];
-[PKPaletteHostView tooltipPresentationHandle];
-[PKPaletteHostView touchDownFeedbackGestureRecognizer];
-[PKPaletteHostView transitionExpandedToCollapsedRatioDidChange:];
-[PKPaletteHostView transitionIntermediateVisualStateDidChange:];
-[PKPaletteHostView transitionPointingDirectionDidChange:];
-[PKPaletteHostView updateKeyboardAvoidanceForPalette:];
```
