# `DBSExternalDisplayManager`

- Image: [`/System/Library/PrivateFrameworks/Settings/DisplayAndBrightnessSettings.framework/DisplayAndBrightnessSettings`](../userland/System__Library__PrivateFrameworks__Settings__DisplayAndBrightnessSettings.framework__DisplayAndBrightnessSettings.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBSExternalDisplayServiceObserver`
- 6 instance variables, 18 properties, 44 instance methods, 1 class methods

## Instance variables

```
@"FBSDisplayLayoutMonitor" _layoutMonitor;
@"NSHashTable" _observers;
@"BrightnessSystemClient" _brightnessSystemClient;
@"SBSExternalDisplayService" _displayService;
@"SBSConnectedDisplayInfo" _displayInfo;
{CGSize="width"d"height"d} _nativeDisplaySize;
```

## Properties

```
@property (T@"BrightnessSystemClient",&,N,V_brightnessSystemClient) brightnessSystemClient;
@property (T@"SBSExternalDisplayService",&,N,V_displayService) displayService;
@property (T@"SBSConnectedDisplayInfo",&,N,V_displayInfo) displayInfo;
@property (TB,R,N) externalDisplayAvailable;
@property (TB,R,N) externalDisplayBrightnessAvailable;
@property (TB,R,N) externalDisplayAutoBrightnessAvailable;
@property (T@"NSString",&,N) currentHDRMode;
@property (TB,N) matchContent;
@property (TB,N) limitRefreshRate;
@property (TB,N) adaptiveSyncEnabled;
@property (T@"NSNumber",R,N) externalDisplayBrightness;
@property (TB,N) autoBrightnessEnabled;
@property (TB,N,GisMirroringEnabled) mirroringEnabled;
@property (T{CGSize=dd},R,N,V_nativeDisplaySize) nativeDisplaySize;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[DBSExternalDisplayManager defaultManager];
```

## Instance methods

```
-[DBSExternalDisplayManager isMirroringEnabled];
-[DBSExternalDisplayManager supportedHDRModes];
-[DBSExternalDisplayManager observeValueForKeyPath:ofObject:change:context:];
-[DBSExternalDisplayManager removeObserver:];
-[DBSExternalDisplayManager init];
-[DBSExternalDisplayManager preferredHDRModes];
-[DBSExternalDisplayManager dealloc];
-[DBSExternalDisplayManager setMirroringEnabled:];
-[DBSExternalDisplayManager externalDisplayWillDisconnect:];
-[DBSExternalDisplayManager addObserver:];
-[DBSExternalDisplayManager externalDisplayDidConnect:];
-[DBSExternalDisplayManager matchContent];
-[DBSExternalDisplayManager setMatchContent:];
-[DBSExternalDisplayManager setDisplayInfo:];
-[DBSExternalDisplayManager displayInfo];
-[DBSExternalDisplayManager autoBrightnessEnabled];
-[DBSExternalDisplayManager setAutoBrightnessEnabled:];
-[DBSExternalDisplayManager brightnessSystemClient];
-[DBSExternalDisplayManager setBrightnessSystemClient:];
-[DBSExternalDisplayManager setDisplayService:];
-[DBSExternalDisplayManager mainDisplayName];
-[DBSExternalDisplayManager _isTVOutDisplayUnavailableForChamois];
-[DBSExternalDisplayManager _notifyObserversDidUpdateMirroringEnabledState:];
-[DBSExternalDisplayManager _updateDisplayInfo];
-[DBSExternalDisplayManager adaptiveSyncEnabled];
-[DBSExternalDisplayManager currentHDRMode];
-[DBSExternalDisplayManager deviceSupportsChamoisExternalDisplay];
-[DBSExternalDisplayManager displayService];
-[DBSExternalDisplayManager externalDisplayAutoBrightnessAvailable];
-[DBSExternalDisplayManager externalDisplayAvailable];
-[DBSExternalDisplayManager externalDisplayBrightness];
-[DBSExternalDisplayManager externalDisplayBrightnessAvailable];
-[DBSExternalDisplayManager externalDisplayName];
-[DBSExternalDisplayManager externalDisplaySize];
-[DBSExternalDisplayManager limitRefreshRate];
-[DBSExternalDisplayManager mainDisplayImageWithWidth:];
-[DBSExternalDisplayManager nativeDisplaySize];
-[DBSExternalDisplayManager setAdaptiveSyncEnabled:];
-[DBSExternalDisplayManager setCurrentHDRMode:];
-[DBSExternalDisplayManager setExternalDisplayBrightness:shouldCommit:];
-[DBSExternalDisplayManager setLimitRefreshRate:];
-[DBSExternalDisplayManager supportedHDRModesWithHighRefreshRate];
-[DBSExternalDisplayManager supportedHDRModesWithVRR];
-[DBSExternalDisplayManager updateNativeDisplaySize:];
```
