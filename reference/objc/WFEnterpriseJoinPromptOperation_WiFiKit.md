# `WFEnterpriseJoinPromptOperation`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFUserPromptOperation`
- Protocols: `WFCredentialsProvider`
- 3 instance variables, 4 properties, 3 instance methods, 1 class methods

## Instance variables

```
@"NSString" password;
@"NSString" username;
^{__SecIdentity=} TLSIdentity;
```

## Properties

```
@property (T^{__SecIdentity=},R,N,VTLSIdentity) TLSIdentity;
@property (T@"NSString",R,C,N,Vusername) username;
@property (T@"NSString",R,C,N,Vpassword) password;
@property (TB,?,R,N) wantsModalPresentation;
```

## Class methods

```
+[WFEnterpriseJoinPromptOperation enterpriseJoinPromptOperationWithDeviceCapability:];
```

## Instance methods

```
-[WFEnterpriseJoinPromptOperation username];
-[WFEnterpriseJoinPromptOperation password];
-[WFEnterpriseJoinPromptOperation TLSIdentity];
```
