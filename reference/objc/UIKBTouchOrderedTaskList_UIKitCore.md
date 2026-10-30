# `UIKBTouchOrderedTaskList`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 6 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSUUID" _touchUUID;
@"NSObject<OS_dispatch_queue>" _touchStateTasksQueue;
@"NSMutableArray" _touchStateTasks;
@"NSValue" _currentTouchPoint;
B _ignoredOnBegin;
Q _pathIndex;
d _originalStartTime;
```

## Properties

```
@property (T@"NSUUID",R,N,V_touchUUID) touchUUID;
@property (TQ,R,N,V_pathIndex) pathIndex;
@property (Td,R,N,V_originalStartTime) originalStartTime;
@property (T@"NSValue",R,N,V_currentTouchPoint) currentTouchPoint;
@property (TB,N,V_ignoredOnBegin) ignoredOnBegin;
@property (TB,R,N) hasTasks;
```

## Class methods

```
+[UIKBTouchOrderedTaskList taskListForTouchUUID:withPathIndex:];
```

## Instance methods

```
-[UIKBTouchOrderedTaskList addTask:];
-[UIKBTouchOrderedTaskList dealloc];
-[UIKBTouchOrderedTaskList pathIndex];
-[UIKBTouchOrderedTaskList touchUUID];
-[UIKBTouchOrderedTaskList firstTouchStateForUITouchPhase:];
-[UIKBTouchOrderedTaskList currentTouchPoint];
-[UIKBTouchOrderedTaskList executeTasksInView:withBlock:];
-[UIKBTouchOrderedTaskList hasTasks];
-[UIKBTouchOrderedTaskList ignoredOnBegin];
-[UIKBTouchOrderedTaskList initWithTouchUUID:withPathIndex:];
-[UIKBTouchOrderedTaskList isExecutingFirstTask];
-[UIKBTouchOrderedTaskList originalStartTime];
-[UIKBTouchOrderedTaskList removeTasksMatchingFilter:];
-[UIKBTouchOrderedTaskList setIgnoredOnBegin:];
```
