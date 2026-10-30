# `_UICompanionContainerSceneClientComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `BSDescriptionStreaming`, `_UISceneAccessoryContainerClient`, `_UICompanionContainerSceneClient`, `FBSSceneObserver`
- 4 instance variables, 8 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"_UICompanionContainerSceneClientSettingsApplicator" _clientSettingsApplicator;
@"<BSInvalidatable>" _stateCaptureToken;
@"NSHashTable" _observers;
@"FBScene" _clientSettingsSourceScene;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"FBSSceneIdentityToken",R,N) accessoryProvidingSceneIdentityToken;
@property (T@"NSArray",R,C,N) availableAttributes;
@property (TB,N,GisRenderingContent) renderingContent;
@property (T@"FBSSceneIdentityToken",R,N) companionProvidingSceneIdentityToken;
```

## Instance methods

```
-[_UICompanionContainerSceneClientComponent debugDescription];
-[_UICompanionContainerSceneClientComponent removeObserver:];
-[_UICompanionContainerSceneClientComponent scene:didUpdateSettings:];
-[_UICompanionContainerSceneClientComponent setScene:];
-[_UICompanionContainerSceneClientComponent dealloc];
-[_UICompanionContainerSceneClientComponent succinctDescription];
-[_UICompanionContainerSceneClientComponent addObserver:];
-[_UICompanionContainerSceneClientComponent invalidate];
-[_UICompanionContainerSceneClientComponent description];
-[_UICompanionContainerSceneClientComponent appendDescriptionToStream:];
-[_UICompanionContainerSceneClientComponent accessoryProvidingSceneIdentityToken];
-[_UICompanionContainerSceneClientComponent availableAttributes];
-[_UICompanionContainerSceneClientComponent companionProvidingSceneIdentityToken];
-[_UICompanionContainerSceneClientComponent isRenderingContent];
-[_UICompanionContainerSceneClientComponent setRenderingContent:];
```
