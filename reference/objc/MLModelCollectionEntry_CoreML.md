# `MLModelCollectionEntry`

- Image: [`/System/Library/Frameworks/CoreML.framework/CoreML`](../userland/System__Library__Frameworks__CoreML.framework__CoreML.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 2 instance variables, 2 properties, 7 instance methods, 1 class methods

## Instance variables

```
@"NSString" _modelIdentifier;
@"NSURL" _modelURL;
```

## Properties

```
@property (T@"NSString",R,N,V_modelIdentifier) modelIdentifier;
@property (T@"NSURL",R,N,V_modelURL) modelURL;
```

## Class methods

```
+[MLModelCollectionEntry entryWithModelIdentifier:modelURL:];
```

## Instance methods

```
-[MLModelCollectionEntry modelIdentifier];
-[MLModelCollectionEntry hash];
-[MLModelCollectionEntry description];
-[MLModelCollectionEntry modelURL];
-[MLModelCollectionEntry isEqual:];
-[MLModelCollectionEntry _initWithModelIdentifier:modelUrl:];
-[MLModelCollectionEntry isEqualToModelCollectionEntry:];
```
