# `BKUIPearlPillContainerView`

- Image: [`/System/Library/PrivateFrameworks/BiometricKitUI.framework/BiometricKitUI`](../userland/System__Library__PrivateFrameworks__BiometricKitUI.framework__BiometricKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 13 instance variables, 5 properties, 26 instance methods, 0 class methods

## Instance variables

```
@"NSMutableArray" _pillViews;
@"LAUICheckmarkLayer" _successAnimation;
q _numberOfVisiblePillViews;
q _clockwise;
q _counterwise;
q _lastAngle;
B _hasPillStateStash;
[120Q] _stashedPillStates;
B _squareNeedsPositionLayout;
i _state;
d _radius;
@"<UITraitChangeRegistration>" _traitChangeRegistration;
{CGPoint="x"d"y"d} _enrollViewCenter;
```

## Properties

```
@property (Ti,N,V_state) state;
@property (T{CGPoint=dd},N,V_enrollViewCenter) enrollViewCenter;
@property (T@"<UITraitChangeRegistration>",&,N,V_traitChangeRegistration) traitChangeRegistration;
@property (Td,R,N,V_radius) radius;
@property (TB,N,V_squareNeedsPositionLayout) squareNeedsPositionLayout;
```

## Instance methods

```
-[BKUIPearlPillContainerView setState:];
-[BKUIPearlPillContainerView init];
-[BKUIPearlPillContainerView dealloc];
-[BKUIPearlPillContainerView layoutSubviews];
-[BKUIPearlPillContainerView radius];
-[BKUIPearlPillContainerView state];
-[BKUIPearlPillContainerView setTraitChangeRegistration:];
-[BKUIPearlPillContainerView traitChangeRegistration];
-[BKUIPearlPillContainerView _indexForPillAtAngle:];
-[BKUIPearlPillContainerView animateToState:completion:];
-[BKUIPearlPillContainerView fillPillsAroundAngle:];
-[BKUIPearlPillContainerView stashPillStates];
-[BKUIPearlPillContainerView _animateToFinishedCompletion:];
-[BKUIPearlPillContainerView _numberOfVisiblePillViews];
-[BKUIPearlPillContainerView enrollViewCenter];
-[BKUIPearlPillContainerView fillPillsAroundAngle:forTutorial:];
-[BKUIPearlPillContainerView percentOfPillsCompleted];
-[BKUIPearlPillContainerView resetPillsAnimated:];
-[BKUIPearlPillContainerView setAllPillState:animated:completion:];
-[BKUIPearlPillContainerView setEnrollViewCenter:];
-[BKUIPearlPillContainerView setRadius:center:animated:completion:];
-[BKUIPearlPillContainerView unfilledDirections];
-[BKUIPearlPillContainerView unstashPillStatesAnimated:];
-[BKUIPearlPillContainerView unstashPillStatesIfNeededAnimated:];
-[BKUIPearlPillContainerView setSquareNeedsPositionLayout:];
-[BKUIPearlPillContainerView squareNeedsPositionLayout];
```
