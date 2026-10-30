# `CTRoamingStatus`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 2 instance variables, 2 properties, 8 instance methods, 1 class methods

## Instance variables

```
B _isVoiceRoaming;
B _isDataRoaming;
```

## Properties

```
@property (TB,N,V_isVoiceRoaming) isVoiceRoaming;
@property (TB,N,V_isDataRoaming) isDataRoaming;
```

## Class methods

```
+[CTRoamingStatus supportsSecureCoding];
```

## Instance methods

```
-[CTRoamingStatus encodeWithCoder:];
-[CTRoamingStatus description];
-[CTRoamingStatus initWithCoder:];
-[CTRoamingStatus copyWithZone:];
-[CTRoamingStatus isDataRoaming];
-[CTRoamingStatus isVoiceRoaming];
-[CTRoamingStatus setIsDataRoaming:];
-[CTRoamingStatus setIsVoiceRoaming:];
```
