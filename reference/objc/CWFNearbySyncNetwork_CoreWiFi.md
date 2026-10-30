# `CWFNearbySyncNetwork`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 7 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"CWFNetworkProfile" _knownNetworkProfile;
@"NSString" _password;
@"NSDictionary" _captivePortalCredentials;
@"CWFChannel" _channel;
```

## Properties

```
@property (T@"CWFNetworkProfile",C,D) knownNetworkProfile;
@property (T@"NSString",C,V_password) password;
@property (T@"NSDictionary",C,V_captivePortalCredentials) captivePortalCredentials;
@property (T@"CWFChannel",C,V_channel) channel;
@property (TB,R,D) isNearbySyncable;
@property (TB,R,D) isNearbyRecommendable;
@property (TB,R) isNearbyBrokenBackhaulStateSyncable;
```

## Class methods

```
+[CWFNearbySyncNetwork supportsSecureCoding];
```

## Instance methods

```
-[CWFNearbySyncNetwork setChannel:];
-[CWFNearbySyncNetwork channel];
-[CWFNearbySyncNetwork isNearbyBrokenBackhaulStateSyncable];
-[CWFNearbySyncNetwork isEqualToNearbySyncNetwork:];
-[CWFNearbySyncNetwork externalForm];
-[CWFNearbySyncNetwork knownNetworkProfile];
-[CWFNearbySyncNetwork setKnownNetworkProfile:];
-[CWFNearbySyncNetwork captivePortalCredentials];
-[CWFNearbySyncNetwork initWithExternalForm:];
-[CWFNearbySyncNetwork encodeWithCoder:];
-[CWFNearbySyncNetwork hash];
-[CWFNearbySyncNetwork description];
-[CWFNearbySyncNetwork isNearbySyncable];
-[CWFNearbySyncNetwork initWithCoder:];
-[CWFNearbySyncNetwork setPassword:];
-[CWFNearbySyncNetwork copyWithZone:];
-[CWFNearbySyncNetwork isEqual:];
-[CWFNearbySyncNetwork password];
-[CWFNearbySyncNetwork setCaptivePortalCredentials:];
-[CWFNearbySyncNetwork isNearbyRecommendable];
```
