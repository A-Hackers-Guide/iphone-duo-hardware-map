# `SBDeviceApplicationRemoteTransientOverlayViewProviding` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 2 properties, 10 instance methods, 0 class methods

## Properties

```
@property (T@"SBWindowScene",R,W,N) windowScene;
@property (T@"FBScene",R,N) containingScene;
```

## Instance methods

```
-[SBDeviceApplicationRemoteTransientOverlayViewProviding windowScene];
-[SBDeviceApplicationRemoteTransientOverlayViewProviding containingScene];
-[SBDeviceApplicationRemoteTransientOverlayViewProviding canHandlePresentationRequest:];
-[SBDeviceApplicationRemoteTransientOverlayViewProviding dismissRemoteTransientOverlayViewController:];
-[SBDeviceApplicationRemoteTransientOverlayViewProviding isPresentingOnBehalfOfApplication:];
-[SBDeviceApplicationRemoteTransientOverlayViewProviding isPresentingOnBehalfOfSceneIdentityTokenString:];
-[SBDeviceApplicationRemoteTransientOverlayViewProviding isPresentingOnBehalfOfScenePersistentIdentifier:];
-[SBDeviceApplicationRemoteTransientOverlayViewProviding isPresentingTransientOverlay:];
-[SBDeviceApplicationRemoteTransientOverlayViewProviding isPresentingTransientOverlayWithSceneIdentityTokenString:];
-[SBDeviceApplicationRemoteTransientOverlayViewProviding presentRemoteTransientOverlayViewController:presentationRequest:];
```
