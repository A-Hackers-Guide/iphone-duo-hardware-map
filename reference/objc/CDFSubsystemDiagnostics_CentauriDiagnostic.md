# `CDFSubsystemDiagnostics`

- Image: [`/System/Library/PrivateFrameworks/CentauriDiagnostic.framework/CentauriDiagnostic`](../userland/System__Library__PrivateFrameworks__CentauriDiagnostic.framework__CentauriDiagnostic.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 5 instance methods, 6 class methods

## Instance variables

```
B _collectCoredumps;
Q _buildEnv;
```

## Properties

```
@property (TQ,R,V_buildEnv) buildEnv;
@property (TB,R,V_collectCoredumps) collectCoredumps;
```

## Class methods

```
+[CDFSubsystemDiagnostics collectFileWithRegex:from:to:mostRecent:];
+[CDFSubsystemDiagnostics collectFilesWithRegex:from:to:];
+[CDFSubsystemDiagnostics collectFilesWithRegexes:from:to:mostRecent:];
+[CDFSubsystemDiagnostics createSubsystemDirectoryStructure:outputDir:subDirectoryList:];
+[CDFSubsystemDiagnostics isCentauriPlatform];
+[CDFSubsystemDiagnostics isFatalCollection:];
```

## Instance methods

```
-[CDFSubsystemDiagnostics init];
-[CDFSubsystemDiagnostics buildEnv];
-[CDFSubsystemDiagnostics collectCoredumps];
-[CDFSubsystemDiagnostics collectLogsFrom:to:runtimeFlags:];
-[CDFSubsystemDiagnostics collectStateSnapshotsFrom:to:runtimeFlags:];
```
