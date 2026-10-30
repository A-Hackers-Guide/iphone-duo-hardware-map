# `IOSurfaceTransaction`

- Image: [`/System/Library/Frameworks/IOSurface.framework/IOSurface`](../userland/System__Library__Frameworks__IOSurface.framework__IOSurface.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"IOSurfaceSharedEvent" _event;
Q _waitValue;
B _isWrite;
```

## Properties

```
@property (T@"IOSurfaceSharedEvent",R,V_event) event;
@property (TQ,R,V_waitValue) waitValue;
@property (TB,R,V_isWrite) isWrite;
```

## Instance methods

```
-[IOSurfaceTransaction dealloc];
-[IOSurfaceTransaction event];
-[IOSurfaceTransaction isWrite];
-[IOSurfaceTransaction initWithSharedEvent:waitValue:isWrite:];
-[IOSurfaceTransaction waitValue];
-[IOSurfaceTransaction fromSerialized:];
```
