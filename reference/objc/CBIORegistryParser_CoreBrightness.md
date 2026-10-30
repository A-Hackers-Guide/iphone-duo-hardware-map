# `CBIORegistryParser`

- Image: [`/System/Library/PrivateFrameworks/CoreBrightness.framework/CoreBrightness`](../userland/System__Library__PrivateFrameworks__CoreBrightness.framework__CoreBrightness.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `CBNopConfigurationProvider`
- 1 instance variables, 1 properties, 21 instance methods, 1 class methods

## Instance variables

```
@"<CBIORegInterface>" _reader;
```

## Properties

```
@property (T@"<CBIORegInterface>",R,V_reader) reader;
```

## Class methods

```
+[CBIORegistryParser parserWithReader:];
```

## Instance methods

```
-[CBIORegistryParser dealloc];
-[CBIORegistryParser description];
-[CBIORegistryParser reader];
-[CBIORegistryParser initWithReader:];
-[CBIORegistryParser loadIOFixedArray:toDestination:];
-[CBIORegistryParser floatArrayFor:];
-[CBIORegistryParser iofixedArrayFor:];
-[CBIORegistryParser loadBool:toDestination:];
-[CBIORegistryParser loadData:toDestination:];
-[CBIORegistryParser loadFixedFloat:toDestination:];
-[CBIORegistryParser loadFixedFloat:withScaler:toDestination:];
-[CBIORegistryParser loadFloat:toDestination:];
-[CBIORegistryParser loadFloatArray:toDestination:];
-[CBIORegistryParser loadInt16Array:toDestination:];
-[CBIORegistryParser loadInt:toDestination:];
-[CBIORegistryParser loadString:];
-[CBIORegistryParser loadUint16Array:toDestination:];
-[CBIORegistryParser loadUint:toDestination:];
-[CBIORegistryParser loadUintArray:toDestination:];
-[CBIORegistryParser nestedProviderFor:];
-[CBIORegistryParser uintArrayFor:];
```
