# `FBProcessState`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `NSCopying`
- 6 instance variables, 10 properties, 19 instance methods, 0 class methods

## Instance variables

```
B _running;
B _foreground;
B _debugging;
i _pid;
q _taskState;
q _visibility;
```

## Properties

```
@property (Ti,N,V_pid) pid;
@property (Tq,N,V_taskState) taskState;
@property (Tq,N,V_visibility) visibility;
@property (TB,N,GisDebugging,V_debugging) debugging;
@property (TB,R,N,GisRunning,V_running) running;
@property (TB,R,N,GisForeground,V_foreground) foreground;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBProcessState isRunning];
-[FBProcessState setTaskState:];
-[FBProcessState setPid:];
-[FBProcessState isDebugging];
-[FBProcessState setVisibility:];
-[FBProcessState taskState];
-[FBProcessState succinctDescriptionBuilder];
-[FBProcessState init];
-[FBProcessState visibility];
-[FBProcessState setDebugging:];
-[FBProcessState descriptionWithMultilinePrefix:];
-[FBProcessState isForeground];
-[FBProcessState succinctDescription];
-[FBProcessState pid];
-[FBProcessState description];
-[FBProcessState copyWithZone:];
-[FBProcessState isEqual:];
-[FBProcessState initWithPid:];
-[FBProcessState descriptionBuilderWithMultilinePrefix:];
```
