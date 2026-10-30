# `FBSSceneClientIdentity`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSSceneClientIdentifying`, `NSCopying`, `NSSecureCoding`
- 4 instance variables, 7 properties, 13 instance methods, 7 class methods

## Instance variables

```
@"NSString" _description;
B _local;
B _direct;
@"RBSProcessIdentity" _processIdentity;
```

## Properties

```
@property (TB,R,N,V_direct) targetsClientEndpoint;
@property (TB,R,N,GisLocal,V_local) local;
@property (T@"RBSProcessIdentity",R,C,N,V_processIdentity) processIdentity;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSSceneClientIdentity supportsSecureCoding];
+[FBSSceneClientIdentity identityForBundleID:];
+[FBSSceneClientIdentity identityForManagedEndpointOfProcessIdentity:];
+[FBSSceneClientIdentity identityForProcessIdentity:];
+[FBSSceneClientIdentity defaultIdentityForProcessIdentity:];
+[FBSSceneClientIdentity identityForInjectedEndpointToProcessIdentity:];
+[FBSSceneClientIdentity localIdentity];
```

## Instance methods

```
-[FBSSceneClientIdentity processIdentity];
-[FBSSceneClientIdentity fbs_sceneClientIdentity];
-[FBSSceneClientIdentity bundleIdentifier];
-[FBSSceneClientIdentity isLocal];
-[FBSSceneClientIdentity _initWithLocal:direct:identity:description:];
-[FBSSceneClientIdentity targetsClientEndpoint];
-[FBSSceneClientIdentity encodeWithCoder:];
-[FBSSceneClientIdentity isValid];
-[FBSSceneClientIdentity hash];
-[FBSSceneClientIdentity description];
-[FBSSceneClientIdentity initWithCoder:];
-[FBSSceneClientIdentity copyWithZone:];
-[FBSSceneClientIdentity isEqual:];
```
