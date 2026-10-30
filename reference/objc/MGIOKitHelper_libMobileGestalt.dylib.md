# `MGIOKitHelper`

- Image: [`/usr/lib/libMobileGestalt.dylib`](../userland/usr__lib__libMobileGestalt.dylib.md) (iOS 27.2 dyld shared cache) **[DSC]**
- Superclass: `NSObject`
- 1 instance variables, 0 properties, 17 instance methods, 0 class methods

## Instance variables

```
I devIterator;
```

## Instance methods

```
-[MGIOKitHelper init];
-[MGIOKitHelper dealloc];
-[MGIOKitHelper copyBooleanFromServiceTree:withFirstChar:propertyName:withPropertyFirstChar:];
-[MGIOKitHelper copyDataFromDeviceTree:withFirstChar:propertyName:withPropertyFirstChar:];
-[MGIOKitHelper copyDataFromServiceTree:withFirstChar:propertyName:withPropertyFirstChar:];
-[MGIOKitHelper copyDeviceTreeProperty:withFirstChar:propertyName:withPropertyFirstChar:];
-[MGIOKitHelper copyDeviceTreeStructureNext:withFirstChar:];
-[MGIOKitHelper copyNumberFromData:];
-[MGIOKitHelper copyNumberFromDeviceTree:withFirstChar:propertyName:withPropertyFirstChar:];
-[MGIOKitHelper copyPropertyFromServiceTree:withFirstChar:propertyName:withPropertyFirstChar:];
-[MGIOKitHelper copyServiceTreeProperty:withFirstChar:propertyName:withPropertyFirstChar:];
-[MGIOKitHelper copyStringFromDeviceTree:withFirstChar:propertyName:withPropertyFirstChar:];
-[MGIOKitHelper copyStringFromServiceTree:withFirstChar:propertyName:withPropertyFirstChar:];
-[MGIOKitHelper createTreeIterator:];
-[MGIOKitHelper deleteIterator];
-[MGIOKitHelper deviceTreeNodeIsPresent:withExactName:withNodeClass:];
-[MGIOKitHelper iteratorCopyBusyServiceNames];
```
