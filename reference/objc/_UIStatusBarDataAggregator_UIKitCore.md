# `_UIStatusBarDataAggregator`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 9 properties, 28 instance methods, 1 class methods

## Instance variables

```
@"_UIStatusBarData" _overlayData;
@? _updateBlock;
# _dataClass;
@"NSCountedSet" _delayedKeys;
@"NSMutableDictionary" _pendingUpdates;
@"NSMutableDictionary" _coalescedKeys;
@"NSMutableDictionary" _coalescedTimers;
```

## Properties

```
@property (T@?,C,N,V_updateBlock) updateBlock;
@property (T#,C,N,V_dataClass) dataClass;
@property (T@"NSCountedSet",&,N,V_delayedKeys) delayedKeys;
@property (T@"NSMutableDictionary",&,N,V_pendingUpdates) pendingUpdates;
@property (T@"NSMutableDictionary",&,N,V_coalescedKeys) coalescedKeys;
@property (T@"NSMutableDictionary",&,N,V_coalescedTimers) coalescedTimers;
@property (T@"_UIStatusBarData",C,N,V_overlayData) overlayData;
@property (T@"NSSet",R,C,N) delayedEntryKeys;
@property (T@"NSSet",R,C,N) coalescedEntryKeys;
```

## Class methods

```
+[_UIStatusBarDataAggregator initialize];
```

## Instance methods

```
-[_UIStatusBarDataAggregator dataClass];
-[_UIStatusBarDataAggregator updateWithData:];
-[_UIStatusBarDataAggregator delayedKeys];
-[_UIStatusBarDataAggregator _updateForDelayedKeysWithData:];
-[_UIStatusBarDataAggregator delayedEntryKeys];
-[_UIStatusBarDataAggregator setUpdateBlock:];
-[_UIStatusBarDataAggregator coalescedEntryKeys];
-[_UIStatusBarDataAggregator endCoalescingUpdatesForEntryKeys:];
-[_UIStatusBarDataAggregator updateBlock];
-[_UIStatusBarDataAggregator overlayData];
-[_UIStatusBarDataAggregator _updateForCoalescedKeysWithData:];
-[_UIStatusBarDataAggregator setOverlayData:];
-[_UIStatusBarDataAggregator pendingUpdates];
-[_UIStatusBarDataAggregator coalescedTimers];
-[_UIStatusBarDataAggregator initWithUpdateBlock:];
-[_UIStatusBarDataAggregator setDelayedKeys:];
-[_UIStatusBarDataAggregator coalescedKeys];
-[_UIStatusBarDataAggregator setCoalescedTimers:];
-[_UIStatusBarDataAggregator setDataClass:];
-[_UIStatusBarDataAggregator _updateFromPendingUpdatesForKeys:block:];
-[_UIStatusBarDataAggregator _updateForOverlayWithData:];
-[_UIStatusBarDataAggregator setCoalescedKeys:];
-[_UIStatusBarDataAggregator beginDelayingUpdatesForEntryKeys:];
-[_UIStatusBarDataAggregator setPendingUpdates:];
-[_UIStatusBarDataAggregator _updatedDataFromData:delayedKeys:];
-[_UIStatusBarDataAggregator beginCoalescingUpdatesForEntryKeys:delay:];
-[_UIStatusBarDataAggregator _coalescedUpdateForEntryKeys:];
-[_UIStatusBarDataAggregator endDelayingUpdatesForEntryKeys:];
```
