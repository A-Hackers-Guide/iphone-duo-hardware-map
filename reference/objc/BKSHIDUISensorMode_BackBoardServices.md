# `BKSHIDUISensorMode`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `BSDescriptionStreaming`, `BSProtobufSerializable`, `BSXPCSecureCoding`
- 13 instance variables, 27 properties, 43 instance methods, 5 class methods

## Instance variables

```
q _identifier;
@"NSString" _reason;
q _versionedPID;
Q _changeSource;
i _proximityDetectionMode;
@"NSSet" _multitouchHostStateKeys;
@"NSSet" _proximityHostStateKeys;
q _displayState;
B _digitizerEnabled;
B _pocketTouchesExpected;
B _estimatedProximityMode;
B _postEventWithCurrentDetectionMask;
B _proximityDetectionModeWasInherited;
```

## Properties

```
@property (T@"NSString",R,C,N) _identifierDescription;
@property (TB,R,N,GisRestrictedToSystemShell) restrictedToSystemShell;
@property (TB,R,N) estimatedProximityMode;
@property (TB,R,N) proximityDetectionModeWasInherited;
@property (Tq,R,N) versionedPID;
@property (Tq,R,N,V_identifier) identifier;
@property (T@"NSString",R,C,N) reason;
@property (TQ,R,N) changeSource;
@property (TB,R,N) postEventWithCurrentDetectionMask;
@property (Ti,R,N) proximityDetectionMode;
@property (Tq,R,N) displayState;
@property (TB,R,N) digitizerEnabled;
@property (TB,R,N) pocketTouchesExpected;
@property (TB,R,N) tapToWakeEnabled;
@property (TB,R,N) coverGestureEnabled;
@property (TB,R,N) alwaysOnGesturesEnabled;
@property (TB,R,N) wakeOnSwipeEnabled;
@property (TB,R,N) wakeOnLongPressEnabled;
@property (TB,R,N) wakeOnTapThroughEnabled;
@property (TB,R,N) wakeOnSwipeThroughEnabled;
@property (TB,R,N) wakeOnLongPressThroughEnabled;
@property (T@"NSSet",R,C,N,V_multitouchHostStateKeys) multitouchHostStateKeys;
@property (T@"NSSet",R,C,N,V_proximityHostStateKeys) proximityHostStateKeys;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[BKSHIDUISensorMode supportsBSXPCSecureCoding];
+[BKSHIDUISensorMode protobufSchema];
+[BKSHIDUISensorMode new];
+[BKSHIDUISensorMode _prevailingMode:];
+[BKSHIDUISensorMode buildModeForReason:builder:];
```

## Instance methods

```
-[BKSHIDUISensorMode didFinishProtobufDecodingWithError:];
-[BKSHIDUISensorMode tapToWakeEnabled];
-[BKSHIDUISensorMode identifier];
-[BKSHIDUISensorMode initForProtobufDecoding];
-[BKSHIDUISensorMode init];
-[BKSHIDUISensorMode wakeOnLongPressThroughEnabled];
-[BKSHIDUISensorMode copy];
-[BKSHIDUISensorMode _identifierDescription];
-[BKSHIDUISensorMode digitizerEnabled];
-[BKSHIDUISensorMode proximityDetectionMode];
-[BKSHIDUISensorMode wakeOnLongPressEnabled];
-[BKSHIDUISensorMode coverGestureEnabled];
-[BKSHIDUISensorMode versionedPID];
-[BKSHIDUISensorMode displayState];
-[BKSHIDUISensorMode proximityHostStateKeys];
-[BKSHIDUISensorMode _init];
-[BKSHIDUISensorMode multitouchHostStateKeys];
-[BKSHIDUISensorMode isRestrictedToSystemShell];
-[BKSHIDUISensorMode changeSource];
-[BKSHIDUISensorMode isEqualExceptIdentifierAndReasons:];
-[BKSHIDUISensorMode encodeWithCoder:];
-[BKSHIDUISensorMode wakeOnTapThroughEnabled];
-[BKSHIDUISensorMode _comparisonScore];
-[BKSHIDUISensorMode isEffectivelyEqualToMode:];
-[BKSHIDUISensorMode hash];
-[BKSHIDUISensorMode description];
-[BKSHIDUISensorMode wakeOnSwipeThroughEnabled];
-[BKSHIDUISensorMode alwaysOnGesturesEnabled];
-[BKSHIDUISensorMode initWithCoder:];
-[BKSHIDUISensorMode appendDescriptionToStream:];
-[BKSHIDUISensorMode _settingKeysAllowed:];
-[BKSHIDUISensorMode encodeWithBSXPCCoder:];
-[BKSHIDUISensorMode reason];
-[BKSHIDUISensorMode initWithBSXPCCoder:];
-[BKSHIDUISensorMode estimatedProximityMode];
-[BKSHIDUISensorMode copyWithZone:];
-[BKSHIDUISensorMode pocketTouchesExpected];
-[BKSHIDUISensorMode _initCopyFrom:];
-[BKSHIDUISensorMode isEqual:];
-[BKSHIDUISensorMode mutableCopy];
-[BKSHIDUISensorMode wakeOnSwipeEnabled];
-[BKSHIDUISensorMode postEventWithCurrentDetectionMask];
-[BKSHIDUISensorMode proximityDetectionModeWasInherited];
```
