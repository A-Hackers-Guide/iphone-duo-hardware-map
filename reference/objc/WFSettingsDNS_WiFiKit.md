# `WFSettingsDNS`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WFSettingsPersistable`
- 3 instance variables, 7 properties, 10 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _serverAddresses;
@"NSArray" _searchDomains;
@"NSDictionary" _items;
```

## Properties

```
@property (T@"NSArray",&,N,V_serverAddresses) serverAddresses;
@property (T@"NSArray",&,N,V_searchDomains) searchDomains;
@property (T@"NSDictionary",&,N,V_items) items;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[WFSettingsDNS automaticConfig];
```

## Instance methods

```
-[WFSettingsDNS protocol];
-[WFSettingsDNS initWithDictionary:];
-[WFSettingsDNS setItems:];
-[WFSettingsDNS items];
-[WFSettingsDNS description];
-[WFSettingsDNS searchDomains];
-[WFSettingsDNS setSearchDomains:];
-[WFSettingsDNS setServerAddresses:];
-[WFSettingsDNS serverAddresses];
-[WFSettingsDNS initWithServerAddresses:searchDomains:];
```
