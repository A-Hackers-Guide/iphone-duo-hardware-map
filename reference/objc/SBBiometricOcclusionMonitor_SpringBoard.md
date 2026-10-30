# `SBBiometricOcclusionMonitor`

- Image: [`/System/Library/PrivateFrameworks/SpringBoard.framework/SpringBoard`](../userland/System__Library__PrivateFrameworks__SpringBoard.framework__SpringBoard.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SBFDevicePoseProviderObserver`, `CSBiometricSuppressionProviding`
- 4 instance variables, 5 properties, 9 instance methods, 0 class methods

## Instance variables

```
@"SBFDevicePoseProvider" _devicePoseProvider;
@"NSHashTable" _observers;
Q _suppressedBiometricModalities;
@"<BSInvalidatable>" _mesaOcclusionAssertion;
```

## Properties

```
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (TQ,R,N) suppressedBiometricModalities;
```

## Instance methods

```
-[SBBiometricOcclusionMonitor dealloc];
-[SBBiometricOcclusionMonitor poseProvider:didUpdateFromPose:toPose:];
-[SBBiometricOcclusionMonitor initWithDevicePoseProvider:];
-[SBBiometricOcclusionMonitor addBiometricSuppressionObserver:];
-[SBBiometricOcclusionMonitor removeBiometricSuppressionObserver:];
-[SBBiometricOcclusionMonitor suppressedBiometricModalities];
-[SBBiometricOcclusionMonitor _modalitiesSuppressedForPose:];
-[SBBiometricOcclusionMonitor _updateMesaOcclusionAssertion];
-[SBBiometricOcclusionMonitor _updateSuppressionFromPose:];
```
