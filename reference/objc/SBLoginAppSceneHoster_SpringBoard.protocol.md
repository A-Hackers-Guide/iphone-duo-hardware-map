# `SBLoginAppSceneHoster` (protocol)

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Protocols: `NSObject`
- 0 instance variables, 6 properties, 11 instance methods, 0 class methods

## Properties

```
@property (T@"<SBLoginAppSceneHosterDelegate>",W,N) delegate;
@property (T@"UIView",R,N) contentView;
@property (T@"NSString",R,N) hostedAppBundleID;
@property (T@"NSString",R,N) hostedSceneIdentifier;
@property (T@"SBApplication",R,N) hostedApp;
@property (TB,N) deferHIDEvents;
```

## Instance methods

```
-[SBLoginAppSceneHoster setDelegate:];
-[SBLoginAppSceneHoster contentView];
-[SBLoginAppSceneHoster delegate];
-[SBLoginAppSceneHoster updateSettingsWithTransitionBlock:];
-[SBLoginAppSceneHoster deferHIDEvents];
-[SBLoginAppSceneHoster hostedApp];
-[SBLoginAppSceneHoster hostedAppBundleID];
-[SBLoginAppSceneHoster hostedSceneIdentifier];
-[SBLoginAppSceneHoster killLoginApp];
-[SBLoginAppSceneHoster launchLoginAppWithInitialOrientation:completion:];
-[SBLoginAppSceneHoster setDeferHIDEvents:];
```
