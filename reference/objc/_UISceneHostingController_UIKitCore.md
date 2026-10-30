# `_UISceneHostingController`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `FBSceneDelegate`, `BSDescriptionStreaming`, `BSInvalidatable`, `_UIRemoteSheet`
- 7 instance variables, 16 properties, 41 instance methods, 2 class methods

## Instance variables

```
{?="hostingForeignScene"I"clientIsReady"b1"invalidated"b1} _flags;
@"_UISceneHostingViewController" _sceneViewController;
@"NSMutableArray" _queuedActions;
B _fencesDisabled;
@"FBScene" _fbScene;
@"_UISceneHostingView" _sceneView;
@"<_UISceneHostingControllerDelegate>" _delegate;
```

## Properties

```
@property (T@"_UISceneHostingActivationStateHostComponent",R,N) activationStateComponent;
@property (T@"<_UISceneIntelligenceSupportHost>",R,N) intelligenceComponent;
@property (T@"<_UISceneInterfaceProtectionHost>",R,N) interfaceProtectionComponent;
@property (T@"<_UISceneHostingSheetPresentationHostProviding>",R,N) _remoteSheetProvider;
@property (T@"_UIViewServiceHostSceneComponent",R,N) _viewServiceComponent;
@property (T@"<_UISceneTouchSharing>",R,N) touchSharing;
@property (T@"_UISceneHostingView",R,N,V_sceneView) sceneView;
@property (T@"UIViewController",R,N) sceneViewController;
@property (T@"<_UISceneHostingControllerDelegate>",W,N,V_delegate) delegate;
@property (T@"<_UISceneHostingActivationControlling>",&,N) activationController;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"_UISheetPresentationControllerConfiguration",&,D,N,S_setSheetConfiguration:) _sheetConfiguration;
@property (TB,D,N,S_setViewClipsToBounds:) _viewClipsToBounds;
```

## Class methods

```
+[_UISceneHostingController initialize];
+[_UISceneHostingController createSceneWithConfiguration:];
```

## Instance methods

```
-[_UISceneHostingController _objc_initiateDealloc];
-[_UISceneHostingController sceneDidDeactivate:withContext:];
-[_UISceneHostingController sceneWillActivate:];
-[_UISceneHostingController sceneDidInvalidate:withContext:];
-[_UISceneHostingController debugDescription];
-[_UISceneHostingController scene:handleActions:];
-[_UISceneHostingController setActivationController:];
-[_UISceneHostingController sceneDidActivate:];
-[_UISceneHostingController sceneViewController];
-[_UISceneHostingController activationController];
-[_UISceneHostingController dealloc];
-[_UISceneHostingController addExtension:];
-[_UISceneHostingController sceneContentStateDidChange:];
-[_UISceneHostingController addExtensions:];
-[_UISceneHostingController sceneView];
-[_UISceneHostingController initWithScene:];
-[_UISceneHostingController succinctDescription];
-[_UISceneHostingController invalidate];
-[_UISceneHostingController setDelegate:];
-[_UISceneHostingController sendAction:];
-[_UISceneHostingController delegate];
-[_UISceneHostingController description];
-[_UISceneHostingController appendDescriptionToStream:];
-[_UISceneHostingController _clientIsReady];
-[_UISceneHostingController _eventDeferringComponent];
-[_UISceneHostingController _initWithScene:sceneIsForeign:];
-[_UISceneHostingController _remoteSheetProvider];
-[_UISceneHostingController _viewServiceComponent];
-[_UISceneHostingController activationStateComponent];
-[_UISceneHostingController componentForExtension:ofClass:];
-[_UISceneHostingController configureScene];
-[_UISceneHostingController contentSizePreferenceProvider];
-[_UISceneHostingController initWithAdvancedConfiguration:];
-[_UISceneHostingController initWithProcessIdentity:sceneSpecification:];
-[_UISceneHostingController intelligenceComponent];
-[_UISceneHostingController interfaceProtectionComponent];
-[_UISceneHostingController invalidateAndExtractScene];
-[_UISceneHostingController keyboardSuppressionController];
-[_UISceneHostingController removeExtension:];
-[_UISceneHostingController removeExtensions:];
-[_UISceneHostingController touchSharing];
```
