# `BKUIJindoContainerScrollview`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `BKUIScrollableContainer`
- 10 instance variables, 16 properties, 26 instance methods, 0 class methods

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
@"UIScrollView" _scrollview;
```

## Properties

```
@property (T@"UIScrollView",&,N,V_scrollview) scrollview;
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
-[BKUIJindoContainerScrollview setContentOffset:animated:];
-[BKUIJindoContainerScrollview scrollview];
-[BKUIJindoContainerScrollview indicatorStyle];
-[BKUIJindoContainerScrollview setIndicatorStyle:];
-[BKUIJindoContainerScrollview setShowsVerticalScrollIndicator:];
-[BKUIJindoContainerScrollview showsVerticalScrollIndicator];
-[BKUIJindoContainerScrollview buttonTray];
-[BKUIJindoContainerScrollview setButtonTray:];
-[BKUIJindoContainerScrollview instructionView];
-[BKUIJindoContainerScrollview setInstructionView:];
-[BKUIJindoContainerScrollview scrollContentView];
-[BKUIJindoContainerScrollview setScrollContentView:];
-[BKUIJindoContainerScrollview animatingInstructionView];
-[BKUIJindoContainerScrollview buttonTrayTopAnchor];
-[BKUIJindoContainerScrollview horizontalConstraint];
-[BKUIJindoContainerScrollview initWithFrame:buttonTray:];
-[BKUIJindoContainerScrollview instructionViewTopConstraint];
-[BKUIJindoContainerScrollview pinButtonTrayToScrollViewBottomConstraint];
-[BKUIJindoContainerScrollview setAnimatingInstructionView:];
-[BKUIJindoContainerScrollview setButtonTrayTopAnchor:];
-[BKUIJindoContainerScrollview setHorizontalConstraint:];
-[BKUIJindoContainerScrollview setInstructionViewTopConstraint:];
-[BKUIJindoContainerScrollview setPinButtonTrayToScrollViewBottomConstraint:];
-[BKUIJindoContainerScrollview setScrollview:];
-[BKUIJindoContainerScrollview setTopToSuperViewConstraint:];
-[BKUIJindoContainerScrollview topToSuperViewConstraint];
```
