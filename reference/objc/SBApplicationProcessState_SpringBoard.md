# `SBApplicationProcessState`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`
- 3 instance variables, 10 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"FBApplicationProcess" _process;
@"FBProcessState" _processState;
B _isBeingDebugged;
```

## Properties

```
@property (Ti,R,N) pid;
@property (TB,R,N,GisRunning) running;
@property (TB,R,N,GisForeground) foreground;
@property (Tq,R,N) taskState;
@property (Tq,R,N) visibility;
@property (TB,R,N) isBeingDebugged;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBApplicationProcessState isRunning];
-[SBApplicationProcessState isBeingDebugged];
-[SBApplicationProcessState taskState];
-[SBApplicationProcessState succinctDescriptionBuilder];
-[SBApplicationProcessState visibility];
-[SBApplicationProcessState descriptionWithMultilinePrefix:];
-[SBApplicationProcessState isForeground];
-[SBApplicationProcessState succinctDescription];
-[SBApplicationProcessState pid];
-[SBApplicationProcessState _initWithProcess:stateSnapshot:];
-[SBApplicationProcessState hash];
-[SBApplicationProcessState description];
-[SBApplicationProcessState isEqual:];
-[SBApplicationProcessState descriptionBuilderWithMultilinePrefix:];
```
