# `PLBasebandEurekaLogMessage`

- Image: [`/System/Library/PrivateFrameworks/PowerlogLiteOperators.framework/PowerlogLiteOperators`](../userland/System__Library__PrivateFrameworks__PowerlogLiteOperators.framework__PowerlogLiteOperators.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLBasebandMessage`
- 2 instance variables, 3 properties, 11 instance methods, 0 class methods

## Instance variables

```
^{_PLBasebandLogHeader={_PLBasebandMessageHeader=C}SS[8C]} _header;
@"NSData" _payload;
```

## Properties

```
@property (T^{_PLBasebandLogHeader={_PLBasebandMessageHeader=C}SS[8C]},V_header) header;
@property (T@"NSData",&,V_payload) payload;
@property (TI,R) eventCode;
```

## Instance methods

```
-[PLBasebandEurekaLogMessage header];
-[PLBasebandEurekaLogMessage setHeader:];
-[PLBasebandEurekaLogMessage payload];
-[PLBasebandEurekaLogMessage setPayload:];
-[PLBasebandEurekaLogMessage parseData:];
-[PLBasebandEurekaLogMessage initWithData:];
-[PLBasebandEurekaLogMessage payloadString];
-[PLBasebandEurekaLogMessage eventCode];
-[PLBasebandEurekaLogMessage logWithLogger:];
-[PLBasebandEurekaLogMessage stringForUnknownBytes:];
-[PLBasebandEurekaLogMessage tooShortErrorString];
```
