# `ULBLEKeyManager`

- Image: [`/System/Library/PrivateFrameworks/MicroLocationDaemon.framework/MicroLocationDaemon`](../userland/System__Library__PrivateFrameworks__MicroLocationDaemon.framework__MicroLocationDaemon.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ULBleIdentityBridgeDelegate`
- 6 instance variables, 7 properties, 21 instance methods, 0 class methods

## Instance variables

```
{unordered_set<ULBleIdentityItem, ULBleIdentityItem::HashItem, ULBleIdentityItem::PredicateItem, std::allocator<ULBleIdentityItem>>="__table_"{__hash_table<ULBleIdentityItem, ULBleIdentityItem::HashItem, ULBleIdentityItem::PredicateItem, std::allocator<ULBleIdentityItem>>="__bucket_list_"{unique_ptr<std::__hash_node_base<std::__hash_node<ULBleIdentityItem, void *> *> *[], std::__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<ULBleIdentityItem, void *> *> *>>>=""{?="__ptr_"^^v"__deleter_"{__bucket_list_deallocator<std::allocator<std::__hash_node_base<std::__hash_node<ULBleIdentityItem, void *> *> *>>=""{?="__size_"Q}}}}""{?="__first_node_"{__hash_node_base<std::__hash_node<ULBleIdentityItem, void *> *>="__next_"^v}}""{?="__size_"Q}""{?="__max_load_factor_"f}}} sameAccountBleIdentitiesInternal;
@"ULEnvironment" _environment;
^{ULDatabaseStoreInterface=^^?} _dbStore;
@"NSMutableSet" _oobKeysInternal;
^{ULBLEKeyManagerDelegate=^^?} _delegate;
@"ULBleIdentityBridge" _bleIdentityBridge;
```

## Properties

```
@property (T@"ULEnvironment",&,N,V_environment) environment;
@property (T^{ULDatabaseStoreInterface=^^?},N,V_dbStore) dbStore;
@property (T@"NSMutableSet",&,N,V_oobKeysInternal) oobKeysInternal;
@property (T^{ULBLEKeyManagerDelegate=^^?},N,V_delegate) delegate;
@property (T@"ULBleIdentityBridge",&,N,V_bleIdentityBridge) bleIdentityBridge;
@property (T@"NSArray",R,N) oobKeys;
@property (T@"NSArray",R,N) sameAccountBleIdentities;
```

## Instance methods

```
-[ULBLEKeyManager setEnvironment:];
-[ULBLEKeyManager oobKeys];
-[ULBLEKeyManager setDelegate:];
-[ULBLEKeyManager delegate];
-[ULBLEKeyManager setDependencies:];
-[ULBLEKeyManager environment];
-[ULBLEKeyManager startMonitoringEvents];
-[ULBLEKeyManager dbStore];
-[ULBLEKeyManager oobKeysInternal];
-[ULBLEKeyManager _handleULRapportMonitorEventIdentities:];
-[ULBLEKeyManager backupSameAccountBleIdentities];
-[ULBLEKeyManager bleIdentityBridge];
-[ULBLEKeyManager initWithDelegate:environment:andDbStore:];
-[ULBLEKeyManager loadSameAccountBleIdentitiesFromDb];
-[ULBLEKeyManager onBleIdentityItem:];
-[ULBLEKeyManager resetSameAccountBleIdentities];
-[ULBLEKeyManager sameAccountBleIdentities];
-[ULBLEKeyManager setBleIdentityBridge:];
-[ULBLEKeyManager setDbStore:];
-[ULBLEKeyManager setOobKeysInternal:];
-[ULBLEKeyManager stopMonitoringEvents];
```
