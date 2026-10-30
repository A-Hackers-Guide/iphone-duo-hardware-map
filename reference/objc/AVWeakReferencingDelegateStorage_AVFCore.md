# `AVWeakReferencingDelegateStorage`

- Image: [`/System/Library/PrivateFrameworks/AVFCore.framework/AVFCore`](../userland/System__Library__PrivateFrameworks__AVFCore.framework__AVFCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _ivarAccessQueue;
@ _weakDelegate;
@"NSObject<OS_dispatch_queue>" _delegateQueue;
```

## Properties

```
@property (T@,R,N) delegate;
@property (T@"NSObject<OS_dispatch_queue>",R,N) delegateQueue;
```

## Class methods

```
+[AVWeakReferencingDelegateStorage initialize];
```

## Instance methods

```
-[AVWeakReferencingDelegateStorage setDelegate:queue:];
-[AVWeakReferencingDelegateStorage init];
-[AVWeakReferencingDelegateStorage dealloc];
-[AVWeakReferencingDelegateStorage delegate];
-[AVWeakReferencingDelegateStorage invokeDelegateCallbackWithBlock:synchronouslyIfDelegateQueueIsQueue:];
-[AVWeakReferencingDelegateStorage invokeDelegateCallbackWithBlock:];
-[AVWeakReferencingDelegateStorage delegateQueue];
-[AVWeakReferencingDelegateStorage getRetainedDelegate:retainedDelegateQueue:];
```
