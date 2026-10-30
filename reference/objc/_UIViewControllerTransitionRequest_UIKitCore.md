# `_UIViewControllerTransitionRequest`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 9 instance variables, 9 properties, 10 instance methods, 0 class methods

## Instance variables

```
B _keyboardShouldAnimateAlongsideForInteractiveTransitions;
@"_UIViewControllerOneToOneTransitionContext" _transitionContext;
@"<UIViewControllerAnimatedTransitioning>" _animator;
@"<UIViewControllerInteractiveTransitioning>" _interactor;
@? _interactiveUpdateHandler;
@"_UIViewControllerKeyboardAnimationStyle" _keyboardAnimationStyle;
@"UIResponder" _pinningInputViewsResponder;
@? _extraPinningInputViewsBlock;
@"_UIViewControllerAnimatedTransitionHandoffData" _handoffData;
```

## Properties

```
@property (T@"_UIViewControllerOneToOneTransitionContext",R,N,V_transitionContext) transitionContext;
@property (T@"<UIViewControllerAnimatedTransitioning>",R,N,V_animator) animator;
@property (T@"<UIViewControllerInteractiveTransitioning>",R,N,V_interactor) interactor;
@property (T@?,R,C,N,V_interactiveUpdateHandler) interactiveUpdateHandler;
@property (TB,R,N,V_keyboardShouldAnimateAlongsideForInteractiveTransitions) keyboardShouldAnimateAlongsideForInteractiveTransitions;
@property (T@"_UIViewControllerKeyboardAnimationStyle",R,N,V_keyboardAnimationStyle) keyboardAnimationStyle;
@property (T@"UIResponder",R,N,V_pinningInputViewsResponder) pinningInputViewsResponder;
@property (T@?,R,C,N,V_extraPinningInputViewsBlock) extraPinningInputViewsBlock;
@property (T@"_UIViewControllerAnimatedTransitionHandoffData",R,N,V_handoffData) handoffData;
```

## Instance methods

```
-[_UIViewControllerTransitionRequest keyboardAnimationStyle];
-[_UIViewControllerTransitionRequest interactor];
-[_UIViewControllerTransitionRequest transitionContext];
-[_UIViewControllerTransitionRequest pinningInputViewsResponder];
-[_UIViewControllerTransitionRequest keyboardShouldAnimateAlongsideForInteractiveTransitions];
-[_UIViewControllerTransitionRequest interactiveUpdateHandler];
-[_UIViewControllerTransitionRequest handoffData];
-[_UIViewControllerTransitionRequest animator];
-[_UIViewControllerTransitionRequest initWithTransitionContext:animator:interactor:interactiveUpdateHandler:keyboardShouldAnimateAlongsideForInteractiveTransitions:keyboardAnimationStyle:pinningInputViewsResponder:extraPinningInputViewsBlock:handoffData:];
-[_UIViewControllerTransitionRequest extraPinningInputViewsBlock];
```
