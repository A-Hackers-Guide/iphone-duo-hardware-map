# `FBSSceneIdentity`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCSecureCoding`, `NSSecureCoding`, `NSCopying`, `NSMutableCopying`
- 3 instance variables, 7 properties, 13 instance methods, 5 class methods

## Instance variables

```
@"NSString" _identifier;
@"NSString" _workspaceIdentifier;
@"NSString" _internalWorkspaceIdentifier;
```

## Properties

```
@property (T@"NSString",R,C,N) internalWorkspaceIdentifier;
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (T@"NSString",R,C,N,V_workspaceIdentifier) workspaceIdentifier;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSSceneIdentity supportsBSXPCSecureCoding];
+[FBSSceneIdentity supportsSecureCoding];
+[FBSSceneIdentity identityForIdentifier:];
+[FBSSceneIdentity identityForIdentifier:workspaceIdentifier:];
+[FBSSceneIdentity identityForIdentifier:workspaceIdentifier:internalWorkspaceIdentifier:];
```

## Instance methods

```
-[FBSSceneIdentity internalWorkspaceIdentifier];
-[FBSSceneIdentity mutableCopyWithZone:];
-[FBSSceneIdentity identifier];
-[FBSSceneIdentity workspaceIdentifier];
-[FBSSceneIdentity encodeWithCoder:];
-[FBSSceneIdentity isValid];
-[FBSSceneIdentity hash];
-[FBSSceneIdentity description];
-[FBSSceneIdentity initWithCoder:];
-[FBSSceneIdentity encodeWithBSXPCCoder:];
-[FBSSceneIdentity initWithBSXPCCoder:];
-[FBSSceneIdentity copyWithZone:];
-[FBSSceneIdentity isEqual:];
```
