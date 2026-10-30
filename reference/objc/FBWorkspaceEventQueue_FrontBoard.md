# `FBWorkspaceEventQueue`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BSEventQueue`
- 0 instance variables, 0 properties, 9 instance methods, 1 class methods

## Class methods

```
+[FBWorkspaceEventQueue sharedInstance];
```

## Instance methods

```
-[FBWorkspaceEventQueue _noteWillExecuteEvent:];
-[FBWorkspaceEventQueue executeOrPrependEvent:];
-[FBWorkspaceEventQueue _noteQueueDidUnlock];
-[FBWorkspaceEventQueue _noteWillCancelEventsWithName:count:];
-[FBWorkspaceEventQueue executeOrAppendEvent:];
-[FBWorkspaceEventQueue _noteWillPendEvents:atPosition:];
-[FBWorkspaceEventQueue _shouldProcessEvent:enqueuedDuringExecutionOfEvent:];
-[FBWorkspaceEventQueue executeOrPrependEvents:];
-[FBWorkspaceEventQueue _noteQueueDidLock];
```
