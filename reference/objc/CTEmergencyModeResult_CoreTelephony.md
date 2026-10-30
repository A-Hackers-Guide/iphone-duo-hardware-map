# `CTEmergencyModeResult`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"CTEmergencyMode" _mode;
@"CTXPCServiceSubscriptionContext" _context;
```

## Properties

```
@property (T@"CTEmergencyMode",R,N,V_mode) mode;
@property (T@"CTXPCServiceSubscriptionContext",R,N,V_context) context;
```

## Class methods

```
+[CTEmergencyModeResult supportsSecureCoding];
```

## Instance methods

```
-[CTEmergencyModeResult encodeWithCoder:];
-[CTEmergencyModeResult mode];
-[CTEmergencyModeResult description];
-[CTEmergencyModeResult initWithCoder:];
-[CTEmergencyModeResult copyWithZone:];
-[CTEmergencyModeResult context];
-[CTEmergencyModeResult initWithMode:andContext:];
```
