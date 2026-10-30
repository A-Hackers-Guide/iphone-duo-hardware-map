# `CTLazuliOperationStatus`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 5 instance variables, 5 properties, 17 instance methods, 1 class methods

## Instance variables

```
q _registrationState;
q _switchState;
q _cellularDataRequirement;
q _disablementReason;
q _quickSwitchRole;
```

## Properties

```
@property (Tq,N,V_registrationState) registrationState;
@property (Tq,N,V_switchState) switchState;
@property (Tq,N,V_cellularDataRequirement) cellularDataRequirement;
@property (Tq,N,V_disablementReason) disablementReason;
@property (Tq,N,V_quickSwitchRole) quickSwitchRole;
```

## Class methods

```
+[CTLazuliOperationStatus supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliOperationStatus setDisablementReason:];
-[CTLazuliOperationStatus registrationState];
-[CTLazuliOperationStatus encodeWithCoder:];
-[CTLazuliOperationStatus description];
-[CTLazuliOperationStatus initWithCoder:];
-[CTLazuliOperationStatus copyWithZone:];
-[CTLazuliOperationStatus disablementReason];
-[CTLazuliOperationStatus isEqual:];
-[CTLazuliOperationStatus quickSwitchRole];
-[CTLazuliOperationStatus setSwitchState:];
-[CTLazuliOperationStatus cellularDataRequirement];
-[CTLazuliOperationStatus initWithReflection:];
-[CTLazuliOperationStatus isEqualToCTLazuliOperationStatus:];
-[CTLazuliOperationStatus setCellularDataRequirement:];
-[CTLazuliOperationStatus setQuickSwitchRole:];
-[CTLazuliOperationStatus setRegistrationState:];
-[CTLazuliOperationStatus switchState];
```
