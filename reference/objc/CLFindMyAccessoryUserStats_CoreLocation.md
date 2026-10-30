# `CLFindMyAccessoryUserStats`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 41 instance variables, 41 properties, 50 instance methods, 2 class methods

## Instance variables

```
Q _version;
Q _overflowFlag;
Q _crashCount;
Q _multiTime;
Q _nearOwnerTime;
Q _wildTime;
Q _soundCount;
Q _soundTime;
Q _rangingCount;
Q _rangingTime;
Q _multiLeashTime;
Q _multiConnectionTime;
Q _nearOwnerTimeV2;
Q _singleLeashTime;
Q _singleConnectionTime;
Q _dualConnectionTime;
Q _dualLeashTime;
Q _utAccelCount;
Q _lastClear;
Q _roseOnTime;
Q _ownerLongSoundCount;
Q _ownerShortSoundCount;
Q _utLongSoundCount;
Q _utShortSoundCount;
Q _bomSoundCount;
Q _fc1ndRangingCount;
Q _fc1ndRangingTime;
Q _lastPIn;
q _batteryState;
Q _nbmmsRangingTime;
Q _abandonedFwUpdateCount;
Q _abandonedFwUpdateTime;
Q _roseInitCount;
Q _pairingAttemptsCount;
Q _tempVeryLowCount;
Q _tempLowCount;
Q _tempOkCount;
Q _tempHighCount;
Q _proxPairingTime;
Q _tempLastPIn;
Q _nbmmsRangingCount;
```

## Properties

```
@property (TQ,N,V_version) version;
@property (TQ,R,V_overflowFlag) overflowFlag;
@property (TQ,R,V_crashCount) crashCount;
@property (TQ,R,V_multiTime) multiTime;
@property (TQ,R,V_nearOwnerTime) nearOwnerTime;
@property (TQ,R,V_wildTime) wildTime;
@property (TQ,R,V_soundCount) soundCount;
@property (TQ,R,V_soundTime) soundTime;
@property (TQ,R,V_rangingCount) rangingCount;
@property (TQ,R,V_rangingTime) rangingTime;
@property (TQ,R,V_multiLeashTime) multiLeashTime;
@property (TQ,R,V_multiConnectionTime) multiConnectionTime;
@property (TQ,R,V_nearOwnerTimeV2) nearOwnerTimeV2;
@property (TQ,R,V_singleLeashTime) singleLeashTime;
@property (TQ,R,V_singleConnectionTime) singleConnectionTime;
@property (TQ,R,V_dualConnectionTime) dualConnectionTime;
@property (TQ,R,V_dualLeashTime) dualLeashTime;
@property (TQ,R,V_utAccelCount) utAccelCount;
@property (TQ,R,V_lastClear) lastClear;
@property (TQ,R,V_roseOnTime) roseOnTime;
@property (TQ,R,V_ownerLongSoundCount) ownerLongSoundCount;
@property (TQ,R,V_ownerShortSoundCount) ownerShortSoundCount;
@property (TQ,R,V_utLongSoundCount) utLongSoundCount;
@property (TQ,R,V_utShortSoundCount) utShortSoundCount;
@property (TQ,R,V_bomSoundCount) bomSoundCount;
@property (TQ,R,V_fc1ndRangingCount) fc1ndRangingCount;
@property (TQ,R,V_fc1ndRangingTime) fc1ndRangingTime;
@property (TQ,R,V_lastPIn) lastPIn;
@property (Tq,R,V_batteryState) batteryState;
@property (TQ,R,V_nbmmsRangingTime) nbmmsRangingTime;
@property (TQ,R,V_abandonedFwUpdateCount) abandonedFwUpdateCount;
@property (TQ,R,V_abandonedFwUpdateTime) abandonedFwUpdateTime;
@property (TQ,R,V_roseInitCount) roseInitCount;
@property (TQ,R,V_pairingAttemptsCount) pairingAttemptsCount;
@property (TQ,R,V_tempVeryLowCount) tempVeryLowCount;
@property (TQ,R,V_tempLowCount) tempLowCount;
@property (TQ,R,V_tempOkCount) tempOkCount;
@property (TQ,R,V_tempHighCount) tempHighCount;
@property (TQ,R,V_proxPairingTime) proxPairingTime;
@property (TQ,R,V_tempLastPIn) tempLastPIn;
@property (TQ,R,V_nbmmsRangingCount) nbmmsRangingCount;
```

