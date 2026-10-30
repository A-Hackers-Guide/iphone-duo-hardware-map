# `FBSSceneSnapshotContext`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`, `BSDescriptionProviding`
- 8 instance variables, 12 properties, 23 instance methods, 1 class methods

## Instance variables

```
@"NSString" _sceneID;
@"FBSSceneSettings" _settings;
@"NSString" _name;
d _scale;
@"NSSet" _layersToExclude;
d _expirationInterval;
@"BSSettings" _clientExtendedData;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
```

## Properties

```
@property (T@"FBSSceneSettings",C,N,V_settings) settings;
@property (T@"NSString",R,C,N,V_sceneID) sceneID;
@property (T@"NSString",C,N,V_name) name;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_frame) frame;
@property (Td,N,V_scale) scale;
@property (T@"NSSet",C,N,V_layersToExclude) layersToExclude;
@property (Td,N,V_expirationInterval) expirationInterval;
@property (T@"BSSettings",C,N,V_clientExtendedData) clientExtendedData;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSSceneSnapshotContext contextWithSceneID:settings:];
```

## Instance methods

```
-[FBSSceneSnapshotContext clientExtendedData];
-[FBSSceneSnapshotContext expirationInterval];
-[FBSSceneSnapshotContext sceneID];
-[FBSSceneSnapshotContext setClientExtendedData:];
-[FBSSceneSnapshotContext succinctDescriptionBuilder];
-[FBSSceneSnapshotContext setSettings:];
-[FBSSceneSnapshotContext initWithXPCDictionary:];
-[FBSSceneSnapshotContext settings];
-[FBSSceneSnapshotContext setScale:];
-[FBSSceneSnapshotContext descriptionWithMultilinePrefix:];
-[FBSSceneSnapshotContext succinctDescription];
-[FBSSceneSnapshotContext scale];
-[FBSSceneSnapshotContext encodeWithXPCDictionary:];
-[FBSSceneSnapshotContext setExpirationInterval:];
-[FBSSceneSnapshotContext setFrame:];
-[FBSSceneSnapshotContext description];
-[FBSSceneSnapshotContext setName:];
-[FBSSceneSnapshotContext initWithSceneID:settings:];
-[FBSSceneSnapshotContext layersToExclude];
-[FBSSceneSnapshotContext setLayersToExclude:];
-[FBSSceneSnapshotContext name];
-[FBSSceneSnapshotContext descriptionBuilderWithMultilinePrefix:];
-[FBSSceneSnapshotContext frame];
```
