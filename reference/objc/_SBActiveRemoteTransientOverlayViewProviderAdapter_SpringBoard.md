# `_SBActiveRemoteTransientOverlayViewProviderAdapter`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBDeviceApplicationRemoteTransientOverlayViewProviding`
- 2 instance variables, 8 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"SBDeviceApplicationRemoteTransientOverlayViewProvider" _viewServiceProvider;
@"SBDeviceApplicationRemoteTransientOverlayViewProvider" _sceneBackedProvider;
```

## Properties

```
@property (T@"SBDeviceApplicationRemoteTransientOverlayViewProvider",W,N,V_viewServiceProvider) viewServiceProvider;
@property (T@"SBDeviceApplicationRemoteTransientOverlayViewProvider",W,N,V_sceneBackedProvider) sceneBackedProvider;
@property (T@"SBWindowScene",R,W,N) windowScene;
@property (T@"FBScene",R,N) containingScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_SBActiveRemoteTransientOverlayViewProviderAdapter windowScene];
-[_SBActiveRemoteTransientOverlayViewProviderAdapter containingScene];
-[_SBActiveRemoteTransientOverlayViewProviderAdapter canHandlePresentationRequest:];
-[_SBActiveRemoteTransientOverlayViewProviderAdapter dismissRemoteTransientOverlayViewController:];
-[_SBActiveRemoteTransientOverlayViewProviderAdapter isPresentingOnBehalfOfApplication:];
-[_SBActiveRemoteTransientOverlayViewProviderAdapter isPresentingOnBehalfOfSceneIdentityTokenString:];
-[_SBActiveRemoteTransientOverlayViewProviderAdapter isPresentingOnBehalfOfScenePersistentIdentifier:];
-[_SBActiveRemoteTransientOverlayViewProviderAdapter isPresentingTransientOverlay:];
-[_SBActiveRemoteTransientOverlayViewProviderAdapter isPresentingTransientOverlayWithSceneIdentityTokenString:];
-[_SBActiveRemoteTransientOverlayViewProviderAdapter presentRemoteTransientOverlayViewController:presentationRequest:];
-[_SBActiveRemoteTransientOverlayViewProviderAdapter sceneBackedProvider];
-[_SBActiveRemoteTransientOverlayViewProviderAdapter setSceneBackedProvider:];
-[_SBActiveRemoteTransientOverlayViewProviderAdapter setViewServiceProvider:];
-[_SBActiveRemoteTransientOverlayViewProviderAdapter viewServiceProvider];
```
