# `CATapDescription`

- Image: [`/System/Library/Frameworks/CoreAudio.framework/CoreAudio`](../userland/System__Library__Frameworks__CoreAudio.framework__CoreAudio.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 12 instance variables, 12 properties, 35 instance methods, 0 class methods

## Instance variables

```
B _mono;
B _exclusive;
B _mixdown;
B _privateTap;
B _processRestoreEnabled;
@"NSString" _name;
@"NSUUID" _UUID;
@"NSArray" _processes;
@"NSArray" _bundleIDs;
q _muteBehavior;
@"NSString" _deviceUID;
@"NSNumber" _stream;
```

## Properties

```
@property (T@"NSString",C,V_name) name;
@property (T@"NSUUID",C,V_UUID) UUID;
@property (T@"NSArray",C,V_processes) processes;
@property (T@"NSArray",C,V_bundleIDs) bundleIDs;
@property (TB,GisMono,V_mono) mono;
@property (TB,GisExclusive,V_exclusive) exclusive;
@property (TB,GisMixdown,V_mixdown) mixdown;
@property (TB,GisPrivate,SsetPrivate:,V_privateTap) privateTap;
@property (TB,GisProcessRestoreEnabled,V_processRestoreEnabled) processRestoreEnabled;
@property (Tq,GisMuted,V_muteBehavior) muteBehavior;
@property (T@"NSString",C,V_deviceUID) deviceUID;
@property (T@"NSNumber",C,V_stream) stream;
```

## Instance methods

```
-[CATapDescription isPrivate];
-[CATapDescription bundleIDs];
-[CATapDescription deviceUID];
-[CATapDescription stream];
-[CATapDescription isMuted];
-[CATapDescription processes];
-[CATapDescription initWithDictionary:];
-[CATapDescription init];
-[CATapDescription setUUID:];
-[CATapDescription UUID];
-[CATapDescription setExclusive:];
-[CATapDescription setStream:];
-[CATapDescription isMono];
-[CATapDescription isExclusive];
-[CATapDescription setDeviceUID:];
-[CATapDescription setName:];
-[CATapDescription setMuteBehavior:];
-[CATapDescription setProcesses:];
-[CATapDescription name];
-[CATapDescription setBundleIDs:];
-[CATapDescription setPrivate:];
-[CATapDescription setIsExclusive:];
-[CATapDescription initExcludingProcesses:andDeviceUID:withStream:];
-[CATapDescription initMonoGlobalTapButExcludeProcesses:];
-[CATapDescription initMonoMixdownOfProcesses:];
-[CATapDescription initMonoMixdownOfProcessesIDs:];
-[CATapDescription initStereoGlobalTapButExcludeProcesses:];
-[CATapDescription initStereoMixdownOfProcesses:];
-[CATapDescription initStereoMixdownOfProcessesIDs:];
-[CATapDescription initWithProcesses:andDeviceUID:withStream:];
-[CATapDescription isMixdown];
-[CATapDescription isProcessRestoreEnabled];
-[CATapDescription setMixdown:];
-[CATapDescription setMono:];
-[CATapDescription setProcessRestoreEnabled:];
```
