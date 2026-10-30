# `UISwipeActionDynamicPullViewSwiftUI`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `UISwipeActionPullViewCommonProtocol`
- 13 instance variables, 15 properties, 39 instance methods, 0 class methods

## Instance variables

```
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 viewState;
@"<UISwipeActionPullViewDelegate>" delegate;
Q cellEdge;
{UIEdgeInsets=dddd} contentInsets;
{UIEdgeInsets=dddd} pullViewInsets;
{UIEdgeInsets=dddd} extraInsets;
@"UIColor" backgroundPullColor;
B primaryActionCanBeTriggeredBySwipe;
d currentOffset;
B buttonsUnderlapSwipedView;
B autosizesButtons;
Q state;
v48@0:8@"NSURLSession"16@"NSURLSessionDataTask"24@"NSData"32@?<v@?>40 coreHostingView;
```

## Properties

```
@property (T@"<UISwipeActionPullViewDelegate>",N,&,Vdelegate) delegate;
@property (TQ,N,VcellEdge) cellEdge;
@property (T{UIEdgeInsets=dddd},N,VcontentInsets) contentInsets;
@property (T{UIEdgeInsets=dddd},N,VpullViewInsets) pullViewInsets;
@property (T{UIEdgeInsets=dddd},N,VextraInsets) extraInsets;
@property (T@"UIColor",N,&,VbackgroundPullColor) backgroundPullColor;
@property (T@"UIContextualAction",N,R) primarySwipeAction;
@property (TB,N,R) primaryActionIsDestructive;
@property (TB,N,VprimaryActionCanBeTriggeredBySwipe) primaryActionCanBeTriggeredBySwipe;
@property (Td,N,R) openThreshold;
@property (Td,N,R) confirmationThreshold;
@property (Td,N,VcurrentOffset) currentOffset;
@property (TB,N,VbuttonsUnderlapSwipedView) buttonsUnderlapSwipedView;
@property (TB,N,VautosizesButtons) autosizesButtons;
@property (TQ,N,Vstate) state;
```

## Instance methods

```
-[UISwipeActionDynamicPullViewSwiftUI setState:];
-[UISwipeActionDynamicPullViewSwiftUI setContentInsets:];
-[UISwipeActionDynamicPullViewSwiftUI init];
-[UISwipeActionDynamicPullViewSwiftUI layoutSubviews];
-[UISwipeActionDynamicPullViewSwiftUI hitTest:withEvent:];
-[UISwipeActionDynamicPullViewSwiftUI currentOffset];
-[UISwipeActionDynamicPullViewSwiftUI setDelegate:];
-[UISwipeActionDynamicPullViewSwiftUI delegate];
-[UISwipeActionDynamicPullViewSwiftUI contentInsets];
-[UISwipeActionDynamicPullViewSwiftUI freeze];
-[UISwipeActionDynamicPullViewSwiftUI initWithCoder:];
-[UISwipeActionDynamicPullViewSwiftUI initWithFrame:];
-[UISwipeActionDynamicPullViewSwiftUI state];
-[UISwipeActionDynamicPullViewSwiftUI setExtraInsets:];
-[UISwipeActionDynamicPullViewSwiftUI _performAction:offset:];
-[UISwipeActionDynamicPullViewSwiftUI autosizesButtons];
-[UISwipeActionDynamicPullViewSwiftUI backgroundPullColor];
-[UISwipeActionDynamicPullViewSwiftUI buttonsUnderlapSwipedView];
-[UISwipeActionDynamicPullViewSwiftUI cellEdge];
-[UISwipeActionDynamicPullViewSwiftUI configureWithSwipeActions:];
-[UISwipeActionDynamicPullViewSwiftUI confirmationThreshold];
-[UISwipeActionDynamicPullViewSwiftUI extraInsets];
-[UISwipeActionDynamicPullViewSwiftUI initWithFrame:cellEdge:];
-[UISwipeActionDynamicPullViewSwiftUI moveToOffset:animator:interactive:];
-[UISwipeActionDynamicPullViewSwiftUI moveToOffset:animator:interactive:duration:bounce:blendDuration:];
-[UISwipeActionDynamicPullViewSwiftUI openThreshold];
-[UISwipeActionDynamicPullViewSwiftUI primaryActionCanBeTriggeredBySwipe];
-[UISwipeActionDynamicPullViewSwiftUI primaryActionIsDestructive];
-[UISwipeActionDynamicPullViewSwiftUI primarySwipeAction];
-[UISwipeActionDynamicPullViewSwiftUI pullViewInsets];
-[UISwipeActionDynamicPullViewSwiftUI resetView];
-[UISwipeActionDynamicPullViewSwiftUI setAutosizesButtons:];
-[UISwipeActionDynamicPullViewSwiftUI setBackgroundPullColor:];
-[UISwipeActionDynamicPullViewSwiftUI setButtonsUnderlapSwipedView:];
-[UISwipeActionDynamicPullViewSwiftUI setCellEdge:];
-[UISwipeActionDynamicPullViewSwiftUI setCurrentOffset:];
-[UISwipeActionDynamicPullViewSwiftUI setPrimaryActionCanBeTriggeredBySwipe:];
-[UISwipeActionDynamicPullViewSwiftUI setPullViewInsets:];
-[UISwipeActionDynamicPullViewSwiftUI sourceViewForAction:];
```
