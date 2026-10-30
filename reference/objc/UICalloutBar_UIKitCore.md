# `UICalloutBar`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- 8 instance variables, 9 properties, 23 instance methods, 4 class methods

## Instance variables

```
B _supressesHorizontalMovement;
i _targetDirection;
@"UIView" _targetView;
@"UIResponder" _responderTarget;
@"NSArray" _extraItems;
@"NSString" _untruncatedString;
{CGPoint="x"d"y"d} _targetPoint;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _targetRect;
```

## Properties

```
@property (T{CGPoint=dd},R,N,V_targetPoint) targetPoint;
@property (Ti,R,N,V_targetDirection) targetDirection;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_targetRect) targetRect;
@property (T@"UIView",R,W,N,V_targetView) targetView;
@property (TB,R,N) visible;
@property (T@"UIResponder",W,N,V_responderTarget) responderTarget;
@property (T@"NSArray",C,N,V_extraItems) extraItems;
@property (T@"NSString",C,N,V_untruncatedString) untruncatedString;
@property (TB,N,V_supressesHorizontalMovement) supressesHorizontalMovement;
```

## Class methods

```
+[UICalloutBar activeCalloutBar];
+[UICalloutBar hideSharedCalloutBar];
+[UICalloutBar sharedCalloutBar];
+[UICalloutBar sharedCalloutBarIsVisible];
```

## Instance methods

```
-[UICalloutBar hide];
-[UICalloutBar targetView];
-[UICalloutBar visible];
-[UICalloutBar update];
-[UICalloutBar updateAnimated:];
-[UICalloutBar targetRect];
-[UICalloutBar show];
-[UICalloutBar responderTarget];
-[UICalloutBar setSupressesHorizontalMovement:];
-[UICalloutBar targetDirection];
-[UICalloutBar appear];
-[UICalloutBar clearSupressesHorizontalMovementFrame];
-[UICalloutBar extraItems];
-[UICalloutBar fade];
-[UICalloutBar resetPage];
-[UICalloutBar setExtraItems:];
-[UICalloutBar setResponderTarget:];
-[UICalloutBar setResponderTarget:completion:];
-[UICalloutBar setTargetRect:view:arrowDirection:];
-[UICalloutBar setUntruncatedString:];
-[UICalloutBar supressesHorizontalMovement];
-[UICalloutBar targetPoint];
-[UICalloutBar untruncatedString];
```
