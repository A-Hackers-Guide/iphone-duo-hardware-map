# `BKUIContainerScrollView`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIScrollView`
- Protocols: `BKUIScrollableContainer`
- 9 instance variables, 15 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"UIView" _scrollContentView;
@"BKUIPearlInstructionView" _instructionView;
@"BKUIPearlInstructionView" _animatingInstructionView;
@"BKUIButtonTray" _buttonTray;
@"NSLayoutConstraint" _pinButtonTrayToScrollViewBottomConstraint;
@"NSLayoutConstraint" _horizontalConstraint;
@"NSLayoutConstraint" _instructionViewTopConstraint;
@"NSLayoutConstraint" _buttonTrayTopAnchor;
@"NSLayoutConstraint" _topToSuperViewConstraint;
```

## Properties

```
@property (T@"UIView",&,N,V_scrollContentView) scrollContentView;
@property (T@"BKUIPearlInstructionView",&,N,V_instructionView) instructionView;
@property (T@"BKUIPearlInstructionView",&,N,V_animatingInstructionView) animatingInstructionView;
@property (T@"BKUIButtonTray",&,N,V_buttonTray) buttonTray;
@property (T@"NSLayoutConstraint",&,N,V_pinButtonTrayToScrollViewBottomConstraint) pinButtonTrayToScrollViewBottomConstraint;
@property (T@"NSLayoutConstraint",&,N,V_horizontalConstraint) horizontalConstraint;
@property (T@"NSLayoutConstraint",&,N,V_instructionViewTopConstraint) instructionViewTopConstraint;
@property (T@"NSLayoutConstraint",&,N,V_buttonTrayTopAnchor) buttonTrayTopAnchor;
@property (T@"NSLayoutConstraint",&,N,V_topToSuperViewConstraint) topToSuperViewConstraint;
@property (Tq,N) indicatorStyle;
@property (TB,N) showsVerticalScrollIndicator;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[BKUIContainerScrollView buttonTray];
-[BKUIContainerScrollView setButtonTray:];
-[BKUIContainerScrollView instructionView];
-[BKUIContainerScrollView setInstructionView:];
-[BKUIContainerScrollView scrollContentView];
-[BKUIContainerScrollView setScrollContentView:];
-[BKUIContainerScrollView animatingInstructionView];
-[BKUIContainerScrollView buttonTrayTopAnchor];
-[BKUIContainerScrollView horizontalConstraint];
-[BKUIContainerScrollView initWithFrame:buttonTray:];
-[BKUIContainerScrollView instructionViewTopConstraint];
-[BKUIContainerScrollView pinButtonTrayToScrollViewBottomConstraint];
-[BKUIContainerScrollView setAnimatingInstructionView:];
-[BKUIContainerScrollView setButtonTrayTopAnchor:];
-[BKUIContainerScrollView setHorizontalConstraint:];
-[BKUIContainerScrollView setInstructionViewTopConstraint:];
-[BKUIContainerScrollView setPinButtonTrayToScrollViewBottomConstraint:];
-[BKUIContainerScrollView setTopToSuperViewConstraint:];
-[BKUIContainerScrollView topToSuperViewConstraint];
```
