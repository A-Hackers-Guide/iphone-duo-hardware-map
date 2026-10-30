# `CBExternalDisplayKeyPolicy`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBDisplayPropertyPolicy`
- 3 instance variables, 4 properties, 13 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"<CBDisplayPropertyPolicyDelegate>" _delegate;
@"NSDictionary" _extToGenericKeys;
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
-[CBExternalDisplayKeyPolicy copyPropertyForKey:];
-[CBExternalDisplayKeyPolicy copyStatusInfo];
-[CBExternalDisplayKeyPolicy setProperty:forKey:];
-[CBExternalDisplayKeyPolicy initWithDelegate:];
-[CBExternalDisplayKeyPolicy dealloc];
-[CBExternalDisplayKeyPolicy cancel];
-[CBExternalDisplayKeyPolicy containerDidAdd:];
-[CBExternalDisplayKeyPolicy containerWillRemove:];
-[CBExternalDisplayKeyPolicy copyPropertyForKey:forContainer:];
-[CBExternalDisplayKeyPolicy extKeyFromGenericKey:];
-[CBExternalDisplayKeyPolicy processNotificationForKey:value:container:handle:];
-[CBExternalDisplayKeyPolicy setProperty:forKey:forContainer:];
-[CBExternalDisplayKeyPolicy transformedBroadcastKey:containers:];
```
