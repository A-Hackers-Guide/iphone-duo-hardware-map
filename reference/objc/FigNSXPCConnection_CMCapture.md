# `FigNSXPCConnection`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSXPCConnection`
- 2 instance variables, 1 properties, 6 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_group>" _connectionRunningGroup;
B _explicitlyInvalidated;
```

## Properties

```
@property (TB,R,N,V_explicitlyInvalidated) explicitlyInvalidated;
```

## Instance methods

```
-[FigNSXPCConnection blockUntilInvalidateHandlerHasBeenCalled];
-[FigNSXPCConnection setInvalidationHandler:];
-[FigNSXPCConnection dealloc];
-[FigNSXPCConnection explicitlyInvalidated];
-[FigNSXPCConnection invalidate];
-[FigNSXPCConnection resume];
```
