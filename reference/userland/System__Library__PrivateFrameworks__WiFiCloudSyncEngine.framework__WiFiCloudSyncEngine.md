# `/System/Library/PrivateFrameworks/WiFiCloudSyncEngine.framework/WiFiCloudSyncEngine`

iOS 27.2 dyld shared cache image. Version `865.9.0.0.0`. **[DSC]**

## Linked libraries (6)

- `/System/Library/Frameworks/Security.framework/Security`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/usr/lib/libSystem.B.dylib`
- `/usr/lib/libobjc.A.dylib`

## Objective-C: 2 classes, 0 protocols, 39 methods, 7 properties

### Class pages

Every class and protocol, with its methods: [`WiFiCloudSyncEngineCore`](../objc/WiFiCloudSyncEngineCore_WiFiCloudSyncEngine.md), [`WiFiCloudSyncEngineLogger`](../objc/WiFiCloudSyncEngineLogger_WiFiCloudSyncEngine.md)

### Classes

`WiFiCloudSyncEngineCore`, `WiFiCloudSyncEngineLogger`

### Properties

```
@property (T@"NSUbiquitousKeyValueStore",&,VkeyValueStore) keyValueStore;
@property (T^v,Vcontext) context;
@property (T^?,Vcallback) callback;
@property (T@"NSThread",VclientThread) clientThread;
@property (T@"NSObject<OS_dispatch_queue>",VclientQueue) clientQueue;
@property (TB,ViCloudSyncingEnabled) iCloudSyncingEnabled;
@property (TB,VisKVSEncrypted) isKVSEncrypted;
```

## Strings (334)

```
[WIFICLOUDSYNC] %s (%s:%u)<%@>: entry already exists, will not update (%@ --> %@)
[WIFICLOUDSYNC] %s (%s:%u)done !!!
[WIFICLOUDSYNC] %s (%s:%u)no known network
[WIFICLOUDSYNC] %s (%s:%u)null coreEngine
[WIFICLOUDSYNC] %s (%s:%u)<%@>
[WIFICLOUDSYNC] %s (%s:%u)Password is still not available for network at idx %ld
[WIFICLOUDSYNC] %s (%s:%u)syncing disabled, abort... 
[WIFICLOUDSYNC] %s (%s:%u)null sync coreEngine
[WIFICLOUDSYNC] %s (%s:%u)LOCAL --> CLOUD: <%@> more recently added on local device, update cloud KVS
[WIFICLOUDSYNC] %s (%s:%u)carplay only network, not syncable
[WIFICLOUDSYNC] %s (%s:%u)%ld networks already waiting for password sync
[WIFICLOUDSYNC] %s (%s:%u)Add/update <%@> {length: %lu, max %lu} to KVS
[WIFICLOUDSYNC] %s (%s:%u)captive determination not finished, or captive network, not syncable
[WIFICLOUDSYNC] %s (%s:%u)stop keychain changed notifications and empty the waiting list
[WIFICLOUDSYNC] %s (%s:%u)
[WIFICLOUDSYNC] %s (%s:%u)merge networks from icloud and plist...
[WIFICLOUDSYNC] %s (%s:%u)LOCAL --> CLOUD: <%@> does not exist on cloud KVS, add to cloud KVS
[WIFICLOUDSYNC] %s (%s:%u)NSUbiquitousKeyValueStoreServerChange: %@
[WIFICLOUDSYNC] %s (%s:%u)missing WIFICLOUDSYNC_NETWORKKEY_ISEAP key, not syncable
[WIFICLOUDSYNC] %s (%s:%u)KVS synchronization failed !!
[WIFICLOUDSYNC] %s (%s:%u)<%@>: %@ --> %@
[WIFICLOUDSYNC] %s (%s:%u)null sync engine or cloud format
[WIFICLOUDSYNC] %s (%s:%u)null networkRef
[WIFICLOUDSYNC] %s (%s:%u)CLOUD --> LOCAL: <%@> more recently added on local KVS, defer
[WIFICLOUDSYNC] %s (%s:%u)USERDIRECTED key missing
[WIFICLOUDSYNC] %s (%s:%u)missing WIFICLOUDSYNC_NETWORKKEY_ISCONFIGURED key, not syncable
[WIFICLOUDSYNC] %s (%s:%u)isKeychainSyncEnabled %d
[WIFICLOUDSYNC] %s (%s:%u)was not running...
[WIFICLOUDSYNC] %s (%s:%u)FAILED to migrate network entry to encrypted KVS (missing SSID), %@
[WIFICLOUDSYNC] %s (%s:%u)secured network, but there is no password present...
[WIFICLOUDSYNC] %s (%s:%u)hidden network, not syncable
[WIFICLOUDSYNC] %s (%s:%u)KVS created for bundle id [%@] and store id [%@]
[WIFICLOUDSYNC] %s (%s:%u)WiFiCloudSyncEngineCallbacks version - %ld, bundle id - %@
[WIFICLOUDSYNC] %s (%s:%u)<%@> exists on the device
[WIFICLOUDSYNC] %s (%s:%u)remove network from the known networks list
[WIFICLOUDSYNC] %s (%s:%u)LOCAL --> CLOUD: <%@> more recently added on cloud KVS, defer
[WIFICLOUDSYNC] %s (%s:%u)empty waiting list...
[WIFICLOUDSYNC] %s (%s:%u)null key
[WIFICLOUDSYNC] %s (%s:%u)complete store: %@
[WIFICLOUDSYNC] %s (%s:%u)Will clear %sKVS
[WIFICLOUDSYNC] %s (%s:%u)dispatch KeychainSyncState query
[WIFICLOUDSYNC] %s (%s:%u)CLOUD --> LOCAL: <%@> does not exist on local KVS, add to local KVS
[WIFICLOUDSYNC] %s (%s:%u)minimum version (%ld) not supported by device (version=%ld)
[WIFICLOUDSYNC] %s (%s:%u)[OTClique fetchUserControllableViewsSyncingEnabled:] returned %d, error=%@
[WIFICLOUDSYNC] %s (%s:%u)check waiting list
[WIFICLOUDSYNC] %s (%s:%u)nil known networks
[WIFICLOUDSYNC] %s (%s:%u)null keyValueDictToCloud
[WIFICLOUDSYNC] %s (%s:%u)null createCloudFromNetworkFormatCallback
[WIFICLOUDSYNC] %s (%s:%u)kvs item #%lu - <%@>
[WIFICLOUDSYNC] %s (%s:%u)LOCAL --> CLOUD: <%@> more recently removed on cloud KVS, defer
[WIFICLOUDSYNC] %s (%s:%u)Un-scheduled WiFiCloudSyncEngine on the client runLoop
[WIFICLOUDSYNC] %s (%s:%u)already running...
[WIFICLOUDSYNC] %s (%s:%u)null runLoop or queue
[WIFICLOUDSYNC] %s (%s:%u)null checkWaitingForPasswordTimestamps
[WIFICLOUDSYNC] %s (%s:%u)NSUbiquitousKeyValueStoreQuotaViolationChange: %@
[WIFICLOUDSYNC] %s (%s:%u)null removeNetworkCallback
[WIFICLOUDSYNC] %s (%s:%u)CLOUD --> LOCAL: <%@> is removed on cloud KVS, ignore
[WIFICLOUDSYNC] %s (%s:%u)stopped...
[WIFICLOUDSYNC] %s (%s:%u)adhoc network, not syncable
[WIFICLOUDSYNC] %s (%s:%u)started...
[WIFICLOUDSYNC] %s (%s:%u)KVS synchronized
[WIFICLOUDSYNC] %s (%s:%u)key length exceeded maximum allowed length
[WIFICLOUDSYNC] %s (%s:%u)Scheduled WiFiCloudSyncEngine on the client runLoop
[WIFICLOUDSYNC] %s (%s:%u)<%@> does not exist on icloud, add it
[WIFICLOUDSYNC] %s (%s:%u)CLOUD --> LOCAL: <%@> more recently added on cloud KVS, update local KVS
[WIFICLOUDSYNC] %s (%s:%u)null keychainChangedNotify.source
[WIFICLOUDSYNC] %s (%s:%u)null networksWaitingForPassword
[WIFICLOUDSYNC] %s (%s:%u)null key or value
[WIFICLOUDSYNC] %s (%s:%u)FAILED to initialize OTClique, cannot query sync status
[WIFICLOUDSYNC] %s (%s:%u)null changed keys or syncEngine
[WIFICLOUDSYNC] %s (%s:%u)FAILED to migrate network entry to encrypted KVS, %@
[WIFICLOUDSYNC] %s (%s:%u)auto-join is disabled, not syncable
[WIFICLOUDSYNC] %s (%s:%u)key: <%@>
[WIFICLOUDSYNC] %s (%s:%u)cloud clean up event -- reason %d changed keys : %@
[WIFICLOUDSYNC] %s (%s:%u)there are no networks waiting for password sync, so stop the keychain changed notifications
[WIFICLOUDSYNC] %s (%s:%u)add network to the known networks list 
[WIFICLOUDSYNC] %s (%s:%u)process change #%lu: <%@>
[WIFICLOUDSYNC] %s (%s:%u)NOT SYNCABLE override
[WIFICLOUDSYNC] %s (%s:%u)Un-scheduled WiFiCloudSyncEngine on the client queue
[WIFICLOUDSYNC] %s (%s:%u)null bundleId
[WIFICLOUDSYNC] %s (%s:%u)null addNetworkCallback
[WIFICLOUDSYNC] %s (%s:%u)%ld networks in plist
[WIFICLOUDSYNC] %s (%s:%u)%ld networks waiting for password sync, currently at %ld
[WIFICLOUDSYNC] %s (%s:%u)null keychainChangedNotify.token
[WIFICLOUDSYNC] %s (%s:%u)Got the callback on the client queue, dispatch it on background
[WIFICLOUDSYNC] %s (%s:%u)invalid cloud formatted known network
[WIFICLOUDSYNC] %s (%s:%u)__WiFiCloudSyncEngineAddVersionsToCloudNetwork null cloudNetwork
[WIFICLOUDSYNC] %s (%s:%u)Error !!  not running on client queue
[WIFICLOUDSYNC] %s (%s:%u)wifi icloud syncing is disabled
[WIFICLOUDSYNC] %s (%s:%u)null cloudNetwork
[WIFICLOUDSYNC] %s (%s:%u)there are %ld networks waiting for password sync, and we received a cloud keychain update while processing list, process again
[WIFICLOUDSYNC] %s (%s:%u)null ssid
[WIFICLOUDSYNC] %s (%s:%u)added network <%@> to waiting for password sync list
[WIFICLOUDSYNC] %s (%s:%u)Encrypted KVS created for bundle id [%@] and store id [%@]
[WIFICLOUDSYNC] %s (%s:%u)Secure network, add to waiting list
[WIFICLOUDSYNC] %s (%s:%u)null keychainSyncStateChangedNotify.source
[WIFICLOUDSYNC] %s (%s:%u)there are %ld networks waiting for password sync, and they're unavailable
[WIFICLOUDSYNC] %s (%s:%u)customized network, not syncable
[WIFICLOUDSYNC] %s (%s:%u)null client thread or queue
[WIFICLOUDSYNC] %s (%s:%u)max 'waiting for password' attempts reached (%d per %.1fs), next attempt scheduled for %.1fs from now
[WIFICLOUDSYNC] %s (%s:%u)FAILED to create local representation for cloud format %@, removed network from waiting for password sync list
[WIFICLOUDSYNC] %s (%s:%u)null cloudEventData or syncEngine
[WIFICLOUDSYNC] %s (%s:%u)removed network from waiting for password sync list
[WIFICLOUDSYNC] %s (%s:%u)no known networks
[WIFICLOUDSYNC] %s (%s:%u)Processing %lu circle changed notifications
[WIFICLOUDSYNC] %s (%s:%u)set...
[WIFICLOUDSYNC] %s (%s:%u)Remove <%@> from KVS
[WIFICLOUDSYNC] %s (%s:%u)null copyAllNetworksCallback
[WIFICLOUDSYNC] %s (%s:%u)CLOUD --> LOCAL: <%@> more recently removed on cloud KVS, remove from local KVS
[WIFICLOUDSYNC] %s (%s:%u)null syncEngine 
[WIFICLOUDSYNC] %s (%s:%u)ignoring non-ssid key %@
[WIFICLOUDSYNC] %s (%s:%u)invalid cloudNetwork
[WIFICLOUDSYNC] %s (%s:%u)secured network, so set password syncable
[WIFICLOUDSYNC] %s (%s:%u)open network, not syncable
[WIFICLOUDSYNC] %s (%s:%u)%s
[WIFICLOUDSYNC] %s (%s:%u)Error: null keyValueDict 
[WIFICLOUDSYNC] %s (%s:%u)Error: null key
[WIFICLOUDSYNC] %s (%s:%u)Got the callback on the client thread, dispatch it on background
[WIFICLOUDSYNC] %s (%s:%u)null sync engine
[WIFICLOUDSYNC] %s (%s:%u)null syncEngine
[WIFICLOUDSYNC] %s (%s:%u)configured network, not syncable
[WIFICLOUDSYNC] %s (%s:%u)null callBacks
[WIFICLOUDSYNC] %s (%s:%u)null createNetworkFromCloudFormatCallback
[WIFICLOUDSYNC] %s (%s:%u)null setPasswordSyncStateCallback
[WIFICLOUDSYNC] %s (%s:%u)null cloud network
[WIFICLOUDSYNC] %s (%s:%u)<%@> exists on icloud
[WIFICLOUDSYNC] %s (%s:%u)set...but not started
[WIFICLOUDSYNC] %s (%s:%u)EAP network, not syncable
[WIFICLOUDSYNC] %s (%s:%u)missing WIFICLOUDSYNC_NETWORKKEY_ISCUSTOMIZED key, not syncable
[WIFICLOUDSYNC] %s (%s:%u)....
[WIFICLOUDSYNC] %s (%s:%u)Scheduled WiFiCloudSyncEngine on the client queue
[WIFICLOUDSYNC] %s (%s:%u)Open network, not adding to waiting list
[WIFICLOUDSYNC] %s (%s:%u)KVS networks: %@
[WIFICLOUDSYNC] %s (%s:%u)check keychain view membership
[WIFICLOUDSYNC] %s (%s:%u)NSUbiquitousKeyValueStoreInitialSyncChange: %@
[WIFICLOUDSYNC] %s (%s:%u)Remove <%@> from passwords waiting list
[WIFICLOUDSYNC] %s (%s:%u)...
[WIFICLOUDSYNC] %s (%s:%u)null ssidStr
[WIFICLOUDSYNC] %s (%s:%u)Error !!  not running on client thread
[WIFICLOUDSYNC] %s (%s:%u)Already migrated from legacy non-encrypted KVS to encrypted KVS, skipping migration
[WIFICLOUDSYNC] %s (%s:%u)null mutableCloudNetwork
[WIFICLOUDSYNC] %s (%s:%u)non-infrastructure network, not syncable
[WIFICLOUDSYNC] %s (%s:%u)null isPasswordPresentCallback
[WIFICLOUDSYNC] %s (%s:%u)Password is now available for network at idx %ld
[WIFICLOUDSYNC] %s (%s:%u)NSUbiquitousKeyValueStoreAccountChange: %@
[WIFICLOUDSYNC] %s (%s:%u)expirable network, not syncable
[WIFICLOUDSYNC] %s (%s:%u)there are no networks already waiting for password sync, so start the keychain changed notifications
%@ %s: %@
WiFiCloudSyncEngineScheduleWithRunLoop
WiFiCloudSyncEngineStopEngine
enabled
__WiFiCloudSyncEngineIsNetworkHidden
lastJoinedByUserAt
WiFiCloudSyncEngineNonSSIDKeyPrefix_
__WiFiCloudSyncEngineSetupKeychainSyncStateChangeNotification
WiFiCloudSyncEngineRemoveNetworkFromKnownNetworksList
UserJoinedAt
IS_PUBLIC
prvateMacPrefTimestamp
__WiFiCloudSyncEngineFlushWaitingForPasswordList
-[WiFiCloudSyncEngineCore readStoreValueForKey:]
__WiFiCloudSyncEngineSetupKeychainChangedNotification
__WiFiCloudSyncEngineProcessCloudNetworkChangeEvent
IE_KEY_RSN_UCIPHERS
IS_MOVING
IOPlatformExpertDevice
isWAPI
 DISABLING...
