# `CAMNebulaSecondaryState`

- Image: [`/System/Library/PrivateFrameworks/CameraUI.framework/CameraUI`](../userland/System__Library__PrivateFrameworks__CameraUI.framework__CameraUI.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 5 properties, 14 instance methods, 2 class methods

## Instance variables

```
@"NSDate" _stopTime;
q _stopReasons;
@"NSDate" _lastMovieWriteAttemptTime;
q _movieWriteAttemptsCount;
q _failedStateReadAttemptsCount;
```

## Properties

```
@property (T@"NSDate",&,N,V_stopTime) stopTime;
@property (Tq,N,V_stopReasons) stopReasons;
@property (T@"NSDate",R,N,V_lastMovieWriteAttemptTime) lastMovieWriteAttemptTime;
@property (Tq,R,N,V_movieWriteAttemptsCount) movieWriteAttemptsCount;
@property (Tq,N,V_failedStateReadAttemptsCount) failedStateReadAttemptsCount;
```

## Class methods

```
+[CAMNebulaSecondaryState supportsSecureCoding];
+[CAMNebulaSecondaryState secondaryStateWithContentsOfFile:];
```

## Instance methods

```
-[CAMNebulaSecondaryState writeToFile:];
-[CAMNebulaSecondaryState stopTime];
-[CAMNebulaSecondaryState encodeWithCoder:];
-[CAMNebulaSecondaryState description];
-[CAMNebulaSecondaryState initWithCoder:];
-[CAMNebulaSecondaryState setStopTime:];
-[CAMNebulaSecondaryState setStopReasons:];
-[CAMNebulaSecondaryState addStopReasons:stopTime:];
-[CAMNebulaSecondaryState failedStateReadAttemptsCount];
-[CAMNebulaSecondaryState lastMovieWriteAttemptTime];
-[CAMNebulaSecondaryState movieWriteAttemptsCount];
-[CAMNebulaSecondaryState notifyWillAttemptToWriteMovie];
-[CAMNebulaSecondaryState setFailedStateReadAttemptsCount:];
-[CAMNebulaSecondaryState stopReasons];
```
