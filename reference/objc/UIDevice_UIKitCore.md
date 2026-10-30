# `UIDevice`

- Image: [`/System/Library/PrivateFrameworks/UIKitCore.framework/UIKitCore`](../userland/System__Library__PrivateFrameworks__UIKitCore.framework__UIKitCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 20 properties, 62 instance methods, 8 class methods

## Instance variables

```
q _numDeviceOrientationObservers;
f _batteryLevel;
Q _remoteTouchSurfaceType;
B _remoteHasMicrophone;
B _remoteHasMute;
B _remoteSupportsPushToTalk;
{?="batteryMonitoringEnabled"b1"proximityMonitoringEnabled"b1"expectsFaceContactInLandscape"b1"orientation"b3"batteryState"b2"proximityState"b1"hasTouchPadOverride"b1"hasTouchPad"b1"isHardwareKeyboardAvailable"b1} _deviceFlags;
```

## Properties

```
@property (Tq,R,N,G_feedbackSupportLevel) feedbackSupportLevel;
@property (T@"NSString",R,&,N) buildVersion;
@property (TB,R,N) _supportsPencil;
@property (Tf,R,N) _backlightLevel;
@property (TB,R,N,G_isHardwareKeyboardAvailable) _hardwareKeyboardAvailable;
@property (T@"NSString",R,N) name;
@property (T@"NSString",R,N) model;
@property (T@"NSString",R,N) localizedModel;
@property (T@"NSString",R,N) systemName;
@property (T@"NSString",R,N) systemVersion;
@property (Tq,R,N) orientation;
@property (T@"NSUUID",R,N) identifierForVendor;
@property (TB,R,N,GisGeneratingDeviceOrientationNotifications) generatesDeviceOrientationNotifications;
@property (TB,N,GisBatteryMonitoringEnabled) batteryMonitoringEnabled;
@property (Tq,R,N) batteryState;
@property (Tf,R,N) batteryLevel;
@property (TB,N,GisProximityMonitoringEnabled) proximityMonitoringEnabled;
@property (TB,R,N) proximityState;
@property (TB,R,N,GisMultitaskingSupported) multitaskingSupported;
@property (Tq,R,N) userInterfaceIdiom;
```

## Class methods

```
+[UIDevice observeValueForKeyPath:ofObject:change:context:];
+[UIDevice currentDevice];
+[UIDevice invalidateSystemSoundEnablement];
+[UIDevice _hasHomeButton];
+[UIDevice _isLowEnd];
+[UIDevice _isWatch];
+[UIDevice currentDeviceOrientationAllowingAmbiguous:];
+[UIDevice modelSpecificLocalizedStringKeyForKey:];
```

## Instance methods

```
-[UIDevice setOrientation:animated:];
-[UIDevice model];
-[UIDevice setOrientation:];
-[UIDevice playInputClick];
-[UIDevice batteryLevel];
-[UIDevice buildVersion];
-[UIDevice systemVersion];
-[UIDevice init];
-[UIDevice orientation];
-[UIDevice dealloc];
-[UIDevice userInterfaceIdiom];
-[UIDevice _graphicsQuality];
-[UIDevice _backlightLevel];
-[UIDevice setValue:forKey:];
-[UIDevice _playSystemSound:];
-[UIDevice systemName];
-[UIDevice name];
-[UIDevice _enableDeviceOrientationEvents:];
-[UIDevice _supportsPencil];
-[UIDevice _updateSystemSoundActiveStatus:];
-[UIDevice _clearGraphicsQualityOverride];
-[UIDevice _deviceInfoForKey:];
-[UIDevice _feedbackSupportLevel];
-[UIDevice _hardwareKeyboardAvailabilityChanged];
-[UIDevice _hasGraphicsQualityOverride];
-[UIDevice _hasTouchPad];
-[UIDevice _isHardwareKeyboardAvailable];
-[UIDevice _isSystemSoundEnabled];
-[UIDevice _keyboardGraphicsQuality];
-[UIDevice _loadRemoteDeviceInfoIfNeeded];
-[UIDevice _nativeScreenGamut];
-[UIDevice _performShimmedRequestIfPossibleForDeviceOrientation:];
-[UIDevice _playInputDeleteSound];
-[UIDevice _playInputSelectSound];
-[UIDevice _predictionGraphicsQuality];
-[UIDevice _registerForSystemSounds:];
-[UIDevice _remoteHasMicrophoneCapability];
-[UIDevice _remoteTouchSurfaceType];
-[UIDevice _setActiveUserInterfaceIdiom:];
-[UIDevice _setBatteryLevel:];
-[UIDevice _setBatteryState:];
-[UIDevice _setExpectsFaceContactInLandscape:];
-[UIDevice _setGraphicsQualityOverride:];
-[UIDevice _setHasTouchPad:];
-[UIDevice _setProximityState:];
-[UIDevice _supportsDeepColor];
-[UIDevice _supportsForceTouch];
-[UIDevice _supportsPushToTalk];
-[UIDevice _tapticEngine];
-[UIDevice _unregisterForSystemSounds:];
-[UIDevice batteryState];
-[UIDevice beginGeneratingDeviceOrientationNotifications];
-[UIDevice endGeneratingDeviceOrientationNotifications];
-[UIDevice identifierForVendor];
-[UIDevice isBatteryMonitoringEnabled];
-[UIDevice isGeneratingDeviceOrientationNotifications];
-[UIDevice isMultitaskingSupported];
-[UIDevice isProximityMonitoringEnabled];
-[UIDevice localizedModel];
-[UIDevice proximityState];
-[UIDevice setBatteryMonitoringEnabled:];
-[UIDevice setProximityMonitoringEnabled:];
```
