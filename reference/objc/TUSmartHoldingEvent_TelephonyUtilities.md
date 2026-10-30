# `TUSmartHoldingEvent`

- Image: [`/System/Library/PrivateFrameworks/TelephonyUtilities.framework/TelephonyUtilities`](../userland/System__Library__PrivateFrameworks__TelephonyUtilities.framework__TelephonyUtilities.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 5 instance variables, 5 properties, 14 instance methods, 1 class methods

## Instance variables

```
q _eventType;
@"NSString" _text;
@"NSDate" _date;
d _confidenceScore;
@"TUHoldAssistWaitTimePrediction" _prediction;
```

## Properties

```
@property (Tq,R,N,V_eventType) eventType;
@property (T@"NSString",R,N,V_text) text;
@property (T@"NSDate",R,N,V_date) date;
@property (Td,R,N,V_confidenceScore) confidenceScore;
@property (T@"TUHoldAssistWaitTimePrediction",R,N,V_prediction) prediction;
```

## Class methods

```
+[TUSmartHoldingEvent supportsSecureCoding];
```

## Instance methods

```
-[TUSmartHoldingEvent eventType];
-[TUSmartHoldingEvent text];
-[TUSmartHoldingEvent confidenceScore];
-[TUSmartHoldingEvent prediction];
-[TUSmartHoldingEvent date];
-[TUSmartHoldingEvent encodeWithCoder:];
-[TUSmartHoldingEvent description];
-[TUSmartHoldingEvent initWithCoder:];
-[TUSmartHoldingEvent copyWithZone:];
-[TUSmartHoldingEvent isEqual:];
-[TUSmartHoldingEvent initWithType:text:date:];
-[TUSmartHoldingEvent initWithType:text:date:confidenceScore:];
-[TUSmartHoldingEvent initWithType:text:date:confidenceScore:prediction:];
-[TUSmartHoldingEvent isEqualToSession:];
```
