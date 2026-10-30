# `CTLazuliEncryptionCapabilities`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 4 instance variables, 4 properties, 15 instance methods, 1 class methods

## Instance variables

```
B _carrierSupport;
B _showSwitch;
B _canSetSwitch;
B _switchState;
```

## Properties

```
@property (TB,N,V_carrierSupport) carrierSupport;
@property (TB,N,V_showSwitch) showSwitch;
@property (TB,N,V_canSetSwitch) canSetSwitch;
@property (TB,N,V_switchState) switchState;
```

## Class methods

```
+[CTLazuliEncryptionCapabilities supportsSecureCoding];
```

## Instance methods

```
-[CTLazuliEncryptionCapabilities encodeWithCoder:];
-[CTLazuliEncryptionCapabilities description];
-[CTLazuliEncryptionCapabilities initWithCoder:];
-[CTLazuliEncryptionCapabilities copyWithZone:];
-[CTLazuliEncryptionCapabilities isEqual:];
-[CTLazuliEncryptionCapabilities setSwitchState:];
-[CTLazuliEncryptionCapabilities canSetSwitch];
-[CTLazuliEncryptionCapabilities carrierSupport];
-[CTLazuliEncryptionCapabilities initWithReflection:];
-[CTLazuliEncryptionCapabilities isEqualToCTLazuliEncryptionCapabilities:];
-[CTLazuliEncryptionCapabilities setCanSetSwitch:];
-[CTLazuliEncryptionCapabilities setCarrierSupport:];
-[CTLazuliEncryptionCapabilities setShowSwitch:];
-[CTLazuliEncryptionCapabilities showSwitch];
-[CTLazuliEncryptionCapabilities switchState];
```
