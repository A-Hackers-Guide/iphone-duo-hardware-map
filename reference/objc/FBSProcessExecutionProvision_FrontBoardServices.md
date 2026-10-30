# `FBSProcessExecutionProvision`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `NSCopying`
- 7 instance variables, 9 properties, 24 instance methods, 0 class methods

## Instance variables

```
@"<FBSProcessInternal>" _process;
B _activated;
@"NSObject<OS_dispatch_queue>" _delegateCalloutQueue;
B _monitoring;
B _violated;
@"NSError" _error;
@"<FBSProcessExecutionProvisionDelegate>" _delegate;
```

## Properties

```
@property (T@"<FBSProcessExecutionProvisionDelegate>",W,N,V_delegate) delegate;
@property (T@"<FBSProcessInternal>",R,W,N,V_process) process;
@property (TB,R,N,GisMonitoring,V_monitoring) monitoring;
@property (TB,R,N,GisViolated,V_violated) violated;
@property (T@"NSError",R,N,V_error) error;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSProcessExecutionProvision monitorProcess:];
-[FBSProcessExecutionProvision _beginMonitoring];
-[FBSProcessExecutionProvision _prepareForReuse];
-[FBSProcessExecutionProvision isMonitoring];
-[FBSProcessExecutionProvision updateProgress];
-[FBSProcessExecutionProvision succinctDescriptionBuilder];
-[FBSProcessExecutionProvision init];
-[FBSProcessExecutionProvision process];
-[FBSProcessExecutionProvision _stopMonitoring];
-[FBSProcessExecutionProvision _updateProgress];
-[FBSProcessExecutionProvision isViolated];
-[FBSProcessExecutionProvision descriptionWithMultilinePrefix:];
-[FBSProcessExecutionProvision stopMonitoring];
-[FBSProcessExecutionProvision error];
-[FBSProcessExecutionProvision _noteViolatedWithError:];
-[FBSProcessExecutionProvision succinctDescription];
-[FBSProcessExecutionProvision _performDelegateCallout:];
-[FBSProcessExecutionProvision setDelegate:];
-[FBSProcessExecutionProvision isResourceProvision];
-[FBSProcessExecutionProvision prepareForReuse];
-[FBSProcessExecutionProvision delegate];
-[FBSProcessExecutionProvision description];
-[FBSProcessExecutionProvision copyWithZone:];
-[FBSProcessExecutionProvision descriptionBuilderWithMultilinePrefix:];
```
