# `/System/Library/PrivateFrameworks/CentauriDiagnostic.framework/CentauriDiagnostic`

iOS 27.2 dyld shared cache image. Version `129.0.0.0.0`. **[DSC]**

## Linked libraries (7)

- `/System/Library/PrivateFrameworks/Centauri.framework/Centauri`
- `/System/Library/Frameworks/Foundation.framework/Foundation`
- `/usr/lib/libobjc.A.dylib`
- `/usr/lib/libSystem.B.dylib`
- `/System/Library/Frameworks/CoreFoundation.framework/CoreFoundation`
- `/System/Library/Frameworks/IOKit.framework/Versions/A/IOKit`
- `/System/Library/PrivateFrameworks/OSAnalytics.framework/OSAnalytics`

## Objective-C: 5 classes, 0 protocols, 34 methods, 6 properties

### Class pages

Every class and protocol, with its methods: [`CDFAlphaDiagnostics`](../objc/CDFAlphaDiagnostics_CentauriDiagnostic.md), [`CDFBetaDiagnostics`](../objc/CDFBetaDiagnostics_CentauriDiagnostic.md), [`CDFCollectionItem`](../objc/CDFCollectionItem_CentauriDiagnostic.md), [`CDFControlDiagnostics`](../objc/CDFControlDiagnostics_CentauriDiagnostic.md), [`CDFSubsystemDiagnostics`](../objc/CDFSubsystemDiagnostics_CentauriDiagnostic.md)

### Classes

`CDFAlphaDiagnostics`, `CDFBetaDiagnostics`, `CDFCollectionItem`, `CDFControlDiagnostics`, `CDFSubsystemDiagnostics`

### Properties

```
@property (T@"NSString",R,V_name) name;
@property (T@"NSURL",R,V_path) path;
@property (T@"NSDate",R,V_date) date;
@property (T@"NSNumber",R,V_size) size;
@property (TQ,R,V_buildEnv) buildEnv;
@property (TB,R,V_collectCoredumps) collectCoredumps;
```

## Strings (164)

