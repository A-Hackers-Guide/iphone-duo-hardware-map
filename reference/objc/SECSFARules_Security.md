# `SECSFARules`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PBCodable`
- Protocols: `NSCopying`
- 5 instance variables, 6 properties, 30 instance methods, 2 class methods

## Instance variables

```
@"SECSFAVersionMatch" _allowedBuilds;
i _configVersion;
@"NSMutableArray" _eventFilters;
@"NSMutableArray" _eventRules;
{?="configVersion"b1} _has;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V_eventRules) eventRules;
@property (TB,R,N) hasAllowedBuilds;
@property (T@"SECSFAVersionMatch",&,N,V_allowedBuilds) allowedBuilds;
@property (T@"NSMutableArray",&,N,V_eventFilters) eventFilters;
@property (TB,N) hasConfigVersion;
@property (Ti,N,V_configVersion) configVersion;
```

## Class methods

```
+[SECSFARules eventFilterType];
+[SECSFARules eventRulesType];
```

## Instance methods

```
-[SECSFARules writeTo:];
-[SECSFARules mergeFrom:];
-[SECSFARules setEventFilters:];
-[SECSFARules configVersion];
-[SECSFARules hash];
-[SECSFARules copyTo:];
-[SECSFARules description];
-[SECSFARules readFrom:];
-[SECSFARules copyWithZone:];
-[SECSFARules isEqual:];
-[SECSFARules eventFilters];
-[SECSFARules dictionaryRepresentation];
-[SECSFARules StringAsConfigVersion:];
-[SECSFARules eventRulesCount];
-[SECSFARules addEventFilter:];
-[SECSFARules clearEventRules];
-[SECSFARules addEventRules:];
-[SECSFARules allowedBuilds];
-[SECSFARules clearEventFilters];
-[SECSFARules configVersionAsString:];
-[SECSFARules eventFilterAtIndex:];
-[SECSFARules eventFiltersCount];
-[SECSFARules eventRules];
-[SECSFARules eventRulesAtIndex:];
-[SECSFARules hasAllowedBuilds];
-[SECSFARules hasConfigVersion];
-[SECSFARules setAllowedBuilds:];
-[SECSFARules setConfigVersion:];
-[SECSFARules setEventRules:];
-[SECSFARules setHasConfigVersion:];
```
