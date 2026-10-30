# `FigCaptureWorkIntervalRegistry`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 4 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _workIntervalsByType;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _registryLock;
```

## Class methods

```
+[FigCaptureWorkIntervalRegistry sharedInstance];
```

## Instance methods

```
-[FigCaptureWorkIntervalRegistry init];
-[FigCaptureWorkIntervalRegistry dealloc];
-[FigCaptureWorkIntervalRegistry registerWorkInterval:forType:];
-[FigCaptureWorkIntervalRegistry workIntervalForType:];
```
