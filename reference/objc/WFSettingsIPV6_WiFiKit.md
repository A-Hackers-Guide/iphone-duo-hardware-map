# `WFSettingsIPV6`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WFSettingsPersistable`
- 5 instance variables, 9 properties, 14 instance methods, 2 class methods

## Instance variables

```
q _method;
@"NSArray" _addresses;
@"NSArray" _prefixLengths;
@"NSString" _router;
@"NSDictionary" _items;
```

## Properties

```
@property (Tq,N,V_method) method;
@property (T@"NSArray",&,N,V_prefixLengths) prefixLengths;
@property (T@"NSArray",&,N,V_addresses) addresses;
@property (T@"NSString",C,N,V_router) router;
@property (T@"NSDictionary",&,N,V_items) items;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[WFSettingsIPV6 automaticConfig];
+[WFSettingsIPV6 linkLocalConfig];
```

## Instance methods

```
-[WFSettingsIPV6 protocol];
-[WFSettingsIPV6 initWithDictionary:];
-[WFSettingsIPV6 setItems:];
-[WFSettingsIPV6 router];
-[WFSettingsIPV6 items];
-[WFSettingsIPV6 addresses];
-[WFSettingsIPV6 method];
-[WFSettingsIPV6 description];
-[WFSettingsIPV6 setMethod:];
-[WFSettingsIPV6 setAddresses:];
-[WFSettingsIPV6 setRouter:];
-[WFSettingsIPV6 initWithMethod:addresses:prefixLengths:router:];
-[WFSettingsIPV6 prefixLengths];
-[WFSettingsIPV6 setPrefixLengths:];
```
