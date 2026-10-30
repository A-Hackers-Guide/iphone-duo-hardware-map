# `WFCredentialsProvider` (protocol)

- Image: [`/System/Library/PrivateFrameworks/WiFiKitUI.framework/WiFiKitUI`](../userland/System__Library__PrivateFrameworks__WiFiKitUI.framework__WiFiKitUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `WFNetworkView`
- 0 instance variables, 3 properties, 4 instance methods, 0 class methods

## Properties

```
@property (T^{__SecIdentity=},R,N) TLSIdentity;
@property (T@"NSString",R,C,N) username;
@property (T@"NSString",R,C,N) password;
```

## Instance methods

```
-[WFCredentialsProvider username];
-[WFCredentialsProvider password];
-[WFCredentialsProvider TLSIdentity];
-[WFCredentialsProvider receiveSharedPassword:];
```
