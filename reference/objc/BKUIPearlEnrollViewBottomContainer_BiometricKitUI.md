# `BKUIPearlEnrollViewBottomContainer`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 14 instance variables, 14 properties, 58 instance methods, 0 class methods

## Instance variables

```
B _squareNeedsPositionLayout;
B _inBuddy;
@"BKUIPearlInstructionView" _instructionView;
@"NSArray" _onscreenScrollViewConstraints;
d _overlapValue;
@"UILayoutGuide" _instructionBaselineLayoutGuide;
@"UIView<BKUIScrollableContainer>" _onScreenScrollview;
@"UIView<BKUIScrollableContainer>" _offScreenScrollview;
@"<BKUIPearlBottomContainerDelegate>" _delegate;
@"BKUIPearlInstructionView" _animatingInstructionView;
@"NSMutableDictionary" _customInstructionStrings;
@"NSMutableDictionary" _customDetailStrings;
@"UIView<BKUIScrollableContainer>" _scrollview;
@"UIView<BKUIScrollableContainer>" _overlappingScrollview;
```

## Properties

```
@property (TB,N,V_inBuddy) inBuddy;
@property (Td,N,V_overlapValue) overlapValue;
@property (T@"BKUIPearlInstructionView",&,N,V_instructionView) instructionView;
@property (T@"BKUIPearlInstructionView",&,N,V_animatingInstructionView) animatingInstructionView;
@property (T@"NSMutableDictionary",&,N,V_customInstructionStrings) customInstructionStrings;
@property (T@"NSMutableDictionary",&,N,V_customDetailStrings) customDetailStrings;
@property (T@"UIView<BKUIScrollableContainer>",&,N,V_scrollview) scrollview;
@property (T@"UIView<BKUIScrollableContainer>",&,N,V_overlappingScrollview) overlappingScrollview;
@property (T@"UIView<BKUIScrollableContainer>",&,N,V_onScreenScrollview) onScreenScrollview;
@property (T@"UIView<BKUIScrollableContainer>",&,N,V_offScreenScrollview) offScreenScrollview;
@property (TB,N,V_squareNeedsPositionLayout) squareNeedsPositionLayout;
@property (T@"NSArray",&,N,V_onscreenScrollViewConstraints) onscreenScrollViewConstraints;
@property (T@"UILayoutGuide",&,N,V_instructionBaselineLayoutGuide) instructionBaselineLayoutGuide;
@property (T@"<BKUIPearlBottomContainerDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[BKUIPearlEnrollViewBottomContainer layoutSubviews];
-[BKUIPearlEnrollViewBottomContainer scrollview];
-[BKUIPearlEnrollViewBottomContainer setDelegate:];
-[BKUIPearlEnrollViewBottomContainer delegate];
-[BKUIPearlEnrollViewBottomContainer buttonTray];
-[BKUIPearlEnrollViewBottomContainer inBuddy];
-[BKUIPearlEnrollViewBottomContainer setInBuddy:];
-[BKUIPearlEnrollViewBottomContainer instructionView];
-[BKUIPearlEnrollViewBottomContainer setInstructionView:];
-[BKUIPearlEnrollViewBottomContainer finalizeInstructionAnimation];
-[BKUIPearlEnrollViewBottomContainer _horizontalConstraintsForTagAlongTransitionView:state:position:];
-[BKUIPearlEnrollViewBottomContainer nextStateButton];
-[BKUIPearlEnrollViewBottomContainer setCustomDetailString:forState:];
-[BKUIPearlEnrollViewBottomContainer _configureInstructionView:forState:substate:];
-[BKUIPearlEnrollViewBottomContainer _detailTextForState:substate:];
-[BKUIPearlEnrollViewBottomContainer _instructionTextForState:substate:];
-[BKUIPearlEnrollViewBottomContainer _locStateDetailedLabelNameForState:];
-[BKUIPearlEnrollViewBottomContainer _locStateNameForState:];
-[BKUIPearlEnrollViewBottomContainer _targetScrollViewForState:];
-[BKUIPearlEnrollViewBottomContainer _topPaddingForButtonTray:];
-[BKUIPearlEnrollViewBottomContainer _updateButtonLayoutForScrollView:];
-[BKUIPearlEnrollViewBottomContainer _updateButtonVisibilityForScrollView:];
-[BKUIPearlEnrollViewBottomContainer _updateButtonVisibilityForScrollView:state:subState:];
-[BKUIPearlEnrollViewBottomContainer _updateTopPaddingAndReturnHorizontalConstraintsForScrollView:state:position:];
-[BKUIPearlEnrollViewBottomContainer animatingInstructionView];
-[BKUIPearlEnrollViewBottomContainer bottomLinkButton];
-[BKUIPearlEnrollViewBottomContainer buttonTrayTopAnchor];
-[BKUIPearlEnrollViewBottomContainer customDetailStrings];
-[BKUIPearlEnrollViewBottomContainer customInstructionStrings];
-[BKUIPearlEnrollViewBottomContainer escapeHatchButtonWasPressed:];
-[BKUIPearlEnrollViewBottomContainer initWithFrame:inBuddy:scrollView:overlapScrollView:delegate:squareNeedsPositionLayout:];
-[BKUIPearlEnrollViewBottomContainer instructionBaselineLayoutGuide];
-[BKUIPearlEnrollViewBottomContainer nextStateButtonWasPressed:];
-[BKUIPearlEnrollViewBottomContainer offScreenScrollview];
-[BKUIPearlEnrollViewBottomContainer onScreenScrollview];
-[BKUIPearlEnrollViewBottomContainer onscreenScrollViewConstraints];
-[BKUIPearlEnrollViewBottomContainer overlapValue];
-[BKUIPearlEnrollViewBottomContainer overlappingScrollview];
-[BKUIPearlEnrollViewBottomContainer prepareForAnimationToState:fromState:subState:advancing:parentView:];
-[BKUIPearlEnrollViewBottomContainer prepareForAnimationToState:fromState:subState:advancing:tagAlong:parentView:];
-[BKUIPearlEnrollViewBottomContainer retryWasPressed:];
-[BKUIPearlEnrollViewBottomContainer setAnimatingInstructionView:];
-[BKUIPearlEnrollViewBottomContainer setCustomDetailStrings:];
-[BKUIPearlEnrollViewBottomContainer setCustomInstructionString:forState:];
-[BKUIPearlEnrollViewBottomContainer setCustomInstructionStrings:];
-[BKUIPearlEnrollViewBottomContainer setInstructionBaselineLayoutGuide:];
-[BKUIPearlEnrollViewBottomContainer setOffScreenScrollview:];
-[BKUIPearlEnrollViewBottomContainer setOnScreenScrollview:];
-[BKUIPearlEnrollViewBottomContainer setOnscreenScrollViewConstraints:];
-[BKUIPearlEnrollViewBottomContainer setOverlapValue:];
-[BKUIPearlEnrollViewBottomContainer setOverlappingScrollview:];
-[BKUIPearlEnrollViewBottomContainer setScrollview:];
-[BKUIPearlEnrollViewBottomContainer setSquareNeedsPositionLayout:];
-[BKUIPearlEnrollViewBottomContainer setupInitialUI];
-[BKUIPearlEnrollViewBottomContainer squareNeedsPositionLayout];
-[BKUIPearlEnrollViewBottomContainer updateButtonLayout];
-[BKUIPearlEnrollViewBottomContainer updateButtonVisibility];
-[BKUIPearlEnrollViewBottomContainer updateInstructionViewContentForState:substate:];
```
