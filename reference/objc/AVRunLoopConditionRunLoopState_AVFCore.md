# `AVRunLoopConditionRunLoopState`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 7 instance methods, 1 class methods

## Instance variables

```
^{__CFRunLoop=} _runLoop;
^{__CFRunLoopSource=} _signalSource;
B _signaled;
```

## Properties

```
@property (T^{__CFRunLoop=},R,N,V_runLoop) runLoop;
@property (T^{__CFRunLoopSource=},N,V_signalSource) signalSource;
@property (TB,N,V_signaled) signaled;
```

## Class methods

```
+[AVRunLoopConditionRunLoopState runLoopStateWithRunLoop:];
```

## Instance methods

```
-[AVRunLoopConditionRunLoopState signaled];
-[AVRunLoopConditionRunLoopState dealloc];
-[AVRunLoopConditionRunLoopState setSignalSource:];
-[AVRunLoopConditionRunLoopState initWithRunLoop:];
-[AVRunLoopConditionRunLoopState runLoop];
-[AVRunLoopConditionRunLoopState signalSource];
-[AVRunLoopConditionRunLoopState setSignaled:];
```
