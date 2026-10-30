# `FBSProcess`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSProcessInternal`, `BSDescriptionProviding`
- 3 instance variables, 10 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"BSProcessHandle" _handle;
@"RBSProcessIdentity" _identity;
@"BSMachPortTaskNameRight" _taskNameRight;
```

## Properties

```
@property (TB,R,N,GisRunning) running;
@property (T@"BSProcessHandle",R,&,N) handle;
@property (T@"RBSProcessIdentity",R,&,N) identity;
@property (T@"BSMachPortTaskNameRight",R,&,N,V_taskNameRight) taskNameRight;
@property (Ti,R,N) pid;
@property (Tq,R,N) versionedPID;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSProcess currentProcess];
```

## Instance methods

```
-[FBSProcess isRunning];
-[FBSProcess succinctDescriptionBuilder];
-[FBSProcess init];
-[FBSProcess dealloc];
-[FBSProcess versionedPID];
-[FBSProcess descriptionWithMultilinePrefix:];
-[FBSProcess succinctDescription];
-[FBSProcess pid];
-[FBSProcess handle];
-[FBSProcess identity];
-[FBSProcess description];
-[FBSProcess descriptionBuilderWithMultilinePrefix:];
-[FBSProcess taskNameRight];
-[FBSProcess _initForCurrentProcess];
-[FBSProcess _terminateWithRequest:forWatchdog:];
-[FBSProcess _watchdog:shouldTerminateWithDeclineReason:];
-[FBSProcess _watchdog:terminationRequestForError:];
```
