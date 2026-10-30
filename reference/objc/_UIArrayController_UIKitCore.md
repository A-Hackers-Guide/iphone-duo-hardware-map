# `_UIArrayController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 5 properties, 17 instance methods, 0 class methods

## Instance variables

```
B _firstUpdateSent;
B _invalidated;
@"NSArray" _sortDescriptors;
@"NSPredicate" _predicate;
@"<_UIArrayControllerDelegate>" _delegate;
@"NSOperationQueue" _operationQueue;
@"NSOrderedSet" _lastSnapshot;
```

## Properties

```
@property (T@"<_UIArrayControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"NSOrderedSet",C,N,V_lastSnapshot) lastSnapshot;
@property (T@"NSArray",&,N,V_sortDescriptors) sortDescriptors;
@property (T@"NSPredicate",&,N,V_predicate) predicate;
@property (T@"NSOperationQueue",&,N,V_operationQueue) operationQueue;
```

## Instance methods

```
-[_UIArrayController initWithDelegate:];
-[_UIArrayController setSortDescriptors:];
-[_UIArrayController dealloc];
-[_UIArrayController lastSnapshot];
-[_UIArrayController invalidate];
-[_UIArrayController setPredicate:];
-[_UIArrayController setDelegate:];
-[_UIArrayController delegate];
-[_UIArrayController predicate];
-[_UIArrayController operationQueue];
-[_UIArrayController setOperationQueue:];
-[_UIArrayController sortDescriptors];
-[_UIArrayController setLastSnapshot:];
-[_UIArrayController _computeUpdatesFromOld:toNew:changedItems:];
-[_UIArrayController callUpdateHandler:changeDictionary:];
-[_UIArrayController objectAttributeModified:newObject:];
-[_UIArrayController processUpdate:changedObjects:];
```
