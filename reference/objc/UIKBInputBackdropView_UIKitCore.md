# `UIKBInputBackdropView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIAnimatedKeyboardElement`
- 26 instance variables, 21 properties, 64 instance methods, 1 class methods

## Instance variables

```
@"UIKBBackdropView" _inputBackdropFullView;
@"UIKBBackdropView" _inputBackdropLeftView;
@"UIKBBackdropView" _inputBackdropRightView;
Q _innerCorners;
B _isTransitioning;
d _transitionGap;
d _transitionLeftOffset;
d _transitionRightOffset;
q _style;
B _hasStartRect;
B _hasEndRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _savedStartRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _savedEndRect;
B _isAssistantBackground;
@"_UIVisualEffectBackdropView" _captureView;
@"NSArray" _splitConstraints;
@"NSArray" _fullWidthConstraints;
@"NSLayoutConstraint" _leftWidthConstraint;
@"NSLayoutConstraint" _rightWidthConstraint;
@"NSLayoutConstraint" _heightConstraint;
d _leftWidthDiff;
d _rightWidthDiff;
d _tallHeight;
d _heightDiff;
q _backdropStyle;
q _keyboardVisualState;
```

## Properties

```
@property (T@"UIKBBackdropView",&,N,V_inputBackdropFullView) inputBackdropFullView;
@property (T@"UIKBBackdropView",&,N,V_inputBackdropLeftView) inputBackdropLeftView;
@property (T@"UIKBBackdropView",&,N,V_inputBackdropRightView) inputBackdropRightView;
@property (T@"_UIVisualEffectBackdropView",&,N,V_captureView) captureView;
@property (T@"NSArray",&,N,V_splitConstraints) splitConstraints;
@property (T@"NSArray",&,N,V_fullWidthConstraints) fullWidthConstraints;
@property (T@"NSLayoutConstraint",&,N,V_leftWidthConstraint) leftWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_rightWidthConstraint) rightWidthConstraint;
@property (T@"NSLayoutConstraint",&,N,V_heightConstraint) heightConstraint;
@property (Td,N,V_leftWidthDiff) leftWidthDiff;
@property (Td,N,V_rightWidthDiff) rightWidthDiff;
@property (Td,N,V_tallHeight) tallHeight;
@property (Td,N,V_heightDiff) heightDiff;
@property (Tq,N,V_backdropStyle) backdropStyle;
@property (Tq,N,V_keyboardVisualState) keyboardVisualState;
@property (Tq,R,V_style) style;
@property (TB,N,V_isAssistantBackground) isAssistantBackground;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIKBInputBackdropView requiresConstraintBasedLayout];
```

## Instance methods

```
-[UIKBInputBackdropView setHeightConstraint:];
-[UIKBInputBackdropView animatingTransitionFromState:toState:animationType:totalDuration:];
-[UIKBInputBackdropView heightConstraint];
-[UIKBInputBackdropView _isTransitioning];
-[UIKBInputBackdropView sizeForVisualState:];
-[UIKBInputBackdropView prepareForTransitionToState:animationType:interactiveTransition:];
-[UIKBInputBackdropView transitioningToState:animationType:completionPercentage:];
-[UIKBInputBackdropView finishedTransitionToState:animationType:interactiveTransition:];
-[UIKBInputBackdropView backdropStyle];
-[UIKBInputBackdropView _setRenderConfig:];
-[UIKBInputBackdropView setBackdropStyle:];
-[UIKBInputBackdropView dealloc];
-[UIKBInputBackdropView transitionToStyle:];
-[UIKBInputBackdropView _beginSplitTransitionIfNeeded:gapWidth:];
-[UIKBInputBackdropView style];
-[UIKBInputBackdropView captureView];
-[UIKBInputBackdropView setCaptureView:];
-[UIKBInputBackdropView _endSplitTransitionIfNeeded:];
-[UIKBInputBackdropView initWithFrame:];
-[UIKBInputBackdropView textEffectsVisibilityLevel];
-[UIKBInputBackdropView _prepareWithLeftOffset:gapWidth:];
-[UIKBInputBackdropView _setInitialProgressWithFrame:];
-[UIKBInputBackdropView _setProgress:withFrame:];
-[UIKBInputBackdropView _updateForEmptyBackdrop:];
-[UIKBInputBackdropView _updateForLeftOffset:rightOffset:];
-[UIKBInputBackdropView createSplitBackdropIfNeeded];
-[UIKBInputBackdropView fullWidthConstraints];
-[UIKBInputBackdropView heightDiff];
-[UIKBInputBackdropView inputBackdropFullView];
-[UIKBInputBackdropView inputBackdropLeftView];
-[UIKBInputBackdropView inputBackdropRightView];
-[UIKBInputBackdropView isAssistantBackground];
-[UIKBInputBackdropView keyboardVisualState];
-[UIKBInputBackdropView layoutInputBackdropToFullWithRect:];
-[UIKBInputBackdropView layoutInputBackdropToSplitWithHeight:innerCorners:];
-[UIKBInputBackdropView layoutInputBackdropToSplitWithLeftViewRect:andRightViewRect:innerCorners:];
-[UIKBInputBackdropView leftWidthConstraint];
-[UIKBInputBackdropView leftWidthDiff];
-[UIKBInputBackdropView maskCornersIfNeededForStyle:];
-[UIKBInputBackdropView preferredCornerRadiusForState:];
-[UIKBInputBackdropView rightWidthConstraint];
-[UIKBInputBackdropView rightWidthDiff];
-[UIKBInputBackdropView setFullWidthConstraints:];
-[UIKBInputBackdropView setGestureProgressForSplit:];
-[UIKBInputBackdropView setHeightDiff:];
-[UIKBInputBackdropView setInputBackdropFullView:];
-[UIKBInputBackdropView setInputBackdropLeftView:];
-[UIKBInputBackdropView setInputBackdropRightView:];
-[UIKBInputBackdropView setIsAssistantBackground:];
-[UIKBInputBackdropView setKeyboardVisualState:];
-[UIKBInputBackdropView setLeftWidthConstraint:];
-[UIKBInputBackdropView setLeftWidthDiff:];
-[UIKBInputBackdropView setProgress:withFrame:innerCorners:];
-[UIKBInputBackdropView setRightWidthConstraint:];
-[UIKBInputBackdropView setRightWidthDiff:];
-[UIKBInputBackdropView setSplitConstraints:];
-[UIKBInputBackdropView setTallHeight:];
-[UIKBInputBackdropView splitConstraints];
-[UIKBInputBackdropView supportsLightEffects];
-[UIKBInputBackdropView tallHeight];
-[UIKBInputBackdropView transitionToStyle:isSplit:];
-[UIKBInputBackdropView updateCornersWithRadius:];
-[UIKBInputBackdropView updateCornersWithRadius:forVisualState:];
-[UIKBInputBackdropView updateCornersWithRadius:usingCornerRadii:];
```
