# `CAMCaptureMovieFileOutput`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `AVCaptureMovieFileOutput`
- Protocols: `AVCaptureFileOutputRecordingDelegatePrivate`
- 7 instance variables, 12 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"CAMCaptureEngine" __captureEngine;
@"NSObject<OS_dispatch_queue>" __userInfoQueue;
@"NSMutableDictionary" __userInfoBySettingsID;
@"NSMutableArray" __removeOnCompletionSettingsIDs;
@"NSDictionary" _currentUserInfo;
@"NSDictionary" _userInfoForNextCapture;
@"<AVCaptureFileOutputRecordingDelegatePrivate>" _wrappedDelegate;
```

## Properties

```
@property (T@"CAMCaptureEngine",R,W,N,V__captureEngine) _captureEngine;
@property (T@"NSObject<OS_dispatch_queue>",R,N,V__userInfoQueue) _userInfoQueue;
@property (T@"NSMutableDictionary",R,N,V__userInfoBySettingsID) _userInfoBySettingsID;
@property (T@"NSMutableArray",R,N,V__removeOnCompletionSettingsIDs) _removeOnCompletionSettingsIDs;
@property (T@"NSDictionary",C,N,V_currentUserInfo) currentUserInfo;
@property (T@"NSDictionary",C,N,V_userInfoForNextCapture) userInfoForNextCapture;
@property (T@"<AVCaptureFileOutputRecordingDelegatePrivate>",W,N,V_wrappedDelegate) wrappedDelegate;
@property (T@"NSDictionary",C,N) userInfo;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[CAMCaptureMovieFileOutput stopRecording];
-[CAMCaptureMovieFileOutput initWithEngine:];
-[CAMCaptureMovieFileOutput wrappedDelegate];
-[CAMCaptureMovieFileOutput _userInfoQueue];
-[CAMCaptureMovieFileOutput userInfo];
-[CAMCaptureMovieFileOutput setUserInfo:];
-[CAMCaptureMovieFileOutput handleNotification:payload:];
-[CAMCaptureMovieFileOutput setCurrentUserInfo:];
-[CAMCaptureMovieFileOutput captureOutput:didFinishRecordingToOutputFileAtURL:fromConnections:error:];
-[CAMCaptureMovieFileOutput captureOutput:didPauseRecordingToOutputFileAtURL:fromConnections:];
-[CAMCaptureMovieFileOutput userInfoForNextCapture];
-[CAMCaptureMovieFileOutput captureOutput:didResumeRecordingToOutputFileAtURL:fromConnections:];
-[CAMCaptureMovieFileOutput _userInfoBySettingsID];
-[CAMCaptureMovieFileOutput setWrappedDelegate:];
-[CAMCaptureMovieFileOutput startRecordingToOutputFileURL:recordingDelegate:];
-[CAMCaptureMovieFileOutput _removeOnCompletionSettingsIDs];
-[CAMCaptureMovieFileOutput _captureEngine];
-[CAMCaptureMovieFileOutput captureOutput:didStartRecordingToOutputFileAtURL:fromConnections:];
-[CAMCaptureMovieFileOutput captureOutput:readyForClientCompositingForOutputFileAtURL:compositingData:];
-[CAMCaptureMovieFileOutput currentUserInfo];
-[CAMCaptureMovieFileOutput setUserInfoForNextCapture:];
```
