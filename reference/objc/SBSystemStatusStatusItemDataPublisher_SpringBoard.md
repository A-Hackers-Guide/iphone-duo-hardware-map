# `SBSystemStatusStatusItemDataPublisher`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSInvalidatable`
- 8 instance variables, 7 properties, 12 instance methods, 2 class methods

## Instance variables

```
@"STActivityAttribution" _attribution;
@"NSObject<OS_dispatch_queue>" _publishingQueue;
@"NSObject<OS_dispatch_queue>" _calloutQueue;
@"_SBSystemStatusStatusItemDataProviderOperation" _currentOperation;
@"NSMutableOrderedSet" _queuedOperations;
@"STStatusItemsStatusDomainStatusItemAttribution" _queue_attribution;
@"NSString" _statusItemIdentifier;
@"STUserInteractionHandlingStatusDomainPublisher" _statusItemsPublisher;
```

## Properties

```
@property (T@"STUserInteractionHandlingStatusDomainPublisher",R,N,V_statusItemsPublisher) statusItemsPublisher;
@property (T@"NSString",R,C,N,V_statusItemIdentifier) statusItemIdentifier;
@property (TB,R,N,GisStatusItemEnabled) statusItemEnabled;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSystemStatusStatusItemDataPublisher _sharedCalloutQueue];
+[SBSystemStatusStatusItemDataPublisher _sharedPublishingQueue];
```

## Instance methods

```
-[SBSystemStatusStatusItemDataPublisher invalidate];
-[SBSystemStatusStatusItemDataPublisher statusItemIdentifier];
-[SBSystemStatusStatusItemDataPublisher _queue_didCompleteOperation:];
-[SBSystemStatusStatusItemDataPublisher _queue_enqueueOperation:];
-[SBSystemStatusStatusItemDataPublisher _queue_isEnabled];
-[SBSystemStatusStatusItemDataPublisher _queue_startNextOperationIfPossible];
-[SBSystemStatusStatusItemDataPublisher _queue_startOperation:];
-[SBSystemStatusStatusItemDataPublisher initWithStatusItemIdentifier:];
-[SBSystemStatusStatusItemDataPublisher initWithStatusItemIdentifier:statusItemsPublisher:];
-[SBSystemStatusStatusItemDataPublisher isStatusItemEnabled];
-[SBSystemStatusStatusItemDataPublisher setStatusItemEnabled:withCompletion:];
-[SBSystemStatusStatusItemDataPublisher statusItemsPublisher];
```
