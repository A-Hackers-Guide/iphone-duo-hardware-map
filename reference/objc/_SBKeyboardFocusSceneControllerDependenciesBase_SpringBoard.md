# `_SBKeyboardFocusSceneControllerDependenciesBase`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `_SBKeyboardFocusSceneControllerDependencyProviding`
- 3 instance variables, 13 properties, 10 instance methods, 0 class methods

## Instance variables

```
@"SBWindowScene" _sbWindowScene;
@"BKSHIDEventDeliveryManager" _deliveryManager;
@"<SBKeyboardFocusSceneProviding>" _sceneProvider;
```

## Properties

```
@property (T@"BKSHIDEventDeliveryManager",R,N) deliveryManager;
@property (TB,R,N,GisCoverSheetHostingAnApp) coverSheetHostingAnApp;
@property (TB,R,N,GisPresentingModalBannerInLongLook) presentingModalBannerInLongLook;
@property (TB,R,N,GisShowingSystemModalAlert) showingSystemModalAlert;
@property (T@"<_UIEventDeferringSystemShellBehaviorDelegate>",R,N) eventDeferringSystemShellBehaviorDelegate;
@property (T@"<SBKeyboardFocusSceneProviding>",R,N) sceneProvider;
@property (TB,R,N,GisScreenDim) screenDim;
@property (TB,R,N,GisSiriVisible) siriVisible;
@property (TB,R,N,GisSpotlightVisible) spotlightVisible;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[_SBKeyboardFocusSceneControllerDependenciesBase isSiriVisible];
-[_SBKeyboardFocusSceneControllerDependenciesBase deliveryManager];
-[_SBKeyboardFocusSceneControllerDependenciesBase isSpotlightVisible];
-[_SBKeyboardFocusSceneControllerDependenciesBase isCoverSheetHostingAnApp];
-[_SBKeyboardFocusSceneControllerDependenciesBase eventDeferringSystemShellBehaviorDelegate];
-[_SBKeyboardFocusSceneControllerDependenciesBase initWithScene:deliveryManager:sceneProvider:];
-[_SBKeyboardFocusSceneControllerDependenciesBase isPresentingModalBannerInLongLook];
-[_SBKeyboardFocusSceneControllerDependenciesBase isScreenDim];
-[_SBKeyboardFocusSceneControllerDependenciesBase isShowingSystemModalAlert];
-[_SBKeyboardFocusSceneControllerDependenciesBase sceneProvider];
```
