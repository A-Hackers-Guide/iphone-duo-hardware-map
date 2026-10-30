# `CBDictConfigProvider`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBNopConfigurationProvider`
- 1 instance variables, 1 properties, 17 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _dict;
```

## Properties

```
@property (T@"NSDictionary",R,V_dict) dict;
```

## Class methods

```
+[CBDictConfigProvider providerWithDict:];
```

## Instance methods

```
-[CBDictConfigProvider initWithDictionary:];
-[CBDictConfigProvider dealloc];
-[CBDictConfigProvider description];
-[CBDictConfigProvider dict];
-[CBDictConfigProvider loadDictionary:];
-[CBDictConfigProvider floatArrayFor:];
-[CBDictConfigProvider iofixedArrayFor:];
-[CBDictConfigProvider loadBool:toDestination:];
-[CBDictConfigProvider loadFixedFloat:toDestination:];
-[CBDictConfigProvider loadFixedFloat:withScaler:toDestination:];
-[CBDictConfigProvider loadFloat:toDestination:];
-[CBDictConfigProvider loadFloatArray:toDestination:];
-[CBDictConfigProvider loadInt:toDestination:];
-[CBDictConfigProvider loadString:];
-[CBDictConfigProvider loadUint:toDestination:];
-[CBDictConfigProvider nestedProviderFor:];
-[CBDictConfigProvider uintArrayFor:];
```
