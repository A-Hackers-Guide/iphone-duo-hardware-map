# `CTDataConnectionAvailabilityStatus`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
B _available;
i _csiError;
```

## Properties

```
@property (TB,N,V_available) available;
@property (Ti,N,V_csiError) csiError;
```

## Class methods

```
+[CTDataConnectionAvailabilityStatus supportsSecureCoding];
```

## Instance methods

```
-[CTDataConnectionAvailabilityStatus csiError];
-[CTDataConnectionAvailabilityStatus setCsiError:];
-[CTDataConnectionAvailabilityStatus setAvailable:];
-[CTDataConnectionAvailabilityStatus available];
-[CTDataConnectionAvailabilityStatus encodeWithCoder:];
-[CTDataConnectionAvailabilityStatus description];
-[CTDataConnectionAvailabilityStatus initWithCoder:];
-[CTDataConnectionAvailabilityStatus copyWithZone:];
```
