# `UIDragGestureRecognizer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `UIGestureRecognizer`
- 1 instance variables, 4 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"UIDragEvent" _dragEvent;
```

## Properties

```
@property (T@"UIDragEvent",R,W,N,G_dragEvent,V_dragEvent) dragEvent;
@property (T@"<UIDragGestureRecognizerDelegate>",W,D,N) delegate;
@property (T@"_UIInternalDraggingSessionDestination",R,N) sessionDestination;
@property (T@"_UIDropSessionImpl",R,N) dropSession;
```

## Instance methods

```
-[UIDragGestureRecognizer dropSession];
-[UIDragGestureRecognizer canPreventGestureRecognizer:];
-[UIDragGestureRecognizer _shouldReceivePress:];
-[UIDragGestureRecognizer shouldReceiveEvent:];
-[UIDragGestureRecognizer canBePreventedByGestureRecognizer:];
-[UIDragGestureRecognizer initWithTarget:action:];
-[UIDragGestureRecognizer locationInView:];
-[UIDragGestureRecognizer sessionDestination];
-[UIDragGestureRecognizer _dragEvent];
-[UIDragGestureRecognizer _shouldReceiveTouch:forEvent:recognizerView:];
```
