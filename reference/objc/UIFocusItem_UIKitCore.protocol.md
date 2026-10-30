# `UIFocusItem` (protocol)

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `UIFocusEnvironment`
- 0 instance variables, 6 properties, 7 instance methods, 0 class methods

## Properties

```
@property (TB,R,N) canBecomeFocused;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) frame;
@property (T@"UIFocusEffect",?,R,C,N) focusEffect;
@property (Tq,?,R,N) focusGroupPriority;
@property (Tq,?,R,N) focusItemDeferralMode;
@property (TB,?,R,N) isTransparentFocusItem;
```

## Instance methods

```
-[UIFocusItem canBecomeFocused];
-[UIFocusItem frame];
-[UIFocusItem focusEffect];
-[UIFocusItem focusItemDeferralMode];
-[UIFocusItem isTransparentFocusItem];
-[UIFocusItem didHintFocusMovement:];
-[UIFocusItem focusGroupPriority];
```
