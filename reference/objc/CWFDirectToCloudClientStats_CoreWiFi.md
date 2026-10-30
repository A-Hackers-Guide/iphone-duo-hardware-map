# `CWFDirectToCloudClientStats`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 11 instance methods, 1 class methods

## Instance variables

```
B _iRATRecommendsWiFi;
@"NSString" _bundleID;
@"NSString" _hostName;
```

## Properties

```
@property (T@"NSString",R,C,N,V_bundleID) bundleID;
@property (T@"NSString",R,C,N,V_hostName) hostName;
@property (TB,R,N,V_iRATRecommendsWiFi) iRATRecommendsWiFi;
```

## Class methods

```
+[CWFDirectToCloudClientStats supportsSecureCoding];
```

## Instance methods

```
-[CWFDirectToCloudClientStats hostName];
-[CWFDirectToCloudClientStats encodeWithCoder:];
-[CWFDirectToCloudClientStats hash];
-[CWFDirectToCloudClientStats description];
-[CWFDirectToCloudClientStats initWithCoder:];
-[CWFDirectToCloudClientStats bundleID];
-[CWFDirectToCloudClientStats copyWithZone:];
-[CWFDirectToCloudClientStats isEqual:];
-[CWFDirectToCloudClientStats iRATRecommendsWiFi];
-[CWFDirectToCloudClientStats initWithParams:hostName:iRATWiFiRecommendation:];
-[CWFDirectToCloudClientStats isEqualToDTCStats:];
```
