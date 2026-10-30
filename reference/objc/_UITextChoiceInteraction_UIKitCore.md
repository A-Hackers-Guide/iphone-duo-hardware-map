# `_UITextChoiceInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteraction`, `UIGestureRecognizerDelegate`
- 3 instance variables, 8 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"<_UITextChoiceInteractionDelegate>" _delegate;
@"UIView" _textView;
@"UITapGestureRecognizer" _underlineTap;
```

## Properties

```
@property (T@"UIView",W,N,V_textView) textView;
@property (T@"UITapGestureRecognizer",&,N,V_underlineTap) underlineTap;
@property (T@"<_UITextChoiceInteractionDelegate>",W,N,V_delegate) delegate;
@property (T@"UIView",R,W,N) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITextChoiceInteraction setTextView:];
-[_UITextChoiceInteraction underlineTap];
-[_UITextChoiceInteraction initWithDelegate:];
-[_UITextChoiceInteraction textView];
-[_UITextChoiceInteraction tapInteraction:];
-[_UITextChoiceInteraction view];
-[_UITextChoiceInteraction setDelegate:];
-[_UITextChoiceInteraction gestureRecognizerShouldBegin:];
-[_UITextChoiceInteraction willMoveToView:];
-[_UITextChoiceInteraction createGestureRecognizer];
-[_UITextChoiceInteraction gestureRecognizer:shouldRecognizeSimultaneouslyWithGestureRecognizer:];
-[_UITextChoiceInteraction delegate];
-[_UITextChoiceInteraction setUnderlineTap:];
-[_UITextChoiceInteraction didMoveToView:];
```
