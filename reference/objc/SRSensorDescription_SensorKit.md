# `SRSensorDescription`

- Image: [`/System/Library/Frameworks/SensorKit.framework/SensorKit`](../userland/System__Library__Frameworks__SensorKit.framework__SensorKit.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 22 instance variables, 20 properties, 24 instance methods, 5 class methods

## Instance variables

```
@"NSString" _additionalSampleDataNoteKey;
@"NSString" _localizedAdditionalSampleDataNote;
I _legacySampleClassLinkedBefore;
@"NSString" _name;
@"NSString" _authorizationService;
@"NSArray" _relatedSettingsCategories;
@"NSString" _publicEntitlementValue;
@"NSString" _sampleClass;
@"NSString" _exportingSampleClass;
@"NSString" _infoPlistAuthorizationCategory;
@"NSString" _writerAuthorizationService;
q _authorizationVersion;
@"NSString" _onDemandWriterService;
@"NSString" _authorizationStoreCohort;
@"NSString" _legacyName;
@"NSArray" _filters;
@"NSSet" _eligibleDaemons;
d _roundingInterval;
q _datastoreBackend;
@"NSString" _legacySampleClass;
@"NSSet" _additions;
@"NSDictionary" _supportedPlatforms;
```

## Properties

```
@property (T@"NSString",R,C,V_name) name;
@property (T@"NSString",R,C,V_authorizationService) authorizationService;
@property (T@"NSArray",R,C,V_relatedSettingsCategories) relatedSettingsCategories;
@property (T@"NSString",R,C,V_publicEntitlementValue) publicEntitlementValue;
@property (T@"NSString",R,C) sampleClass;
@property (T@"NSString",R,C) exportingSampleClass;
@property (T@"NSString",R,C) localizedAdditionalSampleDataNote;
@property (T@"NSString",R,C,V_infoPlistAuthorizationCategory) infoPlistAuthorizationCategory;
@property (TB,R) metadataEnabled;
@property (TB,R) sensorConfigurationEnabled;
@property (T@"NSString",R,C,V_writerAuthorizationService) writerAuthorizationService;
@property (Tq,R,V_authorizationVersion) authorizationVersion;
@property (T@"NSString",R,C,V_onDemandWriterService) onDemandWriterService;
@property (TB,R) supportsCurrentPlatform;
@property (T@"NSString",R,C,V_authorizationStoreCohort) authorizationStoreCohort;
@property (T@"NSString",R,C,V_legacyName) legacyName;
@property (T@"NSArray",R,C,N,V_filters) filters;
@property (T@"NSSet",R,C,N) eligibleDaemons;
@property (Td,R,N,V_roundingInterval) roundingInterval;
@property (Tq,R,N,V_datastoreBackend) datastoreBackend;
```

## Class methods

```
+[SRSensorDescription initialize];
+[SRSensorDescription allDescriptions];
+[SRSensorDescription sensorDescriptionForDeletionRecordFromDescription:];
+[SRSensorDescription sensorDescriptionForSensor:];
+[SRSensorDescription sensorDescriptionsForAuthorizationService:];
```

## Instance methods

```
-[SRSensorDescription initWithDictionary:];
-[SRSensorDescription dealloc];
-[SRSensorDescription filters];
-[SRSensorDescription supportsCurrentPlatform];
-[SRSensorDescription description];
-[SRSensorDescription name];
-[SRSensorDescription legacyName];
-[SRSensorDescription supportsPlatform:];
-[SRSensorDescription eligibleDaemons];
-[SRSensorDescription metadataEnabled];
-[SRSensorDescription authorizationService];
-[SRSensorDescription authorizationStoreCohort];
-[SRSensorDescription authorizationVersion];
-[SRSensorDescription datastoreBackend];
-[SRSensorDescription exportingSampleClass];
-[SRSensorDescription infoPlistAuthorizationCategory];
-[SRSensorDescription localizedAdditionalSampleDataNote];
-[SRSensorDescription onDemandWriterService];
-[SRSensorDescription publicEntitlementValue];
-[SRSensorDescription relatedSettingsCategories];
-[SRSensorDescription roundingInterval];
-[SRSensorDescription sampleClass];
-[SRSensorDescription sensorConfigurationEnabled];
-[SRSensorDescription writerAuthorizationService];
```
