# `SBFDeviceLockOutController`

- Image: [`/System/Library/PrivateFrameworks/SpringBoardFoundation.framework/SpringBoardFoundation`](../userland/System__Library__PrivateFrameworks__SpringBoardFoundation.framework__SpringBoardFoundation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionProviding`, `SBFThermalConditionObserver`, `SBFPrivateAuthenticationObserver`, `SBFProximityReaderObserver`, `SBFLiquidDetectionObserver`, `SBFLockOutStatusProvider`
- 6 instance variables, 9 properties, 33 instance methods, 0 class methods

## Instance variables

```
@"<SBFThermalBlockProvider>" _thermalProvider;
B _lockedOutCached;
Q _lastBlockedStatus;
@"<SBFLiquidDetectionBlockProvider>" _liquidDetectionBlockProvider;
@"<SBFProximityReaderBlockProvider>" _proximityReaderBlockProvider;
@"SBFUserAuthenticationController" _authenticationController;
```

## Properties

```
@property (T@"SBFUserAuthenticationController",&,N,G_authenticationController,S_setAuthenticationController:,V_authenticationController) authenticationController;
@property (T@"<SBFThermalBlockProvider>",&,N,G_thermalProvider,S_setThermalProvider:,V_thermalProvider) thermalProvider;
@property (TB,N,G_isLockedOutCached,S_setLockedOutCached:,V_lockedOutCached) lockedOutCached;
@property (T@"<SBFLiquidDetectionBlockProvider>",&,N,V_liquidDetectionBlockProvider) liquidDetectionBlockProvider;
@property (T@"<SBFProximityReaderBlockProvider>",&,N,V_proximityReaderBlockProvider) proximityReaderBlockProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Instance methods

```
-[SBFDeviceLockOutController succinctDescriptionBuilder];
-[SBFDeviceLockOutController dealloc];
-[SBFDeviceLockOutController descriptionWithMultilinePrefix:];
-[SBFDeviceLockOutController _authenticationController];
-[SBFDeviceLockOutController succinctDescription];
-[SBFDeviceLockOutController thermalBlockStatusChanged:];
-[SBFDeviceLockOutController isBlocked];
-[SBFDeviceLockOutController description];
-[SBFDeviceLockOutController descriptionBuilderWithMultilinePrefix:];
-[SBFDeviceLockOutController isLockedOut];
-[SBFDeviceLockOutController _isLockedOutCached];
-[SBFDeviceLockOutController _noteLockedOutReasonsMayHaveChanged];
-[SBFDeviceLockOutController _noteLockedOutStateMayHaveChanged:];
-[SBFDeviceLockOutController _setAuthenticationController:];
-[SBFDeviceLockOutController _setLockedOutCached:];
-[SBFDeviceLockOutController _setThermalProvider:];
-[SBFDeviceLockOutController _thermalProvider];
-[SBFDeviceLockOutController deviceBlockStatus];
-[SBFDeviceLockOutController initWithThermalController:authenticationController:];
-[SBFDeviceLockOutController isLiquidDetectionCriticalUIBlocked];
-[SBFDeviceLockOutController isPermanentlyBlocked];
-[SBFDeviceLockOutController isProximityReaderBlocked];
-[SBFDeviceLockOutController isTemporarilyBlocked];
-[SBFDeviceLockOutController isThermallyBlocked];
-[SBFDeviceLockOutController isUserRequestedEraseEnabled];
-[SBFDeviceLockOutController liquidDetectionBlockProvider];
-[SBFDeviceLockOutController liquidDetectionBlockStatusChanged:];
-[SBFDeviceLockOutController proximityReaderBlockProvider];
-[SBFDeviceLockOutController proximityReaderBlockStatusChanged:];
-[SBFDeviceLockOutController setLiquidDetectionBlockProvider:];
-[SBFDeviceLockOutController setProximityReaderBlockProvider:];
-[SBFDeviceLockOutController temporaryBlockStatusChanged];
-[SBFDeviceLockOutController timeIntervalUntilUnblockedSinceReferenceDate];
```
