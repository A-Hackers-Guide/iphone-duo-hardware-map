# `WFSettingsProxy`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `WFSettingsPersistable`
- 10 instance variables, 15 properties, 27 instance methods, 2 class methods

## Instance variables

```
B _customProxy;
B _authenticated;
B _autoConfigured;
B _autoDiscoveryEnabled;
@"NSString" _server;
@"NSString" _port;
@"NSString" _username;
@"NSString" _password;
@"NSString" _autoConfigureURL;
@"NSDictionary" _items;
```

## Properties

```
@property (T@"NSString",C,N,V_server) server;
@property (T@"NSString",C,N,V_port) port;
@property (T@"NSString",C,N,V_username) username;
@property (T@"NSString",C,N,V_autoConfigureURL) autoConfigureURL;
@property (T@"NSDictionary",&,N,V_items) items;
@property (TB,N,V_customProxy) customProxy;
@property (TB,N,V_authenticated) authenticated;
@property (TB,N,V_autoConfigured) autoConfigured;
@property (TB,N,V_autoDiscoveryEnabled) autoDiscoveryEnabled;
@property (T@"NSString",C,N,V_password) password;
@property (TB,R,N,GisAutomatic) automatic;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[WFSettingsProxy defaultProxyConfiguration];
+[WFSettingsProxy offConfig];
```

## Instance methods

```
-[WFSettingsProxy setPort:];
-[WFSettingsProxy setAuthenticated:];
-[WFSettingsProxy protocol];
-[WFSettingsProxy setServer:];
-[WFSettingsProxy isAutomatic];
-[WFSettingsProxy server];
-[WFSettingsProxy initWithDictionary:];
-[WFSettingsProxy setItems:];
-[WFSettingsProxy username];
-[WFSettingsProxy items];
-[WFSettingsProxy port];
-[WFSettingsProxy description];
-[WFSettingsProxy setUsername:];
-[WFSettingsProxy setPassword:];
-[WFSettingsProxy password];
-[WFSettingsProxy authenticated];
-[WFSettingsProxy initDefaultConfig];
-[WFSettingsProxy setCustomProxy:];
-[WFSettingsProxy autoConfigureURL];
-[WFSettingsProxy autoConfigured];
-[WFSettingsProxy autoDiscoveryEnabled];
-[WFSettingsProxy customProxy];
-[WFSettingsProxy initWithAutoConfigureURL:];
-[WFSettingsProxy initWithManualServer:port:username:password:];
-[WFSettingsProxy setAutoConfigureURL:];
-[WFSettingsProxy setAutoConfigured:];
-[WFSettingsProxy setAutoDiscoveryEnabled:];
```
