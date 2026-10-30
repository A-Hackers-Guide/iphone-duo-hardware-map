# `IOSurfaceSharedEvent`

- Image: [`/System/Library/Frameworks/IOSurface.framework/IOSurface`](../userland/System__Library__Frameworks__IOSurface.framework__IOSurface.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
I _eventPort;
r^Q _signaledValue;
Q _globalTraceObjectID;
Q _eventOptions;
```

## Properties

```
@property (TQ) signaledValue;
@property (TI,R,V_eventPort) eventPort;
@property (TQ,R,V_globalTraceObjectID) globalTraceObjectID;
@property (TB,R) supportsRollback;
```

## Class methods

```
+[IOSurfaceSharedEvent supportsSecureCoding];
```

## Instance methods

```
-[IOSurfaceSharedEvent init];
-[IOSurfaceSharedEvent globalTraceObjectID];
-[IOSurfaceSharedEvent dealloc];
-[IOSurfaceSharedEvent initWithOptions:];
-[IOSurfaceSharedEvent encodeWithCoder:];
-[IOSurfaceSharedEvent initWithCoder:];
-[IOSurfaceSharedEvent initWithMachPort:];
-[IOSurfaceSharedEvent eventPort];
-[IOSurfaceSharedEvent notifyListener:atValue:block:];
-[IOSurfaceSharedEvent setSignaledValue:];
-[IOSurfaceSharedEvent signaledValue];
-[IOSurfaceSharedEvent waitUntilSignaledValue:timeoutMS:];
-[IOSurfaceSharedEvent supportsRollback];
```
