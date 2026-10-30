# `SBSwitcherCaptureApplicationActivationWatchdog`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFCaptureApplicationLaunchMonitorDelegate`, `SBSceneHandleObserver`
- 3 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
@"<SBSwitcherCaptureApplicationActivationWatchdogDelegate>" _delegate;
@"NSHashTable" _watchdogEntries;
@"NSSet" _lastEntitiesUpdate;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBSwitcherCaptureApplicationActivationWatchdog sceneHandle:clientConnectedForScene:];
-[SBSwitcherCaptureApplicationActivationWatchdog initWithDelegate:];
-[SBSwitcherCaptureApplicationActivationWatchdog captureApplicationMonitor:hasMetLaunchRequirements:unmetReason:];
-[SBSwitcherCaptureApplicationActivationWatchdog _addEntryForEntity:];
-[SBSwitcherCaptureApplicationActivationWatchdog _beginMonitoringAppRepresentedByEntity:];
-[SBSwitcherCaptureApplicationActivationWatchdog _endMonitoringAppRepresentedByEntity:];
-[SBSwitcherCaptureApplicationActivationWatchdog _entryForEntity:];
-[SBSwitcherCaptureApplicationActivationWatchdog _entryForMonitor:];
-[SBSwitcherCaptureApplicationActivationWatchdog _entryForSceneHandle:];
-[SBSwitcherCaptureApplicationActivationWatchdog _removeEntryForEntity:];
-[SBSwitcherCaptureApplicationActivationWatchdog foregroundWorkspaceEntitiesUpdatedTo:];
```
