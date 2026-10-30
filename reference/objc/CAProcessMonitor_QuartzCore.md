# `CAProcessMonitor`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 0 properties, 5 instance methods, 0 class methods

## Instance variables

```
@? _callback;
@"RBSProcessMonitor" _processMonitor;
@"NSMutableSet" _processIdentifiers;
@"NSObject<OS_dispatch_queue>" _queue;
```

## Instance methods

```
-[CAProcessMonitor updateConfiguration];
-[CAProcessMonitor dealloc];
-[CAProcessMonitor addMonitoringProcess:];
-[CAProcessMonitor initWithCallback:];
-[CAProcessMonitor removeMonitoringProcess:];
```
