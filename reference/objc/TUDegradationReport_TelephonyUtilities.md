# `TUDegradationReport`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 5 properties, 9 instance methods, 2 class methods

## Instance variables

```
q _type;
@"NSDate" _startTimestamp;
d _duration;
Q _participantID;
q _result;
```

## Properties

```
@property (Tq,R,N,V_type) type;
@property (T@"NSDate",R,C,N,V_startTimestamp) startTimestamp;
@property (Td,R,N,V_duration) duration;
@property (TQ,R,N,V_participantID) participantID;
@property (Tq,R,N,V_result) result;
```

## Class methods

```
+[TUDegradationReport supportsSecureCoding];
+[TUDegradationReport reportForDegradations:dateCallConnected:conversationReport:];
```

## Instance methods

```
-[TUDegradationReport participantID];
-[TUDegradationReport duration];
-[TUDegradationReport startTimestamp];
-[TUDegradationReport result];
-[TUDegradationReport type];
-[TUDegradationReport encodeWithCoder:];
-[TUDegradationReport initWithCoder:];
-[TUDegradationReport initWithType:startTimestamp:duration:];
-[TUDegradationReport initWithType:startTimestamp:duration:participantID:result:];
```
