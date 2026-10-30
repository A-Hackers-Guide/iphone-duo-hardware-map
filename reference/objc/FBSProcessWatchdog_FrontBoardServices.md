# `FBSProcessWatchdog`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSProcessExecutionProvisionDelegate`, `BSDescriptionProviding`
- 6 instance variables, 8 properties, 19 instance methods, 0 class methods

## Instance variables

```
@"NSString" _name;
@"<FBSProcessInternal>" _process;
@"FBSProcessWatchdogPolicy" _policy;
B _active;
B _invalidated;
@? _completion;
```

## Properties

```
@property (T@"NSString",R,C,N,V_name) name;
@property (T@"<FBSProcess>",R,W,N,V_process) process;
@property (T@"FBSProcessWatchdogPolicy",R,C,N,V_policy) policy;
@property (T@?,C,N,V_completion) completion;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSProcessWatchdog setCompletion:];
-[FBSProcessWatchdog completion];
-[FBSProcessWatchdog deactivate];
-[FBSProcessWatchdog succinctDescriptionBuilder];
-[FBSProcessWatchdog process];
-[FBSProcessWatchdog dealloc];
-[FBSProcessWatchdog _beginMonitoringConstraints];
-[FBSProcessWatchdog _stopMonitoringConstraints];
-[FBSProcessWatchdog descriptionWithMultilinePrefix:];
-[FBSProcessWatchdog provision:wasViolatedWithError:];
-[FBSProcessWatchdog succinctDescription];
-[FBSProcessWatchdog invalidate];
-[FBSProcessWatchdog activate];
-[FBSProcessWatchdog description];
-[FBSProcessWatchdog isActive];
-[FBSProcessWatchdog initWithName:process:policy:];
-[FBSProcessWatchdog name];
-[FBSProcessWatchdog descriptionBuilderWithMultilinePrefix:];
-[FBSProcessWatchdog policy];
```
