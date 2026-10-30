# `TUHoldAssistWaitTimePrediction`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
q _predictionType;
q _queuePosition;
{_NSRange="location"Q"length"Q} _timeEstimate;
```

## Properties

```
@property (Tq,R,N,V_predictionType) predictionType;
@property (T{_NSRange=QQ},R,N,V_timeEstimate) timeEstimate;
@property (Tq,R,N,V_queuePosition) queuePosition;
```

## Class methods

```
+[TUHoldAssistWaitTimePrediction supportsSecureCoding];
```

## Instance methods

```
-[TUHoldAssistWaitTimePrediction encodeWithCoder:];
-[TUHoldAssistWaitTimePrediction description];
-[TUHoldAssistWaitTimePrediction initWithCoder:];
-[TUHoldAssistWaitTimePrediction copyWithZone:];
-[TUHoldAssistWaitTimePrediction isEqual:];
-[TUHoldAssistWaitTimePrediction predictionType];
-[TUHoldAssistWaitTimePrediction initWithType:timeEstimate:queuePosition:];
-[TUHoldAssistWaitTimePrediction isEqualToWaitTimePrediction:];
-[TUHoldAssistWaitTimePrediction queuePosition];
-[TUHoldAssistWaitTimePrediction timeEstimate];
```
