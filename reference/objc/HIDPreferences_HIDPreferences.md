# `HIDPreferences`

- Image: [`/System/Library/PrivateFrameworks/HIDPreferences.framework/HIDPreferences`](../userland/System__Library__PrivateFrameworks__HIDPreferences.framework__HIDPreferences.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `HIDPreferencesProtocol`
- 3 instance variables, 4 properties, 11 instance methods, 2 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _queue;
i _option;
@"NSObject<OS_xpc_object>" _connection;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[HIDPreferences destroyConnection:];
+[HIDPreferences getReply:];
```

## Instance methods

```
-[HIDPreferences setupConnection];
-[HIDPreferences init];
-[HIDPreferences dealloc];
-[HIDPreferences initWithOption:];
-[HIDPreferences copy:user:host:domain:reply:];
-[HIDPreferences copyDomain:domain:reply:];
-[HIDPreferences copyMultiple:user:host:domain:reply:];
-[HIDPreferences set:value:user:host:domain:];
-[HIDPreferences setDomain:value:domain:];
-[HIDPreferences setMultiple:keysToRemove:user:host:domain:];
-[HIDPreferences synchronize:host:domain:];
```
