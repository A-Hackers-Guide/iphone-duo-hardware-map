# `SBDaemonContext`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 0 properties, 7 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_source>" _dispatchSource;
@"NSMutableDictionary" _daemonRequests;
i _pid;
```

## Instance methods

```
-[SBDaemonContext pid];
-[SBDaemonContext description];
-[SBDaemonContext _newDispatchSourceForPid:queue:];
-[SBDaemonContext _handleCancelation];
-[SBDaemonContext addRequest:forKey:];
-[SBDaemonContext initWithPid:queue:];
-[SBDaemonContext removeRequestForKey:];
```
