# `BKSHIDEventBiometricDescriptor`

- Image: [`/System/Library/PrivateFrameworks/BackBoardServices.framework/BackBoardServices`](../userland/System__Library__PrivateFrameworks__BackBoardServices.framework__BackBoardServices.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `BKSHIDEventDescriptor`
- 2 instance variables, 1 properties, 10 instance methods, 2 class methods

## Instance variables

```
B _isWildcard;
I _biometricEventType;
```

## Properties

```
@property (TI,R,N,V_biometricEventType) biometricEventType;
```

## Class methods

```
+[BKSHIDEventBiometricDescriptor supportsSecureCoding];
+[BKSHIDEventBiometricDescriptor descriptorWithBiometricEventType:];
```

## Instance methods

```
-[BKSHIDEventBiometricDescriptor init];
-[BKSHIDEventBiometricDescriptor initWithBiometricEventType:];
-[BKSHIDEventBiometricDescriptor describes:];
-[BKSHIDEventBiometricDescriptor encodeWithCoder:];
-[BKSHIDEventBiometricDescriptor hash];
-[BKSHIDEventBiometricDescriptor requiresFuzzyMatching];
-[BKSHIDEventBiometricDescriptor initWithCoder:];
-[BKSHIDEventBiometricDescriptor appendDescriptionToStream:];
-[BKSHIDEventBiometricDescriptor biometricEventType];
-[BKSHIDEventBiometricDescriptor isEqual:];
```
