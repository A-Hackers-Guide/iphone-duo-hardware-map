# `CWFHotspotClient`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 9 instance variables, 9 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"NSString" _displayName;
@"NSString" _MACAddress;
@"NSString" _productColor;
@"NSString" _productMarketingName;
@"NSString" _productType;
@"NSString" _peerIdentifier;
@"NSNumber" _dataUsageLastBytes;
@"NSNumber" _dataUsageTotalBytes;
@"NSDate" _dataUsageLastUpdated;
```

## Properties

```
@property (T@"NSString",C,N,V_displayName) displayName;
@property (T@"NSString",C,N,V_MACAddress) MACAddress;
@property (T@"NSString",C,N,V_productColor) productColor;
@property (T@"NSString",C,N,V_productMarketingName) productMarketingName;
@property (T@"NSString",C,N,V_productType) productType;
@property (T@"NSString",C,N,V_peerIdentifier) peerIdentifier;
@property (T@"NSNumber",C,N,V_dataUsageLastBytes) dataUsageLastBytes;
@property (T@"NSNumber",C,N,V_dataUsageTotalBytes) dataUsageTotalBytes;
@property (T@"NSDate",C,N,V_dataUsageLastUpdated) dataUsageLastUpdated;
```

## Class methods

```
+[CWFHotspotClient supportsSecureCoding];
```

## Instance methods

```
-[CWFHotspotClient MACAddress];
-[CWFHotspotClient productColor];
-[CWFHotspotClient displayName];
-[CWFHotspotClient peerIdentifier];
-[CWFHotspotClient setDisplayName:];
-[CWFHotspotClient productType];
-[CWFHotspotClient setProductType:];
-[CWFHotspotClient encodeWithCoder:];
-[CWFHotspotClient description];
-[CWFHotspotClient initWithCoder:];
-[CWFHotspotClient setPeerIdentifier:];
-[CWFHotspotClient copyWithZone:];
-[CWFHotspotClient setProductColor:];
-[CWFHotspotClient dataUsageLastBytes];
-[CWFHotspotClient dataUsageLastUpdated];
-[CWFHotspotClient dataUsageTotalBytes];
-[CWFHotspotClient initWithDisplayName:MACAddress:productColor:productMarketingName:productType:peerIdentifier:dataUsageLastBytes:dataUsageTotalBytes:dataUsageLastUpdated:];
-[CWFHotspotClient productMarketingName];
-[CWFHotspotClient setDataUsageLastBytes:];
-[CWFHotspotClient setDataUsageLastUpdated:];
-[CWFHotspotClient setDataUsageTotalBytes:];
-[CWFHotspotClient setMACAddress:];
-[CWFHotspotClient setProductMarketingName:];
```