-[WiFiCloudSyncEngineCore pruneKVSStoreAndReply:]
AP_MODE
preferredOrderTimestamp
%@.%@.%@.%@.%ld
-[WiFiCloudSyncEngineCore unSubscribeKVStoreNotfications]
-[WiFiCloudSyncEngineCore synchronizeAndCallMergeNetworksAndReply:]
17:23:14
IE_KEY_WPA_UCIPHERS
isAppBased
lowDataMode
AddedAt
__WiFiCloudSyncEngineIsNetworkSyncableFromCloudEncrypted
isOpen
SSID_STR
-[WiFiCloudSyncEngineCore readCompleteKVStore]
-[WiFiCloudSyncEngineCore relayPruneKVSStore:]
WiFiCloudSyncEngineRegisterCallbacksWithQueue
__WiFiCloudSyncEngineCloudEventCallback
privateMacPref
__WiFiCloudSyncEngineCreateCloudFromNetworkFormatCallback
WiFiCloudSyncEngineNonSSIDKeyPrefix_NonNetworkContainer
__WiFiCloudSyncEngineProcessCloudChangeEvent_block_invoke
__WiFiCloudSyncEngineStartKeychainChangedNotifications
-[WiFiCloudSyncEngineCore queryKeychainSyncState]
WiFiCloudSyncEngineUnScheduleWithRunLoop
WiFiCloudSyncEngineMergeKnownNetworksToCloudWithKVS
IE_KEY_RSN_AUTHSELS
_
addedAt
WiFiCloudSyncEnginePruneNetworksInCloud
WiFiCloudSyncEngineMergeKnownNetworksToCloudWithKVS_block_invoke
IE_KEY_RSN_MCIPHER
IS_NETWORK_CUSTOMIZED
NOT_SYNCABLE
enable_network_sync
__WiFiCloudSyncEngineAddVersionsToCloudNetwork
WiFiCloudSyncEngine
__WiFiCloudSyncEngineCreateNetworkFromCloudFormatCallback
isPrivacyProxyEnabled
i
WiFiCloudSyncEngineCore.m
v8@?0
-[WiFiCloudSyncEngineCore removeFromKVStore:]
com.apple.wifi.wcse.kvs_events
WiFiCloudSyncEngineCheckKeychainSyncState
__WiFiCloudSyncEngineIsNetworkSyncableToCloudEncrypted
isWPA2
WPA_IE
WiFiCloudSyncEngineIsRunning
IS_NETWORK_CONFIGURED
IS_NETWORK_APPBASED
isPublic
%@
-[WiFiCloudSyncEngineCore synchronizeKVS]
WiFiCloudSyncEngineStartEngine
UserDirected
IS_NETWORK_EAP
IE_KEY_RSN_CAPS
IS_NETWORK_CAPTIVE
__WiFiCloudSyncEngineAddMissingKeysToCloudNetwork
removedAt
isPSK
-[WiFiCloudSyncEngineCore enableIcloudSyncing:ForBundleId:]
com.apple.security.keychainchanged
%@%@
IS_PRIVACY_PROXY_ENABLED
was6GHzOnlyAtWeek
-[WiFiCloudSyncEngineCore dispatchUbiquitousKeyValueStoreDidChangeOnBackground:]
-[WiFiCloudSyncEngineCore relayKeychainSyncState:]
WiFiCloudSyncEngineRemoveNetworkFromCloud
__WiFiCloudSyncEngineStopKeychainChangedNotifications
IE_KEY_WPA_AUTHSELS
isHidden
IS_NETWORK_WHITELISTING_CAPTIVE
-[WiFiCloudSyncEngineCore addToKVStore:synchronize:]
-[WiFiCloudSyncEngineCore relayReadStoreValueAction:]
-[WiFiCloudSyncEngineCore relayMergeNetworks:]
SSID
MFP_CAPABLE
isIBSS
__WiFiCloudSyncEngineGetNetworkSecurity
-[WiFiCloudSyncEngineCore clearKVS]
__WiFiCloudSyncEngineProcessCloudChangeEvent
IE_KEY_RSN_VERSION
IE_KEY_WPA_VERSION
__WiFiCloudSyncEngineIsNetworkSyncableToCloudLegacy
WiFiCloudSyncEngineNonSSIDKeyPrefix_cleaningKVS
WiFiCloudSyncEngine.m
com.apple.wifi.wcse.serialQ.circleChanges
network.
__WiFiCloudSyncEngineCheckWaitingForPasswordList
MFP_REQUIRED
seamlessSSIDList
__WiFiCloudSyncEngineMigrateToEncryptedKVS
WiFiCloudSyncEngineScheduleWithQueue
WiFiCloudSyncEngineScheduleWithQueue_block_invoke
WiFiCloudSyncEngineAddNetworkToCloud
__WiFiCloudSyncEngineKeychainSyncStateChanged
isCustom
ProductVersion
__WiFiCloudSyncEngineAddToWaitingForPasswordList
__WiFiCloudSyncEngineRemoveFromWaitingForPasswordList
com.apple.wifi.network-sync
minVersion
isMoving
WiFiCloudSyncEngineNonSSIDKeyPrefix_KVSVersion
Oct  3 2026
WiFiCloudSyncEngineCreate
version
.
-[WiFiCloudSyncEngineCore registerCallback:queue:context:]
-[WiFiCloudSyncEngineCore subscribeKVStoreNotficationsForBundleId:]
isWhitelistedCaptive
__WiFiCloudSyncEngineIsCloudNetworkOnDevice
lastJoinedBySystemAtWeek
WiFiCloudSyncEngineUnScheduleWithQueue
resetKVS
isExpirable
LOW_DATA_MODE
q
__WiFiCloudSyncEngineRelease
isProfileBased
ProductBuildVersion
 
