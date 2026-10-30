# `WFProxyKeychainOperation`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFOperation`
- 5 instance variables, 5 properties, 13 instance methods, 3 class methods

## Instance variables

```
@"NSString" _password;
q _type;
@"NSString" _host;
@"NSString" _username;
@"NSString" _port;
```

## Properties

```
@property (Tq,V_type) type;
@property (T@"NSString",C,N,V_password) password;
@property (T@"NSString",C,N,V_host) host;
@property (T@"NSString",C,N,V_username) username;
@property (T@"NSString",C,N,V_port) port;
```

## Class methods

```
+[WFProxyKeychainOperation getPasswordOperationForHost:port:username:];
+[WFProxyKeychainOperation removePasswordOperationForHost:port:username:];
+[WFProxyKeychainOperation savePassswordOperationForHost:port:username:password:];
```

## Instance methods

```
-[WFProxyKeychainOperation setHost:];
-[WFProxyKeychainOperation setPort:];
-[WFProxyKeychainOperation start];
-[WFProxyKeychainOperation username];
-[WFProxyKeychainOperation port];
-[WFProxyKeychainOperation setType:];
-[WFProxyKeychainOperation type];
-[WFProxyKeychainOperation setUsername:];
-[WFProxyKeychainOperation setPassword:];
-[WFProxyKeychainOperation password];
-[WFProxyKeychainOperation host];
-[WFProxyKeychainOperation _credentialsForProtectionSpace:];
-[WFProxyKeychainOperation initWithHost:port:username:password:type:];
```
