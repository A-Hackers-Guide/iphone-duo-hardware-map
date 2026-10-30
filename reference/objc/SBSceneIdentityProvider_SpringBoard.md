# `SBSceneIdentityProvider`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBApplicationSceneIdentityProviding`
- 1 instance variables, 4 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _windowScene;
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
-[SBSceneIdentityProvider sceneIdentityForApplication:uniqueIdentifier:];
-[SBSceneIdentityProvider newSceneIdentityForApplication:];
-[SBSceneIdentityProvider sceneIdentityForApplication:excludingIdentifiers:];
-[SBSceneIdentityProvider sceneIdentityForApplication:];
-[SBSceneIdentityProvider newSceneIdentityForApplication:supportsMultiwindow:];
-[SBSceneIdentityProvider sceneIdentityForApplication:targetContentIdentifier:allowCanMatches:preferNewScene:allowSceneCreation:visibleIdentifiers:preferredDisplay:];
-[SBSceneIdentityProvider newSceneIdentityForBundleIdentifier:uniqueIdentifier:];
-[SBSceneIdentityProvider sceneIdentityForApplication:createPrimaryIfRequired:sceneSessionRole:];
-[SBSceneIdentityProvider sceneIdentityForApplication:targetContentIdentifier:];
-[SBSceneIdentityProvider newSceneIdentityForBundleIdentifier:];
-[SBSceneIdentityProvider initWithWindowScene:];
-[SBSceneIdentityProvider sceneIdentityForApplication:uniqueIdentifier:targetContentIdentifier:];
-[SBSceneIdentityProvider sceneIdentityForApplication:targetContentIdentifier:allowCanMatches:preferNewScene:visibleIdentifiers:];
-[SBSceneIdentityProvider newSceneIdentityForBundleIdentifier:supportsMultiwindow:];
-[SBSceneIdentityProvider sceneIdentityForApplication:uniqueIdentifier:targetContentIdentifier:sceneSessionRole:];
-[SBSceneIdentityProvider _sceneIdentifierForBundleIdentifier:];
```
