# `DSContinuityStore`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"RPLReplicatorControlClient" _replicatorProxy;
@"DSContinuityPairingWrapper" _continuityPairing;
```

## Properties

```
@property (T@"RPLReplicatorControlClient",&,N,V_replicatorProxy) replicatorProxy;
@property (T@"DSContinuityPairingWrapper",&,N,V_continuityPairing) continuityPairing;
```

## Class methods

```
+[DSContinuityStore nullifyReplicatorAllowlist];
```

## Instance methods

```
-[DSContinuityStore init];
-[DSContinuityStore continuityPairing];
-[DSContinuityStore setContinuityPairing:];
-[DSContinuityStore replicatorProxy];
-[DSContinuityStore unpairAllDevicesWithCompletion:];
-[DSContinuityStore fetchPairedDevicesWithCompletion:];
-[DSContinuityStore setReplicatorProxy:];
-[DSContinuityStore unpairDevicesWithIDs:completion:];
```
