# `SBAudioRecordingManager`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 3 properties, 15 instance methods, 0 class methods

## Instance variables

```
@"SBApplicationController" _applicationController;
@"SBApplication" _nowRecordingApplication;
@"SBSBackgroundActivityAssertion" _backgroundActivityAssertion;
@"SBSceneManager" _sceneManager;
```

## Properties

```
@property (T@"SBSBackgroundActivityAssertion",&,N,V_backgroundActivityAssertion) backgroundActivityAssertion;
@property (T@"SBSceneManager",&,N,V_sceneManager) sceneManager;
@property (T@"SBApplication",R,N,V_nowRecordingApplication) nowRecordingApplication;
```

## Instance methods

```
-[SBAudioRecordingManager sceneManager];
-[SBAudioRecordingManager _coverSheetDidPresent:];
-[SBAudioRecordingManager dealloc];
-[SBAudioRecordingManager setSceneManager:];
-[SBAudioRecordingManager setBackgroundActivityAssertion:];
-[SBAudioRecordingManager _callProviderAttributionExistsForAttribution:callDescriptors:];
-[SBAudioRecordingManager _pidForAttribution:];
-[SBAudioRecordingManager _removeBackgroundActivityAssertion];
-[SBAudioRecordingManager _verificationDelayForApplication:];
-[SBAudioRecordingManager _verifyBackgroundAudioActivityForApplication:withDelay:];
-[SBAudioRecordingManager backgroundActivityAssertion];
-[SBAudioRecordingManager initWithSceneManager:applicationController:];
-[SBAudioRecordingManager nowRecordingApplication];
-[SBAudioRecordingManager setNowRecordingAppForActiveAudioRecordingAttributions:callDescriptors:];
-[SBAudioRecordingManager verifyBackgroundAudioActivityForApplication:];
```
