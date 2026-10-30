# `WADeviceAnalytics_Event`

- Image: [`/System/Library/PrivateFrameworks/WiFiAnalytics.framework/WiFiAnalytics`](../userland/System__Library__PrivateFrameworks__WiFiAnalytics.framework__WiFiAnalytics.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 25 instance methods, 11 class methods

## Instance variables

```
@"NSString" _eventType;
@"NSDictionary" _properties;
@"NSPredicate" _entityFilter;
Q _useAs;
@"NSEntityDescription" _entity;
@"NSSet" _keyPathsToFetch;
@"NSArray" _propertiesToFetch;
@"NSArray" _relationshipKeyPathsToFetch;
```

## Properties

```
@property (T@"NSString",&,V_eventType) eventType;
@property (TQ,V_useAs) useAs;
@property (T@"NSEntityDescription",&,V_entity) entity;
@property (T@"NSDictionary",&,V_properties) properties;
@property (T@"NSSet",&,V_keyPathsToFetch) keyPathsToFetch;
@property (T@"NSArray",&,V_propertiesToFetch) propertiesToFetch;
@property (T@"NSArray",&,V_relationshipKeyPathsToFetch) relationshipKeyPathsToFetch;
@property (T@"NSPredicate",&,V_entityFilter) entityFilter;
```

## Class methods

```
+[WADeviceAnalytics_Event eventDescription:from:withError:];
+[WADeviceAnalytics_Event eventsIn:withPredicate:];
+[WADeviceAnalytics_Event sequenceEdgeEventsIn:];
+[WADeviceAnalytics_Event sequenceEndEventsIn:];
+[WADeviceAnalytics_Event sequenceEventsIn:];
+[WADeviceAnalytics_Event sequenceStartEventsIn:];
+[WADeviceAnalytics_Event shallowCopyOfUsedEventsIn:];
+[WADeviceAnalytics_Event useAsDescription:];
+[WADeviceAnalytics_Event useAsEnd:inEvents:withError:];
+[WADeviceAnalytics_Event useAsEvent:inEvents:withError:];
+[WADeviceAnalytics_Event useAsStart:inEvents:withError:];
```

## Instance methods

```
-[WADeviceAnalytics_Event propertiesToFetch];
-[WADeviceAnalytics_Event properties];
-[WADeviceAnalytics_Event eventType];
-[WADeviceAnalytics_Event initWithEntity:];
-[WADeviceAnalytics_Event relationshipKeyPathsToFetch];
-[WADeviceAnalytics_Event setEntity:];
-[WADeviceAnalytics_Event setPropertiesToFetch:];
-[WADeviceAnalytics_Event setEventType:];
-[WADeviceAnalytics_Event useEventAsSequenceStart];
-[WADeviceAnalytics_Event setUseAs:];
-[WADeviceAnalytics_Event useEventAsSequenceEvent];
-[WADeviceAnalytics_Event setProperties:];
-[WADeviceAnalytics_Event usedPropertiesDescription];
-[WADeviceAnalytics_Event setRelationshipKeyPathsToFetch:];
-[WADeviceAnalytics_Event setPropertiesToFetch:withError:];
-[WADeviceAnalytics_Event entity];
-[WADeviceAnalytics_Event initWithUsedPropertiesFromUsedEvent:];
-[WADeviceAnalytics_Event description];
-[WADeviceAnalytics_Event entityFilter];
-[WADeviceAnalytics_Event dontUseEvent];
-[WADeviceAnalytics_Event keyPathsToFetch];
-[WADeviceAnalytics_Event setKeyPathsToFetch:];
-[WADeviceAnalytics_Event useAs];
-[WADeviceAnalytics_Event useEventAsSequenceEnd];
-[WADeviceAnalytics_Event setEntityFilter:];
```
