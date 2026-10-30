# `ANCommand`

- Image: [`/System/Library/PrivateFrameworks/AccessoryInteraction.framework/AccessoryInteraction`](../userland/System__Library__PrivateFrameworks__AccessoryInteraction.framework__AccessoryInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 4 properties, 8 instance methods, 56 class methods

## Instance variables

```
C _protocol;
S _opcode;
@"NSData" _payload;
```

## Properties

```
@property (TC,R,V_protocol) protocol;
@property (TS,R,V_opcode) opcode;
@property (T@"NSData",R,V_payload) payload;
@property (T@"NSData",R) bytes;
```

## Class methods

```
+[ANCommand setAccelerometerSlopeModeConfigurationCommandWithConfiguration:];
+[ANCommand checkCrashesCommand];
+[ANCommand commandWithOpcode:payload:];
+[ANCommand dumpNordicCrashesCommand];
+[ANCommand dumpNordicLogsCommand];
+[ANCommand dumpRoseCrashesCommand];
+[ANCommand dumpRoseLogsCommand];
+[ANCommand fetchAccelerometerModeCommand];
+[ANCommand fetchAccelerometerOrientationModeConfigurationCommand];
+[ANCommand fetchAccelerometerSlopeModeConfigurationCommand];
+[ANCommand fetchBatteryStatusCommand];
+[ANCommand fetchCurrentKeyIndexCommand];
+[ANCommand fetchFindingCapabilitiesCommandWithPayload:];
+[ANCommand fetchFindingCapabilitiesNonOwnerPoshCommand];
+[ANCommand fetchFindingCapabilitiesNonOwnerPoshCommand:];
+[ANCommand fetchUserStatsCommandWithPersistence_v0:];
+[ANCommand fetchUserStatsCommandWithPersistence_v1:];
+[ANCommand induceCrashCommand];
+[ANCommand initRoseCommandWithParameters:];
+[ANCommand initRoseNonOwnerCommandWithParameters:];
+[ANCommand initRosePoshCommandWithParameters:];
+[ANCommand prepareToStartRoseRangingCommand];
+[ANCommand prepareToStartRoseRangingNonOwnerCommand];
+[ANCommand prepareToStartRoseRangingNonOwnerPoshCommand];
+[ANCommand rollWildKeyCommand];
+[ANCommand setAbsoluteWildModeConfigurationCommandWithConfiguration:];
+[ANCommand setAccelerometerOrientationModeConfigurationCommandWithConfiguration:];
+[ANCommand setCentralReferenceTimeCommand];
+[ANCommand setKeyRotationTimeoutCommandWithTimeout:];
+[ANCommand setNearOwnerTimeoutCommandWithTimeout:];
+[ANCommand setRoseNBRangingParametersCommandWithParameters:];
+[ANCommand setRoseNBRangingParametersNonOwnerPoshCommandWithParameters:];
+[ANCommand setRoseRangingParametersCommandWithParameters:];
+[ANCommand setRoseRangingParametersNonOwnerCommandWithParameters:];
+[ANCommand setRoseRangingParametersNonOwnerPoshCommandWithParameters:];
+[ANCommand setTagTypeCommandWithType:];
+[ANCommand setUnauthorizedPlaySoundRateLimitCommand:];
+[ANCommand setWildModeConfigurationCommandWithConfiguration:];
+[ANCommand startRoseNBRangingCommandWithIRK:fragmentCount:];
+[ANCommand startRoseNBRangingNonOwnerPoshCommandWithParameters:];
+[ANCommand startRoseRangingCommandWithParameters:];
+[ANCommand startRoseRangingNonOwnerCommandWithParameters:];
+[ANCommand startRoseRangingNonOwnerPoshCommandWithParameters:];
+[ANCommand startSoundCommand];
+[ANCommand startSoundSequenceCommandWithSequence:];
+[ANCommand startUnauthorizedShortSoundCommand];
+[ANCommand startUnauthorizedSoundCommand];
+[ANCommand stopRoseCommandWithParameters:];
+[ANCommand stopRoseNonOwnerCommandWithParameters:];
+[ANCommand stopRoseNonOwnerPoshCommandWithParameters:];
+[ANCommand stopRoseRangingCommand];
+[ANCommand stopRoseRangingNonOwnerCommandWithParameters:];
+[ANCommand stopRoseRangingNonOwnerPoshCommandWithParameters:];
+[ANCommand stopSoundCommand];
+[ANCommand stopUnauthorizedSoundCommand];
+[ANCommand unpairCommand];
```

## Instance methods

```
-[ANCommand protocol];
-[ANCommand init];
-[ANCommand dealloc];
-[ANCommand payload];
-[ANCommand initWithData:];
-[ANCommand bytes];
-[ANCommand initWithOpcode:payload:];
-[ANCommand opcode];
```
