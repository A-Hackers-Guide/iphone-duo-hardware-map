# `_UITextChoiceAccelerationPassthroughView`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIView`
- Protocols: `_UIEditMenuDismissalGestureRecognizerDelegate`, `_UITouchFallbackViewDelegate`
- 4 instance variables, 7 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _didDismissFromGesture;
@"_UITouchFallbackView" _touchFallbackView;
@"<_UITextChoiceAccelerationPassthroughDelegate>" _delegate;
@"_UIEditMenuDismissalGestureRecognizer" _dismissalGestureRecognizer;
```

## Properties

```
@property (T@"_UIEditMenuDismissalGestureRecognizer",R,N,V_dismissalGestureRecognizer) dismissalGestureRecognizer;
@property (T@"_UITouchFallbackView",R,N,V_touchFallbackView) touchFallbackView;
@property (T@"<_UITextChoiceAccelerationPassthroughDelegate>",W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UITextChoiceAccelerationPassthroughView didRecognizeDismissalGestureRecognizer:];
-[_UITextChoiceAccelerationPassthroughView didMoveToWindow];
-[_UITextChoiceAccelerationPassthroughView setHidden:];
-[_UITextChoiceAccelerationPassthroughView hitTest:withEvent:];
-[_UITextChoiceAccelerationPassthroughView touchFallbackView];
-[_UITextChoiceAccelerationPassthroughView setBounds:];
-[_UITextChoiceAccelerationPassthroughView _installDismissalGesture];
-[_UITextChoiceAccelerationPassthroughView setDelegate:];
-[_UITextChoiceAccelerationPassthroughView willMoveToWindow:];
-[_UITextChoiceAccelerationPassthroughView delegate];
-[_UITextChoiceAccelerationPassthroughView dismissalGestureRecognizer];
-[_UITextChoiceAccelerationPassthroughView setFrame:];
-[_UITextChoiceAccelerationPassthroughView dismissalGestureRecognizer:shouldInteractAtLocation:withEvent:];
-[_UITextChoiceAccelerationPassthroughView touchFallbackView:shouldHitTestAtLocation:withEvent:];
-[_UITextChoiceAccelerationPassthroughView initWithFrame:delegate:];
-[_UITextChoiceAccelerationPassthroughView _hitTest:withEvent:withSourceView:];
-[_UITextChoiceAccelerationPassthroughView _passthroughViewDidChangeSize];
```
