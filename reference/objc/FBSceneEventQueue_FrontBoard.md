# `FBSceneEventQueue`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BSEventQueue`
- 1 instance variables, 0 properties, 5 instance methods, 3 class methods

## Instance variables

```
@"BSEventQueueLock" _idleEventLock;
```

## Class methods

```
+[FBSceneEventQueue executeWhenIdle:];
+[FBSceneEventQueue isIdleWorkSuspended];
+[FBSceneEventQueue suspendIdleWorkForReason:];
```

## Instance methods

```
-[FBSceneEventQueue _noteQueueDidDrain];
-[FBSceneEventQueue _noteQueueDidUnlock];
-[FBSceneEventQueue _noteWillPendEvents:atPosition:];
-[FBSceneEventQueue executeOrAppend:];
-[FBSceneEventQueue _noteQueueDidLock];
```
