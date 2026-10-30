# `SBIdleTimerDescriptor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `BSDescriptionStreamable`, `NSCopying`
- 8 instance variables, 14 properties, 31 instance methods, 0 class methods

## Instance variables

```
q _timerMode;
d _sampleInterval;
d _warnInterval;
d _totalInterval;
d _quickUnwarnInterval;
@"NSMutableArray" _auditEntries;
@"NSArray" _finalAuditChangeEntry;
d _samplingStartBeforeFirstTimeout;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_auditEntries) auditEntries;
@property (T@"NSArray",&,N,V_finalAuditChangeEntry) finalAuditChangeEntry;
@property (Tq,N,V_timerMode) timerMode;
@property (Td,N,V_sampleInterval) sampleInterval;
@property (Td,N,V_samplingStartBeforeFirstTimeout) samplingStartBeforeFirstTimeout;
@property (Td,N,V_warnInterval) warnInterval;
@property (Td,N,V_quickUnwarnInterval) quickUnwarnInterval;
@property (Td,N,V_totalInterval) totalInterval;
@property (TB,R,N) shouldWarn;
@property (TB,R,N) shouldExpireAfterWarn;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBIdleTimerDescriptor totalInterval];
-[SBIdleTimerDescriptor setQuickUnwarnInterval:];
-[SBIdleTimerDescriptor succinctDescriptionBuilder];
-[SBIdleTimerDescriptor sampleInterval];
-[SBIdleTimerDescriptor appendDescriptionToFormatter:];
-[SBIdleTimerDescriptor setFinalAuditChangeEntry:];
-[SBIdleTimerDescriptor samplingStartBeforeFirstTimeout];
-[SBIdleTimerDescriptor shouldWarn];
-[SBIdleTimerDescriptor setTimerMode:];
-[SBIdleTimerDescriptor addAuditReason:];
-[SBIdleTimerDescriptor descriptionWithMultilinePrefix:];
-[SBIdleTimerDescriptor setWarnInterval:];
-[SBIdleTimerDescriptor setSamplingStartBeforeFirstTimeout:];
-[SBIdleTimerDescriptor succinctDescription];
-[SBIdleTimerDescriptor initWithTimerMode:warnInterval:totalInterval:];
-[SBIdleTimerDescriptor warnInterval];
-[SBIdleTimerDescriptor setSampleInterval:];
-[SBIdleTimerDescriptor setTotalInterval:];
-[SBIdleTimerDescriptor shouldExpireAfterWarn];
-[SBIdleTimerDescriptor hash];
-[SBIdleTimerDescriptor description];
-[SBIdleTimerDescriptor auditEntries];
-[SBIdleTimerDescriptor logAuditReasons:];
-[SBIdleTimerDescriptor auditReasonsForStateCapture];
-[SBIdleTimerDescriptor timerMode];
-[SBIdleTimerDescriptor copyWithZone:];
-[SBIdleTimerDescriptor setAuditEntries:];
-[SBIdleTimerDescriptor isEqual:];
-[SBIdleTimerDescriptor finalAuditChangeEntry];
-[SBIdleTimerDescriptor quickUnwarnInterval];
-[SBIdleTimerDescriptor descriptionBuilderWithMultilinePrefix:];
```
