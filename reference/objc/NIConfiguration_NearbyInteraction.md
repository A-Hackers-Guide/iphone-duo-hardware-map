# `NIConfiguration`

- Image: [`/System/Library/Frameworks/NearbyInteraction.framework/NearbyInteraction`](../userland/System__Library__Frameworks__NearbyInteraction.framework__NearbyInteraction.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `NSCopying`, `NSSecureCoding`
- 3 instance variables, 3 properties, 18 instance methods, 2 class methods

## Instance variables

```
B _supportsCameraAssistance;
Q _suspensionPolicy;
Q _enabledGestures;
```

## Properties

```
@property (TB,V_supportsCameraAssistance) supportsCameraAssistance;
@property (TQ,V_suspensionPolicy) suspensionPolicy;
@property (TQ,V_enabledGestures) enabledGestures;
```

## Class methods

```
+[NIConfiguration supportsSecureCoding];
+[NIConfiguration new];
```

## Instance methods

```
-[NIConfiguration init];
-[NIConfiguration descriptionInternal];
-[NIConfiguration initInternal];
-[NIConfiguration initWithConfiguration:];
-[NIConfiguration encodeWithCoder:];
-[NIConfiguration _internalIsCameraAssistanceEnabled];
-[NIConfiguration initWithCoder:];
-[NIConfiguration copyWithZone:];
-[NIConfiguration enabledGestures];
-[NIConfiguration _internalIsCameraAssistanceInClientProcess];
-[NIConfiguration _internalIsExtendedDistanceMeasurementEnabled];
-[NIConfiguration _internalIsMemoryAssertionRequired];
-[NIConfiguration _internalIsPowerAssertionRequired];
-[NIConfiguration setEnabledGestures:];
-[NIConfiguration setSupportsCameraAssistance:];
-[NIConfiguration setSuspensionPolicy:];
-[NIConfiguration supportsCameraAssistance];
-[NIConfiguration suspensionPolicy];
```
