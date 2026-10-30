# `FBSSceneIdentityToken`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCSecureCoding`, `BSXPCCoding`, `NSSecureCoding`, `NSCopying`
- 6 instance variables, 7 properties, 15 instance methods, 7 class methods

## Instance variables

```
@"BSServiceConnectionEndpoint" _endpoint;
@"RBSProcessIdentity" _target;
@"NSString" _workspace;
@"NSString" _identifier;
@"NSString" _stringRepresentation;
q _host;
```

## Properties

```
@property (T@"BSServiceConnectionEndpoint",R,C,N) hostEndpoint;
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (T@"NSString",R,C,N,V_stringRepresentation) stringRepresentation;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSSceneIdentityToken supportsBSXPCSecureCoding];
+[FBSSceneIdentityToken supportsSecureCoding];
+[FBSSceneIdentityToken tokenWithHostPID:viewServiceSessionIdentifier:];
+[FBSSceneIdentityToken tokenWithHostEndpoint:workspace:identifier:];
+[FBSSceneIdentityToken tokenWithHostVPID:viewServiceSessionIdentifier:];
+[FBSSceneIdentityToken pseudoTokenWithIdentifier:];
+[FBSSceneIdentityToken tokenWithHostVPID:directEndpointTarget:workspace:identifier:];
```

## Instance methods

```
-[FBSSceneIdentityToken debugDescription];
-[FBSSceneIdentityToken identifier];
-[FBSSceneIdentityToken init];
-[FBSSceneIdentityToken initWithXPCDictionary:];
-[FBSSceneIdentityToken encodeWithXPCDictionary:];
-[FBSSceneIdentityToken stringRepresentation];
-[FBSSceneIdentityToken encodeWithCoder:];
-[FBSSceneIdentityToken hash];
-[FBSSceneIdentityToken description];
-[FBSSceneIdentityToken initWithCoder:];
-[FBSSceneIdentityToken encodeWithBSXPCCoder:];
-[FBSSceneIdentityToken initWithBSXPCCoder:];
-[FBSSceneIdentityToken copyWithZone:];
-[FBSSceneIdentityToken isEqual:];
-[FBSSceneIdentityToken hostEndpoint];
```
