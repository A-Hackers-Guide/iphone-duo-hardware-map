# `MLDictionaryFeatureProvider`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- Protocols: `MLFeatureProvider`, `NSFastEnumeration`, `NSSecureCoding`
- 2 instance variables, 3 properties, 14 instance methods, 1 class methods

## Instance variables

```
@"NSDictionary" _dictionary;
@"NSSet" _cachedFeatureNames;
```

## Properties

```
@property (T@"NSDictionary",&,N,V_dictionary) dictionary;
@property (T@"NSSet",R,N,V_cachedFeatureNames) cachedFeatureNames;
@property (T@"NSSet",R,N) featureNames;
```

## Class methods

```
+[MLDictionaryFeatureProvider supportsSecureCoding];
```

## Instance methods

```
-[MLDictionaryFeatureProvider setDictionary:];
-[MLDictionaryFeatureProvider initWithDictionary:error:];
-[MLDictionaryFeatureProvider cachedFeatureNames];
-[MLDictionaryFeatureProvider dictionary];
-[MLDictionaryFeatureProvider objectForKeyedSubscript:];
-[MLDictionaryFeatureProvider initWithFeatureProvider:featureNames:];
-[MLDictionaryFeatureProvider countByEnumeratingWithState:objects:count:];
-[MLDictionaryFeatureProvider encodeWithCoder:];
-[MLDictionaryFeatureProvider featureNames];
-[MLDictionaryFeatureProvider description];
-[MLDictionaryFeatureProvider initWithFeatureProvider:];
-[MLDictionaryFeatureProvider initWithCoder:];
-[MLDictionaryFeatureProvider initWithFeatureValueDictionary:];
-[MLDictionaryFeatureProvider featureValueForName:];
```
