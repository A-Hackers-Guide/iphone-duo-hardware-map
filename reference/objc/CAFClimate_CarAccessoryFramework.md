# `CAFClimate`

- Image: [`/System/Library/PrivateFrameworks/CarAccessoryFramework.framework/CarAccessoryFramework`](../userland/System__Library__PrivateFrameworks__CarAccessoryFramework.framework__CarAccessoryFramework.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CAFAccessory`
- 0 instance variables, 33 properties, 37 instance methods, 2 class methods

## Properties

```
@property (T@"CAFCabin",R,N) cabinService;
@property (T@"NSArray",R,N) autoClimateControlServices;
@property (T@"NSArray",R,N) climateControlsLockedServices;
@property (T@"NSArray",R,N) defrostServices;
@property (T@"NSArray",R,N) temperatureServices;
@property (T@"CAFSteeringWheelHeatingCooling",R,N) steeringWheelHeatingCoolingService;
@property (T@"NSArray",R,N) ventServices;
@property (T@"NSArray",R,N) fanServices;
@property (T@"CAFRecirculation",R,N) recirculationService;
@property (T@"NSArray",R,N) zonesSyncedServices;
@property (T@"NSArray",R,N) zoneOnServices;
@property (T@"NSArray",R,N) temperatureLevelServices;
@property (T@"CAFCabin",R,N) cabin;
@property (T@"NSArray",R,N) autoClimateControls;
@property (T@"NSDictionary",R,N) autoClimateControlsIndexed;
@property (T@"NSArray",R,N) climateControlsLockeds;
@property (T@"NSDictionary",R,N) climateControlsLockedsIndexed;
@property (T@"NSArray",R,N) defrosts;
@property (T@"NSDictionary",R,N) defrostsIndexed;
@property (T@"NSArray",R,N) temperatures;
@property (T@"NSDictionary",R,N) temperaturesIndexed;
@property (T@"CAFSteeringWheelHeatingCooling",R,N) steeringWheelHeatingCooling;
@property (T@"NSArray",R,N) vents;
@property (T@"NSDictionary",R,N) ventsIndexed;
@property (T@"NSArray",R,N) fans;
@property (T@"NSDictionary",R,N) fansIndexed;
@property (T@"CAFRecirculation",R,N) recirculation;
@property (T@"NSArray",R,N) zonesSynceds;
@property (T@"NSDictionary",R,N) zonesSyncedsIndexed;
@property (T@"NSArray",R,N) zoneOns;
@property (T@"NSDictionary",R,N) zoneOnsIndexed;
@property (T@"NSArray",R,N) temperatureLevels;
@property (T@"NSDictionary",R,N) temperatureLevelsIndexed;
```

## Class methods

```
+[CAFClimate accessoryIdentifier];
+[CAFClimate observerProtocol];
```

## Instance methods

```
-[CAFClimate removeObserver:];
-[CAFClimate addObserver:];
-[CAFClimate registerObserver:];
-[CAFClimate unregisterObserver:];
-[CAFClimate temperatures];
-[CAFClimate cabin];
-[CAFClimate defrostServices];
-[CAFClimate zoneOns];
-[CAFClimate defrostsIndexed];
-[CAFClimate autoClimateControlServices];
-[CAFClimate autoClimateControls];
-[CAFClimate autoClimateControlsIndexed];
-[CAFClimate cabinService];
-[CAFClimate climateControlsLockedServices];
-[CAFClimate climateControlsLockeds];
-[CAFClimate climateControlsLockedsIndexed];
-[CAFClimate defrosts];
-[CAFClimate fanServices];
-[CAFClimate fans];
-[CAFClimate fansIndexed];
-[CAFClimate recirculation];
-[CAFClimate recirculationService];
-[CAFClimate steeringWheelHeatingCooling];
-[CAFClimate steeringWheelHeatingCoolingService];
-[CAFClimate temperatureLevelServices];
-[CAFClimate temperatureLevels];
-[CAFClimate temperatureLevelsIndexed];
-[CAFClimate temperatureServices];
-[CAFClimate temperaturesIndexed];
-[CAFClimate ventServices];
-[CAFClimate vents];
-[CAFClimate ventsIndexed];
-[CAFClimate zoneOnServices];
-[CAFClimate zoneOnsIndexed];
-[CAFClimate zonesSyncedServices];
-[CAFClimate zonesSynceds];
-[CAFClimate zonesSyncedsIndexed];
```
