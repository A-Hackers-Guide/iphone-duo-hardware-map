# `CAMUserPreferenceOverrides`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 13 properties, 27 instance methods, 0 class methods

## Instance variables

```
B _isSiriContinuation;
B _shouldOpenControlPanel;
@"NSNumber" _captureMode;
@"NSNumber" _captureDevice;
@"NSNumber" _videoConfiguration;
@"NSNumber" _slomoConfiguration;
@"NSNumber" _cinematicConfiguration;
@"NSNumber" _timeLapseConfiguration;
@"NSNumber" _flashMode;
@"NSNumber" _torchMode;
@"NSNumber" _aspectRatioCrop;
@"NSString" _visualIntelligenceSourceApp;
```

## Properties

```
@property (T@"NSNumber",&,N,V_captureMode) captureMode;
@property (T@"NSNumber",&,N,V_captureDevice) captureDevice;
@property (T@"NSNumber",&,N,V_videoConfiguration) videoConfiguration;
@property (T@"NSNumber",&,N,V_slomoConfiguration) slomoConfiguration;
@property (T@"NSNumber",&,N,V_cinematicConfiguration) cinematicConfiguration;
@property (T@"NSNumber",&,N,V_timeLapseConfiguration) timeLapseConfiguration;
@property (T@"NSNumber",&,N,V_flashMode) flashMode;
@property (T@"NSNumber",&,N,V_torchMode) torchMode;
@property (T@"NSNumber",&,N,V_aspectRatioCrop) aspectRatioCrop;
@property (TB,N,V_isSiriContinuation) isSiriContinuation;
@property (TB,N,V_shouldOpenControlPanel) shouldOpenControlPanel;
@property (T@"NSString",C,N,V_visualIntelligenceSourceApp) visualIntelligenceSourceApp;
@property (TB,R,N) hasOverrides;
```

## Instance methods

```
-[CAMUserPreferenceOverrides setAspectRatioCrop:];
-[CAMUserPreferenceOverrides aspectRatioCrop];
-[CAMUserPreferenceOverrides setCaptureDevice:];
-[CAMUserPreferenceOverrides videoConfiguration];
-[CAMUserPreferenceOverrides captureDevice];
-[CAMUserPreferenceOverrides setTorchMode:];
-[CAMUserPreferenceOverrides setCaptureMode:];
-[CAMUserPreferenceOverrides torchMode];
-[CAMUserPreferenceOverrides timeLapseConfiguration];
-[CAMUserPreferenceOverrides captureMode];
-[CAMUserPreferenceOverrides setFlashMode:];
-[CAMUserPreferenceOverrides slomoConfiguration];
-[CAMUserPreferenceOverrides flashMode];
-[CAMUserPreferenceOverrides cinematicConfiguration];
-[CAMUserPreferenceOverrides setVisualIntelligenceSourceApp:];
-[CAMUserPreferenceOverrides hasOverrides];
-[CAMUserPreferenceOverrides initWithConfigurationURL:];
-[CAMUserPreferenceOverrides initWithShortcutItem:];
-[CAMUserPreferenceOverrides isSiriContinuation];
-[CAMUserPreferenceOverrides setCinematicConfiguration:];
-[CAMUserPreferenceOverrides setIsSiriContinuation:];
-[CAMUserPreferenceOverrides setShouldOpenControlPanel:];
-[CAMUserPreferenceOverrides setSlomoConfiguration:];
-[CAMUserPreferenceOverrides setTimeLapseConfiguration:];
-[CAMUserPreferenceOverrides setVideoConfiguration:];
-[CAMUserPreferenceOverrides shouldOpenControlPanel];
-[CAMUserPreferenceOverrides visualIntelligenceSourceApp];
```
