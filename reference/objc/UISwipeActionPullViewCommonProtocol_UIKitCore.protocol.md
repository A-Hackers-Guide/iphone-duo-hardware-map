# `UISwipeActionPullViewCommonProtocol` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 14 properties, 27 instance methods, 0 class methods

## Properties

```
@property (T@"<UISwipeActionPullViewDelegate>",W,N) delegate;
@property (TB,N) primaryActionCanBeTriggeredBySwipe;
@property (TQ,R,N) cellEdge;
@property (T{UIEdgeInsets=dddd},N) contentInsets;
@property (T{UIEdgeInsets=dddd},N) pullViewInsets;
@property (T{UIEdgeInsets=dddd},N) extraInsets;
@property (T@"UIColor",C,N) backgroundPullColor;
@property (T@"UIContextualAction",R,N) primarySwipeAction;
@property (Td,R,N) openThreshold;
@property (Td,R,N) confirmationThreshold;
@property (TB,R,N) primaryActionIsDestructive;
@property (TB,N) buttonsUnderlapSwipedView;
@property (TB,N) autosizesButtons;
@property (TQ,N) state;
```

## Instance methods

```
-[UISwipeActionPullViewCommonProtocol setState:];
-[UISwipeActionPullViewCommonProtocol setContentInsets:];
-[UISwipeActionPullViewCommonProtocol setDelegate:];
-[UISwipeActionPullViewCommonProtocol delegate];
-[UISwipeActionPullViewCommonProtocol contentInsets];
-[UISwipeActionPullViewCommonProtocol freeze];
-[UISwipeActionPullViewCommonProtocol state];
-[UISwipeActionPullViewCommonProtocol setExtraInsets:];
-[UISwipeActionPullViewCommonProtocol autosizesButtons];
-[UISwipeActionPullViewCommonProtocol backgroundPullColor];
-[UISwipeActionPullViewCommonProtocol buttonsUnderlapSwipedView];
-[UISwipeActionPullViewCommonProtocol cellEdge];
-[UISwipeActionPullViewCommonProtocol configureWithSwipeActions:];
-[UISwipeActionPullViewCommonProtocol confirmationThreshold];
-[UISwipeActionPullViewCommonProtocol extraInsets];
-[UISwipeActionPullViewCommonProtocol openThreshold];
-[UISwipeActionPullViewCommonProtocol primaryActionCanBeTriggeredBySwipe];
-[UISwipeActionPullViewCommonProtocol primaryActionIsDestructive];
-[UISwipeActionPullViewCommonProtocol primarySwipeAction];
-[UISwipeActionPullViewCommonProtocol pullViewInsets];
-[UISwipeActionPullViewCommonProtocol resetView];
-[UISwipeActionPullViewCommonProtocol setAutosizesButtons:];
-[UISwipeActionPullViewCommonProtocol setBackgroundPullColor:];
-[UISwipeActionPullViewCommonProtocol setButtonsUnderlapSwipedView:];
-[UISwipeActionPullViewCommonProtocol setPrimaryActionCanBeTriggeredBySwipe:];
-[UISwipeActionPullViewCommonProtocol setPullViewInsets:];
-[UISwipeActionPullViewCommonProtocol sourceViewForAction:];
```
