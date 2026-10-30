# `_UIKeyboardAnimatorAnimationStyleControllerContext`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_UIKeyboardAnimatorState`
- 6 instance variables, 8 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"<UIInputViewAnimationHost>" _host;
@"UIInputViewSetPlacement" _start;
@"UIInputViewSetPlacement" _end;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _startFrame;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _endFrame;
B _hidden;
```

## Properties

```
@property (T@"UIView",R,&,N) animatingView;
@property (TB,N,V_hidden) inputViewsHidden;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_startFrame) startFrame;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},R,N,V_endFrame) endFrame;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIKeyboardAnimatorAnimationStyleControllerContext setInputViewsHidden:];
-[_UIKeyboardAnimatorAnimationStyleControllerContext endFrame];
-[_UIKeyboardAnimatorAnimationStyleControllerContext complete];
-[_UIKeyboardAnimatorAnimationStyleControllerContext startFrame];
-[_UIKeyboardAnimatorAnimationStyleControllerContext animatingView];
-[_UIKeyboardAnimatorAnimationStyleControllerContext initWithHost:startPlacement:endPlacement:];
-[_UIKeyboardAnimatorAnimationStyleControllerContext inputViewsHidden];
```
