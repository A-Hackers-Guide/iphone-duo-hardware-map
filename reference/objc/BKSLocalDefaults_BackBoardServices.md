# `BKSLocalDefaults`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BSAbstractDefaultDomain`
- 5 instance variables, 41 properties, 15 instance methods, 0 class methods

## Instance variables

```
B _disableExtendedDisplayByDefault;
B _allowWirelessExtendedDisplay;
B _disableStudyLogAccelerometerLogging;
B _disableStudyLogALSLogging;
B _disableStudyLogGyroLogging;
```

## Properties

```
@property (TB,D,N) ignoreAccelerometerAndOrientationEvents;
@property (TB,D,N,GisALSEnabled) ALSEnabled;
@property (Tq,D,N) ALSEpoch;
@property (T@"NSDictionary",&,D,N) ALSUserPreferences;
@property (Tf,D,N) ALSDelayOnUnlock;
@property (Ti,D,N) brightnessCurve;
@property (TB,D,N,GisDigitizerSignpostsEnabled) digitizerSignpostsEnabled;
@property (TB,D,N) digitizerVisualizeTouches;
@property (TB,D,N) digitizerVisualizeHitTestRegions;
@property (T@"NSArray",D,N) digitizerServicePersistentProperties;
@property (TB,D,N) showBuildNumber;
@property (TB,D,N,GisEventBufferingEnabled) eventBufferingEnabled;
@property (TB,D,N,GisSqueezeForSystemShortcutEnabled) squeezeForSystemShortcutEnabled;
@property (TB,D,N) visualizeMousePointer;
@property (TI,D,N) pointerRegionArrangementEdge;
@property (T@"NSArray",&,D,N) mouseInterpolation;
@property (T@"NSData",&,D,N) globalMouseDevicePreferences;
@property (TB,D,N) logMouseInterpolationDetails;
@property (T@"NSArray",W,D,N) loggingTypesEnabled;
@property (T@"NSString",W,D,N) forceMirroredOrientation;
@property (TB,D,N) hideAppleLogoOnLaunch;
@property (TB,D,N,GisSteveNoteRotationEnabled) steveNoteRotationEnabled;
@property (TB,D,N) disableCloneMirroring;
@property (TB,D,N) disableCAOverscan;
@property (TB,D,N) disableCAYUV;
@property (TB,D,N) disableCAScaling;
@property (TB,D,N,GisSteveNoteOverscanEnabled) steveNoteOverscanEnabled;
@property (TB,D,N) forceCloneMirroring;
@property (TB,N,V_disableExtendedDisplayByDefault) disableExtendedDisplayByDefault;
@property (TB,N,V_allowWirelessExtendedDisplay) allowWirelessExtendedDisplay;
@property (TB,D,N) disableStudyLogBTKeyboardEventLogging;
@property (TB,D,N) disableStudyLogBTKeyboardEventRedirection;
@property (TB,D,N) disableStudyLogVolumeKeyLogging;
@property (TB,D,N) disableStudyLogHomeButtonLogging;
@property (TB,D,N) disableStudyLogButtonLogging;
@property (TB,D,N) disableStudyLogCameraKeyLogging;
@property (TB,D,N) disableStudyLogPowerButtonLogging;
@property (TB,N,V_disableStudyLogAccelerometerLogging) disableStudyLogAccelerometerLogging;
@property (TB,N,V_disableStudyLogALSLogging) disableStudyLogALSLogging;
@property (TB,N,V_disableStudyLogGyroLogging) disableStudyLogGyroLogging;
@property (T@"NSDictionary",&,D,N) keyboardTypeRemap;
```

## Instance methods

```
-[BKSLocalDefaults init];
-[BKSLocalDefaults setValue:forKey:];
-[BKSLocalDefaults disableExtendedDisplayByDefault];
-[BKSLocalDefaults _bindAndRegisterDefaults];
-[BKSLocalDefaults allowWirelessExtendedDisplay];
-[BKSLocalDefaults disableStudyLogALSLogging];
-[BKSLocalDefaults disableStudyLogAccelerometerLogging];
-[BKSLocalDefaults disableStudyLogGyroLogging];
-[BKSLocalDefaults migrateDefaultsIfNecessary];
-[BKSLocalDefaults setAllowWirelessExtendedDisplay:];
-[BKSLocalDefaults setDisableExtendedDisplayByDefault:];
-[BKSLocalDefaults setDisableStudyLogALSLogging:];
-[BKSLocalDefaults setDisableStudyLogAccelerometerLogging:];
-[BKSLocalDefaults setDisableStudyLogGyroLogging:];
-[BKSLocalDefaults valueForKey:defaultValueProvider:];
```
