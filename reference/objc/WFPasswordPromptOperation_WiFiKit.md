# `WFPasswordPromptOperation`

- Image: [`/System/Library/PrivateFrameworks/WiFiKit.framework/WiFiKit`](../userland/System__Library__PrivateFrameworks__WiFiKit.framework__WiFiKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `WFUserPromptOperation`
- Protocols: `WFCredentialsProvider`
- 4 instance variables, 5 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSString" password;
^{__SecIdentity=} TLSIdentity;
@"NSString" username;
@"<WFCredentialsProviderContext>" _credentialsProviderContext;
```

## Properties

```
@property (T@"<WFCredentialsProviderContext>",&,N,V_credentialsProviderContext) credentialsProviderContext;
@property (T@"NSString",C,N,Vpassword) password;
@property (T^{__SecIdentity=},R,N,VTLSIdentity) TLSIdentity;
@property (T@"NSString",R,C,N,Vusername) username;
@property (TB,?,R,N) wantsModalPresentation;
```

## Class methods

```
+[WFPasswordPromptOperation passwordPromptOperationWithCredentialsContext:];
```

## Instance methods

```
-[WFPasswordPromptOperation username];
-[WFPasswordPromptOperation setPassword:];
-[WFPasswordPromptOperation password];
-[WFPasswordPromptOperation TLSIdentity];
-[WFPasswordPromptOperation credentialsProviderContext];
-[WFPasswordPromptOperation setCredentialsProviderContext:];
```
