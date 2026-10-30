# `FBSSceneDefinition`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSMutableCopying`, `BSDescriptionProviding`
- 3 instance variables, 7 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"FBSSceneIdentity" _identity;
@"FBSSceneClientIdentity" _clientIdentity;
@"FBSSceneSpecification" _specification;
```

## Properties

```
@property (T@"FBSSceneIdentity",C,N,V_identity) identity;
@property (T@"FBSSceneClientIdentity",C,N,V_clientIdentity) clientIdentity;
@property (T@"FBSSceneSpecification",C,N,V_specification) specification;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSSceneDefinition definition];
```

## Instance methods

```
-[FBSSceneDefinition mutableCopyWithZone:];
-[FBSSceneDefinition succinctDescriptionBuilder];
-[FBSSceneDefinition descriptionWithMultilinePrefix:];
-[FBSSceneDefinition setIdentity:];
-[FBSSceneDefinition setClientIdentity:];
-[FBSSceneDefinition setSpecification:];
-[FBSSceneDefinition succinctDescription];
-[FBSSceneDefinition isValid];
-[FBSSceneDefinition hash];
-[FBSSceneDefinition identity];
-[FBSSceneDefinition description];
-[FBSSceneDefinition specification];
-[FBSSceneDefinition clientIdentity];
-[FBSSceneDefinition copyWithZone:];
-[FBSSceneDefinition isEqual:];
-[FBSSceneDefinition descriptionBuilderWithMultilinePrefix:];
```
