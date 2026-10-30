# `ACCFeaturePluginHID`

- Image: [`/System/Library/CoreAccessories/PlugIns/Features/HID.feature/HID`](../userland/System__Library__CoreAccessories__PlugIns__Features__HID.feature__HID.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `ACCFeaturePluginProtocol`
- 2 instance variables, 7 properties, 9 instance methods, 0 class methods

## Instance variables

```
B _isRunning;
@"ACCFeaturePluginHIDProvider" _hidProvider;
```

## Properties

```
@property (TB,N,V_isRunning) isRunning;
@property (T@"ACCFeaturePluginHIDProvider",&,N,V_hidProvider) hidProvider;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
@property (T@"NSString",R,N) pluginName;
```

## Instance methods

```
-[ACCFeaturePluginHID isRunning];
-[ACCFeaturePluginHID stopPlugin];
-[ACCFeaturePluginHID pluginName];
-[ACCFeaturePluginHID startPlugin];
-[ACCFeaturePluginHID initPlugin];
-[ACCFeaturePluginHID description];
-[ACCFeaturePluginHID setIsRunning:];
-[ACCFeaturePluginHID setHidProvider:];
-[ACCFeaturePluginHID hidProvider];
```
