# `FigDelegateStorage`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _delegateQueue;
@ _delegate;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _lock;
```

## Properties

```
@property (T@,R) delegate;
@property (T@"NSObject<OS_dispatch_queue>",R) delegateQueue;
```

## Class methods

```
+[FigDelegateStorage initialize];
```

## Instance methods

```
-[FigDelegateStorage setDelegate:queue:];
-[FigDelegateStorage init];
-[FigDelegateStorage dealloc];
-[FigDelegateStorage delegate];
-[FigDelegateStorage invokeDelegateCallbackWithBlock:];
-[FigDelegateStorage delegateQueue];
```
