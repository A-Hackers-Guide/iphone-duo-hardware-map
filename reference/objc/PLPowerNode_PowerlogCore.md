# `PLPowerNode`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 8 instance variables, 8 properties, 20 instance methods, 0 class methods

## Instance variables

```
@"NSString" _name;
d _fgEnergy;
d _bgEnergy;
d _fgTime;
d _bgTime;
d _bgAudioTime;
d _bgLocationTime;
@"NSArray" _rootNodeEnergyRows;
```

## Properties

```
@property (T@"NSString",&,V_name) name;
@property (Td,V_fgEnergy) fgEnergy;
@property (Td,V_bgEnergy) bgEnergy;
@property (Td,V_fgTime) fgTime;
@property (Td,V_bgTime) bgTime;
@property (Td,V_bgAudioTime) bgAudioTime;
@property (Td,V_bgLocationTime) bgLocationTime;
@property (T@"NSArray",&,V_rootNodeEnergyRows) rootNodeEnergyRows;
```

## Instance methods

```
-[PLPowerNode energy];
-[PLPowerNode serialize];
-[PLPowerNode setName:];
-[PLPowerNode name];
-[PLPowerNode time];
-[PLPowerNode setBgAudioTime:];
-[PLPowerNode bgAudioTime];
-[PLPowerNode bgEnergy];
-[PLPowerNode bgLocationTime];
-[PLPowerNode bgTime];
-[PLPowerNode fgEnergy];
-[PLPowerNode fgTime];
-[PLPowerNode initWithName:withFGEnergy:withBGEnergy:withFGTime:withBGTime:withBGAudioTime:withBGLocationTime:withRootNodeEnergyRows:];
-[PLPowerNode rootNodeEnergyRows];
-[PLPowerNode setBgEnergy:];
-[PLPowerNode setBgLocationTime:];
-[PLPowerNode setBgTime:];
-[PLPowerNode setFgEnergy:];
-[PLPowerNode setFgTime:];
-[PLPowerNode setRootNodeEnergyRows:];
```
