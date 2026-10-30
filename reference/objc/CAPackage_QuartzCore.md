# `CAPackage`

- Image: [`/System/Library/Frameworks/QuartzCore.framework/QuartzCore`](../userland/System__Library__Frameworks__QuartzCore.framework__QuartzCore.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 2 properties, 18 instance methods, 2 class methods

## Instance variables

```
^{_CAPackageData=@@@BB@@} _data;
```

## Properties

```
@property (T@"CALayer",R) rootLayer;
@property (TB,R,GisGeometryFlipped) geometryFlipped;
```

## Class methods

```
+[CAPackage packageWithContentsOfURL:type:options:error:];
+[CAPackage packageWithData:type:options:error:];
```

## Instance methods

```
-[CAPackage publishedObjectNames];
-[CAPackage publishedObjectWithName:];
-[CAPackage CAMLParser:resourceForURL:];
-[CAPackage unarchiver:cannotDecodeObjectOfClassName:originalClasses:];
-[CAPackage isGeometryFlipped];
-[CAPackage dealloc];
-[CAPackage CAMLParser:didLoadResource:fromURL:];
-[CAPackage substitutedClasses];
-[CAPackage _readFromCAMLURL:type:options:error:];
-[CAPackage _initWithContentsOfURL:type:options:error:];
-[CAPackage rootLayer];
-[CAPackage CAMLParser:didFailToFindClassWithName:];
-[CAPackage _addClassSubstitutions:];
-[CAPackage _initWithData:type:options:error:];
-[CAPackage foreachLayer:];
-[CAPackage _readFromArchiveData:options:error:];
-[CAPackage _readFromCAMLData:type:options:error:];
-[CAPackage unarchiver:didDecodeObject:];
```
