# `CLRegion`

- Image: [`/System/Library/Frameworks/CoreLocation.framework/CoreLocation`](../userland/System__Library__Frameworks__CoreLocation.framework__CoreLocation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 13 instance variables, 13 properties, 35 instance methods, 1 class methods

## Instance variables

```
B _notifyOnEntry;
B _notifyOnExit;
B _conservativeEntry;
B _emergency;
B _requiresWirelessClientInfo;
i _referenceFrame;
i _type;
d _radius;
@"NSString" _identifier;
@"NSUUID" _deviceId;
@"NSString" _handoffTag;
@"NSString" _onBehalfOfBundleId;
{CLLocationCoordinate2D="latitude"d"longitude"d} _center;
```

## Properties

```
@property (T@"NSUUID",R,C,N,V_deviceId) deviceId;
@property (T@"NSString",R,C,N,V_handoffTag) handoffTag;
@property (T@"NSString",C,N,V_onBehalfOfBundleId) onBehalfOfBundleId;
@property (TB,V_conservativeEntry) conservativeEntry;
@property (Ti,V_referenceFrame) referenceFrame;
@property (TB,V_emergency) emergency;
@property (TB,V_requiresWirelessClientInfo) requiresWirelessClientInfo;
@property (Ti,V_type) type;
@property (T{CLLocationCoordinate2D=dd},R,V_center) center;
@property (Td,R,V_radius) radius;
@property (T@"NSString",R,C,N,V_identifier) identifier;
@property (TB,V_notifyOnEntry) notifyOnEntry;
@property (TB,V_notifyOnExit) notifyOnExit;
```

## Class methods

```
+[CLRegion supportsSecureCoding];
```

## Instance methods

```
-[CLRegion deviceId];
-[CLRegion identifier];
-[CLRegion dealloc];
-[CLRegion setEmergency:];
-[CLRegion referenceFrame];
-[CLRegion radius];
-[CLRegion setType:];
-[CLRegion type];
-[CLRegion center];
-[CLRegion encodeWithCoder:];
-[CLRegion hash];
-[CLRegion description];
-[CLRegion initWithCoder:];
-[CLRegion containsCoordinate:];
-[CLRegion copyWithZone:];
-[CLRegion isEqual:];
-[CLRegion setReferenceFrame:];
-[CLRegion initWithIdentifier:];
-[CLRegion notifyOnEntry];
-[CLRegion notifyOnExit];
-[CLRegion conservativeEntry];
-[CLRegion emergency];
-[CLRegion handoffTag];
-[CLRegion initCircularRegionWithCenter:radius:identifier:];
-[CLRegion initWithClientRegion:];
-[CLRegion initWithIdentifier:andRegionType:];
-[CLRegion initWithIdentifier:onBehalfOf:regionType:notifyOnEntry:notifyOnExit:conservativeEntry:emergency:requiresWirelessClientInfo:];
-[CLRegion initWithIdentifier:onBehalfOf:regionType:notifyOnEntry:notifyOnExit:conservativeEntry:emergency:requiresWirelessClientInfo:deviceId:handoffTag:];
-[CLRegion onBehalfOfBundleId];
-[CLRegion requiresWirelessClientInfo];
-[CLRegion setConservativeEntry:];
-[CLRegion setNotifyOnEntry:];
-[CLRegion setNotifyOnExit:];
-[CLRegion setOnBehalfOfBundleId:];
-[CLRegion setRequiresWirelessClientInfo:];
```
