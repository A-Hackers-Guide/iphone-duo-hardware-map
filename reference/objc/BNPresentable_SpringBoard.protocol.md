# `BNPresentable` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `BNPresentableIdentifying`, `BNPresentableObserving`
- 0 instance variables, 8 properties, 11 instance methods, 0 class methods

## Properties

```
@property (Tq,?,R,N) presentableBehavior;
@property (T@"<BNPresentableContext>",?,W,N) presentableContext;
@property (T@"NSSet",?,R,C,N) preferredBackgroundActivitiesToSuppress;
@property (TB,?,R,N,GisDraggingDismissalEnabled) draggingDismissalEnabled;
@property (TB,?,R,N,GisDraggingInteractionEnabled) draggingInteractionEnabled;
@property (TB,?,R,N,GisTouchOutsideDismissalEnabled) touchOutsideDismissalEnabled;
@property (T@"UIViewController",?,R,N) viewController;
@property (Tq,?,R,N) presentableType;
```

## Instance methods

```
-[BNPresentable isTouchOutsideDismissalEnabled];
-[BNPresentable isDraggingInteractionEnabled];
-[BNPresentable presentableBehavior];
-[BNPresentable isDraggingDismissalEnabled];
-[BNPresentable viewController];
-[BNPresentable preferredBackgroundActivitiesToSuppress];
-[BNPresentable setPresentableContext:];
-[BNPresentable presentableContext];
-[BNPresentable presentableType];
-[BNPresentable draggingDidBeginWithGestureProxy:];
-[BNPresentable presentableDescription];
```
