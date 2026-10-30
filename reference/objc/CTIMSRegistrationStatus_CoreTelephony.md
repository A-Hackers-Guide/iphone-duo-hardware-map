# `CTIMSRegistrationStatus`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
B _isRegisteredForVoice;
B _isRegisteredForSMS;
```

## Properties

```
@property (TB,N,V_isRegisteredForVoice) isRegisteredForVoice;
@property (TB,N,V_isRegisteredForSMS) isRegisteredForSMS;
```

## Class methods

```
+[CTIMSRegistrationStatus supportsSecureCoding];
```

## Instance methods

```
-[CTIMSRegistrationStatus encodeWithCoder:];
-[CTIMSRegistrationStatus description];
-[CTIMSRegistrationStatus initWithCoder:];
-[CTIMSRegistrationStatus copyWithZone:];
-[CTIMSRegistrationStatus isRegisteredForSMS];
-[CTIMSRegistrationStatus isRegisteredForVoice];
-[CTIMSRegistrationStatus setIsRegisteredForSMS:];
-[CTIMSRegistrationStatus setIsRegisteredForVoice:];
```
