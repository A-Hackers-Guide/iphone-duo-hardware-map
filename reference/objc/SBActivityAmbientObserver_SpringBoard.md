# `SBActivityAmbientObserver`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBActivityObserver`
- 3 instance variables, 9 properties, 22 instance methods, 0 class methods

## Instance variables

```
@"<SBActivityAmbientObserverDelegate>" _delegate;
@"NSMutableOrderedSet" _activeActivityItems;
@"NSMutableOrderedSet" _pendingItems;
```

## Properties

```
@property (T@"NSMutableOrderedSet",&,N,V_activeActivityItems) activeActivityItems;
@property (T@"NSMutableOrderedSet",&,N,V_pendingItems) pendingItems;
@property (T@"<SBActivityAmbientObserverDelegate>",W,N,V_delegate) delegate;
@property (TB,R,N) hasPendingItem;
@property (T@"SBActivityItem",R,N) nextPendingItem;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBActivityAmbientObserver activityDidEnd:];
-[SBActivityAmbientObserver init];
-[SBActivityAmbientObserver dealloc];
-[SBActivityAmbientObserver activityDidDismiss:];
-[SBActivityAmbientObserver presentAlert:];
-[SBActivityAmbientObserver activityDidStart:];
-[SBActivityAmbientObserver setDelegate:];
-[SBActivityAmbientObserver dismissAlert:];
-[SBActivityAmbientObserver delegate];
-[SBActivityAmbientObserver shouldHandleActivityItem:];
-[SBActivityAmbientObserver activityProminenceChanged:item:];
-[SBActivityAmbientObserver pendingItems];
-[SBActivityAmbientObserver setPendingItems:];
-[SBActivityAmbientObserver addPendingItem:];
-[SBActivityAmbientObserver nextPendingItem];
-[SBActivityAmbientObserver _sortActivityItems];
-[SBActivityAmbientObserver activeActivityItems];
-[SBActivityAmbientObserver addOverlaysForOngoingActivitiesIfNecessary];
-[SBActivityAmbientObserver hasPendingItem];
-[SBActivityAmbientObserver isActiveActivityItem:];
-[SBActivityAmbientObserver removePendingItem:];
-[SBActivityAmbientObserver setActiveActivityItems:];
```
