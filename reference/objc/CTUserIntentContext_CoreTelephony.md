# `CTUserIntentContext`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`, `NSCopying`
- 2 instance variables, 2 properties, 13 instance methods, 2 class methods

## Instance variables

```
Q _flowType;
@"NSString" _sessionId;
```

## Properties

```
@property (TQ,V_flowType) flowType;
@property (T@"NSString",&,V_sessionId) sessionId;
```

## Class methods

```
+[CTUserIntentContext supportsSecureCoding];
+[CTUserIntentContext contextFromDictionary:];
```

## Instance methods

```
-[CTUserIntentContext toDictionary];
-[CTUserIntentContext init];
-[CTUserIntentContext sessionId];
-[CTUserIntentContext setSessionId:];
-[CTUserIntentContext encodeWithCoder:];
-[CTUserIntentContext hash];
-[CTUserIntentContext description];
-[CTUserIntentContext initWithCoder:];
-[CTUserIntentContext flowType];
-[CTUserIntentContext copyWithZone:];
-[CTUserIntentContext isEqual:];
-[CTUserIntentContext initWithFlow:sessionId:];
-[CTUserIntentContext setFlowType:];
```
