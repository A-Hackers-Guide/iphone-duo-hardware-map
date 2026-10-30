# `CBBrightDotMitigation`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBModule`
- Protocols: `CBContainerModuleProtocol`
- 1 instance variables, 2 properties, 14 instance methods, 1 class methods

## Instance variables

```
bdm;
```

## Properties

```
@property (TB,N,R) isActive;
@property (Tf,N,R) currentCap;
```

## Class methods

```
+[CBBrightDotMitigation transitionLengthFrom:to:];
```

## Instance methods

```
-[CBBrightDotMitigation copyPropertyForKey:];
-[CBBrightDotMitigation setProperty:forKey:];
-[CBBrightDotMitigation initWithQueue:];
-[CBBrightDotMitigation init];
-[CBBrightDotMitigation stop];
-[CBBrightDotMitigation start];
-[CBBrightDotMitigation setLux:];
-[CBBrightDotMitigation handleNotificationForKey:withProperty:];
-[CBBrightDotMitigation isActive];
-[CBBrightDotMitigation copyPropertyForKey:withParameter:];
-[CBBrightDotMitigation initWithCapabilities:];
-[CBBrightDotMitigation calculateNitsCapForLux:];
-[CBBrightDotMitigation currentCap];
-[CBBrightDotMitigation setReferenceModeEnabled:];
```
