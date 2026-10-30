# `CTEmergencyAlertMetadata`

- Image: [`/System/Library/Frameworks/CoreTelephony.framework/CoreTelephony`](../userland/System__Library__Frameworks__CoreTelephony.framework__CoreTelephony.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 12 instance variables, 12 properties, 29 instance methods, 1 class methods

## Instance variables

```
B _active;
B _displayed;
@"NSString" _alertHash;
@"NSString" _title;
@"NSString" _message;
@"NSString" _instructionMessage;
@"NSString" _emergencyCategory;
@"NSString" _language;
@"NSDate" _deliveryTime;
@"NSDate" _displayTime;
@"NSArray" _polygonalGeofences;
@"NSArray" _circularGeofences;
```

## Properties

```
@property (T@"NSString",&,N,V_alertHash) alertHash;
@property (T@"NSString",&,N,V_title) title;
@property (T@"NSString",&,N,V_message) message;
@property (T@"NSString",&,N,V_instructionMessage) instructionMessage;
@property (T@"NSString",&,N,V_emergencyCategory) emergencyCategory;
@property (T@"NSString",&,N,V_language) language;
@property (TB,N,V_active) active;
@property (T@"NSDate",&,N,V_deliveryTime) deliveryTime;
@property (T@"NSDate",&,N,V_displayTime) displayTime;
@property (TB,N,V_displayed) displayed;
@property (T@"NSArray",&,N,V_polygonalGeofences) polygonalGeofences;
@property (T@"NSArray",&,N,V_circularGeofences) circularGeofences;
```

## Class methods

```
+[CTEmergencyAlertMetadata supportsSecureCoding];
```

## Instance methods

```
-[CTEmergencyAlertMetadata language];
-[CTEmergencyAlertMetadata active];
-[CTEmergencyAlertMetadata setMessage:];
-[CTEmergencyAlertMetadata init];
-[CTEmergencyAlertMetadata message];
-[CTEmergencyAlertMetadata setActive:];
-[CTEmergencyAlertMetadata title];
-[CTEmergencyAlertMetadata encodeWithCoder:];
-[CTEmergencyAlertMetadata initWithCoder:];
-[CTEmergencyAlertMetadata setTitle:];
-[CTEmergencyAlertMetadata copyWithZone:];
-[CTEmergencyAlertMetadata setLanguage:];
-[CTEmergencyAlertMetadata setDisplayTime:];
-[CTEmergencyAlertMetadata displayTime];
-[CTEmergencyAlertMetadata displayed];
-[CTEmergencyAlertMetadata deliveryTime];
-[CTEmergencyAlertMetadata setDisplayed:];
-[CTEmergencyAlertMetadata alertHash];
-[CTEmergencyAlertMetadata circularGeofences];
-[CTEmergencyAlertMetadata emergencyCategory];
-[CTEmergencyAlertMetadata initWithAlertHash:title:message:instructionMessage:emergencyCategory:language:active:deliveryTime:displayTime:displayed:polygonalGeofences:circularGeofences:];
-[CTEmergencyAlertMetadata instructionMessage];
-[CTEmergencyAlertMetadata polygonalGeofences];
-[CTEmergencyAlertMetadata setAlertHash:];
-[CTEmergencyAlertMetadata setCircularGeofences:];
-[CTEmergencyAlertMetadata setDeliveryTime:];
-[CTEmergencyAlertMetadata setEmergencyCategory:];
-[CTEmergencyAlertMetadata setInstructionMessage:];
-[CTEmergencyAlertMetadata setPolygonalGeofences:];
```
