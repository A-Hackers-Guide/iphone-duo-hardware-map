# `CMVO2MaxRetrocomputeManager`

- Image: [`/System/Library/Frameworks/CoreMotion.framework/CoreMotion`](../userland/System__Library__Frameworks__CoreMotion.framework__CoreMotion.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 1 properties, 11 instance methods, 0 class methods

## Instance variables

```
^v fLocationdConnection;
@"NSObject<OS_dispatch_queue>" fInternalQueue;
B fStartedUpdates;
@"<CMVO2MaxRetrocomputeDelegate>" _delegate;
```

## Properties

```
@property (T@"<CMVO2MaxRetrocomputeDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[CMVO2MaxRetrocomputeManager connect];
-[CMVO2MaxRetrocomputeManager init];
-[CMVO2MaxRetrocomputeManager dealloc];
-[CMVO2MaxRetrocomputeManager disconnect];
-[CMVO2MaxRetrocomputeManager setDelegate:];
-[CMVO2MaxRetrocomputeManager delegate];
-[CMVO2MaxRetrocomputeManager triggerRetrocomputeWithHandler:];
-[CMVO2MaxRetrocomputeManager retrocomputeStateWithHandler:];
-[CMVO2MaxRetrocomputeManager retrocomputeStatusWithHandler:];
-[CMVO2MaxRetrocomputeManager startRetrocomputeStatusUpdates];
-[CMVO2MaxRetrocomputeManager stopRetrocomputeStatusUpdates];
```
