# `FBSProcessResourceProvision`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSProcessExecutionProvision`
- 8 instance variables, 2 properties, 18 instance methods, 2 class methods

## Instance variables

```
{?="type"q"value"Q"reserved"Q} _allowance;
Q _baselineValue;
Q _consumedValue;
@"NSObject<OS_dispatch_queue>" _queue;
@"BSAbsoluteMachTimer" _timer;
@"RBSProcessHandle" _processHandle;
d _timerFireInterval;
Q _timerFireCount;
```

## Properties

```
@property (Tq,D,N) type;
@property (T{?=qQQ},N,V_allowance) allowance;
```

## Class methods

```
+[FBSProcessResourceProvision provisionWithAllowance:];
+[FBSProcessResourceProvision provisionWithResourceType:timeInterval:];
```

## Instance methods

```
-[FBSProcessResourceProvision _beginMonitoring];
-[FBSProcessResourceProvision _prepareForReuse];
-[FBSProcessResourceProvision succinctDescriptionBuilder];
-[FBSProcessResourceProvision _stopMonitoring];
-[FBSProcessResourceProvision dealloc];
-[FBSProcessResourceProvision setAllowance:];
-[FBSProcessResourceProvision _updateProgress];
-[FBSProcessResourceProvision _queue_noteAllowanceExhausted];
-[FBSProcessResourceProvision isResourceProvision];
-[FBSProcessResourceProvision type];
-[FBSProcessResourceProvision _queue_updateConsumption];
-[FBSProcessResourceProvision _queue_evaluateConsumptionFromTimer:];
-[FBSProcessResourceProvision initWithAllowance:];
-[FBSProcessResourceProvision copyWithZone:];
-[FBSProcessResourceProvision _queue_calculateValueConsumed:];
-[FBSProcessResourceProvision allowanceRemaining:];
-[FBSProcessResourceProvision allowance];
-[FBSProcessResourceProvision _queue_stopMonitoring];
```
