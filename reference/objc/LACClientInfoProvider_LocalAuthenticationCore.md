# `LACClientInfoProvider`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `LACClientInfoProviding`
- 0 instance variables, 4 properties, 12 instance methods, 1 class methods

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[LACClientInfoProvider sharedInstance];
```

## Instance methods

```
-[LACClientInfoProvider _infoForClientWithBundleRecord:];
-[LACClientInfoProvider _infoForClientWithApplicationIdentityData:];
-[LACClientInfoProvider _infoForClientWithAuditToken:];
-[LACClientInfoProvider _infoForClientWithAuditTokenData:];
-[LACClientInfoProvider _isNonUiExtensionPointIdentifier:];
-[LACClientInfoProvider applicationIdentityDataForProcessId:];
-[LACClientInfoProvider auditTokenDataForProcessId:];
-[LACClientInfoProvider canCallToDependencies];
-[LACClientInfoProvider infoForXPCClient:];
-[LACClientInfoProvider infoForXPCClient:evaluationOptions:];
-[LACClientInfoProvider processId:toAuditToken:];
-[LACClientInfoProvider processIdForAuditToken:];
```
