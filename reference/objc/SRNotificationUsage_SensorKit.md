# `SRNotificationUsage`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`
- 2 instance variables, 6 properties, 10 instance methods, 2 class methods

## Instance variables

```
@"NSString" _bundleIdentifier;
q _event;
```

## Properties

```
@property (T@"NSString",C,V_bundleIdentifier) bundleIdentifier;
@property (Tq,V_event) event;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRNotificationUsage supportsSecureCoding];
+[SRNotificationUsage notificationUsageWithBundleIdentifier:eventType:];
```

## Instance methods

```
-[SRNotificationUsage setEvent:];
-[SRNotificationUsage dealloc];
-[SRNotificationUsage bundleIdentifier];
-[SRNotificationUsage event];
-[SRNotificationUsage encodeWithCoder:];
-[SRNotificationUsage description];
-[SRNotificationUsage initWithCoder:];
-[SRNotificationUsage setBundleIdentifier:];
-[SRNotificationUsage isEqual:];
-[SRNotificationUsage sr_dictionaryRepresentation];
```
