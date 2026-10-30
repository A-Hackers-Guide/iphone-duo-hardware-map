# `CWFKeyValueStore`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 10 instance variables, 5 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_dispatch_queue>" _mutexQueue;
@"NSObject<OS_dispatch_queue>" _eventQueue;
@"NSUbiquitousKeyValueStore" _ubiquitousKVS;
i _firstUnlockNotificationToken;
B _unlockedSinceBoot;
B _activated;
q _type;
@"NSString" _identifier;
@? _invalidationHandler;
@? _eventHandler;
```

## Properties

```
@property (TB,N,GisActivated,V_activated) activated;
@property (Tq,R,V_type) type;
@property (T@"NSString",R,C,V_identifier) identifier;
@property (T@?,C,V_invalidationHandler) invalidationHandler;
@property (T@?,C,V_eventHandler) eventHandler;
```

## Instance methods

```
-[CWFKeyValueStore isActivated];
-[CWFKeyValueStore eventHandler];
-[CWFKeyValueStore addEntriesFromDictionary:];
-[CWFKeyValueStore setEventHandler:];
-[CWFKeyValueStore setActivated:];
-[CWFKeyValueStore synchronize];
-[CWFKeyValueStore identifier];
-[CWFKeyValueStore setInvalidationHandler:];
-[CWFKeyValueStore initWithType:identifier:];
-[CWFKeyValueStore objectForKey:];
-[CWFKeyValueStore invalidate];
-[CWFKeyValueStore type];
-[CWFKeyValueStore removeAllEntries];
-[CWFKeyValueStore activate];
-[CWFKeyValueStore setObject:forKey:];
-[CWFKeyValueStore invalidationHandler];
-[CWFKeyValueStore dictionaryRepresentation];
-[CWFKeyValueStore __synchronize];
-[CWFKeyValueStore __debugDescriptionForType:];
-[CWFKeyValueStore __ubiquitousKVSChanged:];
```