model
isWEP
isWPA
isWPA3
isAutoJoinDisabled
ProductName
__WiFiCloudSyncEngineRemoveCloudFormatNetworkFromCloud
-[WiFiCloudSyncEngineCore printCompleteKVStore]
WiFiCloudSyncEngineMergeKnownNetworksToCloud
isCaptive
__WiFiCloudSyncEngineIsNetworkSyncableFromCloudLegacy
BSSID
com.apple.wifi.syncable-networks
com.apple.wifid.known-networks
WiFiCloudSyncEngineRegisterCallbacks
__WiFiCloudSyncEngineAddNetworkToCloudAndPurge
isEAP
WEP
WPA3_RSN_IE
-[WiFiCloudSyncEngineCore ubiquitousKeyValueStoreDidChange:]
v16@?0^{__CFRunLoopTimer=}8
[NO client logger] <%s %s> %@
IS_NETWORK_EXPIRABLE
isCarPlayOnly
IS_NETWORK_CARPLAY_ONLY
UserPreferredTimestamp
-[WiFiCloudSyncEngineCore registerCallback:context:]
RSN_IE
 ENABLING...
WiFiCloudSyncEngineScheduleWithRunLoop_block_invoke
WiFiCloudSyncEngineAddNetworkToKnownNetworksList
IE_KEY_WPA_MCIPHER
__WiFiCloudSyncEngineAddNetworkToCloudAndPurge_block_invoke
addedByVersion
Encrypted 
reason
changedKeys
-[WiFiCloudSyncEngineCore relayCloudCleanUpEvent]
v12@?0i8
__WiFiCloudSyncEngineKeychainChangedNotificationCallback
/System/Library/CoreServices/SystemVersion.plist
-[WiFiCloudSyncEngineCore relayCloudEvent:]
```
