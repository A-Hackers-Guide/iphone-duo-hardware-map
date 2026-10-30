# `AVAudioApplication`

- Image: [`/System/Library/PrivateFrameworks/AudioSession.framework/AudioSession`](../userland/System__Library__PrivateFrameworks__AudioSession.framework__AudioSession.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 4 properties, 29 instance methods, 14 class methods

## Instance variables

```
{unique_ptr<caulk::synchronized<avas::client::AVAudioApplicationImpl>, std::default_delete<caulk::synchronized<avas::client::AVAudioApplicationImpl>>>=""{?="__ptr_"^v}} _impl;
B _inputMuted;
```

## Properties

```
@property (TI,R) clientID;
@property (TB,R,N,GisInputMuted,V_inputMuted) inputMuted;
@property (Tq,R) recordPermission;
@property (Tq,R) microphoneInjectionPermission;
```

## Class methods

```
+[AVAudioApplication sharedInstance];
+[AVAudioApplication allowAppToInitiatePlaybackTemporarily:error:];
+[AVAudioApplication appleTVSupportsEnhanceDialogue];
+[AVAudioApplication currentRouteSupportsEnhanceDialogue:];
+[AVAudioApplication getEnhanceDialogueLevel:error:];
+[AVAudioApplication homeAccessorySupportsEnhanceDialogue];
+[AVAudioApplication iosDeviceSupportsEnhanceDialogue];
+[AVAudioApplication muteRunningInputs:];
+[AVAudioApplication requestMicrophoneInjectionPermissionWithCompletionHandler:];
+[AVAudioApplication requestRecordPermissionWithCompletionHandler:];
+[AVAudioApplication setEnhanceDialogueLevel:error:];
+[AVAudioApplication setEnhanceDialoguePreference:error:];
+[AVAudioApplication toggleInputMute:];
+[AVAudioApplication visionosDeviceSupportsEnhanceDialogue];
```

## Instance methods

```
-[AVAudioApplication clientID];
-[AVAudioApplication postNotificationName:userInfo:];
-[AVAudioApplication dealloc];
-[AVAudioApplication initWithSpecification:];
-[AVAudioApplication initDelegateForProcess:processAttribution:];
-[AVAudioApplication initPrivate:];
-[AVAudioApplication initProxyForProcess:];
-[AVAudioApplication isInputMuted];
-[AVAudioApplication microphoneInjectionPermission];
-[AVAudioApplication privateCreateAudioApplicationInServer:];
-[AVAudioApplication privateEnableSystemMute:];
-[AVAudioApplication privateGetAppProperty:];
-[AVAudioApplication privateGetConnection];
-[AVAudioApplication privateGetImplGuard];
-[AVAudioApplication privateGetMXProperty:];
-[AVAudioApplication privateHandlePing];
-[AVAudioApplication privateOptInToStemClickMuting];
-[AVAudioApplication privateRecreateAudioApplicationInServer];
-[AVAudioApplication privateSetAppProperty:value:];
-[AVAudioApplication privateSetAppProperty:value:guard:];
-[AVAudioApplication privateSetMXPropertyOnAllSessions:value:];
-[AVAudioApplication privateUpdateAppProperty:value:context:];
-[AVAudioApplication recordPermission];
-[AVAudioApplication requestRecordPermissionWithCompletionHandler:];
-[AVAudioApplication sessionIDs];
-[AVAudioApplication setInputMuteStateChangeHandler:error:];
-[AVAudioApplication setInputMuted:context:error:];
-[AVAudioApplication setInputMuted:error:];
-[AVAudioApplication stemClickMutingEnabled];
```
