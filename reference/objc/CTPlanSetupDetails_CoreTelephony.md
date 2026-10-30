# `CTPlanSetupDetails`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 5 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _inBuddy;
@"NSString" _carrierName;
Q _setupType;
Q _setupResult;
Q _duration;
```

## Properties

```
@property (TB,V_inBuddy) inBuddy;
@property (T@"NSString",&,V_carrierName) carrierName;
@property (TQ,V_setupType) setupType;
@property (TQ,V_setupResult) setupResult;
@property (TQ,V_duration) duration;
```

## Class methods

```
+[CTPlanSetupDetails supportsSecureCoding];
```

## Instance methods

```
-[CTPlanSetupDetails carrierName];
-[CTPlanSetupDetails setCarrierName:];
-[CTPlanSetupDetails duration];
-[CTPlanSetupDetails encodeWithCoder:];
-[CTPlanSetupDetails description];
-[CTPlanSetupDetails initWithCoder:];
-[CTPlanSetupDetails setDuration:];
-[CTPlanSetupDetails isEqual:];
-[CTPlanSetupDetails setSetupType:];
-[CTPlanSetupDetails setupType];
-[CTPlanSetupDetails inBuddy];
-[CTPlanSetupDetails setSetupResult:];
-[CTPlanSetupDetails initWithInBuddy:carrierName:setupType:setupResult:duration:];
-[CTPlanSetupDetails setInBuddy:];
-[CTPlanSetupDetails setupResult];
```
