# `AVRunLoopCondition`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSCondition`
- 1 instance variables, 0 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _runLoopStateList;
```

## Class methods

```
+[AVRunLoopCondition initialize];
```

## Instance methods

```
-[AVRunLoopCondition waitInMode:];
-[AVRunLoopCondition init];
-[AVRunLoopCondition dealloc];
-[AVRunLoopCondition wait];
-[AVRunLoopCondition waitUntilDate:];
-[AVRunLoopCondition signal];
-[AVRunLoopCondition _waitInMode:untilDate:];
-[AVRunLoopCondition broadcast];
-[AVRunLoopCondition _signalRunLoopWithState:];
-[AVRunLoopCondition waitUntilDate:inMode:];
```
