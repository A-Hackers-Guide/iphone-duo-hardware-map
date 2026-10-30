# `WFPrivateAddressConfig`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`
- 3 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
B _carrierBundleBased;
Q _disabledReason;
@"NSString" _ssid;
```

## Properties

```
@property (TQ,N,V_disabledReason) disabledReason;
@property (TB,N,GisCarrierBundleBased,V_carrierBundleBased) carrierBundleBased;
@property (T@"NSString",C,N,V_ssid) ssid;
```

## Instance methods

```
-[WFPrivateAddressConfig ssid];
-[WFPrivateAddressConfig setSsid:];
-[WFPrivateAddressConfig hash];
-[WFPrivateAddressConfig description];
-[WFPrivateAddressConfig copyWithZone:];
-[WFPrivateAddressConfig isEqual:];
-[WFPrivateAddressConfig disabledReason];
-[WFPrivateAddressConfig setDisabledReason:];
-[WFPrivateAddressConfig initWithPrivateAddressConfigDictionary:ssid:];
-[WFPrivateAddressConfig isCarrierBundleBased];
-[WFPrivateAddressConfig setCarrierBundleBased:];
```
