# `CAMTransientDataSource`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `PUTransientDataSource`
- 8 instance variables, 14 properties, 32 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" __observers;
@"NSMutableArray" __assetUUIDs;
@"NSMutableDictionary" __assetsByUUID;
@"NSMutableDictionary" __representativeAssetsByBurstIdentifier;
@"NSMutableDictionary" __enqueuedBurstAssetUUIDByBurstIdentifier;
@"NSMutableDictionary" __enqueuedBurstConvertiblesByAssetUUID;
q __nestedPerformChanges;
q __pendingChangeNotifications;
```

## Properties

```
@property (T@"NSHashTable",R,N,V__observers) _observers;
@property (T@"NSMutableArray",R,N,V__assetUUIDs) _assetUUIDs;
@property (T@"NSMutableDictionary",R,N,V__assetsByUUID) _assetsByUUID;
@property (T@"NSMutableDictionary",R,N,V__representativeAssetsByBurstIdentifier) _representativeAssetsByBurstIdentifier;
@property (T@"NSMutableDictionary",R,N,V__enqueuedBurstAssetUUIDByBurstIdentifier) _enqueuedBurstAssetUUIDByBurstIdentifier;
@property (T@"NSMutableDictionary",R,N,V__enqueuedBurstConvertiblesByAssetUUID) _enqueuedBurstConvertiblesByAssetUUID;
@property (Tq,N,S_setNestedPerformChanges:,V__nestedPerformChanges) _nestedPerformChanges;
@property (Tq,N,S_setPendingChangeNotifications:,V__pendingChangeNotifications) _pendingChangeNotifications;
@property (TB,R,N,GisEmpty) empty;
@property (T@"NSSet",R,N) existingBurstIdentifiers;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMTransientDataSource registerChangeObserver:];
-[CAMTransientDataSource _enqueuedBurstAssetUUIDByBurstIdentifier];
-[CAMTransientDataSource insertAssetWithConvertible:];
-[CAMTransientDataSource transientAssetMapping];
-[CAMTransientDataSource _notifyObserversOfDataSourceChange];
-[CAMTransientDataSource _representativeAssetsByBurstIdentifier];
-[CAMTransientDataSource init];
-[CAMTransientDataSource unregisterChangeObserver:];
-[CAMTransientDataSource uuids];
-[CAMTransientDataSource performChanges:];
-[CAMTransientDataSource _pendingChangeNotifications];
-[CAMTransientDataSource removeRepresentativeAssetForBurstIdentifier:];
-[CAMTransientDataSource _nestedPerformChanges];
-[CAMTransientDataSource _observers];
-[CAMTransientDataSource removeAssetWithUUID:];
-[CAMTransientDataSource existingRepresentativeAssetForBurstIdentifier:];
-[CAMTransientDataSource _setNestedPerformChanges:];
-[CAMTransientDataSource removeAllAssets];
-[CAMTransientDataSource isEmpty];
-[CAMTransientDataSource _enqueuedBurstConvertiblesByAssetUUID];
-[CAMTransientDataSource _assetsByUUID];
-[CAMTransientDataSource existingBurstIdentifiers];
-[CAMTransientDataSource updateAssetWithConvertible:];
-[CAMTransientDataSource description];
-[CAMTransientDataSource enqueuePendingBurstAssetWithConvertible:];
-[CAMTransientDataSource _removeAssetWithUUID:];
-[CAMTransientDataSource processPendingBurstAssets];
-[CAMTransientDataSource existingAssetForUUID:];
-[CAMTransientDataSource _assetUUIDs];
-[CAMTransientDataSource _setPendingChangeNotifications:];
-[CAMTransientDataSource existingAssetUUIDs];
-[CAMTransientDataSource transientBurstMapping];
```
