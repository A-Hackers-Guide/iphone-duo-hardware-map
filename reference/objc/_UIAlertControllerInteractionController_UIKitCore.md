# `_UIAlertControllerInteractionController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIPercentDrivenInteractiveTransition`
- Protocols: `UIForceInteractionController`, `UIInteractionProgressObserver`
- 2 instance variables, 9 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"UIAlertController" _alertController;
@"<UIViewControllerContextTransitioning>" _context;
```

## Properties

```
@property (T@"UIAlertController",&,N,V_alertController) alertController;
@property (T@"<UIViewControllerContextTransitioning>",&,N,V_context) context;
@property (Td,?,R,N) completionSpeed;
@property (Tq,?,R,N) completionCurve;
@property (TB,?,R,N) wantsInteractiveStart;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIAlertControllerInteractionController interactionProgressDidUpdate:];
-[_UIAlertControllerInteractionController interactionProgress:didEnd:];
-[_UIAlertControllerInteractionController alertController];
-[_UIAlertControllerInteractionController startInteractiveTransition:];
-[_UIAlertControllerInteractionController setContext:];
-[_UIAlertControllerInteractionController setAlertController:];
-[_UIAlertControllerInteractionController context];
```
