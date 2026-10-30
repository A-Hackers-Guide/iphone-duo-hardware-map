# `UISwipeActionDynamicPullView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UISwipeActionDynamicButtonViewDelegate`, `UISwipeActionPullViewCommonProtocol`
- 20 instance variables, 27 properties, 66 instance methods, 0 class methods

## Instance variables

```
B _primaryActionCanBeTriggeredBySwipe;
B _buttonsUnderlapSwipedView;
B _autosizesButtons;
B _swipeActionsDidChange;
B _pullViewHeightDidChange;
Q _cellEdge;
@"<UISwipeActionPullViewDelegate>" _delegate;
@"UIColor" _backgroundPullColor;
d _currentOffset;
d _openThreshold;
d _confirmationThreshold;
@"UIColor" _primaryActionColor;
Q _state;
@"NSMutableArray" _buttons;
@"NSArray" _actions;
@"UIView" _containerView;
@"_UIGroupCompletion" _animationGroupCompletion;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _contentInsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _pullViewInsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _extraInsets;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_buttons) buttons;
@property (T@"NSArray",&,N,V_actions) actions;
@property (TB,N,V_swipeActionsDidChange) swipeActionsDidChange;
@property (TB,N,V_pullViewHeightDidChange) pullViewHeightDidChange;
@property (Td,N,V_openThreshold) openThreshold;
@property (Td,N,V_confirmationThreshold) confirmationThreshold;
@property (T@"UIView",&,N,V_containerView) containerView;
@property (T@"_UIGroupCompletion",&,N,V_animationGroupCompletion) animationGroupCompletion;
@property (T@"<UISwipeActionPullViewDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_primaryActionCanBeTriggeredBySwipe) primaryActionCanBeTriggeredBySwipe;
@property (TQ,R,N,V_cellEdge) cellEdge;
@property (T{UIEdgeInsets=dddd},N,V_contentInsets) contentInsets;
@property (T{UIEdgeInsets=dddd},N,V_pullViewInsets) pullViewInsets;
@property (T{UIEdgeInsets=dddd},N,V_extraInsets) extraInsets;
@property (T@"UIColor",C,N,V_backgroundPullColor) backgroundPullColor;
@property (T@"UIContextualAction",R,N) primarySwipeAction;
@property (Td,R,N,V_currentOffset) currentOffset;
@property (T@"UIColor",R,N,V_primaryActionColor) primaryActionColor;
@property (TB,R,N) primaryActionIsDestructive;
@property (TB,R,N) hasActions;
@property (TB,N,V_buttonsUnderlapSwipedView) buttonsUnderlapSwipedView;
@property (TB,N,V_autosizesButtons) autosizesButtons;
@property (TQ,N,V_state) state;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UISwipeActionDynamicPullView buttons];
-[UISwipeActionDynamicPullView setContainerView:];
-[UISwipeActionDynamicPullView setState:];
-[UISwipeActionDynamicPullView setContentInsets:];
-[UISwipeActionDynamicPullView hasActions];
-[UISwipeActionDynamicPullView setActions:];
-[UISwipeActionDynamicPullView layoutSubviews];
-[UISwipeActionDynamicPullView setButtons:];
-[UISwipeActionDynamicPullView currentOffset];
-[UISwipeActionDynamicPullView actions];
-[UISwipeActionDynamicPullView setBounds:];
-[UISwipeActionDynamicPullView containerView];
-[UISwipeActionDynamicPullView setDelegate:];
-[UISwipeActionDynamicPullView delegate];
-[UISwipeActionDynamicPullView contentInsets];
-[UISwipeActionDynamicPullView setFrame:];
-[UISwipeActionDynamicPullView description];
-[UISwipeActionDynamicPullView freeze];
-[UISwipeActionDynamicPullView state];
-[UISwipeActionDynamicPullView _rebuildButtons];
-[UISwipeActionDynamicPullView setExtraInsets:];
-[UISwipeActionDynamicPullView _directionalMultiplier];
-[UISwipeActionDynamicPullView _interButtonPadding];
-[UISwipeActionDynamicPullView _moveToOffset:animator:interactive:animated:];
-[UISwipeActionDynamicPullView _moveToOffset:animator:interactive:duration:bounce:blendDuration:animated:];
-[UISwipeActionDynamicPullView _performAction:offset:];
-[UISwipeActionDynamicPullView _processSizeChange:newSize:];
-[UISwipeActionDynamicPullView _setFrame:processSizeChange:];
-[UISwipeActionDynamicPullView _totalInterButtonPadding];
-[UISwipeActionDynamicPullView animationGroupCompletion];
-[UISwipeActionDynamicPullView autosizesButtons];
-[UISwipeActionDynamicPullView backgroundPullColor];
-[UISwipeActionDynamicPullView buttonTypes];
-[UISwipeActionDynamicPullView buttonsUnderlapSwipedView];
-[UISwipeActionDynamicPullView calculateAllInlineWidths:];
-[UISwipeActionDynamicPullView calculateUniformSize];
-[UISwipeActionDynamicPullView cellEdge];
-[UISwipeActionDynamicPullView configureWithSwipeActions:];
-[UISwipeActionDynamicPullView confirmationThreshold];
-[UISwipeActionDynamicPullView extraInsets];
-[UISwipeActionDynamicPullView initWithFrame:cellEdge:];
-[UISwipeActionDynamicPullView moveToOffset:animator:interactive:];
-[UISwipeActionDynamicPullView moveToOffset:animator:interactive:duration:bounce:blendDuration:];
-[UISwipeActionDynamicPullView openThreshold];
-[UISwipeActionDynamicPullView prepareButtons];
-[UISwipeActionDynamicPullView primaryActionCanBeTriggeredBySwipe];
-[UISwipeActionDynamicPullView primaryActionColor];
-[UISwipeActionDynamicPullView primaryActionIsDestructive];
-[UISwipeActionDynamicPullView primarySwipeAction];
-[UISwipeActionDynamicPullView pullViewHeightDidChange];
-[UISwipeActionDynamicPullView pullViewInsets];
-[UISwipeActionDynamicPullView resetView];
-[UISwipeActionDynamicPullView setAnimationGroupCompletion:];
-[UISwipeActionDynamicPullView setAutosizesButtons:];
-[UISwipeActionDynamicPullView setBackgroundPullColor:];
-[UISwipeActionDynamicPullView setButtonsUnderlapSwipedView:];
-[UISwipeActionDynamicPullView setConfirmationThreshold:];
-[UISwipeActionDynamicPullView setOpenThreshold:];
-[UISwipeActionDynamicPullView setPrimaryActionCanBeTriggeredBySwipe:];
-[UISwipeActionDynamicPullView setPullViewHeightDidChange:];
-[UISwipeActionDynamicPullView setPullViewInsets:];
-[UISwipeActionDynamicPullView setSwipeActionsDidChange:];
-[UISwipeActionDynamicPullView sourceViewForAction:];
-[UISwipeActionDynamicPullView swipeActionButtonDidTouchUpInside:];
-[UISwipeActionDynamicPullView swipeActionWillDisplayMenuForButton:];
-[UISwipeActionDynamicPullView swipeActionsDidChange];
```
