# `PLMultiKeyEntry`

- Image: [`/System/Library/PrivateFrameworks/PowerlogCore.framework/PowerlogCore`](../userland/System__Library__PrivateFrameworks__PowerlogCore.framework__PowerlogCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `PLEntry`
- 1 instance variables, 1 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSMutableDictionary" _multiKeys;
```

## Properties

```
@property (T@"NSMutableDictionary",&,V_multiKeys) multiKeys;
```

## Class methods

```
+[PLMultiKeyEntry load];
```

## Instance methods

```
-[PLMultiKeyEntry init];
-[PLMultiKeyEntry serializedForJSON];
-[PLMultiKeyEntry objectsForSubKey:ofSubKeyType:];
-[PLMultiKeyEntry multiKeys];
-[PLMultiKeyEntry setObject:forKey:];
-[PLMultiKeyEntry keysForSubKey:ofSubKeyType:];
-[PLMultiKeyEntry setMultiKeys:];
```
