# `AccessoryDetection`

- Image: [`/usr/lib/libBasebandManagerICE.dylib`](../userland/usr__lib__libBasebandManagerICE.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ACCConnectionInfoDelegateProtocol`
- 5 instance variables, 9 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _fAlreadyStarted;
@"ACCConnectionInfo" _fConnectionInfoProvider;
@"NSMutableDictionary" _fAccessoryEndpointList;
@"NSMutableDictionary" _fConnectionInfoFilter;
{AccessoryDetectionCallback="attached"@?"detached"@?} _fCallback;
```

## Properties

```
@property (T@"ACCConnectionInfo",&,V_fConnectionInfoProvider) fConnectionInfoProvider;
@property (T{AccessoryDetectionCallback=@?@?},V_fCallback) fCallback;
@property (T@"NSMutableDictionary",&,V_fAccessoryEndpointList) fAccessoryEndpointList;
@property (T@"NSMutableDictionary",&,V_fConnectionInfoFilter) fConnectionInfoFilter;
@property (TB,V_fAlreadyStarted) fAlreadyStarted;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[AccessoryDetection stop];
-[AccessoryDetection start];
-[AccessoryDetection accessoryEndpointAttached:transportType:protocol:properties:forConnection:];
-[AccessoryDetection accessoryEndpointDetached:forConnection:];
-[AccessoryDetection initWithCallback:];
-[AccessoryDetection fCallback];
-[AccessoryDetection setFCallback:];
-[AccessoryDetection fAlreadyStarted];
-[AccessoryDetection fAccessoryEndpointList];
-[AccessoryDetection fConnectionInfoFilter];
-[AccessoryDetection fConnectionInfoProvider];
-[AccessoryDetection setFAccessoryEndpointList:];
-[AccessoryDetection setFAlreadyStarted:];
-[AccessoryDetection setFConnectionInfoFilter:];
-[AccessoryDetection setFConnectionInfoProvider:];
```
