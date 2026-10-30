# `WFSettingsIPV4`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WFSettingsPersistable`
- 6 instance variables, 10 properties, 16 instance methods, 2 class methods

## Instance variables

```
q _method;
@"NSArray" _addresses;
@"NSArray" _subnetMasks;
@"NSString" _router;
@"NSString" _dhcpClientID;
@"NSDictionary" _items;
```

## Properties

```
@property (Tq,N,V_method) method;
@property (T@"NSArray",&,N,V_addresses) addresses;
@property (T@"NSArray",&,N,V_subnetMasks) subnetMasks;
@property (T@"NSString",C,N,V_router) router;
@property (T@"NSString",C,N,V_dhcpClientID) dhcpClientID;
@property (T@"NSDictionary",&,N,V_items) items;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[WFSettingsIPV4 automaticConfig];
+[WFSettingsIPV4 bootPConfig];
```

## Instance methods

```
-[WFSettingsIPV4 protocol];
-[WFSettingsIPV4 initWithDictionary:];
-[WFSettingsIPV4 setItems:];
-[WFSettingsIPV4 router];
-[WFSettingsIPV4 items];
-[WFSettingsIPV4 addresses];
-[WFSettingsIPV4 method];
-[WFSettingsIPV4 description];
-[WFSettingsIPV4 setMethod:];
-[WFSettingsIPV4 setAddresses:];
-[WFSettingsIPV4 setRouter:];
-[WFSettingsIPV4 subnetMasks];
-[WFSettingsIPV4 setSubnetMasks:];
-[WFSettingsIPV4 dhcpClientID];
-[WFSettingsIPV4 initWithMethod:addresses:subnetMasks:router:dhcpClientID:];
-[WFSettingsIPV4 setDhcpClientID:];
```
