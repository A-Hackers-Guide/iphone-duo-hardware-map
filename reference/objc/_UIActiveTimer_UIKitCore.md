# `_UIActiveTimer`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 1 properties, 4 instance methods, 0 class methods

## Instance variables

```
@"CADisplayLink" _displayLink;
@? _updateHandler;
```

## Properties

```
@property (TB,R,N,GisComplete) complete;
```

## Instance methods

```
-[_UIActiveTimer isComplete];
-[_UIActiveTimer invalidate];
-[_UIActiveTimer _tick:];
-[_UIActiveTimer initWithDuration:updateHandler:];
```
