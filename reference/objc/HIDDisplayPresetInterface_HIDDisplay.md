# `HIDDisplayPresetInterface`

- Image: [`/System/Library/PrivateFrameworks/HIDDisplay.framework/HIDDisplay`](../userland/System__Library__PrivateFrameworks__HIDDisplay.framework__HIDDisplay.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `HIDDisplayInterface`
- 2 instance variables, 1 properties, 14 instance methods, 0 class methods

## Instance variables

```
@"NSDictionary" _usageElementMap;
@"NSArray" _presets;
```

## Properties

```
@property (T@"NSArray",R,V_presets) presets;
```

## Instance methods

```
-[HIDDisplayPresetInterface setupPresets];
-[HIDDisplayPresetInterface initWithContainerID:];
-[HIDDisplayPresetInterface capabilities];
-[HIDDisplayPresetInterface initWithService:];
-[HIDDisplayPresetInterface presets];
-[HIDDisplayPresetInterface createPresets];
-[HIDDisplayPresetInterface getActivePresetIndex:];
-[HIDDisplayPresetInterface getCurrentPresetIndex:];
-[HIDDisplayPresetInterface getFactoryDefaultPresetIndex:];
-[HIDDisplayPresetInterface getHIDDevices];
-[HIDDisplayPresetInterface getHIDElementForUsage:];
-[HIDDisplayPresetInterface initWithMatching:];
-[HIDDisplayPresetInterface setActivePresetIndex:error:];
-[HIDDisplayPresetInterface setCurrentPresetIndex:error:];
```
