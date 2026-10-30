# `AUParameterValueTranslation`

- Image: [`/System/Library/PrivateFrameworks/AudioToolboxCore.framework/AudioToolboxCore`](../userland/System__Library__PrivateFrameworks__AudioToolboxCore.framework__AudioToolboxCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 5 instance variables, 5 properties, 13 instance methods, 1 class methods

## Instance variables

```
I _otherParamID;
f _otherValue;
f _auValue;
@"NSData" _otherDesc;
Q _auParamID;
```

## Properties

```
@property (T@"NSData",&,N,V_otherDesc) otherDesc;
@property (TI,N,V_otherParamID) otherParamID;
@property (Tf,N,V_otherValue) otherValue;
@property (TQ,N,V_auParamID) auParamID;
@property (Tf,N,V_auValue) auValue;
```

## Class methods

```
+[AUParameterValueTranslation supportsSecureCoding];
```

## Instance methods

```
-[AUParameterValueTranslation dealloc];
-[AUParameterValueTranslation encodeWithCoder:];
-[AUParameterValueTranslation initWithCoder:];
-[AUParameterValueTranslation auValue];
-[AUParameterValueTranslation auParamID];
-[AUParameterValueTranslation otherDesc];
-[AUParameterValueTranslation otherParamID];
-[AUParameterValueTranslation otherValue];
-[AUParameterValueTranslation setAuParamID:];
-[AUParameterValueTranslation setAuValue:];
-[AUParameterValueTranslation setOtherDesc:];
-[AUParameterValueTranslation setOtherParamID:];
-[AUParameterValueTranslation setOtherValue:];
```
