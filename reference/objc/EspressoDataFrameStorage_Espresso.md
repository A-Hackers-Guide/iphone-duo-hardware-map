# `EspressoDataFrameStorage`

- Image: [`/System/Library/PrivateFrameworks/Espresso.framework/Espresso`](../userland/System__Library__PrivateFrameworks__Espresso.framework__Espresso.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 3 instance variables, 3 properties, 8 instance methods, 1 class methods

## Instance variables

```
@"NSMutableArray" _dataFrames;
@"NSMutableDictionary" _mappedFiles;
@"NSString" _baseFilename;
```

## Properties

```
@property (T@"NSMutableArray",&,V_dataFrames) dataFrames;
@property (T@"NSMutableDictionary",&,V_mappedFiles) mappedFiles;
@property (T@"NSString",&,V_baseFilename) baseFilename;
```

## Class methods

```
+[EspressoDataFrameStorage dataFrameStorageFromPath:error:];
```

## Instance methods

```
-[EspressoDataFrameStorage setMappedFiles:];
-[EspressoDataFrameStorage baseFilename];
-[EspressoDataFrameStorage dataFrameAtIndex:];
-[EspressoDataFrameStorage dataFrames];
-[EspressoDataFrameStorage mappedFiles];
-[EspressoDataFrameStorage numberOfDataFrames];
-[EspressoDataFrameStorage setBaseFilename:];
-[EspressoDataFrameStorage setDataFrames:];
```
