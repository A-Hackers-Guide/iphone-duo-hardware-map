# `MLProbabilityDictionary`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSDictionary`
- 2 instance variables, 2 properties, 13 instance methods, 1 class methods

## Instance variables

```
@"MLProbabilityDictionarySharedKeySet" _labelIndexMap;
@"<MLProbabilityDictionaryStorage>" _storage;
```

## Properties

```
@property (T@"MLProbabilityDictionarySharedKeySet",R,V_labelIndexMap) labelIndexMap;
@property (T@"<MLProbabilityDictionaryStorage>",R,V_storage) storage;
```

## Class methods

```
+[MLProbabilityDictionary sharedKeySetForLabels:];
```

## Instance methods

```
-[MLProbabilityDictionary keyEnumerator];
-[MLProbabilityDictionary count];
-[MLProbabilityDictionary initWithObjects:forKeys:count:];
-[MLProbabilityDictionary objectForKey:];
-[MLProbabilityDictionary storage];
-[MLProbabilityDictionary classLabelOfMaxProbability];
-[MLProbabilityDictionary initWithLabelIndexMap:storage:];
-[MLProbabilityDictionary initWithLabels:probabilities:];
-[MLProbabilityDictionary initWithLabels:probabilityArray:];
-[MLProbabilityDictionary initWithSharedKeySet:probabilities:];
-[MLProbabilityDictionary initWithSharedKeySet:probabilityArray:];
-[MLProbabilityDictionary initWithSharedKeySet:probabilityMultiArray:];
-[MLProbabilityDictionary labelIndexMap];
```
