# `_UIFallbackPresentationViewController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIApplicationRotationFollowingController`
- 5 instance variables, 4 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"_UIFallbackPresentationWindow" _presentationWindow;
B _hasPreservedKeyboardInputViews;
B _hasDismissCompletionHandler;
@"UIWindow" _rotationDecider;
@? _presentationPreparationBlock;
```

## Properties

```
@property (TB,N,V_hasPreservedKeyboardInputViews) hasPreservedKeyboardInputViews;
@property (TB,N,V_hasDismissCompletionHandler) hasDismissCompletionHandler;
@property (T@"UIWindow",&,N,V_rotationDecider) rotationDecider;
@property (T@?,C,N,V_presentationPreparationBlock) presentationPreparationBlock;
```

## Instance methods

```
-[_UIFallbackPresentationViewController _preparePresentationControllerForPresenting:];
-[_UIFallbackPresentationViewController viewDidLoad];
-[_UIFallbackPresentationViewController _canShowWhileLocked];
-[_UIFallbackPresentationViewController rotationDecider];
-[_UIFallbackPresentationViewController setHasDismissCompletionHandler:];
-[_UIFallbackPresentationViewController _dismissViewControllerWithTransition:from:completion:];
-[_UIFallbackPresentationViewController _presentViewController:sendingView:animated:];
-[_UIFallbackPresentationViewController _preserveInputViewsAnimated:];
-[_UIFallbackPresentationViewController _restoreInputViewsAnimated:];
-[_UIFallbackPresentationViewController hasDismissCompletionHandler];
-[_UIFallbackPresentationViewController hasPreservedKeyboardInputViews];
-[_UIFallbackPresentationViewController presentationPreparationBlock];
-[_UIFallbackPresentationViewController setHasPreservedKeyboardInputViews:];
-[_UIFallbackPresentationViewController setPresentationPreparationBlock:];
-[_UIFallbackPresentationViewController setRotationDecider:];
```
