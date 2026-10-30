# `SBLayoutStateSceneIdentityProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBApplicationSceneIdentityProviding`
- 2 instance variables, 4 properties, 17 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _windowScene;
@"SBApplicationSceneIdentityCreator" _sceneIdentityCreator;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBLayoutStateSceneIdentityProvider sceneIdentityForApplication:uniqueIdentifier:];
-[SBLayoutStateSceneIdentityProvider newSceneIdentityForApplication:];
-[SBLayoutStateSceneIdentityProvider sceneIdentityForApplication:excludingIdentifiers:];
-[SBLayoutStateSceneIdentityProvider sceneIdentityForApplication:];
-[SBLayoutStateSceneIdentityProvider newSceneIdentityForApplication:supportsMultiwindow:];
-[SBLayoutStateSceneIdentityProvider sceneIdentityForApplication:targetContentIdentifier:allowCanMatches:preferNewScene:allowSceneCreation:visibleIdentifiers:preferredDisplay:];
-[SBLayoutStateSceneIdentityProvider initWithWindowScene:applicationController:];
-[SBLayoutStateSceneIdentityProvider newSceneIdentityForBundleIdentifier:uniqueIdentifier:];
-[SBLayoutStateSceneIdentityProvider sceneIdentityForApplication:createPrimaryIfRequired:sceneSessionRole:];
-[SBLayoutStateSceneIdentityProvider sceneIdentityForApplication:targetContentIdentifier:];
-[SBLayoutStateSceneIdentityProvider newSceneIdentityForBundleIdentifier:];
-[SBLayoutStateSceneIdentityProvider sceneIdentityForApplication:uniqueIdentifier:targetContentIdentifier:];
-[SBLayoutStateSceneIdentityProvider sceneIdentityForApplication:targetContentIdentifier:allowCanMatches:preferNewScene:visibleIdentifiers:];
-[SBLayoutStateSceneIdentityProvider newSceneIdentityForBundleIdentifier:supportsMultiwindow:];
-[SBLayoutStateSceneIdentityProvider sceneIdentityForApplication:uniqueIdentifier:targetContentIdentifier:sceneSessionRole:];
-[SBLayoutStateSceneIdentityProvider _identifierForApplication:];
-[SBLayoutStateSceneIdentityProvider _sceneIdentityForApplication:uniqueIdentifier:targetContentIdentifier:allowCanMatches:preferNewScene:allowSceneCreation:visibleIdentifiers:excludingIdentifiers:sceneSessionRole:preferredDisplay:];
```
