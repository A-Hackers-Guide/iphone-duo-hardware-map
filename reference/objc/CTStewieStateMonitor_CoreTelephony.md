# `CTStewieStateMonitor`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 0 properties, 6 instance methods, 0 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} fLock;
@"CTStewieState" fState;
@"<CTStewieStateMonitorDelegate>" fDelegate;
@"NSObject<OS_dispatch_queue>" fDelegateQueue;
@"NSObject<OS_nw_path_evaluator>" fPathEvaluator;
B fStarted;
```

## Instance methods

```
-[CTStewieStateMonitor initWithDelegate:queue:];
-[CTStewieStateMonitor dealloc];
-[CTStewieStateMonitor start];
-[CTStewieStateMonitor stateFromPath:];
-[CTStewieStateMonitor startWithEndpoint:parameters:];
-[CTStewieStateMonitor getState];
```
