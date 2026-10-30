# `TUSmartHoldingSession`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 6 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _hostedOnCurrentDevice;
@"NSUUID" _uuid;
Q _state;
Q _requiresUserAttentionReason;
@"NSArray" _events;
```

## Properties

```
@property (T@"NSUUID",R,N,V_uuid) uuid;
@property (TQ,R,N,V_state) state;
@property (TQ,R,N,V_requiresUserAttentionReason) requiresUserAttentionReason;
@property (TB,R,N,GisHostedOnCurrentDevice,V_hostedOnCurrentDevice) hostedOnCurrentDevice;
@property (T@"NSArray",R,N,V_events) events;
@property (T@"NSArray",R,N) transcription;
```

## Class methods

```
+[TUSmartHoldingSession supportsSecureCoding];
```

## Instance methods

```
-[TUSmartHoldingSession isHostedOnCurrentDevice];
-[TUSmartHoldingSession uuid];
-[TUSmartHoldingSession events];
-[TUSmartHoldingSession encodeWithCoder:];
-[TUSmartHoldingSession description];
-[TUSmartHoldingSession initWithCoder:];
-[TUSmartHoldingSession copyWithZone:];
-[TUSmartHoldingSession isEqual:];
-[TUSmartHoldingSession state];
-[TUSmartHoldingSession initWithUUID:state:events:requiresUserAttentionReason:hostedOnCurrentDevice:];
-[TUSmartHoldingSession isEqualToSession:];
-[TUSmartHoldingSession requiresUserAttentionReason];
-[TUSmartHoldingSession transcription];
```
