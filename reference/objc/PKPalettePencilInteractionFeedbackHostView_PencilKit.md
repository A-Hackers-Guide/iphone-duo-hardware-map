# `PKPalettePencilInteractionFeedbackHostView`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 16 instance variables, 16 properties, 43 instance methods, 0 class methods

## Instance variables

```
B _pencilInteractionFeedbackViewVisible;
@"<PKPalettePencilInteractionFeedbackHostViewDelegate>" _delegate;
@"PKPalettePencilInteractionFeedbackView" _pencilInteractionFeedbackView;
@"NSTimer" _pencilInteractionFeedbackViewAutodismissTimer;
@"UILayoutGuide" _pencilInteractionFeedbackViewLayoutGuide;
@"NSLayoutConstraint" _layoutGuideWidthConstraint;
@"NSLayoutConstraint" _layoutGuideHeightConstraint;
@"NSLayoutConstraint" _layoutGuideCenterXConstraint;
@"NSLayoutConstraint" _layoutGuideCenterYConstraint;
@"NSLayoutConstraint" _pencilInteractionFeedbackViewBottomConstraint;
@"NSLayoutConstraint" _pencilInteractionFeedbackViewLeftConstraint;
@"NSLayoutConstraint" _pencilInteractionFeedbackViewTopConstraint;
@"NSLayoutConstraint" _pencilInteractionFeedbackViewRightConstraint;
@"NSLayoutConstraint" _pencilInteractionFeedbackViewCenterXConstraint;
@"NSLayoutConstraint" _pencilInteractionFeedbackViewCenterYConstraint;
@"UIViewFloatAnimatableProperty" _feedbackViewVisibilityAnimatableProperty;
```

## Properties

```
@property (T@"<PKPalettePencilInteractionFeedbackHostViewDelegate>",W,N,V_delegate) delegate;
@property (T@"PKPalettePencilInteractionFeedbackView",&,N,V_pencilInteractionFeedbackView) pencilInteractionFeedbackView;
@property (T@"NSTimer",&,N,V_pencilInteractionFeedbackViewAutodismissTimer) pencilInteractionFeedbackViewAutodismissTimer;
@property (T@"UILayoutGuide",&,N,V_pencilInteractionFeedbackViewLayoutGuide) pencilInteractionFeedbackViewLayoutGuide;
@property (T@"NSLayoutConstraint",&,N,V_layoutGuideWidthConstraint) layoutGuideWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_layoutGuideHeightConstraint) layoutGuideHeightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_layoutGuideCenterXConstraint) layoutGuideCenterXConstraint;
@property (T@"NSLayoutConstraint",&,N,V_layoutGuideCenterYConstraint) layoutGuideCenterYConstraint;
@property (T@"NSLayoutConstraint",&,N,V_pencilInteractionFeedbackViewBottomConstraint) pencilInteractionFeedbackViewBottomConstraint;
@property (T@"NSLayoutConstraint",&,N,V_pencilInteractionFeedbackViewLeftConstraint) pencilInteractionFeedbackViewLeftConstraint;
@property (T@"NSLayoutConstraint",&,N,V_pencilInteractionFeedbackViewTopConstraint) pencilInteractionFeedbackViewTopConstraint;
@property (T@"NSLayoutConstraint",&,N,V_pencilInteractionFeedbackViewRightConstraint) pencilInteractionFeedbackViewRightConstraint;
@property (T@"NSLayoutConstraint",&,N,V_pencilInteractionFeedbackViewCenterXConstraint) pencilInteractionFeedbackViewCenterXConstraint;
@property (T@"NSLayoutConstraint",&,N,V_pencilInteractionFeedbackViewCenterYConstraint) pencilInteractionFeedbackViewCenterYConstraint;
@property (TB,N,GisPencilInteractionFeedbackViewVisible,V_pencilInteractionFeedbackViewVisible) pencilInteractionFeedbackViewVisible;
@property (T@"UIViewFloatAnimatableProperty",&,N,V_feedbackViewVisibilityAnimatableProperty) feedbackViewVisibilityAnimatableProperty;
```

## Instance methods

