# `_UIHIDTransformer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 2 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"_UIHIDContext" _hidContext;
@"NSMutableArray" _hidEvents;
@"NSMutableDictionary" _hidContextByContextId;
I _contextId;
^{__IOHIDEvent=} _hidEvent;
{CGSize="width"d"height"d} _canvasSize;
{CGAffineTransform="a"d"b"d"c"d"d"d"tx"d"ty"d} _eventTransform;
```

## Properties

```
@property (T{CGSize=dd},N,V_canvasSize) canvasSize;
@property (TI,N,V_contextId) contextId;
```

## Instance methods

```
-[_UIHIDTransformer canvasSize];
-[_UIHIDTransformer contextId];
-[_UIHIDTransformer addOutputHIDEvent:injected:];
-[_UIHIDTransformer initWithQueue:];
-[_UIHIDTransformer setContextId:];
-[_UIHIDTransformer drainOutputHIDEvents];
-[_UIHIDTransformer setCanvasSize:];
-[_UIHIDTransformer handleHIDEvent:];
-[_UIHIDTransformer _inputEventsForHIDEvent:contextId:];
```
