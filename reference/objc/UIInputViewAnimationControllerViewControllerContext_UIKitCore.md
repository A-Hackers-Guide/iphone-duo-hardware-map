# `UIInputViewAnimationControllerViewControllerContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIViewControllerKeyboardContextTransitioning`
- 8 instance variables, 9 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"_UIViewControllerTransitionContext" _context;
@"<UIInputViewAnimationHost>" _host;
@"UIView" _from;
@"UIView" _to;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _fromRect;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _toRect;
@"UIKBViewTreeSnapshotter" _kbSnapshotter;
@"UIInputViewSet" _preservedInputViewSet;
```

## Properties

```
@property (T@"<UIViewControllerContextTransitioning>",R,N) mainContext;
@property (T@"UIView",R,N) fromKeyboard;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) fromKeyboardFrame;
@property (T@"UIView",R,N) toKeyboard;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N) toKeyboardFrame;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UIInputViewAnimationControllerViewControllerContext contextWithHost:startPlacement:endPlacement:transitionContext:];
```

## Instance methods

```
-[UIInputViewAnimationControllerViewControllerContext dealloc];
-[UIInputViewAnimationControllerViewControllerContext toKeyboardFrame];
-[UIInputViewAnimationControllerViewControllerContext fromKeyboard];
-[UIInputViewAnimationControllerViewControllerContext fromKeyboardFrame];
-[UIInputViewAnimationControllerViewControllerContext initWithHost:startPlacement:endPlacement:transitionContext:];
-[UIInputViewAnimationControllerViewControllerContext mainContext];
-[UIInputViewAnimationControllerViewControllerContext toKeyboard];
```
