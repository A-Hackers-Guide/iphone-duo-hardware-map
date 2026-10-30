# `LACDTOBiometryWatchdogPack`

- Image: [`/System/Library/PrivateFrameworks/LocalAuthenticationCore.framework/LocalAuthenticationCore`](../userland/System__Library__PrivateFrameworks__LocalAuthenticationCore.framework__LocalAuthenticationCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSSecureCoding`
- 2 instance variables, 3 properties, 9 instance methods, 2 class methods

## Instance variables

```
@"LACDTOBiometryWatchdog" _biometryWatchdogGlobal;
@"LACDTOBiometryWatchdog" _biometryWatchdogDTO;
```

## Properties

```
@property (T@"LACDTOBiometryWatchdog",R,N,V_biometryWatchdogGlobal) biometryWatchdogGlobal;
@property (T@"LACDTOBiometryWatchdog",R,N,V_biometryWatchdogDTO) biometryWatchdogDTO;
@property (TB,R,N) isBarking;
```

## Class methods

```
+[LACDTOBiometryWatchdogPack supportsSecureCoding];
+[LACDTOBiometryWatchdogPack nullInstance];
```

## Instance methods

```
-[LACDTOBiometryWatchdogPack encodeWithCoder:];
-[LACDTOBiometryWatchdogPack description];
-[LACDTOBiometryWatchdogPack initWithCoder:];
-[LACDTOBiometryWatchdogPack isEqual:];
-[LACDTOBiometryWatchdogPack biometryWatchdogDTO];
-[LACDTOBiometryWatchdogPack biometryWatchdogGlobal];
-[LACDTOBiometryWatchdogPack initWithBiometryWatchdogGlobal:biometryWatchdogDTO:];
-[LACDTOBiometryWatchdogPack isBarking];
-[LACDTOBiometryWatchdogPack watchdogForOptions:];
```
