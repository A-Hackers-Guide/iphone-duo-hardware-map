# `_UIFocusItemDummy`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIFocusItem`
- 2 instance variables, 15 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<UIFocusEnvironment>" _parentFocusEnvironment;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
```

## Properties

```
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_frame) frame;
@property (T@"<UIFocusEnvironment>",W,N,V_parentFocusEnvironment) parentFocusEnvironment;
@property (TB,R,N) canBecomeFocused;
@property (T@"UIFocusEffect",?,R,C,N) focusEffect;
@property (Tq,?,R,N) focusGroupPriority;
@property (Tq,?,R,N) focusItemDeferralMode;
@property (TB,?,R,N) isTransparentFocusItem;
@property (T@"NSArray",R,C,N) preferredFocusEnvironments;
@property (T@"<UIFocusItemContainer>",R,N) focusItemContainer;
@property (T@"UIView",?,R,W,N) preferredFocusedView;
@property (T@"NSString",?,R,C,N) focusGroupIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIFocusItemDummy updateFocusIfNeeded];
-[_UIFocusItemDummy didUpdateFocusInContext:withAnimationCoordinator:];
-[_UIFocusItemDummy setNeedsFocusUpdate];
-[_UIFocusItemDummy parentFocusEnvironment];
-[_UIFocusItemDummy focusItemContainer];
-[_UIFocusItemDummy canBecomeFocused];
-[_UIFocusItemDummy setFrame:];
-[_UIFocusItemDummy preferredFocusEnvironments];
-[_UIFocusItemDummy shouldUpdateFocusInContext:];
-[_UIFocusItemDummy frame];
-[_UIFocusItemDummy setParentFocusEnvironment:];
```
