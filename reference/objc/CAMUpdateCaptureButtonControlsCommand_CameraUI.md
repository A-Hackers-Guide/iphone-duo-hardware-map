# `CAMUpdateCaptureButtonControlsCommand`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAMCaptureCommand`
- 5 instance variables, 5 properties, 8 instance methods, 0 class methods

## Instance variables

```
B __recording;
B __depthSuggestionEnabled;
B __styledCaptureAllowed;
q __captureMode;
q __devicePosition;
```

## Properties

```
@property (Tq,R,N,V__captureMode) _captureMode;
@property (Tq,R,N,V__devicePosition) _devicePosition;
@property (TB,R,N,V__recording) _recording;
@property (TB,R,N,V__depthSuggestionEnabled) _depthSuggestionEnabled;
@property (TB,R,N,V__styledCaptureAllowed) _styledCaptureAllowed;
```

## Instance methods

```
-[CAMUpdateCaptureButtonControlsCommand _captureMode];
-[CAMUpdateCaptureButtonControlsCommand _devicePosition];
-[CAMUpdateCaptureButtonControlsCommand executeWithContext:];
-[CAMUpdateCaptureButtonControlsCommand copyWithZone:];
-[CAMUpdateCaptureButtonControlsCommand _styledCaptureAllowed];
-[CAMUpdateCaptureButtonControlsCommand _depthSuggestionEnabled];
-[CAMUpdateCaptureButtonControlsCommand _recording];
-[CAMUpdateCaptureButtonControlsCommand initWithRecording:captureMode:devicePosition:depthSuggestionEnabled:styledCaptureAllowed:];
```
