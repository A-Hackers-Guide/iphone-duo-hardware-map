# `BKDevicePearl`

- Image: [`/System/Library/PrivateFrameworks/BiometricKit.framework/BiometricKit`](../userland/System__Library__PrivateFrameworks__BiometricKit.framework__BiometricKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKDevice`
- 0 instance variables, 2 properties, 19 instance methods, 1 class methods

## Properties

```
@property (T@"<BKDevicePearlDelegate>",W,D,N) delegate;
@property (Tq,R,N) pearlState;
```

## Class methods

```
+[BKDevicePearl deviceAvailableWithFailure:];
```

## Instance methods

```
-[BKDevicePearl statusMessage:client:];
-[BKDevicePearl pearlState];
-[BKDevicePearl setTemplate:forIdentity:error:];
-[BKDevicePearl deviceEventWithStatus:];
-[BKDevicePearl deviceStateWithStatus:];
-[BKDevicePearl removePeriocularEnrollmentsForUser:identityUUID:removeAll:async:reply:];
-[BKDevicePearl removePeriocularEnrollmentsForUser:removeAll:error:];
-[BKDevicePearl createMatchOperationWithError:];
-[BKDevicePearl createPresenceDetectOperationWithError:];
-[BKDevicePearl prewarmCamera:error:];
-[BKDevicePearl removePeriocularEnrollmentsForUser:removeAll:reply:];
-[BKDevicePearl periocularMatchStateWithError:];
-[BKDevicePearl removePeriocularEnrollmentsFromIdentity:removeAll:error:];
-[BKDevicePearl createEnrollOperationWithError:];
-[BKDevicePearl removePeriocularEnrollmentsFromIdentity:removeAll:reply:];
-[BKDevicePearl supportsPeriocularEnrollmentWithError:];
-[BKDevicePearl periocularMatchStateForUser:error:];
-[BKDevicePearl clearIdentityMigrationFailureForUser:error:];
-[BKDevicePearl queryIdentityMigrationFailureForUser:error:];
```
