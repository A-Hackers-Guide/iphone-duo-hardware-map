# `SBVideoOutController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSDisplayObserving`, `SBAVSystemControllerCacheObserver`, `SBDisplayPortObserverDelegate`
- 11 instance variables, 5 properties, 23 instance methods, 0 class methods

## Instance variables

```
@"SBFUserAuthenticationController" _authenticationController;
B _screenSharingViaAVSystemController;
B _screenSharingViaDisplayMonitor;
B _screenSharingSetsBackgroundActivity;
@"NSTimer" _screenSharingBackgroundActivityTimer;
@"NSTimer" _videoOutBackgroundActivityTimer;
@"MRScreenMirroringObserver" _screenMirroringObserver;
@"SBSBackgroundActivityAssertion" _screenSharingBackgroundActivityAssertion;
@"SBSBackgroundActivityAssertion" _videoOutBackgroundActivityAssertion;
@"SBAVSystemControllerCache" _avCache;
@"SBDisplayPortObserver" _displayPortObserver;
```

## Properties

```
@property (TB,R,N,GisScreenSharing) screenSharing;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBVideoOutController _unregisterForNotifications];
-[SBVideoOutController _registerForNotifications];
-[SBVideoOutController initWithAuthenticationController:];
-[SBVideoOutController dealloc];
-[SBVideoOutController _authenticationStateChanged:];
-[SBVideoOutController displayMonitor:willDisconnectIdentity:];
-[SBVideoOutController displayMonitor:didConnectIdentity:withConfiguration:];
-[SBVideoOutController isScreenSharing];
-[SBVideoOutController _updateAVRoutes];
-[SBVideoOutController _notifyThatScreenSharingChanged];
-[SBVideoOutController _displayMonitorHasAConnectedExternalIdentity];
-[SBVideoOutController _main_clearScreenSharingBackgroundActivityAssertion];
-[SBVideoOutController _main_clearVideoOutBackgroundActivityAssertion];
-[SBVideoOutController _main_startVideoOutBackgroundActivityAssertion];
-[SBVideoOutController _main_updateScreenSharingBackgroundActivityAssertion];
-[SBVideoOutController _main_updateScreenSharingBackgroundActivityAssertionSuppressionPreference:];
-[SBVideoOutController _main_updateVideoOutBackgroundActivityAssertion];
-[SBVideoOutController _updateDisplayMonitorState];
-[SBVideoOutController _updateScreenMirroringObserverWithSuppressionPreferenceFromDefaults:];
-[SBVideoOutController cache:didUpdateAirplayDisplayActive:];
-[SBVideoOutController cacheDidRebuildAfterServerDeath:];
-[SBVideoOutController displayPortObserver:connectionStateChanged:];
-[SBVideoOutController updateScreenSharingBackgroundActivityAssertion];
```
