# `_UICompanionContainerSceneHostComponent`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSSceneComponent`
- Protocols: `BSDescriptionStreaming`, `_UICompanionContainerSceneHost`, `FBSceneObserver`
- 1 instance variables, 8 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSHashTable" _observers;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"FBSSceneIdentityToken",&,N) companionProvidingSceneIdentityToken;
@property (T@"NSArray",C,N) availableAttributes;
@property (TB,R,N) isClientRenderingContent;
@property (T@"FBSSceneIdentityToken",&,N) accessoryProvidingSceneIdentityToken;
```

## Instance methods

```
-[_UICompanionContainerSceneHostComponent debugDescription];
-[_UICompanionContainerSceneHostComponent removeObserver:];
-[_UICompanionContainerSceneHostComponent succinctDescription];
-[_UICompanionContainerSceneHostComponent addObserver:];
-[_UICompanionContainerSceneHostComponent description];
-[_UICompanionContainerSceneHostComponent appendDescriptionToStream:];
-[_UICompanionContainerSceneHostComponent scene:didUpdateClientSettings:];
-[_UICompanionContainerSceneHostComponent accessoryProvidingSceneIdentityToken];
-[_UICompanionContainerSceneHostComponent availableAttributes];
-[_UICompanionContainerSceneHostComponent companionProvidingSceneIdentityToken];
-[_UICompanionContainerSceneHostComponent isClientRenderingContent];
-[_UICompanionContainerSceneHostComponent setAccessoryProvidingSceneIdentityToken:];
-[_UICompanionContainerSceneHostComponent setAvailableAttributes:];
-[_UICompanionContainerSceneHostComponent setCompanionProvidingSceneIdentityToken:];
```
