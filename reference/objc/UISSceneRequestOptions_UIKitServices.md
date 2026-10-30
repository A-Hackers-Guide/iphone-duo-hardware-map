# `UISSceneRequestOptions`

- Image: [`/System/Library/PrivateFrameworks/UIKitServices.framework/UIKitServices`](../userland/System__Library__PrivateFrameworks__UIKitServices.framework__UIKitServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSWorkspaceSceneRequestOptions`
- Protocols: `BSXPCSecureCoding`
- 10 instance variables, 14 properties, 23 instance methods, 1 class methods

## Instance variables

```
B _requestFullscreen;
B _requestBackground;
B _preserveLayout;
B _requestQuickLookScene;
B _requestCenterSlot;
@"NSString" _sourceIdentifier;
@"NSSet" _actions;
q _sceneRequestIntent;
@"NSString" _interactionIdentifier;
@"UISScenePlacementConfiguration" _scenePlacementConfiguration;
```

## Properties

```
@property (T@"NSString",C,N,V_sourceIdentifier) sourceIdentifier;
@property (T@"NSString",C,N,V_interactionIdentifier) interactionIdentifier;
@property (T@"NSSet",C,N,V_actions) actions;
@property (Tq,N,V_sceneRequestIntent) sceneRequestIntent;
@property (TB,N,V_requestQuickLookScene) requestQuickLookScene;
@property (T@"UISScenePlacementConfiguration",&,N,V_scenePlacementConfiguration) scenePlacementConfiguration;
@property (TB,N,V_requestFullscreen) requestFullscreen;
@property (TB,N,V_requestBackground) requestBackground;
@property (TB,N,V_preserveLayout) preserveLayout;
@property (TB,N,V_requestCenterSlot) requestCenterSlot;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[UISSceneRequestOptions supportsBSXPCSecureCoding];
```

## Instance methods

```
-[UISSceneRequestOptions interactionIdentifier];
-[UISSceneRequestOptions scenePlacementConfiguration];
-[UISSceneRequestOptions setInteractionIdentifier:];
-[UISSceneRequestOptions setActions:];
-[UISSceneRequestOptions requestBackground];
-[UISSceneRequestOptions preserveLayout];
-[UISSceneRequestOptions setRequestBackground:];
-[UISSceneRequestOptions actions];
-[UISSceneRequestOptions sourceIdentifier];
-[UISSceneRequestOptions requestCenterSlot];
-[UISSceneRequestOptions setSourceIdentifier:];
-[UISSceneRequestOptions setRequestCenterSlot:];
-[UISSceneRequestOptions setScenePlacementConfiguration:];
-[UISSceneRequestOptions requestQuickLookScene];
-[UISSceneRequestOptions setSceneRequestIntent:];
-[UISSceneRequestOptions encodeWithBSXPCCoder:];
-[UISSceneRequestOptions isKindOfClass:];
-[UISSceneRequestOptions initWithBSXPCCoder:];
-[UISSceneRequestOptions setPreserveLayout:];
-[UISSceneRequestOptions requestFullscreen];
-[UISSceneRequestOptions setRequestFullscreen:];
-[UISSceneRequestOptions sceneRequestIntent];
-[UISSceneRequestOptions setRequestQuickLookScene:];
```
