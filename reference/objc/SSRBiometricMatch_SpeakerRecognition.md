# `SSRBiometricMatch`

- Image: [`/System/Library/PrivateFrameworks/SpeakerRecognition.framework/SpeakerRecognition`](../userland/System__Library__PrivateFrameworks__SpeakerRecognition.framework__SpeakerRecognition.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BKDeviceDelegate`
- 1 instance variables, 5 properties, 5 instance methods, 1 class methods

## Instance variables

```
@"BKDevice" _biometricDevice;
```

## Properties

```
@property (T@"BKDevice",&,N,V_biometricDevice) biometricDevice;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SSRBiometricMatch sharedInstance];
```

## Instance methods

```
-[SSRBiometricMatch init];
-[SSRBiometricMatch biometricDevice];
-[SSRBiometricMatch setBiometricDevice:];
-[SSRBiometricMatch _getLastBiometricMatchEvent:atTime:];
-[SSRBiometricMatch getLastBiometricMatchForVoiceTriggerTimeStamp:];
```
