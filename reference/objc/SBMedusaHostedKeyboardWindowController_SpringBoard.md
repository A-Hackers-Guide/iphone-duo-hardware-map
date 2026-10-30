# `SBMedusaHostedKeyboardWindowController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneObserver`, `BSInvalidatable`
- 6 instance variables, 6 properties, 16 instance methods, 0 class methods

## Instance variables

```
@"SBApplicationController" _applicationController;
@"NSHashTable" _observers;
@"SBWindowScene" _windowScene;
@"FBSSceneClientSettingsDiffInspector" _keyboardLayersClientSettingsDiffInspector;
B _isUsingMedusaHostedKeyboardWindow;
@"UIWindow" _medusaHostedKeyboardWindow;
```

## Properties

```
@property (T@"UIWindow",R,N,V_medusaHostedKeyboardWindow) medusaHostedKeyboardWindow;
@property (TB,R,N,GisUsingMedusaHostedKeyboardWindow,V_isUsingMedusaHostedKeyboardWindow) isUsingMedusaHostedKeyboardWindow;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBMedusaHostedKeyboardWindowController removeObserver:];
-[SBMedusaHostedKeyboardWindowController dealloc];
-[SBMedusaHostedKeyboardWindowController initWithWindowScene:applicationController:];
-[SBMedusaHostedKeyboardWindowController addObserver:];
-[SBMedusaHostedKeyboardWindowController invalidate];
-[SBMedusaHostedKeyboardWindowController scene:didUpdateClientSettings:];
-[SBMedusaHostedKeyboardWindowController shouldKeyboardBeWindowSizedForHostWithIdentity:];
-[SBMedusaHostedKeyboardWindowController isKeyboardVisibleForSpringBoard];
-[SBMedusaHostedKeyboardWindowController _doObserverCalloutWithBlock:];
-[SBMedusaHostedKeyboardWindowController _keyboardLayersClientSettingsDiffInspector];
-[SBMedusaHostedKeyboardWindowController isUsingMedusaHostedKeyboardWindow];
-[SBMedusaHostedKeyboardWindowController medusaHostedKeyboardWindow];
-[SBMedusaHostedKeyboardWindowController newMedusaHostedKeyboardWindowLevelAssertionWithPriority:windowLevel:];
-[SBMedusaHostedKeyboardWindowController sceneDidCompleteUpdate:];
-[SBMedusaHostedKeyboardWindowController updateMedusaHostedKeyboardWindow];
-[SBMedusaHostedKeyboardWindowController updateMedusaHostedKeyboardWindowForScene:isForeground:];
```
