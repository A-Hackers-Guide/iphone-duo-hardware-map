# `SecLaunchSequence`

- Image: [`/System/Library/Frameworks/Security.framework/Security`](../userland/System__Library__Frameworks__Security.framework__Security.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 7 instance variables, 7 properties, 22 instance methods, 0 class methods

## Instance variables

```
B _firstLaunch;
B _launched;
@"NSString" _name;
@"NSMutableDictionary" _events;
@"NSMutableDictionary" _attributes;
@"NSBlockOperation" _launchOperation;
@"NSMutableDictionary" _dependantLaunches;
```

## Properties

```
@property (TB,V_launched) launched;
@property (T@"NSString",&,V_name) name;
@property (T@"NSMutableDictionary",&,V_events) events;
@property (T@"NSMutableDictionary",&,V_attributes) attributes;
@property (T@"NSBlockOperation",&,V_launchOperation) launchOperation;
@property (T@"NSMutableDictionary",&,V_dependantLaunches) dependantLaunches;
@property (TB) firstLaunch;
```

## Instance methods

```
-[SecLaunchSequence dependantLaunches];
-[SecLaunchSequence launchOperation];
-[SecLaunchSequence addEvent:];
-[SecLaunchSequence setEvents:];
-[SecLaunchSequence setLaunched:];
-[SecLaunchSequence setAttributes:];
-[SecLaunchSequence metricsReport];
-[SecLaunchSequence events];
-[SecLaunchSequence eventsRelativeTime];
-[SecLaunchSequence addDependantLaunch:child:];
-[SecLaunchSequence setLaunchOperation:];
-[SecLaunchSequence firstLaunch];
-[SecLaunchSequence launched];
-[SecLaunchSequence launch];
-[SecLaunchSequence addAttribute:value:];
-[SecLaunchSequence setFirstLaunch:];
-[SecLaunchSequence eventsByTime];
-[SecLaunchSequence setName:];
-[SecLaunchSequence attributes];
-[SecLaunchSequence initWithRocketName:];
-[SecLaunchSequence name];
-[SecLaunchSequence setDependantLaunches:];
```
