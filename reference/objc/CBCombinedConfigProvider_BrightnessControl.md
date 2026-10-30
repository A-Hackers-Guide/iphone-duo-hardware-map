# `CBCombinedConfigProvider`

- Image: [`/System/Library/PrivateFrameworks/BrightnessControl.framework/BrightnessControl`](../userland/System__Library__PrivateFrameworks__BrightnessControl.framework__BrightnessControl.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `CBPrimitiveConfigurationProvider`
- 2 instance variables, 6 properties, 22 instance methods, 1 class methods

## Instance variables

```
@"NSObject<OS_os_log>" logHandle;
@"NSArray" _providers;
```

## Properties

```
@property (T@"NSArray",R,V_providers) providers;
@property (T@"NSObject<OS_os_log>",&,VlogHandle) logHandle;
@property (TQ,R) hash;
@property (T#,R) superclass;
@property (T@"NSString",R,C) description;
@property (T@"NSString",?,R,C) debugDescription;
```

## Class methods

```
+[CBCombinedConfigProvider providerFromList:];
```

## Instance methods

```
-[CBCombinedConfigProvider providers];
-[CBCombinedConfigProvider logHandle];
-[CBCombinedConfigProvider dealloc];
-[CBCombinedConfigProvider setLogHandle:];
-[CBCombinedConfigProvider initWithProviders:];
-[CBCombinedConfigProvider loadIOFixedArray:toDestination:];
-[CBCombinedConfigProvider floatArrayFor:];
-[CBCombinedConfigProvider iofixedArrayFor:];
-[CBCombinedConfigProvider loadBool:toDestination:];
-[CBCombinedConfigProvider loadData:toDestination:];
-[CBCombinedConfigProvider loadFixedFloat:toDestination:];
-[CBCombinedConfigProvider loadFixedFloat:withScaler:toDestination:];
-[CBCombinedConfigProvider loadFloat:toDestination:];
-[CBCombinedConfigProvider loadFloatArray:toDestination:];
-[CBCombinedConfigProvider loadInt16Array:toDestination:];
-[CBCombinedConfigProvider loadInt:toDestination:];
-[CBCombinedConfigProvider loadString:];
-[CBCombinedConfigProvider loadUint16Array:toDestination:];
-[CBCombinedConfigProvider loadUint:toDestination:];
-[CBCombinedConfigProvider loadUintArray:toDestination:];
-[CBCombinedConfigProvider nestedProviderFor:];
-[CBCombinedConfigProvider uintArrayFor:];
```
