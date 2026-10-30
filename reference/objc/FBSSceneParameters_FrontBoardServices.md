# `FBSSceneParameters`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`, `NSCopying`, `NSMutableCopying`, `BSDescriptionProviding`
- 3 instance variables, 7 properties, 20 instance methods, 1 class methods

## Instance variables

```
@"FBSSceneSettings" _settings;
@"FBSSceneClientSettings" _clientSettings;
@"FBSSceneSpecification" _specification;
```

## Properties

```
@property (T@"FBSSceneSettings",C,N,V_settings) settings;
@property (T@"FBSSceneClientSettings",C,N,V_clientSettings) clientSettings;
@property (T@"FBSSceneSpecification",R,C,N,V_specification) specification;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSSceneParameters parametersForSpecification:];
```

## Instance methods

```
-[FBSSceneParameters initWithParameters:];
-[FBSSceneParameters mutableCopyWithZone:];
-[FBSSceneParameters succinctDescriptionBuilder];
-[FBSSceneParameters setSettings:];
-[FBSSceneParameters init];
-[FBSSceneParameters initWithXPCDictionary:];
-[FBSSceneParameters settings];
-[FBSSceneParameters descriptionWithMultilinePrefix:];
-[FBSSceneParameters succinctDescription];
-[FBSSceneParameters setClientSettings:];
-[FBSSceneParameters encodeWithXPCDictionary:];
-[FBSSceneParameters initWithSpecification:];
-[FBSSceneParameters hash];
-[FBSSceneParameters description];
-[FBSSceneParameters specification];
-[FBSSceneParameters updateSettingsWithBlock:];
-[FBSSceneParameters clientSettings];
-[FBSSceneParameters copyWithZone:];
-[FBSSceneParameters isEqual:];
-[FBSSceneParameters descriptionBuilderWithMultilinePrefix:];
```
