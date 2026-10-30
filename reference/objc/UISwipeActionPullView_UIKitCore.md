# `UISwipeActionPullView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UISwipeActionButtonDelegate`, `UISwipeActionPullViewCommonProtocol`
- 23 instance variables, 23 properties, 57 instance methods, 0 class methods

## Instance variables

```
@"UIView" _clippingView;
@"NSMutableArray" _buttons;
@"NSArray" _actions;
@"UISwipeActionButton" _pressedButton;
B _swipeActionsDidChange;
B _isTentative;
d _openThreshold;
d _confirmationThreshold;
d _minimumOffset;
Q _style;
B _primaryActionCanBeTriggeredBySwipe;
B _buttonsUnderlapSwipedView;
B _autosizesButtons;
Q _cellEdge;
d _currentOffset;
@"<UISwipeActionPullViewDelegate>" _delegate;
@"UIColor" _backgroundPullColor;
Q _state;
@"<UISwipeActionVisualStyle>" _visualStyle;
d _roundedStyleCornerRadius;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _contentInsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _pullViewInsets;
{UIEdgeInsets="top"d"left"d"bottom"d"right"d} _extraInsets;
```

## Properties

```
@property (T@"<UISwipeActionVisualStyle>",&,N,V_visualStyle) visualStyle;
@property (Td,N,G_roundedStyleCornerRadius,S_setRoundedStyleCornerRadius:,V_roundedStyleCornerRadius) roundedStyleCornerRadius;
@property (T@"<UISwipeActionPullViewDelegate>",W,N,V_delegate) delegate;
@property (TB,N,V_primaryActionCanBeTriggeredBySwipe) primaryActionCanBeTriggeredBySwipe;
@property (TQ,R,N,V_cellEdge) cellEdge;
@property (T{UIEdgeInsets=dddd},N,V_contentInsets) contentInsets;
@property (T{UIEdgeInsets=dddd},N,V_pullViewInsets) pullViewInsets;
@property (T{UIEdgeInsets=dddd},N,V_extraInsets) extraInsets;
@property (T@"UIColor",C,N,V_backgroundPullColor) backgroundPullColor;
@property (T@"UIContextualAction",R,N) primarySwipeAction;
@property (Td,R,N,V_currentOffset) currentOffset;
@property (Td,R,N) openThreshold;
@property (Td,R,N) confirmationThreshold;
@property (T@"UIColor",R,N) primaryActionColor;
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
-[UISwipeActionPullView setVisualStyle:];
-[UISwipeActionPullView setState:];
-[UISwipeActionPullView setContentInsets:];
-[UISwipeActionPullView hasActions];
-[UISwipeActionPullView visualStyle];
-[UISwipeActionPullView layoutSubviews];
-[UISwipeActionPullView hitTest:withEvent:];
-[UISwipeActionPullView currentOffset];
-[UISwipeActionPullView setBounds:];
-[UISwipeActionPullView setDelegate:];
-[UISwipeActionPullView delegate];
-[UISwipeActionPullView contentInsets];
-[UISwipeActionPullView setFrame:];
-[UISwipeActionPullView description];
-[UISwipeActionPullView freeze];
-[UISwipeActionPullView state];
-[UISwipeActionPullView _pressedButton:];
-[UISwipeActionPullView _rebuildButtons];
-[UISwipeActionPullView setExtraInsets:];
-[UISwipeActionPullView _buttonClass];
-[UISwipeActionPullView _directionalMultiplier];
-[UISwipeActionPullView _interButtonPadding];
-[UISwipeActionPullView _layoutClippingLayer];
-[UISwipeActionPullView _paddingToSwipedView];
-[UISwipeActionPullView _performAction:offset:extraOffset:];
-[UISwipeActionPullView _roundedStyleCornerRadius];
-[UISwipeActionPullView _setLayerBounds:];
-[UISwipeActionPullView _setRoundedStyleCornerRadius:];
-[UISwipeActionPullView _setWidth:];
-[UISwipeActionPullView _setupClippingViewIfNeeded];
-[UISwipeActionPullView _swipeActionCount];
-[UISwipeActionPullView _tappedButton:];
-[UISwipeActionPullView _totalInterButtonPadding];
-[UISwipeActionPullView _unpressedButton:];
-[UISwipeActionPullView autosizesButtons];
-[UISwipeActionPullView backgroundPullColor];
-[UISwipeActionPullView buttonsUnderlapSwipedView];
-[UISwipeActionPullView cellEdge];
-[UISwipeActionPullView configureWithSwipeActions:];
-[UISwipeActionPullView confirmationThreshold];
-[UISwipeActionPullView extraInsets];
-[UISwipeActionPullView initWithFrame:cellEdge:style:];
-[UISwipeActionPullView moveToOffset:extraOffset:animator:usingSpringWithStiffness:initialVelocity:];
-[UISwipeActionPullView openThreshold];
-[UISwipeActionPullView primaryActionCanBeTriggeredBySwipe];
-[UISwipeActionPullView primaryActionColor];
-[UISwipeActionPullView primaryActionIsDestructive];
-[UISwipeActionPullView primarySwipeAction];
-[UISwipeActionPullView pullViewInsets];
-[UISwipeActionPullView resetView];
-[UISwipeActionPullView setAutosizesButtons:];
-[UISwipeActionPullView setBackgroundPullColor:];
-[UISwipeActionPullView setButtonsUnderlapSwipedView:];
-[UISwipeActionPullView setPrimaryActionCanBeTriggeredBySwipe:];
-[UISwipeActionPullView setPullViewInsets:];
-[UISwipeActionPullView sourceViewForAction:];
-[UISwipeActionPullView swipeActionButton:willDisplayContextMenuWithAnimator:];
```
