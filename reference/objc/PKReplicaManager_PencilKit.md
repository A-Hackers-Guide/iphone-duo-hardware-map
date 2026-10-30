# `PKReplicaManager`

- Image: [`/System/Library/Frameworks/PencilKit.framework/PencilKit`](../userland/System__Library__Frameworks__PencilKit.framework__PencilKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 2 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _uuidAccessQueue;
@"NSMutableOrderedSet" _replicaUUIDs;
@"NSMutableDictionary" _replicaEntries;
@"NSMutableArray" _replicaManagerErrors;
@? _saveStateBlock;
B _dirtyTokenSet;
B _shouldPersist;
B _testMode;
```

## Properties

```
@property (TB,N,V_testMode) testMode;
@property (T@"NSArray",R,N) replicaManagerErrors;
```

## Class methods

```
+[PKReplicaManager sharedReplicaManager];
```

## Instance methods

```
-[PKReplicaManager testMode];
-[PKReplicaManager init];
-[PKReplicaManager _applicationWillTerminate];
-[PKReplicaManager setTestMode:];
-[PKReplicaManager description];
-[PKReplicaManager persistIfNeeded];
-[PKReplicaManager _loadState];
-[PKReplicaManager _resetAllReplicaUUIDs];
-[PKReplicaManager _saveStateImmediately];
-[PKReplicaManager _scheduleSaveState];
-[PKReplicaManager _setReplicasDirtyToken];
-[PKReplicaManager checkoutReplicaUUIDForDrawing:];
-[PKReplicaManager isValidBundleIDForSaving:];
-[PKReplicaManager replicaManagerErrors];
-[PKReplicaManager returnReplicaForDrawing:];
-[PKReplicaManager updateVersionForDrawing:];
```
