# `_UIGestureRecognizerCompositionDriver`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `_UIGestureRecognizerDriver`
- Protocols: `_UIGestureRecognizerDriverDelegate`
- 2 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSArray" _drivers;
^? _stateCombiner;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_UIGestureRecognizerCompositionDriver touchesEnded:withEvent:];
-[_UIGestureRecognizerCompositionDriver fail];
-[_UIGestureRecognizerCompositionDriver shouldReceiveEvent:];
-[_UIGestureRecognizerCompositionDriver touchesCancelled:withEvent:];
-[_UIGestureRecognizerCompositionDriver _gestureRecognizerDriver:didUpdateState:previousState:];
-[_UIGestureRecognizerCompositionDriver reset];
-[_UIGestureRecognizerCompositionDriver transformChangedWithEvent:];
-[_UIGestureRecognizerCompositionDriver touchesBegan:withEvent:];
-[_UIGestureRecognizerCompositionDriver touchesMoved:withEvent:];
-[_UIGestureRecognizerCompositionDriver setContext:];
-[_UIGestureRecognizerCompositionDriver description];
-[_UIGestureRecognizerCompositionDriver shouldReceiveComponent:withEvent:];
```
