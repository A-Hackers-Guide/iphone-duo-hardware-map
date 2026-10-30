# `CTPlanTravelDetails`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 4 instance variables, 4 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _isTraveleSIM;
B _isUserTraveling;
B _isGlobalMVNO;
@"NSNumber" _isDataOnly;
```

## Properties

```
@property (TB,N,V_isTraveleSIM) isTraveleSIM;
@property (TB,N,V_isUserTraveling) isUserTraveling;
@property (TB,N,V_isGlobalMVNO) isGlobalMVNO;
@property (T@"NSNumber",&,N,V_isDataOnly) isDataOnly;
```

## Class methods

```
+[CTPlanTravelDetails supportsSecureCoding];
```

## Instance methods

```
-[CTPlanTravelDetails init];
-[CTPlanTravelDetails encodeWithCoder:];
-[CTPlanTravelDetails description];
-[CTPlanTravelDetails initWithCoder:];
-[CTPlanTravelDetails isEqual:];
-[CTPlanTravelDetails isUserTraveling];
-[CTPlanTravelDetails isDataOnly];
-[CTPlanTravelDetails isGlobalMVNO];
-[CTPlanTravelDetails isTraveleSIM];
-[CTPlanTravelDetails setIsDataOnly:];
-[CTPlanTravelDetails setIsGlobalMVNO:];
-[CTPlanTravelDetails setIsTraveleSIM:];
-[CTPlanTravelDetails setIsUserTraveling:];
```
