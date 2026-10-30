# `CWFSensingHMADataCollector`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `HMAccessoryDelegate`
- 6 instance variables, 10 properties, 18 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" __sensingParams;
@"HMAccessory" __accessory;
@"NSError" __serviceRegistrationError;
@"NSObject<OS_dispatch_queue>" __serviceQueue;
@"<CWFSensingHMADataCollectorDelegate>" __delegate;
q __attempt;
```

## Properties

```
@property (T@"NSDictionary",&,N,V__sensingParams) _sensingParams;
@property (T@"HMAccessory",&,N,V__accessory) _accessory;
@property (T@"NSError",&,N,V__serviceRegistrationError) _serviceRegistrationError;
@property (T@"NSObject<OS_dispatch_queue>",&,N,V__serviceQueue) _serviceQueue;
@property (T@"<CWFSensingHMADataCollectorDelegate>",&,N,V__delegate) _delegate;
@property (Tq,N,V__attempt) _attempt;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CWFSensingHMADataCollector createCWFSensingHMADataCollectorFor:withOptions:andDelegate:];
```

## Instance methods

```
-[CWFSensingHMADataCollector _delegate];
-[CWFSensingHMADataCollector set_delegate:];
-[CWFSensingHMADataCollector _serviceQueue];
-[CWFSensingHMADataCollector set_serviceQueue:];
-[CWFSensingHMADataCollector _accessory];
-[CWFSensingHMADataCollector set_accessory:];
-[CWFSensingHMADataCollector accessory:service:didUpdateValueForCharacteristic:];
-[CWFSensingHMADataCollector _attempt];
-[CWFSensingHMADataCollector _sensingParams];
-[CWFSensingHMADataCollector _serviceRegistrationError];
-[CWFSensingHMADataCollector currentRoomIdentifier];
-[CWFSensingHMADataCollector deregisterForPrimaryServiceNotificationWith:];
-[CWFSensingHMADataCollector handleSensingResult:];
-[CWFSensingHMADataCollector initWithAccessory:andOptions:andDelegate:];
-[CWFSensingHMADataCollector registerForPrimaryServiceNotificationWith:];
-[CWFSensingHMADataCollector set_attempt:];
-[CWFSensingHMADataCollector set_sensingParams:];
-[CWFSensingHMADataCollector set_serviceRegistrationError:];
```
