# `CTIMSRegistrationTransportInfo`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 10 instance methods, 1 class methods

## Instance variables

```
B _isRegistered;
i _contextType;
i _transportType;
```

## Properties

```
@property (TB,N,V_isRegistered) isRegistered;
@property (Ti,N,V_contextType) contextType;
@property (Ti,N,V_transportType) transportType;
```

## Class methods

```
+[CTIMSRegistrationTransportInfo supportsSecureCoding];
```

## Instance methods

```
-[CTIMSRegistrationTransportInfo isRegistered];
-[CTIMSRegistrationTransportInfo setTransportType:];
-[CTIMSRegistrationTransportInfo contextType];
-[CTIMSRegistrationTransportInfo setIsRegistered:];
-[CTIMSRegistrationTransportInfo setContextType:];
-[CTIMSRegistrationTransportInfo transportType];
-[CTIMSRegistrationTransportInfo encodeWithCoder:];
-[CTIMSRegistrationTransportInfo description];
-[CTIMSRegistrationTransportInfo initWithCoder:];
-[CTIMSRegistrationTransportInfo copyWithZone:];
```
