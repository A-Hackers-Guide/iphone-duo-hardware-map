# `CWFLocalNetworkDevice`

- Image: [`/System/Library/PrivateFrameworks/CoreWiFi.framework/CoreWiFi`](../userland/System__Library__PrivateFrameworks__CoreWiFi.framework__CoreWiFi.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 4 properties, 12 instance methods, 0 class methods

## Instance variables

```
@"NSString" _name;
@"NSSet" _sourceAddresses;
@"NSSet" _serviceNames;
@"NSString" _deviceInfo;
```

## Properties

```
@property (T@"NSSet",C,N,V_sourceAddresses) sourceAddresses;
@property (T@"NSString",C,N,V_deviceInfo) deviceInfo;
@property (T@"NSString",C,N,V_name) name;
@property (T@"NSSet",C,N,V_serviceNames) serviceNames;
```

## Instance methods

```
-[CWFLocalNetworkDevice setDeviceInfo:];
-[CWFLocalNetworkDevice deviceInfo];
-[CWFLocalNetworkDevice hash];
-[CWFLocalNetworkDevice description];
-[CWFLocalNetworkDevice setName:];
-[CWFLocalNetworkDevice name];
-[CWFLocalNetworkDevice serviceNames];
-[CWFLocalNetworkDevice setServiceNames:];
-[CWFLocalNetworkDevice sanitizedName];
-[CWFLocalNetworkDevice sourceAddresses];
-[CWFLocalNetworkDevice preferredSourceAddress];
-[CWFLocalNetworkDevice setSourceAddresses:];
```
