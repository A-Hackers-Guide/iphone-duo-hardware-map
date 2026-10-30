# `_UIFocusPromiseItem`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIFocusItemContainer`, `UIFocusItem`
- 6 instance variables, 19 properties, 22 instance methods, 0 class methods

## Instance variables

```
{?="didFulfillPromise"b1} _flags;
@"<UIFocusItem>" _fulfilledItem;
@"<UIFocusEnvironment>" _parentFocusEnvironment;
@"NSString" _debugIdentifier;
@? _fulfillmentHandler;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
```

## Properties

```
@property (T@"<UIFocusEnvironment>",W,N,V_parentFocusEnvironment) parentFocusEnvironment;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_frame) frame;
@property (T@?,C,N,V_fulfillmentHandler) fulfillmentHandler;
@property (T@"<UIFocusItem>",R,N,V_fulfilledItem) fulfilledItem;
@property (T@"NSString",C,N,V_debugIdentifier) debugIdentifier;
@property (T@"<UICoordinateSpace>",R,N) coordinateSpace;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TB,R,N) canBecomeFocused;
@property (T@"UIFocusEffect",?,R,C,N) focusEffect;
@property (Tq,?,R,N) focusGroupPriority;
@property (Tq,?,R,N) focusItemDeferralMode;
@property (TB,?,R,N) isTransparentFocusItem;
@property (T@"NSArray",R,C,N) preferredFocusEnvironments;
@property (T@"<UIFocusItemContainer>",R,N) focusItemContainer;
@property (T@"UIView",?,R,W,N) preferredFocusedView;
@property (T@"NSString",?,R,C,N) focusGroupIdentifier;
```

## Instance methods

```
-[_UIFocusPromiseItem _isEligibleForFocusInteraction];
-[_UIFocusPromiseItem updateFocusIfNeeded];
-[_UIFocusPromiseItem setDebugIdentifier:];
-[_UIFocusPromiseItem debugIdentifier];
-[_UIFocusPromiseItem coordinateSpace];
-[_UIFocusPromiseItem focusItemsInRect:];
-[_UIFocusPromiseItem didUpdateFocusInContext:withAnimationCoordinator:];
-[_UIFocusPromiseItem setNeedsFocusUpdate];
-[_UIFocusPromiseItem parentFocusEnvironment];
-[_UIFocusPromiseItem focusItemContainer];
-[_UIFocusPromiseItem canBecomeFocused];
-[_UIFocusPromiseItem setFrame:];
-[_UIFocusPromiseItem description];
-[_UIFocusPromiseItem preferredFocusEnvironments];
-[_UIFocusPromiseItem shouldUpdateFocusInContext:];
-[_UIFocusPromiseItem frame];
-[_UIFocusPromiseItem _isLazyFocusItemContainer];
-[_UIFocusPromiseItem fulfilledItem];
-[_UIFocusPromiseItem fulfillmentHandler];
-[_UIFocusPromiseItem initWithParentEnvironment:frame:fullfillmentHandler:];
-[_UIFocusPromiseItem setFulfillmentHandler:];
-[_UIFocusPromiseItem setParentFocusEnvironment:];
```
