# `CTEmergencyMode`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 6 instance variables, 6 properties, 23 instance methods, 2 class methods

## Instance variables

```
B _enabled;
B _isEmergencyText;
B _isEmergencySetup;
B _isStewieActive;
q _type;
q _state;
```

## Properties

```
@property (TB,N,V_enabled) enabled;
@property (Tq,N,V_type) type;
@property (TB,N,V_isEmergencyText) isEmergencyText;
@property (TB,N,V_isEmergencySetup) isEmergencySetup;
@property (Tq,N,V_state) state;
@property (TB,R,N,V_isStewieActive) isStewieActive;
```

## Class methods

```
+[CTEmergencyMode supportsSecureCoding];
+[CTEmergencyMode convertFromEmergencyMode:];
```

## Instance methods

```
-[CTEmergencyMode isStewieActive];
-[CTEmergencyMode setState:];
-[CTEmergencyMode enabled];
-[CTEmergencyMode init];
-[CTEmergencyMode setType:];
-[CTEmergencyMode type];
-[CTEmergencyMode setEnabled:];
-[CTEmergencyMode encodeWithCoder:];
-[CTEmergencyMode description];
-[CTEmergencyMode initWithCoder:];
-[CTEmergencyMode copyWithZone:];
-[CTEmergencyMode isEqual:];
-[CTEmergencyMode state];
-[CTEmergencyMode isEmergencyText];
-[CTEmergencyMode initWithEnabled:type:isEmergencyText:];
-[CTEmergencyMode initWithEnabled:type:isEmergencyText:isEmergencySetup:];
-[CTEmergencyMode initWithEnabled:type:isEmergencyText:isEmergencySetup:isStewieActive:];
-[CTEmergencyMode initWithEnabled:type:isEmergencyText:isEmergencySetup:isStewieActive:state:];
-[CTEmergencyMode initWithEnabled:type:isEmergencyText:isEmergencySetup:state:];
-[CTEmergencyMode isEmergencySetup];
-[CTEmergencyMode isEqualToCTEmergencyMode:];
-[CTEmergencyMode setIsEmergencySetup:];
-[CTEmergencyMode setIsEmergencyText:];
```
