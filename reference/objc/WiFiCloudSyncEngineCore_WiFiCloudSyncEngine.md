# `WiFiCloudSyncEngineCore`

- Image: [`/System/Library/PrivateFrameworks/WiFiCloudSyncEngine.framework/WiFiCloudSyncEngine`](../userland/System__Library__PrivateFrameworks__WiFiCloudSyncEngine.framework__WiFiCloudSyncEngine.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 39 instance methods, 0 class methods

## Instance variables

```
@"NSUbiquitousKeyValueStore" keyValueStore;
^v context;
^? callback;
@"NSThread" clientThread;
@"NSObject<OS_dispatch_queue>" clientQueue;
B iCloudSyncingEnabled;
B isKVSEncrypted;
```

## Properties

```
@property (T@"NSUbiquitousKeyValueStore",&,VkeyValueStore) keyValueStore;
@property (T^v,Vcontext) context;
@property (T^?,Vcallback) callback;
@property (T@"NSThread",VclientThread) clientThread;
@property (T@"NSObject<OS_dispatch_queue>",VclientQueue) clientQueue;
@property (TB,ViCloudSyncingEnabled) iCloudSyncingEnabled;
@property (TB,VisKVSEncrypted) isKVSEncrypted;
```

## Instance methods

```
-[WiFiCloudSyncEngineCore setClientQueue:];
-[WiFiCloudSyncEngineCore clientQueue];
-[WiFiCloudSyncEngineCore clientThread];
-[WiFiCloudSyncEngineCore callback];
-[WiFiCloudSyncEngineCore synchronizeKVS];
-[WiFiCloudSyncEngineCore registerCallback:queue:context:];
-[WiFiCloudSyncEngineCore setCallback:];
-[WiFiCloudSyncEngineCore iCloudSyncingEnabled];
-[WiFiCloudSyncEngineCore relayCloudCleanUpEvent];
-[WiFiCloudSyncEngineCore unSubscribeKVStoreNotfications];
-[WiFiCloudSyncEngineCore initWithEncryptedKVS:];
-[WiFiCloudSyncEngineCore registerCallback:context:];
-[WiFiCloudSyncEngineCore pruneKVSStoreAndReply:];
-[WiFiCloudSyncEngineCore setIsKVSEncrypted:];
-[WiFiCloudSyncEngineCore dealloc];
-[WiFiCloudSyncEngineCore relayCloudEvent:];
-[WiFiCloudSyncEngineCore removeFromKVStore:];
-[WiFiCloudSyncEngineCore readCompleteKVStore];
-[WiFiCloudSyncEngineCore dispatchUbiquitousKeyValueStoreDidChangeOnBackground:];
-[WiFiCloudSyncEngineCore synchronizeAndCallMergeNetworksAndReply:];
-[WiFiCloudSyncEngineCore clearKVS];
-[WiFiCloudSyncEngineCore isKVSEncrypted];
-[WiFiCloudSyncEngineCore enableIcloudSyncing:ForBundleId:];
-[WiFiCloudSyncEngineCore setICloudSyncingEnabled:];
-[WiFiCloudSyncEngineCore setContext:];
-[WiFiCloudSyncEngineCore queryKeychainSyncState];
-[WiFiCloudSyncEngineCore subscribeKVStoreNotficationsForBundleId:];
-[WiFiCloudSyncEngineCore printCompleteKVStore];
-[WiFiCloudSyncEngineCore relayReadStoreValueAction:];
-[WiFiCloudSyncEngineCore setClientThread:];
-[WiFiCloudSyncEngineCore relayMergeNetworks:];
-[WiFiCloudSyncEngineCore addToKVStore:synchronize:];
-[WiFiCloudSyncEngineCore ubiquitousKeyValueStoreDidChange:];
-[WiFiCloudSyncEngineCore relayKeychainSyncState:];
-[WiFiCloudSyncEngineCore context];
-[WiFiCloudSyncEngineCore readStoreValueForKey:];
-[WiFiCloudSyncEngineCore keyValueStore];
-[WiFiCloudSyncEngineCore setKeyValueStore:];
-[WiFiCloudSyncEngineCore relayPruneKVSStore:];
```
