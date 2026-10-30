# `SBSpotlightDelegateManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SPUIRemoteSearchViewDelegate`, `SBSSpotlightActivationRequestServerDelegate`
- 4 instance variables, 7 properties, 16 instance methods, 1 class methods

## Instance variables

```
@"SBSSpotlightActivationRequestServer" _activationRequestServer;
@"NSMutableDictionary" _delegatesForLevel;
@"SPUISpotlightRemoteViewController" _latestSpotlightRemoteViewController;
@"FBScene" _latestSpotlightScene;
```

## Properties

```
@property (T@"NSMutableDictionary",&,N,V_delegatesForLevel) delegatesForLevel;
@property (T@"SPUISpotlightRemoteViewController",W,N,V_latestSpotlightRemoteViewController) latestSpotlightRemoteViewController;
@property (T@"FBScene",W,N,V_latestSpotlightScene) latestSpotlightScene;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBSpotlightDelegateManager sharedInstance];
```

## Instance methods

```
-[SBSpotlightDelegateManager dismissSearchView];
-[SBSpotlightDelegateManager activeDelegate];
-[SBSpotlightDelegateManager init];
-[SBSpotlightDelegateManager spotlightActivationRequestServerDidRequestSpotlightActivation:];
-[SBSpotlightDelegateManager _modifyDelegatesWithBlock:];
-[SBSpotlightDelegateManager addSpotlightDelegate:forLevel:];
-[SBSpotlightDelegateManager delegatesForLevel];
-[SBSpotlightDelegateManager latestSpotlightRemoteViewController];
-[SBSpotlightDelegateManager latestSpotlightScene];
-[SBSpotlightDelegateManager removeSpotlightDelegate:forLevel:];
-[SBSpotlightDelegateManager searchViewContentAvailabilityDidChange];
-[SBSpotlightDelegateManager searchViewKeyboardPresentationStateDidChange];
-[SBSpotlightDelegateManager setDelegatesForLevel:];
-[SBSpotlightDelegateManager setLatestSpotlightRemoteViewController:];
-[SBSpotlightDelegateManager setLatestSpotlightScene:];
-[SBSpotlightDelegateManager spotlightRemoteViewController:didCreateScene:];
```
