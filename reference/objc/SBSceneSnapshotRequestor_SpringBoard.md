# `SBSceneSnapshotRequestor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `BSInvalidatable`
- 3 instance variables, 5 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"NSMutableSet" _outgoingSnapshots;
@"NSMutableSet" _incomingSnapshots;
@"<SBSceneSnapshotRequestorDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBSceneSnapshotRequestorDelegate>",R,W,N,V_delegate) delegate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSceneSnapshotRequestor preventTakingSupplementalSnapshotsForBackgroundingScenesWithReason:];
```

## Instance methods

```
-[SBSceneSnapshotRequestor initWithDelegate:];
-[SBSceneSnapshotRequestor succinctDescriptionBuilder];
-[SBSceneSnapshotRequestor descriptionWithMultilinePrefix:];
-[SBSceneSnapshotRequestor succinctDescription];
-[SBSceneSnapshotRequestor invalidate];
-[SBSceneSnapshotRequestor delegate];
-[SBSceneSnapshotRequestor description];
-[SBSceneSnapshotRequestor descriptionBuilderWithMultilinePrefix:];
-[SBSceneSnapshotRequestor handleSnapshotRequestAction:forSceneHandle:groupID:application:];
-[SBSceneSnapshotRequestor _fbsSceneSnapshotRequestsFromSBSceneSnapshotRequests:forSceneHandle:settings:snapshotRequestContext:];
-[SBSceneSnapshotRequestor _sbSceneSnapshotRequestsForSceneHandle:settings:snapshotRequestContext:];
-[SBSceneSnapshotRequestor _sbSceneSnapshotRequestsForSceneHandle:settings:snapshotRequestContext:usingStrategy:];
-[SBSceneSnapshotRequestor _sceneSnapshotRequestContext];
-[SBSceneSnapshotRequestor _sceneSnapshotRequestStrategyForSceneHandle:snapshotRequestContext:];
-[SBSceneSnapshotRequestor invalidatePendingSnapshotsForSceneID:];
-[SBSceneSnapshotRequestor requestSnapshotsForSceneHandle:forUpdate:];
```