```
Data/com.apple.driver.AppleCentauriControl/CoexFirmwareLogs
crash_moverDisabledSince
q24@?0@\"NSURL\"8@\"NSURL\"16
ClientRequested-%@
B24@?0@\"NSURL\"8@\"NSError\"16
^\\[\\d{4}-\\d{2}-\\d{2}_\\d{2},\\d{2},\\d{2}\\.\\d{6}\\]-CentauriCoexLogs-\\d{3}\\.pcapng(\\.gz)?(\\.synced)?$
Data/com.apple.driver.AppleCentauriManager/DriverLogs
Data/com.apple.driver.AppleCentauriControl/DebugDriverLogs
WL
Data/com.apple.driver.AppleCentauriControl/DriverLogs
Data/com.apple.driver.AppleCentauriControl/StateSnapshots
^\\[\\d{4}-\\d{2}-\\d{2}_\\d{2},\\d{2},\\d{2}\\.\\d{6}\\]-CentauriAlphaLogs-\\d{3}\\.txt\\.gz(\\.synced)?$
^\\[\\d{4}-\\d{2}-\\d{2}_\\d{2},\\d{2},\\d{2}\\.\\d{6}\\]-AppleWLAN_Datapath-\\d{3}\\.pcapng(\\.gz)?(\\.synced)?$
^\\[\\d{4}-\\d{2}-\\d{2}_\\d{2},\\d{2},\\d{2}\\.\\d{6}\\]-io80211Family-\\d{3}\\.pcapng(\\.gz)?(\\.synced)?$
Data/com.apple.driver.AppleCentauriAlpha/DriverLogs
Data/com.apple.driver.AppleCentauriAlpha/StateSnapshots
sysdiagnose
^\\[\\d{4}-\\d{2}-\\d{2}_\\d{2},\\d{2},\\d{2}\\.\\d{6}\\]-CentauriBetaLogs-\\d{3}\\.txt\\.gz(\\.synced)?$
^\\[\\d{4}-\\d{2}-\\d{2}_\\d{2},\\d{2},\\d{2}\\.\\d{6}\\]-CentauriAlphaFwLogsHp-\\d{3}\\.pcapng(\\.gz)?(\\.synced)?$
Data/com.apple.WLAN.driver/DatapathEvents
^(COEX\\.rta\\.bin|WFL2G\\.(dmem|imem|aslr|recipeoverride|recipeoverridesram|regdump|rtmem|txscr)\\.bin|WFL5G\\.(dmem|imem|aslr|recipeoverride|recipeoverridesram|regdump|rtmem|txscr)\\.bin|WFMAIN\\.(dtcm|itcm|aslr|regdump|socram|sram|memswa
+[CDFSubsystemDiagnostics createSubsystemDirectoryStructure:outputDir:subDirectoryList:]
CDFSubsystemDiagnostics.m
^(system|capture)\\.plist(\\.synced)?$
^\\[\\d{4}-\\d{2}-\\d{2}_\\d{2},\\d{2},\\d{2}\\.\\d{6}\\]-CentauriBetaDebugLogs-\\d{3}\\.txt\\.gz(\\.synced)?$
Data/com.apple.driver.AppleCentauriBeta/DriverLogs
Data/com.apple.WLAN.driver/defaultTextLog
Data/com.apple.WLAN.driver/ControlEvents
Data/com.apple.iokit.IO80211Family/IO80211P2PPeerManager
-[CDFAlphaDiagnostics collectLogsFrom:to:runtimeFlags:]
-[CDFSubsystemDiagnostics collectStateSnapshotsFrom:to:runtimeFlags:]
Data/com.apple.driver.AppleCentauriAlpha/AlphaFirmwareLogs
^\\[\\d{4}-\\d{2}-\\d{2}_\\d{2},\\d{2},\\d{2}\\.\\d{6}\\]-CentauriManagerLogs-\\d{3}\\.txt\\.gz(\\.synced)?$
^\\[\\d{4}-\\d{2}-\\d{2}_\\d{2},\\d{2},\\d{2}\\.\\d{6}\\]-CentauriControlDebugLogs-\\d{3}\\.txt\\.gz(\\.synced)?$
^\\[\\d{4}-\\d{2}-\\d{2}_\\d{2},\\d{2},\\d{2}\\.\\d{6}\\]-AppleWLAN_TextLogs-\\d{3}\\.txt(\\.gz)?(\\.synced)?$
matchingDict
detected
not detected
MultiFunctionManager
Data/com.apple.driver.AppleCentauriBeta/BetaFirmwareLogs
AutoBugCapture
WiFiDebug~ttr
Metadata
Data/com.apple.driver.AppleCentauriBeta/StateSnapshots
^(COEX\\.rta\\.bin|BT2G\\.(dmem|imem|aslr)\\.bin|BT5G\\.(dmem|imem|aslr)\\.bin|BTLPS\\.(dmem|imem|aslr|regdump)\\.bin|BTMAIN\\.(apiram|dtcm|itcm|memswapptt|aslr|regdump|sram)\\.bin|BTSEC\\.(dtcm|itcm|aslr|regdump)\\.bin|MemSwapWorkingCopy\\
^(CentauriConfigAccessLog|CentauriEventLog|CentauriMSILog|CentauriPowerStateLog|CentauriStateDump|CentauriChipInfo)\\.txt(\\.synced)?$
WiFi
EnhancedDiagnostics
/private/var/dextcores
getTotalSizeForPath_block_invoke
getTotalSizeForPath
-[CDFAlphaDiagnostics collectStateSnapshotsFrom:to:runtimeFlags:]
-[CDFSubsystemDiagnostics init]
+[CDFSubsystemDiagnostics collectFilesWithRegex:from:to:]
/Library/Logs/CoreCapture
BT
^\\[\\d{4}-\\d{2}-\\d{2}_\\d{2},\\d{2},\\d{2}\\.\\d{6}\\]-CentauriBetaFwLogs-\\d{3}\\.pcapng(\\.gz)?(\\.synced)?$
^\\[\\d{4}-\\d{2}-\\d{2}_\\d{2},\\d{2},\\d{2}\\.\\d{6}\\]-AppleWLAN_Control-\\d{3}\\.pcapng(\\.gz)?(\\.synced)?$
+[CDFSubsystemDiagnostics isCentauriPlatform]
[Fatal]
MF
collectFoldersForSubsystem
BluetoothDebug~AMFM~sysdiag
collectDextCoresWithMaxCount
^(AppleCentauriManagerStateDump|CentauriMemoryAccessLog)\\.txt(\\.synced)?$
^\\[\\d{4}-\\d{2}-\\d{2}_\\d{2},\\d{2},\\d{2}\\.\\d{6}\\]-LQMLogging-\\d{3}\\.txt(\\.gz)?(\\.synced)?$
^(ap\\d+_(AllPeersVerbose|PrintState)_IO80211PeerManager\\.txt|awdl\\d+_(AllPeersVerbose|PrintState)_IO80211AWDLPeerManager\\.txt|en\\d+_(AllPeersVerbose|PrintState)_IO80211PeerManager\\.txt|nan\\d+_(AllPeersVerbose|PrintState)_IO80211NANPe
TapToRadar
FeedbackAssistant
collectDextCoresWithMaxCount_block_invoke
-[CDFControlDiagnostics collectLogsFrom:to:runtimeFlags:]
StateSnapshots
-[CDFControlDiagnostics collectLPMDebugDataFrom:to:]
-[CDFBetaDiagnostics collectStateSnapshotsFrom:to:runtimeFlags:]
+[CDFSubsystemDiagnostics collectFilesWithRegexes:from:to:mostRecent:]
/Library/Logs/CrashReporter/CoreCapture
collectSubsystemLogsForClient
collectClientLogsWithSizeAndOverride
%@-%@
FLRLimit
^(AddFileList|FaultReportState|History)\\.txt(\\.synced)?$
^(Crashlog\\.CTRL\\.bin|Crashlog\\.WDMAInfo\\.txt)(\\.synced)?$
^(COEX\\.rta\\.bin|CTRL\\.regdump\\.bin|CTRL\\.sram\\.clientport\\.bin|CTRL\\.sram\\.loadport\\.bin|MemSwapWorkingCopy\\.bin|CTRL\\.memswapptt\\.bin)(\\.synced)?$
^\\[\\d{4}-\\d{2}-\\d{2}_\\d{2},\\d{2},\\d{2}\\.\\d{6}\\]-CentauriAlphaFwLogs-\\d{3}\\.pcapng(\\.gz)?(\\.synced)?$
^(AirshipStateDump)\\.bin(\\.synced)?$
%s-triggered
getfilteredURLsForClient
^(COEX\\.rta\\.bin|BT2G\\.(dmem|imem|aslr)\\.bin|BT5G\\.(dmem|imem|aslr)\\.bin|BTLPS\\.(dmem|imem|aslr|regdump)\\.bin|BTMAIN\\.(apiram|dtcm|itcm|memswapptt|aslr|regdump|sram)\\.bin|BTSEC\\.(dtcm|itcm|aslr|regdump)\\.bin)(\\.synced)?$
-[CDFBetaDiagnostics collectLogsFrom:to:runtimeFlags:]
^Crashlog\\.(BT2G|BT5G|BTLPS|BTMAIN|BTS)\\.bin(\\.synced)?$|^Crashlog\\.WDMAInfo\\.txt(\\.synced)?$
-[CDFControlDiagnostics collectStateSnapshotsFrom:to:runtimeFlags:]
AppleCentauriManager
BluetoothDebug~sysdiag
^\\[\\d{4}-\\d{2}-\\d{2}_\\d{2},\\d{2},\\d{2}\\.\\d{6}\\]-CentauriControlLogs-\\d{3}\\.txt\\.gz(\\.synced)?$
in
Data/com.apple.driver.AppleCentauriBeta/DebugDriverLogs
^\\[\\d{4}-\\d{2}-\\d{2}_\\d{2},\\d{2},\\d{2}\\.\\d{6}\\]-CentauriAlphaDebugLogs-\\d{3}\\.txt\\.gz(\\.synced)?$
^Crashlog\\.(WFL2G|WFL5G|WFMAIN|WFP2G|WFP5G|WFRX|WFSC|WFTX)\\.bin(\\.synced)?$|^Crashlog\\.WDMAInfo\\.txt(\\.synced)?$
/var/mobile/Library/Logs/CrashReporter/CoreCapture
getSortedFolderURLsForSubsystem
WiFiDebug~sysdiag
Data/com.apple.driver.AppleCentauriAlpha/DebugDriverLogs
Data/com.apple.iokit.IO80211Family/LQMLogging
Data/com.apple.driver.AppleCentauriAlpha/AlphaFirmwareLogsHp
+[CDFSubsystemDiagnostics collectFileWithRegex:from:to:mostRecent:]
CDF: %s: Warning: potential file drops - copied size %{public}lluMB exceeds client limit %{public}luMB
CDF: %s: Failed to collect logs from %{public}@
CDF: %s: folder size %llu would exceed maximum bytes %{public}llu, currently %{public}llu
CDF: %s: Invalid date, skipping collection %{public}@
CDF: %s: Failed to get %{public}@ contents:error %{public}@
CDF: %s: copying %{public}@ to %{public}@, size %{public}llu date %{public}@
CDF: %s: transfer %{public}scomplete for control coredumps
CDF: %s: Failed to transfer %{public}@ error domain: %{public}@: code:%{public}ld
CDF: %s: transfer %{public}scomplete for %@
CDF: %s: skipping folder with zero size: %{public}@
CDF: %s: failed to create attachment for folder %{public}@
CDF: %s: failed to enumerate directory %{public}@
CDF: %s: transfer %{public}scomplete for control crashlogs
CDF: %s: transfer %{public}scomplete for beta crashlogs
CDF: %s: invalid directory path sourceURL: %{public}@
CDF: %s: invalid name %{public}@ with count %{public}lu
CDF: %s: invalid dir
CDF: %s: transfer %{public}scomplete for control snapshots
CDF: %s: unsupported client %{public}lu
CDF: %s: failed to get Alpha subsystem attachments: %{public}@
CDF: %s: copying to %{public}@, date %{public}@
CDF: %s: Failed to create subdirectories
CDF: %s: invalid src dir
CDF: %s: Failed to create subdirectory %{public}@
CDF: %s: No Connectivity logs found on filesystem for %@
CDF: %s: transfer %{public}scomplete for beta coredumps
CDF: %s: Failed to create regex from pattern %{public}@: %{public}@
CDF: %s: client:%{public}lu, dir:%{public}@, size:%{public}luMB flags:%{public}lu
CDF: %s: Skipping collection of files created before %{public}@
CDF: %s: invalid dest dir
CDF: %s: Failed to get directory contents from %{public}@: %{public}@
CDF: %s: transfer %{public}scomplete for lpm related beta crashlogs
CDF: %s: invalid directory path sourcepath: %{public}@
CDF: %s: failed to get Beta subsystem attachments: %{public}@
CDF: %s: Failed to create diagObg for folder %{public}@
CDF: %s: transfer %{public}scomplete for alpha crashlogs
CDF: %s: Failed to copy %{public}@: %{public}@
CDF: %s: fileURLWithPath:dir failed
CDF: %s: Failed to create path URL for subsystem:%{public}@
CDF: %s: enumerating directory %{public}@
CDF: %s: failed to create attachment for file %{public}@
CDF: %s: transfer %{public}scomplete for alpha coredumps
CDF: %s: transfer %{public}scomplete for alpha snapshots
CDF: %s: invalid arguments client:%{public}lu, dir:%{public}@, size:%{public}luMB flags:%{public}lu
CDF: %s: failed to copy %{public}@: %{public}@
CDF: %s: manager service %{public}s
CDF: %s: Skipping collecting %{public}@ 
CDF: %s: transfer %{public}scomplete for subsystem logs
CDF: %s: invoked by %{public}s
CDF: %s: folder already exists: %{public}@ - abandon copying
CDF: %s: Collected from %{public}@ succesfully
CDF: %s: failed to enumerate file %{public}@: %{public}@
CDF: %s: failed to get Control subsystem attachments: %{public}@
CDF: %s: Failed to copy items to dir %{public}@ %{public}@
CDF: %s: failed to get dext core path %{public}@
CDF: %s: failed to retrieve size for file %{public}@ error: %{public}ld
CDF: %s: invalid directory path destpath: %{public}@
CDF: %s: copying error: %{public}@, from %{public}@ to %{public}@
CDF: %s: buildEnv %{public}lu
```
