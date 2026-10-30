# `PLBasebandMavLogMessage`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLBasebandMessage`
- 4 instance variables, 4 properties, 11 instance methods, 0 class methods

## Instance variables

```
^{_PLBasebandLogHeader={_PLBasebandMessageHeader=C}SS[8C]} _header;
@"NSData" _payload;
I _eventCode;
@"NSString" _eventCodeString;
```

## Properties

```
@property (T^{_PLBasebandLogHeader={_PLBasebandMessageHeader=C}SS[8C]},V_header) header;
@property (T@"NSData",&,V_payload) payload;
@property (T@"NSString",R,V_eventCodeString) eventCodeString;
@property (TI,R,V_eventCode) eventCode;
```

## Instance methods

```
-[PLBasebandMavLogMessage header];
-[PLBasebandMavLogMessage setHeader:];
-[PLBasebandMavLogMessage payload];
-[PLBasebandMavLogMessage setPayload:];
-[PLBasebandMavLogMessage parseData:];
-[PLBasebandMavLogMessage initWithData:];
-[PLBasebandMavLogMessage eventCode];
-[PLBasebandMavLogMessage eventCodeString];
-[PLBasebandMavLogMessage logWithLogger:];
-[PLBasebandMavLogMessage stringForUnknownBytes:];
-[PLBasebandMavLogMessage tooShortErrorString];
```
