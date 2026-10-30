# `HIDPreferencesHelperClient`

- Image: [`/System/Library/PrivateFrameworks/HIDPreferences.framework/HIDPreferences`](../userland/System__Library__PrivateFrameworks__HIDPreferences.framework__HIDPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `HIDPreferencesProtocol`
- 2 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_xpc_object>" _connection;
@"HIDPreferencesHelperListener" _listener;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[HIDPreferencesHelperClient handleMessage:];
-[HIDPreferencesHelperClient invalidateConnection];
-[HIDPreferencesHelperClient copy:user:host:domain:reply:];
-[HIDPreferencesHelperClient copyDomain:domain:reply:];
-[HIDPreferencesHelperClient copyMultiple:user:host:domain:reply:];
-[HIDPreferencesHelperClient initWithConnection:listener:onQueue:];
-[HIDPreferencesHelperClient set:value:user:host:domain:];
-[HIDPreferencesHelperClient setDomain:value:domain:];
-[HIDPreferencesHelperClient setMultiple:keysToRemove:user:host:domain:];
-[HIDPreferencesHelperClient setupConnectionOnQueue:];
-[HIDPreferencesHelperClient synchronize:host:domain:];
```
