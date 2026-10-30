# `SBNonInteractivePresentation`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneObserver`, `_UICompanionContainerSceneHostObserver`, `BSDescriptionStreaming`, `BSInvalidatable`
- 7 instance variables, 11 properties, 19 instance methods, 1 class methods

## Instance variables

```
@"FBScene" _nonInteractiveScene;
@"<UIScenePresenter>" _scenePresenter;
@"<SBNonInteractivePresentationObserver>" _observer;
@"<BSInvalidatable>" _stateCaptureAssertion;
B _usesCompanionScenes;
@"FBScene" _appScene;
@"SBNonInteractiveDisplayPreferences" _displayPreferences;
```

## Properties

```
@property (T@"NSString",R,C,N) identifier;
@property (T@"FBScene",R,N,V_appScene) appScene;
@property (T@"UIView",R,N) presentationView;
@property (T@"FBScene",&,N) nonInteractiveScene;
@property (TB,R,N,V_usesCompanionScenes) usesCompanionScenes;
@property (TB,R,N) isActive;
@property (T@"SBNonInteractiveDisplayPreferences",R,N,V_displayPreferences) displayPreferences;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SBNonInteractivePresentation _processIdentityKeyForScene:];
```

## Instance methods

```
-[SBNonInteractivePresentation deactivate];
-[SBNonInteractivePresentation identifier];
-[SBNonInteractivePresentation presentationView];
-[SBNonInteractivePresentation invalidate];
-[SBNonInteractivePresentation activate];
-[SBNonInteractivePresentation hash];
-[SBNonInteractivePresentation description];
-[SBNonInteractivePresentation appendDescriptionToStream:];
-[SBNonInteractivePresentation isActive];
-[SBNonInteractivePresentation isEqual:];
-[SBNonInteractivePresentation _scene:didUpdateClientRenderingContent:];
-[SBNonInteractivePresentation scene:didUpdateClientSettings:];
-[SBNonInteractivePresentation displayPreferences];
-[SBNonInteractivePresentation _updateDisplayPreferences:];
-[SBNonInteractivePresentation appScene];
-[SBNonInteractivePresentation initWithAppScene:usesCompanionScenes:observer:];
-[SBNonInteractivePresentation nonInteractiveScene];
-[SBNonInteractivePresentation setNonInteractiveScene:];
-[SBNonInteractivePresentation usesCompanionScenes];
```
