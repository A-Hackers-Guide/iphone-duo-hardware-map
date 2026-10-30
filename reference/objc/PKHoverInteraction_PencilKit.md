# `PKHoverInteraction`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PKHoverControllerDelegate`, `UIInteraction`
- 3 instance variables, 7 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"<PKHoverInteractionDelegate>" _delegate;
@"UIView" _view;
@"PKHoverController" _hoverController;
```

## Properties

```
@property (T@"UIView",W,N,V_view) view;
@property (T@"PKHoverController",&,N,V_hoverController) hoverController;
@property (T@"<PKHoverInteractionDelegate>",R,W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[PKHoverInteraction initWithDelegate:];
-[PKHoverInteraction setView:];
-[PKHoverInteraction view];
-[PKHoverInteraction willMoveToView:];
-[PKHoverInteraction delegate];
-[PKHoverInteraction didMoveToView:];
-[PKHoverInteraction hoverController];
-[PKHoverInteraction hoverController:holdGestureMeanInputPoint:latestInputPoint:];
-[PKHoverInteraction hoverControllerHoldGestureEnded:];
-[PKHoverInteraction setHoverController:];
```
