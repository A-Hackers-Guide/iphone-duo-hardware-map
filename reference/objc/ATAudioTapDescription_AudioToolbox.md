# `ATAudioTapDescription`

- Image: [`/System/Library/Frameworks/AudioToolbox.framework/AudioToolbox`](../userland/System__Library__Frameworks__AudioToolbox.framework__AudioToolbox.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 11 instance variables, 12 properties, 35 instance methods, 1 class methods

## Instance variables

```
B _preSpatial;
I _audioSessionID;
I _sessionType;
q _tapType;
@"NSArray" _processIdentifiers;
@"NSArray" _excludedPIDs;
@"NSString" _name;
@"NSUUID" _UUID;
@"AVAudioFormat" _format;
@"NSString" _sceneIdentifier;
q _muteBehavior;
```

## Properties

```
@property (Tq,R,N,V_tapType) tapType;
@property (Ti,N) processIdentifier;
@property (T@"NSArray",C,N,V_processIdentifiers) processIdentifiers;
@property (T@"NSArray",C,N,V_excludedPIDs) excludedPIDs;
@property (T@"NSString",R,N,V_name) name;
@property (T@"NSUUID",R,N,V_UUID) UUID;
@property (T@"AVAudioFormat",R,N,V_format) format;
@property (TB,R,N,GisPreSpatial,V_preSpatial) preSpatial;
@property (TI,R,N,V_audioSessionID) audioSessionID;
@property (TI,R,N,V_sessionType) sessionType;
@property (T@"NSString",R,N,V_sceneIdentifier) sceneIdentifier;
@property (Tq,N,V_muteBehavior) muteBehavior;
```

## Class methods

```
+[ATAudioTapDescription supportsSecureCoding];
```

## Instance methods

```
-[ATAudioTapDescription initPreSpatialSceneIdentifierTapWithFormat:sceneIdentifier:];
-[ATAudioTapDescription audioSessionID];
-[ATAudioTapDescription initPreSpatialTapInternalWithFormat:PIDs:sessionID:sessionType:sceneID:];
-[ATAudioTapDescription processIdentifiers];
-[ATAudioTapDescription setProcessIdentifier:];
-[ATAudioTapDescription setProcessIdentifiersChecked:];
-[ATAudioTapDescription tapType];
-[ATAudioTapDescription muteBehavior];
-[ATAudioTapDescription UUID];
-[ATAudioTapDescription initSystemTapWithFormat:excludePIDs:];
-[ATAudioTapDescription initSystemTapWithFormat:];
-[ATAudioTapDescription isPreSpatial];
-[ATAudioTapDescription sceneIdentifier];
-[ATAudioTapDescription sessionType];
-[ATAudioTapDescription initPreSpatialSessionTypeTapWithFormat:sessionType:];
-[ATAudioTapDescription initPreSpatialProcessTapWithFormat:PIDs:];
-[ATAudioTapDescription encodeWithCoder:];
-[ATAudioTapDescription initPreSpatialProcessTapWithFormat:PID:];
-[ATAudioTapDescription setProcessIdentifiers:];
-[ATAudioTapDescription description];
-[ATAudioTapDescription initProcessTapWithFormat:PID:];
-[ATAudioTapDescription initWithCoder:];
-[ATAudioTapDescription setExcludedPIDs:];
-[ATAudioTapDescription processIdentifier];
-[ATAudioTapDescription initProcessTapWithFormat:PID:deviceUID:];
-[ATAudioTapDescription setMuteBehavior:];
-[ATAudioTapDescription initBaseTapInternalWithFormat:];
-[ATAudioTapDescription isEqual:];
-[ATAudioTapDescription initPreSpatialAudioSessionTapWithFormat:sessionID:];
-[ATAudioTapDescription excludedPIDs];
-[ATAudioTapDescription initProcessTapWithFormat:PIDs:];
-[ATAudioTapDescription format];
-[ATAudioTapDescription name];
-[ATAudioTapDescription initScreenSharingTapWithFormat:];
-[ATAudioTapDescription initTapInternalWithFormat:PIDs:];
```
