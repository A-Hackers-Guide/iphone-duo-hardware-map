# `FBProcessWatchdog`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSProcessWatchdog`
- 5 instance variables, 3 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"RBSProcessHandle" _handle;
@"BSAtomicSignal" _unblockSignal;
q _event;
@"FBProcessWatchdogEventContext" _eventContext;
@"FBProcessCPUStatistics" _cpuStatistics;
```

## Properties

```
@property (Tq,R,N,V_event) event;
@property (T@"FBProcessWatchdogEventContext",R,&,N,V_eventContext) eventContext;
@property (T@"FBProcessCPUStatistics",R,&,N,V_cpuStatistics) cpuStatistics;
```

## Instance methods

```
-[FBProcessWatchdog deactivate];
-[FBProcessWatchdog initWithProcess:context:policy:];
-[FBProcessWatchdog eventContext];
-[FBProcessWatchdog _getPolicyWallTime:cpuTime:];
-[FBProcessWatchdog _policyDesc];
-[FBProcessWatchdog event];
-[FBProcessWatchdog cpuStatistics];
-[FBProcessWatchdog activate];
```
