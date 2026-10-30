# `DSSourceDescriptor`

- Image: [`/System/Library/PrivateFrameworks/DigitalSeparation.framework/DigitalSeparation`](../userland/System__Library__PrivateFrameworks__DigitalSeparation.framework__DigitalSeparation.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 14 properties, 25 instance methods, 3 class methods

## Instance variables

```
@"NSString" _sourceName;
@"NSBundle" _localizationBundle;
@"NSDictionary" _sourceProperties;
```

## Properties

```
@property (T@"NSString",R,C,N) localizedName;
@property (T@"NSString",R,C,N) localizedAppName;
@property (T@"NSString",R,C,N) localizedAlertButtonLabel;
@property (T@"NSString",R,C,N) localizedStopAllLabel;
@property (T@"NSString",R,C,N) localizedStopAllAlertLabel;
@property (T@"NSString",R,C,N) localizedStopAllAlertDetail;
@property (TB,R,N) supportsResourceTypes;
@property (Tq,R,N) priority;
@property (T@"NSArray",R,C,N) darwinNotifications;
@property (T@"NSDictionary",R,C,N) ignoreErrors;
@property (T@"NSString",R,C,N) dataUsageBundleIdentifier;
@property (TB,R,N) requiresWifi;
@property (TB,R,N) requiresCellular;
@property (T@"NSString",R,C,N) correspondingApplicationIdentifier;
```

## Class methods

```
+[DSSourceDescriptor initialize];
+[DSSourceDescriptor sourceDescriptorForSource:];
+[DSSourceDescriptor sourceDescriptorForSource:localizationBundle:];
```

## Instance methods

```
-[DSSourceDescriptor priority];
-[DSSourceDescriptor ignoreErrors];
-[DSSourceDescriptor localizedName];
-[DSSourceDescriptor objectForKeyedSubscript:];
-[DSSourceDescriptor localizedAppName];
-[DSSourceDescriptor dataUsageBundleIdentifier];
-[DSSourceDescriptor requiresWifi];
-[DSSourceDescriptor correspondingApplicationIdentifier];
-[DSSourceDescriptor darwinNotifications];
-[DSSourceDescriptor localizedAlertButtonLabel];
-[DSSourceDescriptor localizedAlertDetailForSelectedPeople:];
-[DSSourceDescriptor localizedAlertTextForPerson:];
-[DSSourceDescriptor localizedDetailTextByType:];
-[DSSourceDescriptor localizedPublicSharingDetailTextByType:];
-[DSSourceDescriptor localizedResourceNamesForPerson:];
-[DSSourceDescriptor localizedStopAllAlertDetail];
-[DSSourceDescriptor localizedStopAllAlertDetailForPeople:];
-[DSSourceDescriptor localizedStopAllAlertLabel];
-[DSSourceDescriptor localizedStopAllLabel];
-[DSSourceDescriptor localizedStopByPerson:];
-[DSSourceDescriptor localizedStopByPersonBlocking:];
-[DSSourceDescriptor localizedStopByTypeSubtitleForSharingType:];
-[DSSourceDescriptor requiresCellular];
-[DSSourceDescriptor shouldIgnoreError:];
-[DSSourceDescriptor supportsResourceTypes];
```
