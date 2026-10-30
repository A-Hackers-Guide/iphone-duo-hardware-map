# `CTLazuliBusinessMessagingCapabilities`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 13 instance methods, 1 class methods

## Instance variables

```
B _supported;
B _enabledByDefault;
q _userPreferenceForSwitch;
```

## Properties

```
@property (Tq,N,V_userPreferenceForSwitch) userPreferenceForSwitch;
@property (TB,N,V_supported) supported;
@property (TB,N,V_enabledByDefault) enabledByDefault;
```

## Class methods

```
+[CTLazuliBusinessMessagingCapabilities supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliBusinessMessagingCapabilities supported];
-[CTLazuliBusinessMessagingCapabilities setSupported:];
-[CTLazuliBusinessMessagingCapabilities setEnabledByDefault:];
-[CTLazuliBusinessMessagingCapabilities encodeWithCoder:];
-[CTLazuliBusinessMessagingCapabilities description];
-[CTLazuliBusinessMessagingCapabilities initWithCoder:];
-[CTLazuliBusinessMessagingCapabilities copyWithZone:];
-[CTLazuliBusinessMessagingCapabilities enabledByDefault];
-[CTLazuliBusinessMessagingCapabilities isEqual:];
-[CTLazuliBusinessMessagingCapabilities initWithReflection:];
-[CTLazuliBusinessMessagingCapabilities isEqualToCTLazuliBusinessMessagingCapabilities:];
-[CTLazuliBusinessMessagingCapabilities setUserPreferenceForSwitch:];
-[CTLazuliBusinessMessagingCapabilities userPreferenceForSwitch];
```
