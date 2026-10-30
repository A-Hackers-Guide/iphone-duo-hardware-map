# `BKIOHIDServicePersistentPropertyController`

- Image: [`/System/Library/PrivateFrameworks/BackBoardHIDEventFoundation.framework/BackBoardHIDEventFoundation`](../userland/System__Library__PrivateFrameworks__BackBoardHIDEventFoundation.framework__BackBoardHIDEventFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 6 instance variables, 1 properties, 7 instance methods, 3 class methods

## Instance variables

```
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _handlersLock;
{os_unfair_lock_s="_os_unfair_lock_opaque"I} _defaultsLock;
@"BKSLocalDefaults" _defaultsLock_defaults;
@"NSHashTable" _handlersLock_handlers;
@"NSString" _clientEntitlement;
@"NSString" _defaultsKey;
```

## Properties

```
@property (T@"NSString",R,C,N,V_clientEntitlement) clientEntitlement;
```

## Class methods

```
+[BKIOHIDServicePersistentPropertyController sharedInstances];
+[BKIOHIDServicePersistentPropertyController digitizerServicePersistentPropertyController];
+[BKIOHIDServicePersistentPropertyController touchSensitiveButtonServicePersistentPropertyController];
```

## Instance methods

```
-[BKIOHIDServicePersistentPropertyController registerHandler:];
-[BKIOHIDServicePersistentPropertyController clientEntitlement];
-[BKIOHIDServicePersistentPropertyController allPersistentPropertiesForServicesMatchingDescriptor:];
-[BKIOHIDServicePersistentPropertyController initWithClientEntitlement:defaults:defaultsKey:];
-[BKIOHIDServicePersistentPropertyController persistentPropertiesForKeys:forSenderDescriptor:];
-[BKIOHIDServicePersistentPropertyController setPersistentProperties:forSenderDescriptor:];
-[BKIOHIDServicePersistentPropertyController unregisterHandler:];
```
