# `PLAccessoryAgent`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLAgent`
- Protocols: `ACCConnectionInfoDelegateProtocol`
- 2 instance variables, 6 properties, 10 instance methods, 4 class methods

## Instance variables

```
@"ACCConnectionInfo" _accConnectionInfo;
@"NSMutableDictionary" _connectedEndpoints;
```

## Properties

```
@property (T@"ACCConnectionInfo",&,V_accConnectionInfo) accConnectionInfo;
@property (T@"NSMutableDictionary",&,V_connectedEndpoints) connectedEndpoints;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[PLAccessoryAgent entryEventPointDefinitions];
+[PLAccessoryAgent load];
+[PLAccessoryAgent defaults];
+[PLAccessoryAgent entryEventPointDefinitionsReceivedPush];
```

## Instance methods

```
-[PLAccessoryAgent accConnectionInfo];
-[PLAccessoryAgent init];
-[PLAccessoryAgent initOperatorDependancies];
-[PLAccessoryAgent accessoryEndpointAttached:transportType:protocol:properties:forConnection:];
-[PLAccessoryAgent accessoryConnectionAttached:type:];
-[PLAccessoryAgent accessoryConnectionDetached:];
-[PLAccessoryAgent setAccConnectionInfo:];
-[PLAccessoryAgent accessoryEndpointDetached:forConnection:];
-[PLAccessoryAgent connectedEndpoints];
-[PLAccessoryAgent setConnectedEndpoints:];
```
