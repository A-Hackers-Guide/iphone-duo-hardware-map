# `_UINavigationControllerVisualStyle`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 4 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"UINavigationController" _navigationController;
```

## Properties

```
@property (T@"UINavigationController",N,V_navigationController) navigationController;
@property (T@"<UIViewControllerAnimatedTransitioning>",R,N) transitionController;
@property (T@"<UIViewControllerInteractiveTransitioning>",R,N) interactionController;
@property (TB,R,N) isUsingParallaxTransition;
```

## Instance methods

```
-[_UINavigationControllerVisualStyle initWithNavigationController:];
-[_UINavigationControllerVisualStyle updateTransitionControllerWithOperation:];
-[_UINavigationControllerVisualStyle layoutContainerViewSemanticContentAttributeChanged:];
-[_UINavigationControllerVisualStyle interactionController];
-[_UINavigationControllerVisualStyle transitionController];
-[_UINavigationControllerVisualStyle isUsingParallaxTransition];
-[_UINavigationControllerVisualStyle setNavigationController:];
-[_UINavigationControllerVisualStyle navigationController];
-[_UINavigationControllerVisualStyle containerViewWillLayoutSubviews:];
-[_UINavigationControllerVisualStyle navigationBarFrameChanged];
-[_UINavigationControllerVisualStyle navigationBarVisibilityChanged];
-[_UINavigationControllerVisualStyle shouldUseInteractionControllerForInteractiveTransition];
-[_UINavigationControllerVisualStyle toolbarFrameChanged];
-[_UINavigationControllerVisualStyle toolbarVisibilityChanged];
```
