# `_BKSHIDUISensorOverseer`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 0 properties, 3 instance methods, 0 class methods

## Instance variables

```
@"BSCompoundAssertion" _transactionAssertion;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _connectionLock;
@"BSServiceInitiatingConnection" _connectionLock_connection;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _dataLock;
@"NSMutableDictionary" _dataLock_displayUUIDToSensorService;
@"NSDictionary" _dataLock_currentDisplayUUIDToSensorModes;
@"NSDictionary" _dataLock_sentDisplayUUIDToSensorModes;
```

## Instance methods

```
-[_BKSHIDUISensorOverseer init];
-[_BKSHIDUISensorOverseer _systemShellDidReconnect];
-[_BKSHIDUISensorOverseer initWithServiceConnection:];
```
