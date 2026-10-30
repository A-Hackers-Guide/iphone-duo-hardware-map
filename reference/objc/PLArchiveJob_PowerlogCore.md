# `PLArchiveJob`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 5 properties, 23 instance methods, 3 class methods

## Instance variables

```
@"<PLArchiveJobManager>" _manager;
@"PLArchiveEntry" _archiveEntry;
@"PLTimer" _watchdog;
```

## Properties

```
@property (T@"PLTimer",&,V_watchdog) watchdog;
@property (T@"<PLArchiveJobManager>",&,V_manager) manager;
@property (T@"PLArchiveEntry",&,V_archiveEntry) archiveEntry;
@property (Tq,N) stage;
@property (TQ,N) numAttempts;
```

## Class methods

```
+[PLArchiveJob storageQueue];
+[PLArchiveJob recoverSelectorForStage:];
+[PLArchiveJob runSelectorForStage:];
```

## Instance methods

```
-[PLArchiveJob startWatchdog];
-[PLArchiveJob stage];
-[PLArchiveJob setManager:];
-[PLArchiveJob manager];
-[PLArchiveJob watchdog];
-[PLArchiveJob setStage:];
-[PLArchiveJob setWatchdog:];
-[PLArchiveJob recover];
-[PLArchiveJob run];
-[PLArchiveJob setNumAttempts:];
-[PLArchiveJob numAttempts];
-[PLArchiveJob archiveEntry];
-[PLArchiveJob setArchiveEntry:];
-[PLArchiveJob recoverCompress];
-[PLArchiveJob initWithManager:andArchiveEntry:];
-[PLArchiveJob recoverCopy];
-[PLArchiveJob recoverTrim];
-[PLArchiveJob stageCompress];
-[PLArchiveJob stageCopy];
-[PLArchiveJob stageRemove];
-[PLArchiveJob stageStart];
-[PLArchiveJob stageTrim];
-[PLArchiveJob stopWatchdog];
```
