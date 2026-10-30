# `CSSecureAppHosting` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 4 properties, 7 instance methods, 0 class methods

## Properties

```
@property (T@"SBApplicationSceneHandle",R,N) applicationSceneHandle;
@property (TB,?,N) intentToTransitionFromSecureAppToFull;
@property (TB,?,N,GisTransferringBetweenWindowScenes,SsetTransferringBetweenWindowScenes:) transferringBetweenWindowScenes;
@property (T@"CSCoverSheetViewController",?,W,N) coverSheetViewController;
```

## Instance methods

```
-[CSSecureAppHosting applicationSceneHandle];
-[CSSecureAppHosting coverSheetViewController];
-[CSSecureAppHosting setTransferringBetweenWindowScenes:];
-[CSSecureAppHosting setCoverSheetViewController:];
-[CSSecureAppHosting setIntentToTransitionFromSecureAppToFull:];
-[CSSecureAppHosting isTransferringBetweenWindowScenes];
-[CSSecureAppHosting intentToTransitionFromSecureAppToFull];
```
