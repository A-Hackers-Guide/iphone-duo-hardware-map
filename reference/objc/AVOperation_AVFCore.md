# `AVOperation`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSOperation`
- 3 instance variables, 2 properties, 13 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _ivarAccessQueue;
q _status;
@"NSError" _error;
```

## Properties

```
@property (Tq,R) status;
@property (T@"NSError",R) error;
```

## Class methods

```
+[AVOperation initialize];
+[AVOperation statusOfOperations:error:];
```

## Instance methods

```
-[AVOperation isFinished];
-[AVOperation isReady];
-[AVOperation init];
-[AVOperation dealloc];
-[AVOperation status];
-[AVOperation error];
-[AVOperation isExecuting];
-[AVOperation markAsCompleted];
-[AVOperation markAsCancelled];
-[AVOperation _setStatus:error:resultingStatus:failureReason:];
-[AVOperation didEnterTerminalState];
-[AVOperation evaluateDependenciesAndMarkAsExecuting];
-[AVOperation markAsFailedWithError:];
```
