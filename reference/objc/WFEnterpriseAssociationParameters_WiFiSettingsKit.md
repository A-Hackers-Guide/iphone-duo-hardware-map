# `WFEnterpriseAssociationParameters`

- Image: [`/System/Library/PrivateFrameworks/WiFiSettingsKit.framework/WiFiSettingsKit`](../userland/System__Library__PrivateFrameworks__WiFiSettingsKit.framework__WiFiSettingsKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 5 instance variables, 5 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"NSString" _username;
@"NSString" _password;
^{__SecIdentity=} _TLSIdentity;
@"NSArray" _certificateChain;
@"NSDictionary" _eapTypes;
```

## Properties

```
@property (T@"NSString",&,N,V_username) username;
@property (T@"NSString",&,N,V_password) password;
@property (T^{__SecIdentity=},N,V_TLSIdentity) TLSIdentity;
@property (T@"NSArray",&,N,V_certificateChain) certificateChain;
@property (T@"NSDictionary",&,N,V_eapTypes) eapTypes;
```

## Instance methods

```
-[WFEnterpriseAssociationParameters username];
-[WFEnterpriseAssociationParameters description];
-[WFEnterpriseAssociationParameters setUsername:];
-[WFEnterpriseAssociationParameters setPassword:];
-[WFEnterpriseAssociationParameters password];
-[WFEnterpriseAssociationParameters eapTypes];
-[WFEnterpriseAssociationParameters setEapTypes:];
-[WFEnterpriseAssociationParameters certificateChain];
-[WFEnterpriseAssociationParameters setCertificateChain:];
-[WFEnterpriseAssociationParameters setTLSIdentity:];
-[WFEnterpriseAssociationParameters TLSIdentity];
```
