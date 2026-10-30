# `SBBlockWorkspaceQueueTestRecipe`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBTestRecipe`
- 2 instance variables, 6 properties, 8 instance methods, 0 class methods

## Instance variables

```
@"NSTimer" _blockTimer;
@"FBWorkspaceEventQueueLock" _queueLock;
```

## Properties

```
@property (T@"NSTimer",&,N,V_blockTimer) blockTimer;
@property (T@"FBWorkspaceEventQueueLock",&,N,V_queueLock) queueLock;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBBlockWorkspaceQueueTestRecipe title];
-[SBBlockWorkspaceQueueTestRecipe queueLock];
-[SBBlockWorkspaceQueueTestRecipe setQueueLock:];
-[SBBlockWorkspaceQueueTestRecipe blockTimer];
-[SBBlockWorkspaceQueueTestRecipe blockTimerDidFire:];
-[SBBlockWorkspaceQueueTestRecipe handleVolumeDecrease];
-[SBBlockWorkspaceQueueTestRecipe handleVolumeIncrease];
-[SBBlockWorkspaceQueueTestRecipe setBlockTimer:];
```
