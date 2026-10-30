# `SBWallpaperServer`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBSServiceFacility`
- 2 instance variables, 1 properties, 29 instance methods, 0 class methods

## Instance variables

```
@"FBServiceClientAuthenticator" _accessAuthenticator;
@"<SBWallpaperServerDelegate>" _delegate;
```

## Properties

```
@property (T@"<SBWallpaperServerDelegate>",W,N,V_delegate) delegate;
```

## Instance methods

```
-[SBWallpaperServer effectiveDelegate];
-[SBWallpaperServer setDelegate:];
-[SBWallpaperServer delegate];
-[SBWallpaperServer noteDidReceiveMessage:withType:fromClient:];
-[SBWallpaperServer _handleFetchWithMultipleRectReturnsWithMessage:type:fromClient:];
-[SBWallpaperServer _clientPermittedToModifyWallpaper:];
-[SBWallpaperServer _contextFromFBSDisplayConfiguration:];
-[SBWallpaperServer _deviceOrientationFromXPCDictionary:];
-[SBWallpaperServer _displayContextFromXPCDictionary:];
-[SBWallpaperServer _handleFetchAdaptiveTimeBoundsForHeightMessage:fromClient:];
-[SBWallpaperServer _handleFetchAdaptiveTimeHeightLimitsMessage:fromClient:];
-[SBWallpaperServer _handleFetchContentCutoutBoundsMessage:fromClient:];
-[SBWallpaperServer _handleFetchDisplayConfigurationMessage:fromClient:];
-[SBWallpaperServer _handleFetchLockScreenSubtitleBoundsMessage:fromClient:];
-[SBWallpaperServer _handleFetchOriginalImageMessage:fromClient:];
-[SBWallpaperServer _handleFetchOriginalVideoURLMessage:fromClient:];
-[SBWallpaperServer _handleFetchPosterSignificantEventsCounterMessage:fromClient:];
-[SBWallpaperServer _handleFetchThumbnailMessage:fromClient:];
-[SBWallpaperServer _handleQuickActionConfigurationRequest:fromClient:];
-[SBWallpaperServer _handleRestoreDefaultWallpaperMessage:fromClient:];
-[SBWallpaperServer _handleSetColorMessage:fromClient:];
-[SBWallpaperServer _handleSetColorNameMessage:fromClient:];
-[SBWallpaperServer _handleSetGradientMessage:fromClient:];
-[SBWallpaperServer _handleSetVideoMessageWithWallpaperMode:fromClient:];
-[SBWallpaperServer _handleTriggerPosterSignificantEventMessage:fromClient:];
-[SBWallpaperServer _wallpaperModeFromXPCDictionary:];
-[SBWallpaperServer _wallpaperVariantFromXPCDictionary:];
-[SBWallpaperServer _xpcObjectIsDictionary:];
-[SBWallpaperServer initWithServiceTarget:accessAuthenticator:];
```
