# `FBWorkspaceConnectionsStateStore`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 0 properties, 1 instance methods, 3 class methods

## Instance variables

```
@"NSString" _path1;
@"NSString" _path2;
@"NSObject<OS_dispatch_queue>" _queue;
@"FBWorkspaceConnectionsState" _queue_state;
q _queue_lastBuffer;
q _queue_nextWriteFailure;
B _queue_writeFailedOnce;
B _queue_invalidated;
```

## Class methods

```
+[FBWorkspaceConnectionsStateStore _loadStateFromPath:outGeneration:outExisted:];
+[FBWorkspaceConnectionsStateStore _storeState:toPath:withGeneration:injectedFailure:];
+[FBWorkspaceConnectionsStateStore _unlinkShmPath:graceful:];
```

## Instance methods

```
-[FBWorkspaceConnectionsStateStore init];
```
