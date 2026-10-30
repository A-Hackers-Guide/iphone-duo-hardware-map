# `CBDisplayClient`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBPropertyObservable`, `CBTargetedPropertyObserver`
- 7 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"NSObject<OS_os_log>" _logHandle;
@"BrightnessSystemClient" _client;
@"CBDisplayHandle" _handle;
@"NSMutableSet" _observers;
@"NSMutableDictionary" _observerContexts;
@"<CBDisplayBrightnessClientProtocol>" _brightnessClient;
@"NSSet" _properties;
```

## Properties

```
@property (T@"<CBDisplayBrightnessClientProtocol>",R,V_brightnessClient) brightnessClient;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"CBHandle",R) handle;
@property (T@"NSSet",R,V_properties) properties;
@property (T@"NSObject<OS_dispatch_queue>",R) notifyQueue;
```

## Instance methods

```
-[CBDisplayClient properties];
-[CBDisplayClient removeObserver:];
-[CBDisplayClient dealloc];
-[CBDisplayClient notifyQueue];
-[CBDisplayClient handle];
-[CBDisplayClient description];
-[CBDisplayClient copyPropertyForKey:error:];
-[CBDisplayClient observeValue:forKey:andHandle:withContext:];
-[CBDisplayClient unregisterObserver:];
-[CBDisplayClient brightnessClient];
-[CBDisplayClient setProperty:forKey:error:];
-[CBDisplayClient initWithClient:andHandle:];
-[CBDisplayClient reevaluateSubscription];
-[CBDisplayClient registerObserver:withContext:error:];
-[CBDisplayClient setPropertyForKey:withValue:error:];
```
