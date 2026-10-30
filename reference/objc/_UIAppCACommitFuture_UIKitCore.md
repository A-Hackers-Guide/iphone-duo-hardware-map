# `_UIAppCACommitFuture`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 5 properties, 11 instance methods, 2 class methods

## Instance variables

```
B isFinished;
B isInvalidated;
? block;
```

## Properties

```
@property (TB,N,VisFinished) isFinished;
@property (TB,N,R) finished;
@property (TB,N,VisInvalidated) isInvalidated;
@property (TB,N,R) invalidated;
@property (T@?,N,C) block;
```

## Class methods

```
+[_UIAppCACommitFuture scheduledPostCommitFuture:enqueue:];
+[_UIAppCACommitFuture scheduledPreCommitFuture:];
```

## Instance methods

```
-[_UIAppCACommitFuture isFinished];
-[_UIAppCACommitFuture invoke];
-[_UIAppCACommitFuture block];
-[_UIAppCACommitFuture finished];
-[_UIAppCACommitFuture invalidated];
-[_UIAppCACommitFuture setBlock:];
-[_UIAppCACommitFuture init];
-[_UIAppCACommitFuture isInvalidated];
-[_UIAppCACommitFuture invalidate];
-[_UIAppCACommitFuture setIsInvalidated:];
-[_UIAppCACommitFuture setIsFinished:];
```
