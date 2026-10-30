# `BKUIScrollableContainer` (protocol)

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 11 properties, 25 instance methods, 0 class methods

## Properties

```
@property (T@"UIView",&,N) scrollContentView;
@property (T@"BKUIPearlInstructionView",&,N) instructionView;
@property (T@"BKUIPearlInstructionView",&,N) animatingInstructionView;
@property (T@"BKUIButtonTray",&,N) buttonTray;
@property (T@"NSLayoutConstraint",&,N) pinButtonTrayToScrollViewBottomConstraint;
@property (T@"NSLayoutConstraint",&,N) horizontalConstraint;
@property (T@"NSLayoutConstraint",&,N) instructionViewTopConstraint;
@property (T@"NSLayoutConstraint",&,N) buttonTrayTopAnchor;
@property (T@"NSLayoutConstraint",&,N) topToSuperViewConstraint;
@property (Tq,N) indicatorStyle;
@property (TB,N) showsVerticalScrollIndicator;
```

## Instance methods

```
-[BKUIScrollableContainer setContentOffset:animated:];
-[BKUIScrollableContainer initWithFrame:];
-[BKUIScrollableContainer indicatorStyle];
-[BKUIScrollableContainer setIndicatorStyle:];
-[BKUIScrollableContainer setShowsVerticalScrollIndicator:];
-[BKUIScrollableContainer showsVerticalScrollIndicator];
-[BKUIScrollableContainer buttonTray];
-[BKUIScrollableContainer setButtonTray:];
-[BKUIScrollableContainer instructionView];
-[BKUIScrollableContainer setInstructionView:];
-[BKUIScrollableContainer scrollContentView];
-[BKUIScrollableContainer setScrollContentView:];
-[BKUIScrollableContainer animatingInstructionView];
-[BKUIScrollableContainer buttonTrayTopAnchor];
-[BKUIScrollableContainer horizontalConstraint];
-[BKUIScrollableContainer initWithFrame:buttonTray:];
-[BKUIScrollableContainer instructionViewTopConstraint];
-[BKUIScrollableContainer pinButtonTrayToScrollViewBottomConstraint];
-[BKUIScrollableContainer setAnimatingInstructionView:];
-[BKUIScrollableContainer setButtonTrayTopAnchor:];
-[BKUIScrollableContainer setHorizontalConstraint:];
-[BKUIScrollableContainer setInstructionViewTopConstraint:];
-[BKUIScrollableContainer setPinButtonTrayToScrollViewBottomConstraint:];
-[BKUIScrollableContainer setTopToSuperViewConstraint:];
-[BKUIScrollableContainer topToSuperViewConstraint];
```
