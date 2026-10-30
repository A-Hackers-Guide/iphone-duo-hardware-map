# `FBSSceneSnapshotRequest`

- Image: [`/System/Library/PrivateFrameworks/FrontBoardServices.framework/FrontBoardServices`](../userland/System__Library__PrivateFrameworks__FrontBoardServices.framework__FrontBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSXPCCoding`
- 5 instance variables, 8 properties, 16 instance methods, 0 class methods

## Instance variables

```
B _handled;
B _allowsProtectedContent;
@"<FBSSceneSnapshotRequestDelegate>" _delegate;
@"NSString" _sceneID;
@"FBSSceneSettings" _settings;
```

## Properties

```
@property (T@"NSString",C,N,V_sceneID) sceneID;
@property (T@"<FBSSceneSnapshotRequestDelegate>",W,N,V_delegate) delegate;
@property (T@"FBSSceneSettings",R,C,N,V_settings) settings;
@property (TB,R,N,V_allowsProtectedContent) allowsProtectedContent;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[FBSSceneSnapshotRequest sceneID];
-[FBSSceneSnapshotRequest setSceneID:];
-[FBSSceneSnapshotRequest succinctDescriptionBuilder];
-[FBSSceneSnapshotRequest initWithXPCDictionary:];
-[FBSSceneSnapshotRequest settings];
-[FBSSceneSnapshotRequest initWithSettings:allowsProtectedContent:];
-[FBSSceneSnapshotRequest descriptionWithMultilinePrefix:];
-[FBSSceneSnapshotRequest succinctDescription];
-[FBSSceneSnapshotRequest performSnapshotWithContext:];
-[FBSSceneSnapshotRequest setDelegate:];
-[FBSSceneSnapshotRequest encodeWithXPCDictionary:];
-[FBSSceneSnapshotRequest delegate];
-[FBSSceneSnapshotRequest description];
-[FBSSceneSnapshotRequest allowsProtectedContent];
-[FBSSceneSnapshotRequest initWithSettings:];
-[FBSSceneSnapshotRequest descriptionBuilderWithMultilinePrefix:];
```