```
-[PKPalettePencilInteractionFeedbackHostView initWithDelegate:];
-[PKPalettePencilInteractionFeedbackHostView layoutSubviews];
-[PKPalettePencilInteractionFeedbackHostView hitTest:withEvent:];
-[PKPalettePencilInteractionFeedbackHostView setDelegate:];
-[PKPalettePencilInteractionFeedbackHostView delegate];
-[PKPalettePencilInteractionFeedbackHostView _updateLayoutGuideConstraints];
-[PKPalettePencilInteractionFeedbackHostView setLayoutGuideHeightConstraint:];
-[PKPalettePencilInteractionFeedbackHostView _animatePencilInteractionFeedbackViewToVisible:animated:completion:];
-[PKPalettePencilInteractionFeedbackHostView _isPencilInteractionFeedbackViewAlmostOffScreen];
-[PKPalettePencilInteractionFeedbackHostView _palettePosition];
-[PKPalettePencilInteractionFeedbackHostView feedbackViewVisibilityAnimatableProperty];
-[PKPalettePencilInteractionFeedbackHostView hideFeedbackView];
-[PKPalettePencilInteractionFeedbackHostView isPencilInteractionFeedbackViewVisible];
-[PKPalettePencilInteractionFeedbackHostView layoutGuideCenterXConstraint];
-[PKPalettePencilInteractionFeedbackHostView layoutGuideCenterYConstraint];
-[PKPalettePencilInteractionFeedbackHostView layoutGuideHeightConstraint];
-[PKPalettePencilInteractionFeedbackHostView layoutGuideWidthConstraint];
-[PKPalettePencilInteractionFeedbackHostView minimizedPaletteScaleFactor];
-[PKPalettePencilInteractionFeedbackHostView minimizedPaletteSize];
-[PKPalettePencilInteractionFeedbackHostView pencilInteractionFeedbackView];
-[PKPalettePencilInteractionFeedbackHostView pencilInteractionFeedbackViewAutodismissTimer];
-[PKPalettePencilInteractionFeedbackHostView pencilInteractionFeedbackViewBottomConstraint];
-[PKPalettePencilInteractionFeedbackHostView pencilInteractionFeedbackViewCenterXConstraint];
-[PKPalettePencilInteractionFeedbackHostView pencilInteractionFeedbackViewCenterYConstraint];
-[PKPalettePencilInteractionFeedbackHostView pencilInteractionFeedbackViewLayoutGuide];
-[PKPalettePencilInteractionFeedbackHostView pencilInteractionFeedbackViewLeftConstraint];
-[PKPalettePencilInteractionFeedbackHostView pencilInteractionFeedbackViewRightConstraint];
-[PKPalettePencilInteractionFeedbackHostView pencilInteractionFeedbackViewTopConstraint];
-[PKPalettePencilInteractionFeedbackHostView setFeedbackViewVisibilityAnimatableProperty:];
-[PKPalettePencilInteractionFeedbackHostView setLayoutGuideCenterXConstraint:];
-[PKPalettePencilInteractionFeedbackHostView setLayoutGuideCenterYConstraint:];
-[PKPalettePencilInteractionFeedbackHostView setLayoutGuideWidthConstraint:];
-[PKPalettePencilInteractionFeedbackHostView setPencilInteractionFeedbackView:];
-[PKPalettePencilInteractionFeedbackHostView setPencilInteractionFeedbackViewAutodismissTimer:];
-[PKPalettePencilInteractionFeedbackHostView setPencilInteractionFeedbackViewBottomConstraint:];
-[PKPalettePencilInteractionFeedbackHostView setPencilInteractionFeedbackViewCenterXConstraint:];
-[PKPalettePencilInteractionFeedbackHostView setPencilInteractionFeedbackViewCenterYConstraint:];
-[PKPalettePencilInteractionFeedbackHostView setPencilInteractionFeedbackViewLayoutGuide:];
-[PKPalettePencilInteractionFeedbackHostView setPencilInteractionFeedbackViewLeftConstraint:];
-[PKPalettePencilInteractionFeedbackHostView setPencilInteractionFeedbackViewRightConstraint:];
-[PKPalettePencilInteractionFeedbackHostView setPencilInteractionFeedbackViewTopConstraint:];
-[PKPalettePencilInteractionFeedbackHostView setPencilInteractionFeedbackViewVisible:];
-[PKPalettePencilInteractionFeedbackHostView showFeedbackForCurrentlySelectedToolInPaletteView];
```
