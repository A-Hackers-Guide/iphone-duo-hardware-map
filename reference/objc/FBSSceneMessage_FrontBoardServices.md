# `FBSSceneMessage`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `BSXPCCoding`, `BSDescriptionProviding`
- 1 instance variables, 5 properties, 12 instance methods, 1 class methods

## Instance variables

```
@"BSMutableKeyedSettings" _payload;
```

## Properties

```
@property (T@"BSMutableKeyedSettings",R,C,N,V_payload) payload;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSSceneMessage message];
```

## Instance methods

```
-[FBSSceneMessage succinctDescriptionBuilder];
-[FBSSceneMessage init];
-[FBSSceneMessage initWithXPCDictionary:];
-[FBSSceneMessage payload];
-[FBSSceneMessage descriptionWithMultilinePrefix:];
-[FBSSceneMessage succinctDescription];
-[FBSSceneMessage _initWithPayload:];
-[FBSSceneMessage encodeWithXPCDictionary:];
-[FBSSceneMessage description];
-[FBSSceneMessage copyWithZone:];
-[FBSSceneMessage fallbackXPCEncodableClass];
-[FBSSceneMessage descriptionBuilderWithMultilinePrefix:];
```
