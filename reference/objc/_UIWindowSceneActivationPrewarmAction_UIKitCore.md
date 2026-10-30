# `_UIWindowSceneActivationPrewarmAction`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BSAction`
- 0 instance variables, 8 properties, 10 instance methods, 1 class methods

## Properties

```
@property (TI,R,N) sourceLayerContextId;
@property (TQ,R,N) morphContainerRenderId;
@property (TQ,R,N) deparentingPortalAlphaSourceLayerRenderId;
@property (T@"NSString",R,N) sourceAppBundleIdentifier;
@property (T@"NSString",R,N) sourceSceneIdentifier;
@property (T@"NSString",R,N) interactionIdentifier;
@property (TB,R,N) requestCenterSlot;
@property (TB,R,N) requestFullscreen;
```

## Class methods

```
+[_UIWindowSceneActivationPrewarmAction actionWithMorphContainer:alphaSource:sourceIdentifier:interactionIdentifier:requestCenterSlot:requestFullscreen:responseHandler:];
```

## Instance methods

```
-[_UIWindowSceneActivationPrewarmAction sourceAppBundleIdentifier];
-[_UIWindowSceneActivationPrewarmAction interactionIdentifier];
-[_UIWindowSceneActivationPrewarmAction UIActionType];
-[_UIWindowSceneActivationPrewarmAction abortForUsageViolation:];
-[_UIWindowSceneActivationPrewarmAction requestCenterSlot];
-[_UIWindowSceneActivationPrewarmAction requestFullscreen];
-[_UIWindowSceneActivationPrewarmAction deparentingPortalAlphaSourceLayerRenderId];
-[_UIWindowSceneActivationPrewarmAction morphContainerRenderId];
-[_UIWindowSceneActivationPrewarmAction sourceLayerContextId];
-[_UIWindowSceneActivationPrewarmAction sourceSceneIdentifier];
```
