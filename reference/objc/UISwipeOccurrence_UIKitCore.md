# `UISwipeOccurrence`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UISwipeActionPullViewDelegate`
- 22 instance variables, 18 properties, 72 instance methods, 2 class methods

## Instance variables

```
{?="isTransitioning"b1"didNotifyWillFinish"b1"didNotifyDidFinish"b1"shouldReenableUserInteraction"b1"isRTL"b1"hasAmbiguousIndexPath"b1"didReloadData"b1} _flags;
Q _actionExecutionCounter;
@"UISwipeActionController" _controller;
Q _style;
Q _defaultStyle;
q _styleFromConfiguration;
d _roundedStyleCornerRadius;
@"UIView<UISwipeActionPullViewCommonProtocol>" _leadingPullView;
@"UIView<UISwipeActionPullViewCommonProtocol>" _trailingPullView;
@"<_UISwipeViewManipulator>" _manipulator;
B _swipedViewMaskWasRemoved;
B _active;
@"NSIndexPath" _indexPath;
q _direction;
d _offset;
q _state;
Q _configuredDirection;
@"UIView<_UISwipedView>" _swipedView;
@"UIContextualAction" _currentAction;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _extraInsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _pullViewInsets;
{?="direction"Q"targetSwipeState"Q"animated"B"xOffset"d"initialSpringVelocity"d"springStiffness"d} _currentSwipeInfo;
```

## Properties

```
@property (T@"NSIndexPath",C,N,V_indexPath) indexPath;
@property (TQ,N,V_configuredDirection) configuredDirection;
@property (T{?=QQBddd},N,V_currentSwipeInfo) currentSwipeInfo;
@property (T{UIEdgeInsets=dddd},N,V_extraInsets) extraInsets;
@property (T{UIEdgeInsets=dddd},N,V_pullViewInsets) pullViewInsets;
@property (T@"UIView<_UISwipedView>",&,N,V_swipedView) swipedView;
@property (TB,N,V_swipedViewMaskWasRemoved) swipedViewMaskWasRemoved;
@property (T@"UIContextualAction",&,N,V_currentAction) currentAction;
@property (TB,N,V_active) active;
@property (TB,R,N) isDynamicPullView;
@property (TB,R,N) isSwiftUIPullView;
@property (Tq,R,N,V_direction) direction;
@property (Td,N,V_offset) offset;
@property (Tq,R,N,V_state) state;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISwipeOccurrence isSwiftUIPullViewEnabled];
+[UISwipeOccurrence pullViewClass];
```

## Instance methods

```
-[UISwipeOccurrence active];
-[UISwipeOccurrence updateLayout];
-[UISwipeOccurrence indexPath];
-[UISwipeOccurrence actionView];
-[UISwipeOccurrence _transitionToState:];
-[UISwipeOccurrence velocity];
-[UISwipeOccurrence setActive:];
-[UISwipeOccurrence direction];
-[UISwipeOccurrence setIndexPath:];
-[UISwipeOccurrence description];
-[UISwipeOccurrence _style];
-[UISwipeOccurrence setOffset:];
-[UISwipeOccurrence offset];
-[UISwipeOccurrence state];
-[UISwipeOccurrence _updateSwipedStateOnSwipedView:];
-[UISwipeOccurrence setupManipulatorWithController:];
-[UISwipeOccurrence shouldDismissWithTouchLocation:];
-[UISwipeOccurrence _moveItemWithSwipeInfo:tracking:alongsideAnimations:completion:];
-[UISwipeOccurrence setExtraInsets:];
-[UISwipeOccurrence _actionView];
-[UISwipeOccurrence _didReloadData];
-[UISwipeOccurrence _executeLifecycleForPerformedAction:sourceView:completionHandler:];
-[UISwipeOccurrence _extraOffsetForOffset:withDirection:];
-[UISwipeOccurrence _forceTeardown];
-[UISwipeOccurrence _frameForPullView:inSwipedItem:withContainer:];
-[UISwipeOccurrence _freezeSwipedViewInsets];
-[UISwipeOccurrence _hasAmbiguousIndexPath];
-[UISwipeOccurrence _isSwipeDirectionExposingLeadingEdgePullView:];
-[UISwipeOccurrence _performSwipeAction:inPullView:swipeInfo:];
-[UISwipeOccurrence _pullViewForLeadingEdge:];
-[UISwipeOccurrence _pullViewForSwipeDirection:];
-[UISwipeOccurrence _removeAndResetPullViewImmediately:];
-[UISwipeOccurrence _removePullViewImmediately:];
-[UISwipeOccurrence _resetItemWithSwipeInfo:animated:deletion:completion:];
-[UISwipeOccurrence _setDidReloadData];
-[UISwipeOccurrence _setHasAmbiguousIndexPath];
-[UISwipeOccurrence _styleForConfiguration:];
-[UISwipeOccurrence _styleFromConfiguration];
-[UISwipeOccurrence _swipeDirectionForPullView:];
-[UISwipeOccurrence _unfreezeSwipedViewInsets];
-[UISwipeOccurrence _updateLayoutUsingCurrentSwipeInfo:];
-[UISwipeOccurrence _updatePullView:];
-[UISwipeOccurrence beginSwipeTracking:];
-[UISwipeOccurrence configuredDirection];
-[UISwipeOccurrence confirmationDistanceForPrimaryActionInSwipeActionPullView:];
-[UISwipeOccurrence currentAction];
-[UISwipeOccurrence currentSwipeInfo];
-[UISwipeOccurrence endSwipe];
-[UISwipeOccurrence extraInsets];
-[UISwipeOccurrence initWithController:indexPath:defaultStyle:];
-[UISwipeOccurrence isDynamicPullView];
-[UISwipeOccurrence isSwiftUIPullView];
-[UISwipeOccurrence lockActionViewForAnimation];
-[UISwipeOccurrence performPrimaryActionWithSwipeInfo:];
-[UISwipeOccurrence prepareWithSwipeDirection:configuration:];
-[UISwipeOccurrence pullViewInsets];
-[UISwipeOccurrence resetAnimated:completion:];
-[UISwipeOccurrence resetForReconfiguration];
-[UISwipeOccurrence resetWhilePreparing];
-[UISwipeOccurrence setConfiguredDirection:];
-[UISwipeOccurrence setCurrentAction:];
-[UISwipeOccurrence setCurrentSwipeInfo:];
-[UISwipeOccurrence setPullViewInsets:];
-[UISwipeOccurrence setSwipedView:];
-[UISwipeOccurrence setSwipedViewMaskWasRemoved:];
-[UISwipeOccurrence swipeActionPullView:tappedAction:];
-[UISwipeOccurrence swipedView];
-[UISwipeOccurrence swipedViewMaskWasRemoved];
-[UISwipeOccurrence swipedViewRestingFrame];
-[UISwipeOccurrence unlockActionViewForAnimation:];
-[UISwipeOccurrence updateOffsetWithSwipeInfo:isTracking:completion:];
-[UISwipeOccurrence updateSwipedView];
```
