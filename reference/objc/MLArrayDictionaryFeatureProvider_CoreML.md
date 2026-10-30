# `MLArrayDictionaryFeatureProvider`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLBatchProvider`, `NSSecureCoding`
- 1 instance variables, 2 properties, 6 instance methods, 1 class methods

## Instance variables

```
@"NSArray" _array;
```

## Properties

```
@property (T@"NSArray",R,N,V_array) array;
@property (Tq,R,N) count;
```

## Class methods

```
+[MLArrayDictionaryFeatureProvider supportsSecureCoding];
```

## Instance methods

```
-[MLArrayDictionaryFeatureProvider count];
-[MLArrayDictionaryFeatureProvider encodeWithCoder:];
-[MLArrayDictionaryFeatureProvider initWithCoder:];
-[MLArrayDictionaryFeatureProvider array];
-[MLArrayDictionaryFeatureProvider featuresAtIndex:];
-[MLArrayDictionaryFeatureProvider initWithDictionaryFeatureProviderArray:];
```