## Class methods

```
+[CLFindMyAccessoryUserStats supportsSecureCoding];
+[CLFindMyAccessoryUserStats batteryStateToString:];
```

## Instance methods

```
-[CLFindMyAccessoryUserStats init];
-[CLFindMyAccessoryUserStats version];
-[CLFindMyAccessoryUserStats encodeWithCoder:];
-[CLFindMyAccessoryUserStats initWithCoder:];
-[CLFindMyAccessoryUserStats setVersion:];
-[CLFindMyAccessoryUserStats copyWithZone:];
-[CLFindMyAccessoryUserStats batteryState];
-[CLFindMyAccessoryUserStats lastPIn];
-[CLFindMyAccessoryUserStats nearOwnerTimeV2];
-[CLFindMyAccessoryUserStats proxPairingTime];
-[CLFindMyAccessoryUserStats singleLeashTime];
-[CLFindMyAccessoryUserStats abandonedFwUpdateCount];
-[CLFindMyAccessoryUserStats abandonedFwUpdateTime];
-[CLFindMyAccessoryUserStats bomSoundCount];
-[CLFindMyAccessoryUserStats crashCount];
-[CLFindMyAccessoryUserStats dualConnectionTime];
-[CLFindMyAccessoryUserStats dualLeashTime];
-[CLFindMyAccessoryUserStats fc1ndRangingCount];
-[CLFindMyAccessoryUserStats fc1ndRangingTime];
-[CLFindMyAccessoryUserStats initWithOverflowFlag:crashCount:multiTime:nearOwnerTime:wildTime:soundCount:soundTime:rangingCount:rangingTime:multiLeashTime:multiConnectionTime:nearOwnerTimeV2:singleLeashTime:singleConnectionTime:dualConnectionTime:dualLeashTime:utAccelCount:lastClear:roseOnTime:ownerLongSoundCount:ownerShortSoundCount:utLongSoundCount:utShortSoundCount:bomSoundCount:fc1ndRangingCount:fc1ndRangingTime:lastPIn:batteryState:nbmmsRangingTime:abandonedFwUpdateCount:abandonedFwUpdateTime:roseInitCount:pairingAttemptsCount:tempVeryLowCount:tempLowCount:tempOkCount:tempHighCount:proxPairingTime:tempLastPIn:nbmmsRangingCount:version:];
-[CLFindMyAccessoryUserStats initWithPayloadV1:];
-[CLFindMyAccessoryUserStats initWithPayloadV2:];
-[CLFindMyAccessoryUserStats initWithPayloadV3:];
-[CLFindMyAccessoryUserStats lastClear];
-[CLFindMyAccessoryUserStats multiConnectionTime];
-[CLFindMyAccessoryUserStats multiLeashTime];
-[CLFindMyAccessoryUserStats multiTime];
-[CLFindMyAccessoryUserStats nbmmsRangingCount];
-[CLFindMyAccessoryUserStats nbmmsRangingTime];
-[CLFindMyAccessoryUserStats nearOwnerTime];
-[CLFindMyAccessoryUserStats overflowFlag];
-[CLFindMyAccessoryUserStats ownerLongSoundCount];
-[CLFindMyAccessoryUserStats ownerShortSoundCount];
-[CLFindMyAccessoryUserStats pairingAttemptsCount];
-[CLFindMyAccessoryUserStats rangingCount];
-[CLFindMyAccessoryUserStats rangingTime];
-[CLFindMyAccessoryUserStats roseInitCount];
-[CLFindMyAccessoryUserStats roseOnTime];
-[CLFindMyAccessoryUserStats singleConnectionTime];
-[CLFindMyAccessoryUserStats soundCount];
-[CLFindMyAccessoryUserStats soundTime];
-[CLFindMyAccessoryUserStats tempHighCount];
-[CLFindMyAccessoryUserStats tempLastPIn];
-[CLFindMyAccessoryUserStats tempLowCount];
-[CLFindMyAccessoryUserStats tempOkCount];
-[CLFindMyAccessoryUserStats tempVeryLowCount];
-[CLFindMyAccessoryUserStats utAccelCount];
-[CLFindMyAccessoryUserStats utLongSoundCount];
-[CLFindMyAccessoryUserStats utShortSoundCount];
-[CLFindMyAccessoryUserStats wildTime];
```
