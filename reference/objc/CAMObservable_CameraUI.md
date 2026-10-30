# `CAMObservable`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 0 properties, 15 instance methods, 0 class methods

## Instance variables

```
q _nestedChanges;
@"NSMutableArray" _pendingChangeBlocks;
q _numAppliedPendingChanges;
Q _currentChange;
B _isEnumeratingObservers;
@"NSObject<OS_dispatch_queue>" _observersQueue;
B _observersQueue_shouldCopyChangeObserversOnWrite;
@"NSMapTable" _observersQueue_changeObserversWithContexts;
```

## Instance methods

```
-[CAMObservable enumerateObserversUsingBlock:];
-[CAMObservable init];
-[CAMObservable performChanges:];
-[CAMObservable mutableChangeObject];
-[CAMObservable didPerformChanges];
-[CAMObservable _didChange];
-[CAMObservable _willChange];
-[CAMObservable registerChangeObserver:context:];
-[CAMObservable _observersQueue_copyChangeObserversForWriteIfNeeded];
-[CAMObservable unregisterChangeObserver:context:];
-[CAMObservable signalChange:];
-[CAMObservable _publishChanges];
-[CAMObservable _applyPendingChanges];
-[CAMObservable didPublishChanges];
-[CAMObservable willPerformChanges];
```
