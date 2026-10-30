# `BKUIButtonTray`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 16 instance variables, 16 properties, 53 instance methods, 0 class methods

## Instance variables

```
B _isInline;
B _willUseActionDelegate;
B _inSheet;
@"UIButton" _nextStateButton;
@"UIView" _nextStateButtonContainer;
@"NSLayoutConstraint" _nextStateButtonContainerHorizontalPositionConstraint;
@"UIButton" _bottomLinkButton;
@"UIButton" _topLinkButton;
@"NSLayoutConstraint" _nextStateButtonContainerBottomConstraintTall;
@"NSLayoutConstraint" _escapeHatchButtonLeadingConstraint;
@"NSLayoutConstraint" _escapeHatchButtonTrailingConstraint;
@"NSLayoutConstraint" _escapeHatchButtonBottomConstraint;
@"<BKUIButtonTrayActionDelegate>" _actionDelegate;
@"UIView" _bottomPaddingView;
@"NSArray" _layoutConstraints;
@"<UITraitChangeRegistration>" _traitChangeRegistration;
```

## Properties

```
@property (TB,N,V_inSheet) inSheet;
@property (T@"UIView",&,N,V_bottomPaddingView) bottomPaddingView;
@property (T@"NSArray",&,N,V_layoutConstraints) layoutConstraints;
@property (T@"<UITraitChangeRegistration>",&,N,V_traitChangeRegistration) traitChangeRegistration;
@property (T@"UIButton",&,N,V_nextStateButton) nextStateButton;
@property (T@"UIView",&,N,V_nextStateButtonContainer) nextStateButtonContainer;
@property (T@"NSLayoutConstraint",&,N,V_nextStateButtonContainerHorizontalPositionConstraint) nextStateButtonContainerHorizontalPositionConstraint;
@property (T@"UIButton",&,N,V_bottomLinkButton) bottomLinkButton;
@property (T@"UIButton",&,N,V_topLinkButton) topLinkButton;
@property (T@"NSLayoutConstraint",&,N,V_nextStateButtonContainerBottomConstraintTall) nextStateButtonContainerBottomConstraintTall;
@property (T@"NSLayoutConstraint",&,N,V_escapeHatchButtonLeadingConstraint) escapeHatchButtonLeadingConstraint;
@property (T@"NSLayoutConstraint",&,N,V_escapeHatchButtonTrailingConstraint) escapeHatchButtonTrailingConstraint;
@property (T@"NSLayoutConstraint",&,N,V_escapeHatchButtonBottomConstraint) escapeHatchButtonBottomConstraint;
@property (TB,N,V_isInline) isInline;
@property (TB,N,V_willUseActionDelegate) willUseActionDelegate;
@property (T@"<BKUIButtonTrayActionDelegate>",W,N,V_actionDelegate) actionDelegate;
```

## Instance methods

```
-[BKUIButtonTray intrinsicContentSize];
-[BKUIButtonTray setLayoutConstraints:];
-[BKUIButtonTray displayState];
-[BKUIButtonTray setActionDelegate:];
-[BKUIButtonTray setIsInline:];
-[BKUIButtonTray isInline];
-[BKUIButtonTray actionDelegate];
-[BKUIButtonTray layoutConstraints];
-[BKUIButtonTray initWithFrame:];
-[BKUIButtonTray _bottomPadding];
-[BKUIButtonTray setTraitChangeRegistration:];
-[BKUIButtonTray traitChangeRegistration];
-[BKUIButtonTray initWithFrame:willUseActionDelegate:];
-[BKUIButtonTray inSheet];
-[BKUIButtonTray nextStateButton];
-[BKUIButtonTray showRetryButton];
-[BKUIButtonTray _layoutInternalButtonsForDisplayState:];
-[BKUIButtonTray allButtonsView];
-[BKUIButtonTray bottomLinkButton];
-[BKUIButtonTray bottomPaddingView];
-[BKUIButtonTray continueButtonPressed:];
-[BKUIButtonTray escapeHatchButtonBottomConstraint];
-[BKUIButtonTray escapeHatchButtonLeadingConstraint];
-[BKUIButtonTray escapeHatchButtonTrailingConstraint];
-[BKUIButtonTray horizontalLayoutConstraints:];
-[BKUIButtonTray linkButtonPressed:];
-[BKUIButtonTray nextStateButtonContainer];
-[BKUIButtonTray nextStateButtonContainerBottomConstraintTall];
-[BKUIButtonTray nextStateButtonContainerHorizontalPositionConstraint];
-[BKUIButtonTray nextStateButtonContainerHorizontalPositionConstraint:];
-[BKUIButtonTray noButtonsView];
-[BKUIButtonTray oneButtonView:];
-[BKUIButtonTray resetAlphaForAllButtons];
-[BKUIButtonTray resetConstraintsForButtons];
-[BKUIButtonTray setBottomLinkButton:];
-[BKUIButtonTray setBottomPaddingView:];
-[BKUIButtonTray setEscapeHatchButtonBottomConstraint:];
-[BKUIButtonTray setEscapeHatchButtonLeadingConstraint:];
-[BKUIButtonTray setEscapeHatchButtonTrailingConstraint:];
-[BKUIButtonTray setInSheet:];
-[BKUIButtonTray setNextStateButton:];
-[BKUIButtonTray setNextStateButtonContainer:];
-[BKUIButtonTray setNextStateButtonContainerBottomConstraintTall:];
-[BKUIButtonTray setNextStateButtonContainerHorizontalPositionConstraint:];
-[BKUIButtonTray setTopLinkButton:];
-[BKUIButtonTray setWillUseActionDelegate:];
-[BKUIButtonTray setupDebugUITraits];
-[BKUIButtonTray topLinkButton];
-[BKUIButtonTray topLinkButtonPressed:];
-[BKUIButtonTray twoButtonView:secondButton:];
-[BKUIButtonTray updateButtonLayout];
-[BKUIButtonTray updateInitialButtonLayout];
-[BKUIButtonTray willUseActionDelegate];
```
