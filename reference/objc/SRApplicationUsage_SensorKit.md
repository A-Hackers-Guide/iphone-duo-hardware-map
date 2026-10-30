# `SRApplicationUsage`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `SRSampleExporting`, `NSSecureCoding`
- 6 instance variables, 12 properties, 20 instance methods, 3 class methods

## Instance variables

```
@"NSString" _bundleIdentifier;
d _usageTime;
@"NSString" _reportApplicationIdentifier;
d _relativeStartTime;
@"NSMutableArray" _mutableTextInputSessions;
@"NSMutableArray" _mutableSupplementalCategories;
```

## Properties

```
@property (T@"NSString",C,V_bundleIdentifier) bundleIdentifier;
@property (Td,V_usageTime) usageTime;
@property (T@"NSString",C,V_reportApplicationIdentifier) reportApplicationIdentifier;
@property (T@"NSMutableArray",&,V_mutableTextInputSessions) mutableTextInputSessions;
@property (T@"NSMutableArray",&,V_mutableSupplementalCategories) mutableSupplementalCategories;
@property (Td,N,V_relativeStartTime) relativeStartTime;
@property (T@"NSArray",R,C) textInputSessions;
@property (T@"NSArray",R,C,N) supplementalCategories;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[SRApplicationUsage supportsSecureCoding];
+[SRApplicationUsage applicationUsageWithBundleIdentifier:reportApplicationIdentifier:totalUsageTime:relativeStartTime:];
+[SRApplicationUsage applicationUsageWithBundleIdentifier:reportApplicationIdentifier:totalUsageTime:relativeStartTime:textInputSessions:supplementalCategories:];
```

## Instance methods

```
-[SRApplicationUsage dealloc];
-[SRApplicationUsage bundleIdentifier];
-[SRApplicationUsage encodeWithCoder:];
-[SRApplicationUsage description];
-[SRApplicationUsage initWithCoder:];
-[SRApplicationUsage setBundleIdentifier:];
-[SRApplicationUsage isEqual:];
-[SRApplicationUsage sr_dictionaryRepresentation];
-[SRApplicationUsage setUsageTime:];
-[SRApplicationUsage usageTime];
-[SRApplicationUsage setReportApplicationIdentifier:];
-[SRApplicationUsage mutableSupplementalCategories];
-[SRApplicationUsage mutableTextInputSessions];
-[SRApplicationUsage relativeStartTime];
-[SRApplicationUsage reportApplicationIdentifier];
-[SRApplicationUsage setMutableSupplementalCategories:];
-[SRApplicationUsage setMutableTextInputSessions:];
-[SRApplicationUsage setRelativeStartTime:];
-[SRApplicationUsage supplementalCategories];
-[SRApplicationUsage textInputSessions];
```
