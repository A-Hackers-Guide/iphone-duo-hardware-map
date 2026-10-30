# `BWStillImageCaptureTimeMachineFrameInfo`

- Image: [`/System/Library/PrivateFrameworks/CMCapture.framework/CMCapture`](../userland/System__Library__PrivateFrameworks__CMCapture.framework__CMCapture.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BWStillImageCaptureFrameInfo`
- Protocols: `NSSecureCoding`
- 2 instance variables, 2 properties, 9 instance methods, 2 class methods

## Instance variables

```
i _timeMachineIndex;
B _isNoLongErrorRecoveryFrame;
```

## Properties

```
@property (Ti,R,N,V_timeMachineIndex) timeMachineIndex;
@property (TB,N,V_isNoLongErrorRecoveryFrame) isNoLongErrorRecoveryFrame;
```

## Class methods

```
+[BWStillImageCaptureTimeMachineFrameInfo supportsSecureCoding];
+[BWStillImageCaptureTimeMachineFrameInfo infoWithTimeMachineIndex:mainFlags:sifrFlags:];
```

## Instance methods

```
-[BWStillImageCaptureTimeMachineFrameInfo encodeWithCoder:];
-[BWStillImageCaptureTimeMachineFrameInfo hash];
-[BWStillImageCaptureTimeMachineFrameInfo description];
-[BWStillImageCaptureTimeMachineFrameInfo initWithCoder:];
-[BWStillImageCaptureTimeMachineFrameInfo isEqual:];
-[BWStillImageCaptureTimeMachineFrameInfo initWithTimeMachineIndex:mainFlags:sifrFlags:];
-[BWStillImageCaptureTimeMachineFrameInfo isNoLongErrorRecoveryFrame];
-[BWStillImageCaptureTimeMachineFrameInfo setIsNoLongErrorRecoveryFrame:];
-[BWStillImageCaptureTimeMachineFrameInfo timeMachineIndex];
```
