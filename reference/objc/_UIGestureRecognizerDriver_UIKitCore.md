# `_UIGestureRecognizerDriver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 17 instance methods, 0 class methods

## Instance variables

```
q _state;
{?="needsTouches"b1"needsTransform"b1} _flags;
@"<_UIGestureRecognizerDriverContext>" _context;
@"<_UIGestureRecognizerDriverDelegate>" _delegate;
```

## Properties

```
@property (Tq,R,N) state;
@property (T@"<_UIGestureRecognizerDriverContext>",&,N,V_context) context;
@property (T@"<_UIGestureRecognizerDriverDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[_UIGestureRecognizerDriver touchesEnded:withEvent:];
-[_UIGestureRecognizerDriver fail];
-[_UIGestureRecognizerDriver shouldReceiveEvent:];
-[_UIGestureRecognizerDriver touchesCancelled:withEvent:];
-[_UIGestureRecognizerDriver init];
-[_UIGestureRecognizerDriver didUpdateState:previousState:];
-[_UIGestureRecognizerDriver reset];
-[_UIGestureRecognizerDriver transformChangedWithEvent:];
-[_UIGestureRecognizerDriver touchesBegan:withEvent:];
-[_UIGestureRecognizerDriver touchesMoved:withEvent:];
-[_UIGestureRecognizerDriver setDelegate:];
-[_UIGestureRecognizerDriver setContext:];
-[_UIGestureRecognizerDriver delegate];
-[_UIGestureRecognizerDriver description];
-[_UIGestureRecognizerDriver context];
-[_UIGestureRecognizerDriver state];
-[_UIGestureRecognizerDriver shouldReceiveComponent:withEvent:];
```
