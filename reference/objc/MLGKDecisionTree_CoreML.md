# `MLGKDecisionTree`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 4 instance variables, 2 properties, 10 instance methods, 0 class methods

## Instance variables

```
^v _trc;
@"MLTreeEnsembleClassifier" _treeClassifier;
@"NSMutableArray" __attributes;
@"NSMutableOrderedSet" __objectStore;
```

## Properties

```
@property (T@"NSMutableArray",&,N,V__attributes) _attributes;
@property (T@"NSMutableOrderedSet",&,N,V__objectStore) _objectStore;
```

## Instance methods

```
-[MLGKDecisionTree _attributes];
-[MLGKDecisionTree dealloc];
-[MLGKDecisionTree _init];
-[MLGKDecisionTree set_attributes:];
-[MLGKDecisionTree _initWithFlattenedTree:];
-[MLGKDecisionTree _loadModelAssetWithModelAtPath:withError:];
-[MLGKDecisionTree _makeInferenceFromAnswers:withError:];
-[MLGKDecisionTree _objectStore];
-[MLGKDecisionTree _saveModelAssetWithModelToPath:withError:];
-[MLGKDecisionTree set_objectStore:];
```
