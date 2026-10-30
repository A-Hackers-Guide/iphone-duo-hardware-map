# `SBFMotionGestureController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 0 properties, 15 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _observersByPriority;
@"CMGestureManager" _motionGestureManager;
```

## Class methods

```
+[SBFMotionGestureController sharedInstance];
```

## Instance methods

```
-[SBFMotionGestureController init];
-[SBFMotionGestureController dealloc];
-[SBFMotionGestureController addGestureObserver:];
-[SBFMotionGestureController removeGestureObserver:];
-[SBFMotionGestureController _addGestureManager];
-[SBFMotionGestureController _addGestureObserver:withPriority:];
-[SBFMotionGestureController _enumerateObserversByPriority:];
-[SBFMotionGestureController _hasObservers];
-[SBFMotionGestureController _highestPriorityObservers];
-[SBFMotionGestureController _notifyObserversOfGesture:];
-[SBFMotionGestureController _observersForPriority:];
-[SBFMotionGestureController _removeGestureManager];
-[SBFMotionGestureController _removeGestureObserver:];
-[SBFMotionGestureController _updateGestureManager];
-[SBFMotionGestureController addGestureObserver:withPriority:];
```
