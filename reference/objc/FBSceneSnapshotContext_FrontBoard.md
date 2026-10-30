# `FBSceneSnapshotContext`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneSnapshotConfigurator`, `BSDescriptionProviding`, `FBSceneSnapshotInternalConfiguration`, `FBMutableSceneSnapshotConfiguration`
- 13 instance variables, 18 properties, 29 instance methods, 1 class methods

## Instance variables

```
B _clientAllowsProtectedContent;
B _opaque;
B _alternateLayout;
@"NSString" _sceneID;
@"FBSSceneClientSettings" _clientSettings;
@"BSSettings" _clientExtendedData;
@"FBSSceneSettings" _settings;
@"NSDate" _expirationDate;
@ _userInfo;
q _orientation;
@"NSSet" _layersToExclude;
@"FBSceneLayer" _backgroundLayer;
{CGRect="origin"{CGPoint="x"d"y"d}"size"{CGSize="width"d"height"d}} _frame;
```

## Properties

```
@property (T@"NSString",R,C,N,V_sceneID) sceneID;
@property (T@"FBSSceneClientSettings",C,N,V_clientSettings) clientSettings;
@property (T@"BSSettings",R,C,N,V_clientExtendedData) clientExtendedData;
@property (T@,&,N,V_userInfo) userInfo;
@property (T{CGRect={CGPoint=dd}{CGSize=dd}},N,V_frame) frame;
@property (TB,N,GisOpaque,V_opaque) opaque;
@property (T@"NSSet",C,N,V_layersToExclude) layersToExclude;
@property (T@"FBSceneLayer",C,N,V_backgroundLayer) backgroundLayer;
@property (TB,N,GisAlternateLayout,V_alternateLayout) alternateLayout;
@property (T@"FBSSceneSettings",R,C,N,V_settings) settings;
@property (Td,R,N) scale;
@property (Tq,R,N,V_orientation) orientation;
@property (TB,R,N,V_clientAllowsProtectedContent) clientAllowsProtectedContent;
@property (T@"NSDate",R,N,V_expirationDate) expirationDate;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[FBSceneSnapshotContext contextWithFBSContext:];
```

## Instance methods

```
-[FBSceneSnapshotContext clientExtendedData];
-[FBSceneSnapshotContext sceneID];
-[FBSceneSnapshotContext succinctDescriptionBuilder];
-[FBSceneSnapshotContext expirationDate];
-[FBSceneSnapshotContext settings];
-[FBSceneSnapshotContext backgroundLayer];
-[FBSceneSnapshotContext orientation];
-[FBSceneSnapshotContext userInfo];
-[FBSceneSnapshotContext setOpaque:];
-[FBSceneSnapshotContext isOpaque];
-[FBSceneSnapshotContext setUserInfo:];
-[FBSceneSnapshotContext descriptionWithMultilinePrefix:];
-[FBSceneSnapshotContext succinctDescription];
-[FBSceneSnapshotContext scale];
-[FBSceneSnapshotContext setClientSettings:];
-[FBSceneSnapshotContext applyContext:];
-[FBSceneSnapshotContext setAlternateLayout:];
-[FBSceneSnapshotContext setFrame:];
-[FBSceneSnapshotContext setBackgroundLayer:];
-[FBSceneSnapshotContext description];
-[FBSceneSnapshotContext clientSettings];
-[FBSceneSnapshotContext layersToExclude];
-[FBSceneSnapshotContext setLayersToExclude:];
-[FBSceneSnapshotContext descriptionBuilderWithMultilinePrefix:];
-[FBSceneSnapshotContext frame];
-[FBSceneSnapshotContext initWithFBSContext:];
-[FBSceneSnapshotContext clientAllowsProtectedContent];
-[FBSceneSnapshotContext initWithScene:configurator:];
-[FBSceneSnapshotContext isAlternateLayout];
```
