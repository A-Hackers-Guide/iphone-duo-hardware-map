# `FBApplicationProcess`

- Image: [`/System/Library/PrivateFrameworks/FrontBoard.framework/FrontBoard`](../userland/System__Library__PrivateFrameworks__FrontBoard.framework__FrontBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `FBProcess`
- 4 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"FBProcessCPUStatistics" _cpuStatistics;
B _recordingAudio;
B _nowPlayingWithAudio;
B _connectedToExternalAccessory;
```

## Properties

```
@property (TB,N,GisRecordingAudio,V_recordingAudio) recordingAudio;
@property (TB,N,GisNowPlayingWithAudio,V_nowPlayingWithAudio) nowPlayingWithAudio;
@property (TB,N,GisConnectedToExternalAccessory,V_connectedToExternalAccessory) connectedToExternalAccessory;
@property (Td,R,N) elapsedCPUTime;
```

## Class methods

```
+[FBApplicationProcess _internalDebugEnvironmentVariables];
```

## Instance methods

```
-[FBApplicationProcess setNowPlayingWithAudio:];
-[FBApplicationProcess isRecordingAudio];
-[FBApplicationProcess elapsedCPUTime];
-[FBApplicationProcess setRecordingAudio:];
-[FBApplicationProcess _createBootstrapContext];
-[FBApplicationProcess setConnectedToExternalAccessory:];
-[FBApplicationProcess _finishInit];
-[FBApplicationProcess killForReason:andReport:withDescription:];
-[FBApplicationProcess isApplicationProcess];
-[FBApplicationProcess _bootstrapDidComplete];
-[FBApplicationProcess isNowPlayingWithAudio];
-[FBApplicationProcess isConnectedToExternalAccessory];
-[FBApplicationProcess killForReason:andReport:withDescription:completion:];
```
