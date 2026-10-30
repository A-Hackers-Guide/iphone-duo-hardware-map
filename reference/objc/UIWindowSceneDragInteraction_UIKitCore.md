# `UIWindowSceneDragInteraction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `UIInteraction`
- 2 instance variables, 7 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"UIView" _view;
@"<_UIWindowSceneDragInteractionImpl>" _impl;
```

## Properties

```
@property (T@"<_UIWindowSceneDragInteractionImpl>",&,N,V_impl) impl;
@property (T@"UIGestureRecognizer",R,N) gestureForFailureRelationships;
@property (T@"UIView",R,W,N,V_view) view;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[UIWindowSceneDragInteraction impl];
-[UIWindowSceneDragInteraction setImpl:];
-[UIWindowSceneDragInteraction init];
-[UIWindowSceneDragInteraction gestureForFailureRelationships];
-[UIWindowSceneDragInteraction view];
-[UIWindowSceneDragInteraction willMoveToView:];
-[UIWindowSceneDragInteraction didMoveToView:];
```
