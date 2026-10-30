# `CBCPMSModule`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBModule`
- Protocols: `CBContainerModuleProtocol`, `CBDisplayModeProtocol`
- 14 instance variables, 10 properties, 21 instance methods, 0 class methods

## Instance variables

```
@"<CBPowerManagementClient>" _cbpm;
@"CBRampManager" _rampManager;
f _minNits;
f _midNits;
f _maxNits;
f _cpmsNitCap;
f _upoCap;
f _cltmCap;
f _currentHDRNits;
B _cpmsFirstBudgetReceived;
B _useModernCPMS;
q _displayMode;
@"NSObject<OS_os_log>" _logHandle;
B _firstBudgetReceived;
```

## Properties

```
@property (Tf,R,N,V_cpmsNitCap) cpmsNitCap;
@property (Tf,R,N,V_upoCap) upoCap;
@property (Tf,R,N,V_cltmCap) cltmCap;
@property (TB,R,N,V_firstBudgetReceived) firstBudgetReceived;
@property (TB,R,N,V_useModernCPMS) useModernCPMS;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (Tq,V_displayMode) displayMode;
```

## Instance methods

```
-[CBCPMSModule copyPropertyForKey:];
-[CBCPMSModule handleDisplayModeUpdate:withDuration:callback:];
-[CBCPMSModule copyStatusInfo];
-[CBCPMSModule setProperty:forKey:];
-[CBCPMSModule setDisplayMode:];
-[CBCPMSModule stop];
-[CBCPMSModule upoCap];
-[CBCPMSModule dealloc];
-[CBCPMSModule displayMode];
-[CBCPMSModule start];
-[CBCPMSModule handleNotificationForKey:withProperty:];
-[CBCPMSModule cltmCap];
-[CBCPMSModule copyPropertyForKey:withParameter:];
-[CBCPMSModule useModernCPMS];
-[CBCPMSModule calculateRampDurationFromStart:toFinish:];
-[CBCPMSModule configureCPMS];
-[CBCPMSModule cpmsNitCap];
-[CBCPMSModule extractIndividualBudgets:];
-[CBCPMSModule firstBudgetReceived];
-[CBCPMSModule handleBudgetUpdate:];
-[CBCPMSModule initWithQueue:powerClient:rampManager:configuration:];
```
